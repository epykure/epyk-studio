
import os
import sys
import json
import importlib
import tornado.web
import tornado.escape
import urllib.request

from epyk.core.py import PyRest
from epyk_studio.static.pages import code_viewer
from epyk_studio.utils import sys_files


class CodeHandler(tornado.web.RequestHandler):

  def post(self):
    """
    Description:
    ------------

    """
    data = tornado.escape.json_decode(self.request.body)
    with open(os.path.join(
      self.application.settings.get('studio_path'),
      sys_files.STUDIO_FILES["sandbox"]["path"],
      data['rpt_name']), "w") as fp:
      fp.write(data['editor'])

  def get(self):
    """
    Description:
    ------------
    The code source page.
    """
    path = os.path.dirname(code_viewer.__file__)
    mod_path = os.path.join(path, "%s.py" % self.get_argument("script"))
    if os.path.exists(mod_path):
      with open(mod_path) as f:
        content = f.read()
      code_viewer.python._vals = content
      self.write(code_viewer.page.outs.html())


class CodeFrameHandler(tornado.web.RequestHandler):

  def get(self):
    """
    Description:
    -----------

    :return:
    """

    # TODO find a way to segregate the loading of the imports
    script = self.get_argument("script")
    classpath = self.get_argument("classpath", "")
    options = True
    if script.startswith("https://"):
      if script.startswith(sys_files.GITHUB_PATHS["website"]):
        url_frgs = script.split("/")
        script = "%s/%s/%s/%s" % (
          sys_files.GITHUB_PATHS["raw_content"], url_frgs[3], url_frgs[4], "/".join(url_frgs[6:]))
      _, script_name = os.path.split(script)
      with urllib.request.urlopen(script) as response:
        content = response.read().decode('utf-8')
        script_full_path = os.path.join(
          self.application.settings.get('studio_path'), sys_files.STUDIO_FILES["sandbox"]["path"], script_name)
        with open(script_full_path, "w") as fp:
          fp.write(content)
      classpath = os.path.join(self.application.settings.get('studio_path'), sys_files.STUDIO_FILES["sandbox"]["path"])
      script = script_name
      options = False

    if classpath:
      for p in classpath.split(";"):
        sys.path.append(p.strip())
    path, script_name = os.path.split(script)
    sys.path.append(path)

    mod = __import__(script_name[:-3], fromlist=['object'])
    importlib.reload(mod)
    if hasattr(mod, 'get_page'):
      from epyk_studio.core.Page import Report

      page = Report()
      mod.get_page(page)
    else:
      page = mod.page

    if options:
      contents = page.ui.contents("Environment", options={"manual": True})
      title_link = contents.add_category("Other Pages", level=1, options={"hidden": True})
      title_link.style.css.margin_top = 10
      script_path, selected_file, next_url = os.path.dirname(mod.__file__), False, None
      for fp in os.listdir(script_path):
        if fp != "__init__.py" and fp.endswith(".py"):
          url = contents.add_url(page.ui.text(fp), r"/code_frame?classpath=&script=%s\%s" % (script_path, fp))
          if selected_file:
            next_url = r"/code_frame?classpath=&script=%s\%s" % (script_path, fp)
            selected_file = False
          if os.path.join(script_path, fp) == mod.__file__:
            url.style.css.color = page.theme.colors[-1]
            url.style.css.bold()
            selected_file = True

      parent_folder = os.path.dirname(script_path)
      title_link = contents.add_category("Other Folders", level=1, options={"hidden": True})
      title_link.style.css.margin_top = 10
      for fp in os.listdir(parent_folder):
        if os.path.isdir(path) and os.path.exists(os.path.join(parent_folder, fp, "__init__.py")):
          url = contents.add_url(
            page.ui.text(fp), r"/code_frame?classpath=&script=%s\%s\__init__.py" % (script_path, fp))
          if os.path.join(parent_folder, fp) == script_path:
            url.style.css.color = page.theme.colors[-1]
            url.style.css.bold()

    doc_link = page.ui.icon("fas fa-book-reader", width=(35, 'px'), height=(30, 'px'))
    doc_link.style.css.fixed(bottom=20, right=20)
    doc_link.goto("/docs")
    doc_link.style.add_classes.div.border_hover()
    doc_link.style.css.border_radius = 15
    doc_link.style.css.z_index = 900
    doc_link.style.css.line_height = 30
    doc_link.style.css.text_align = "center"
    doc_link.style.css.background = page.theme.colors[0]

    if options and next_url is not None:
      doc_next = page.ui.icon("fas fa-caret-right", width=(35, 'px'), height=(30, 'px'))
      doc_next.style.css.fixed(bottom=70, right=20)
      doc_next.style.add_classes.div.border_hover()
      doc_next.goto(next_url)
      doc_next.style.css.border_radius = 15
      doc_next.style.css.min_width = 15
      doc_next.style.css.line_height = 30
      doc_next.style.css.text_align = "center"
      doc_next.style.css.z_index = 900
      doc_next.style.css.background = page.theme.colors[0]

    if hasattr(mod, "INFOS"):
      doc_info = page.ui.icon("fas fa-info")
      doc_info.style.css.fixed(bottom=15, right=60)
      doc_info.style.css.color = page.theme.notch()
      doc_info.style.css.margin = "8px 15px"
      doc_info.click([
        page.js.msg.text(mod.INFOS, cssAttrs={"right": "90px", "bottom": "15px"}, options={"markdown": True})
      ])
    output = page.outs.html()
    self.write(output)

    temp_file = os.path.join(
      self.application.settings.get('studio_path'),
      sys_files.STUDIO_FILES["history"]["path"],
      sys_files.STUDIO_FILES["history"]["file"])
    content = []
    if os.path.exists(temp_file):
      with open(temp_file) as fp:
        content = json.load(fp)

    if script not in content:
      content.insert(0, script)
      with open(temp_file, "w") as fp:
        json.dump(content, fp, indent=4)
    sys.path.remove(path)

  def post(self):
    """
    Description:
    -----------

    """
    data = tornado.escape.json_decode(self.request.body)
    if 'rpt_path' in data:
      url = data['rpt_path']
      if data['rpt_path'].startswith("http"):
        if data['rpt_path'].startswith("%s/epykure/epyk-templates" % sys_files.GITHUB_PATHS['website']):
          url = data['rpt_path'].replace(
            "%s/epykure/epyk-templates/blob/master" % sys_files.GITHUB_PATHS['website'],
            "%s/epykure/epyk-templates/master" % sys_files.GITHUB_PATHS['raw_content'])
        response = PyRest.PyRest().request(url)
        loc = {}
        exec("%s\nhtml_page = page.outs.html() " % response.decode("utf-8"), globals(), loc)
        self.write({'page': loc['html_page'], 'content': response.decode("utf-8")})
      else:
        with open(data['rpt_path']) as fp:
          content = fp.read()

        if data['rpt_classpath']:
          for p in data['rpt_classpath'].split(";"):
            sys.path.append(p.strip())
        path, script_name = os.path.split(data['rpt_path'])
        sys.path.append(path)

        # TODO find a way to segregate the loading of the imports
        mod = __import__(script_name[:-3], fromlist=['object'])
        if hasattr(mod, 'get_page'):
          from epyk_studio.core.Page import Report

          page = Report()
          mod.get_page(page)
        else:
          page = mod.page
        output = page.outs.html()
        self.write({'page': output, 'content': content, 'link': '/code_frame?script=%s&classpath=%s' % (
          data['rpt_path'], data['rpt_classpath'])})
    else:
      loc = {}
      exec("%s\nhtml_page = page.outs.html()" % data['editor'], globals(), loc)
      self.write({'page': loc['html_page']})
