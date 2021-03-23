"""
Internal module to start the webserver which will drive the creation of a project locally.
"""

import tornado.web
import os
import json
import sys
import time
import importlib


TEMPS_FILE_HISTORY = "run_history.json"


def get_components(components, results, alias=None):
  """
  Description:
  ------------
  Get the documentation dynamically from the project structure.
  This will store everything in a global dictionary.

  Attributes:
  ----------
  :param components: HTML Component. An internal HTML Component
  :param results: Dictionary. A dictionary with the documentation per component
  :param alias: String. The components prefix (for the sub categories)
  """
  for v in dir(components):
    if v == 'google':
      continue

    obj = getattr(components, v)
    if callable(obj):
      doc_string = obj.__doc__
      if doc_string is None or "Description" not in doc_string:
        continue

      if alias is None:
        results[obj.__name__] = doc_string
      else:
        results["%s.%s" % (alias, obj.__name__)] = doc_string
    else:
      if hasattr(obj, 'context'):
        if v != 'parent':
          get_components(obj, results, alias=v)
  return results


def parse_doc(doc_string):
  """
  Description:
  ------------
  Parse the documentation and structure this to an internal object in order to be lookup in the Studio to help on
  the implementation.

  Attributes:
  ----------
  :param doc_string: String. The class doctring in the Epyk format
  """
  group = None
  result = {'dsc': [], 'tags': []}
  for line in doc_string.split("\n"):
    s_line = line.strip()
    if s_line.startswith("--------") or not s_line:
      continue

    if s_line == "Description:":
      group = "dsc"
      continue
    elif s_line == "Attributes:":
      group = "params"
      continue
    elif s_line == "Underlying HTML Objects:":
      group = "underlying"
      continue
    elif s_line == "Usage::":
      group = "usage"
      continue
    elif s_line == "Templates:":
      group = "templates"
      continue

    if s_line.startswith(":tags:"):
      result['tags'] = [c.strip() for c in s_line.split(":tags:")[1].split(",")]
      group = None
      continue

    if s_line.startswith(":categories:"):
      result['categories'] = [c.strip() for c in s_line.split(":categories:")[1].split(",")]
      group = None
      continue

    if group is not None:
      result.setdefault(group, []).append(s_line)

  if 'dsc' in result:
    result['dsc'] = "".join(result['dsc'])
  return result


# This is for the compatibility with Python 2
class Namespace:
  def __init__(self, **kwargs):
    self.__dict__.update(kwargs)


class StudioHandler(tornado.web.RequestHandler):

  def initialize(self, current_path):
    self.current_path = current_path


class MainHandler(StudioHandler):

  def get(self):
    """
    Description:
    ------------
    The application home page
    """
    from epyk_studio.static.pages import home

    home.projects.empty()
    for f in os.listdir(self.current_path):
      home.projects.add(
        home.page.ui.div([
          home.page.ui.text(f, align="center"),
        home.page.ui.images.avatar(f, width=(100, 'px'), height=(100, 'px'))], width=(120, 'px')))
    self.write(home.page.outs.html())


class MainHandlerCode(StudioHandler):

  def get(self):
    """
    Description:
    ------------
    The code source page.
    """
    from epyk_studio.static.pages import code_viewer

    path = os.path.dirname(code_viewer.__file__)
    mod_path = os.path.join(path, "%s.py" % self.get_argument("script"))
    if os.path.exists(mod_path):
      with open(mod_path) as f:
        content = f.read()
      code_viewer.python._vals = content
      self.write(code_viewer.page.outs.html())


class MainHandlerPage(tornado.web.RequestHandler):

  def initialize(self, current_path, page):
    self.current_path = current_path
    self.page = page

  def get(self):
    """
    Description:
    ------------

    TODO: Find a way to improve the reload
    """
    data = {"current_path": self.current_path}
    if self.request.query_arguments:
      arguments = self.request.query_arguments
      data.update({arg: self.get_argument(arg) for arg in arguments.keys()})
      if 'theme' in data:
        os.environ["THEME"] = data['theme']
        del data['theme']

      if 'lang' in data:
        os.environ["LANG"] = data['lang']
        del data['lang']

    if self.request.uri == '/project':
      data.update({"count_projects": 0, 'started_project': 0})
      for f in os.listdir(self.current_path):
        if not os.path.isfile(f):
          p_path_ui = os.path.join(self.current_path, f, 'ui')
          p_path = os.path.join(self.current_path, f)
          if os.path.exists(p_path_ui):
            data['count_projects'] += 1
            for p in os.listdir(p_path):
              if p.endswith("_server.py"):
                server_mod = __import__("%s.%s" % (f, p[:-3]), fromlist=['object'])
                if hasattr(server_mod, 'PORT'):
                  app_url = "%s:%s" % (":".join(self.request.full_url().split(":")[0:2]), server_mod.PORT)
                  # TODO: add ping on the server to check and allow a link to it from the studio
    mod = __import__("epyk_studio.static.pages.%s" % self.page, fromlist=['object'])
    importlib.reload(mod)
    if data and hasattr(mod, 'add_inputs'):
      if hasattr(mod, 'add_inputs'):
        mod.add_inputs(data)
    self.write(mod.page.outs.html())


class MainHandlerProjects(StudioHandler):

  def post(self):
    """
    Description:
    ------------

    """
    repo = []
    data = tornado.escape.json_decode(self.request.body)
    filter = data.get('project', '').upper()
    if not filter:
      for f in os.listdir(self.current_path):
        path_dir = os.path.join(self.current_path, f, 'ui')
        if not os.path.isdir(path_dir):
          continue

        repo.append({'text': f, 'url': '/project_page?name=%s' % f, 'button': 'get',
                     'event': {'url': '/test', 'data': {'Ok': f}}})
    else:
      for f in os.listdir(self.current_path):
        path_dir = os.path.join(self.current_path, f, 'ui')
        if not os.path.isdir(path_dir):
          continue

        if filter in f.upper():
          repo.append({'text': f, 'url': '/project_page?name=%s' % f, 'button': 'get',
                       'event': {'url': '/test', 'data': {'Ok': f}}})
    self.write({'projects': repo})


class MainHandlerPageTranspile(StudioHandler):

  def post(self):
    """
    Description:
    ------------
    Shortcut event to the command to transpile a project.
    This command will transpile to HTML all the script in the project's reports folder.

    To be transpiled the project must get the structure defined in the epyk-ui module.
    Some CLI command are available to transpile directly a script.
    """
    from epyk.core.cli import cli_project

    data = tornado.escape.json_decode(self.request.body)
    project_path = os.path.join(self.current_path, data['project'])
    results = cli_project.transpile_all(Namespace(path=project_path, split=data["trans_type"]=='Multiple'))
    if len(results["failed"]) > 0:
      self.write({"status": '%s scripts transpiled, %s errors' % (len(results["completed"]), len(results["failed"]))})
    else:
      self.write({"status": '%s scripts transpiled' % len(results["completed"])})


class MainHandlerPageAddServer(StudioHandler):

  def post(self):
    """
    Description:
    ------------
    Shortcut event to the command to add a server to an existing project.


    """
    from epyk_studio.core.cli import cli_pages

    data = tornado.escape.json_decode(self.request.body)
    cli_pages.add_server(Namespace(path=self.current_path, name=data['project'], server=data['server'].lower()))
    # create the two underlying folders reports and views
    for f in ['reports', 'views']:
      pages_path = os.path.join(self.current_path, data['project'], 'ui', f)
      if not os.path.exists(pages_path):
        os.makedirs(pages_path)
    self.write("")


class MainHandlerPageAdd(StudioHandler):

  def post(self):
    """
    Description:
    ------------

    """
    from epyk_studio.core.cli import cli_pages

    data = tornado.escape.json_decode(self.request.body)
    if data['name']:
      path = os.path.join(self.current_path, data['project'], 'ui', 'reports')
      file_full_path = os.path.join(path, data['name'])
      if not os.path.exists(file_full_path):
        map_category = {"Page": 'new'}
        getattr(cli_pages, map_category.get(data['category'], data['category']).lower())(Namespace(path=path, name=data['name']))
      self.write("")
    else:
      self.write("")


class MainHandlerPageGetExt(StudioHandler):

  def post(self):
    """
    Description:
    ------------

    """
    from epyk.core.cli import utils
    from epyk.core.js import Imports

    data = tornado.escape.json_decode(self.request.body)
    modules = set()
    if data['project']:
      sys.path.append(os.path.join(self.current_path, data['project']))
      path = os.path.join(self.current_path, data['project'], 'ui', 'reports')
      sys.path.append(path)
      for f in os.listdir(path):
        if f.endswith(".py") and f != "__init__.py":
          view_name = f[:-3]
          try:
            mod = __import__(view_name, fromlist=['object'])
            importlib.reload(mod)
            page = utils.get_page(mod, template=True)
            modules |= page.imports().requirements
          except:
            pass

    pkgs = []
    for m in modules:
      if m in Imports.JS_IMPORTS:
        pkgs.append({"pkg": m, 'vr': Imports.JS_IMPORTS[m]['modules'][0]['version'],
                     'get': "<button class='cssbuttonbasic' style='padding:0 5px;line-height:15px!IMPORTANT' onclick='(function(){var xhttp = new XMLHttpRequest(); xhttp.open(\"GET\", \"/get/packages?p=%s\", true); xhttp.send()})()'>get</button>" % m})
    self.write({"packages": pkgs})


class MainHandlerExts(StudioHandler):

  def get(self):
    """
    Description:
    ------------

    """
    from epyk_studio.utils import git

    data = {'script': 'bars.py'}
    if self.request.query_arguments:
      arguments = self.request.query_arguments
      data = {arg: self.get_argument(arg) for arg in arguments.keys()}
      if 'theme' in data:
        os.environ["THEME"] = data['theme']
        del data['theme']

      if 'lang' in data:
        os.environ["LANG"] = data['lang']
        del data['lang']

    git_repos = git(data.get('user', 'epykure'), data.get('project', 'epyk-templates'))
    script_url = None
    for rec in git_repos.trees()['tree']:
      if rec['path'].endswith(data['script']):
        if data.get("folder") is not None:
          if data["folder"] in rec['path']:
            script_url = rec['path']
            break
        else:
          script_url = rec['path']
          break

    html = git_repos.get_file_content(script_url)
    tmps = os.path.join(self.current_path, 'tmps')
    if not os.path.exists(tmps):
      os.makedirs(tmps)

    sys.path.append(tmps)
    with open(os.path.join(tmps, data['script']), "wb") as f:
      f.write(html)

    mod = __import__(data['script'][:-3], fromlist=['object'])
    importlib.reload(mod)
    self.write(mod.page.outs.html())


class MainHandlerPackages(StudioHandler):

  def get(self):
    """

    :return:
    """
    from epyk.core.js import Imports

    js_alias = [self.get_argument("p")]
    Imports.npm(js_alias, self.current_path)
    self.write({'status': "%s - package downloaded" % js_alias[0]})

  def post(self):
    """
    Description:
    ------------
    Get all the JavaScript External packages with a structure similar to the one in NodeJs
    """
    from epyk.core.js import Imports

    if self.request.body:
      data = tornado.escape.json_decode(self.request.body)
      js_alias = data["packages"].split(",")
    else:
      js_alias = list(Imports.JS_IMPORTS.keys())
      for k in Imports.CSS_IMPORTS.keys():
        if k not in js_alias:
          js_alias.append(k)
    Imports.npm(js_alias, self.current_path)
    self.write({'status': "All packages downloaded"})


class MainHandlerAdd(StudioHandler):

  def post(self):
    """
    Description:
    ------------

    """
    from epyk.core.cli import cli_project

    data = tornado.escape.json_decode(self.request.body)
    project_path = os.path.join(self.current_path, data['name'])
    if os.path.exists(project_path):
      self.write({'status': "%s - Project already defined" % data['name'],
                  'css': {'background': 'orange', 'color': 'white', 'padding-top': '20px'}})
    else:
      cli_project.new(Namespace(path=self.current_path, name=data['name']))
      self.write({'status': "%s - Project created" % data['name'], 'css': {'color': 'white', 'marginLeft': '20px'}})


class MainHandlerSearch(StudioHandler):

  def post(self):
    """
    Description:
    ------------

    """
    from epyk_studio.interfaces import Interface

    start = time.time()
    components = Interface.Studio()
    result = {}
    get_components(components, result)
    data = tornado.escape.json_decode(self.request.body)

    components = []
    for k, v in result.items():
      parsed_doc = parse_doc(v)
      if data['category'] == 'All' or data['category'] in parsed_doc.get("categories", []):
        if data['input']:
          if data['input'] in parsed_doc['dsc']:
            links = [{"url": t, 'val': t} for t in parsed_doc.get("templates", [])]

            components.append({"title": k, "urlTitle": '/search/component?v=%s' % k,
                               'dsc': parsed_doc['dsc'], 'links': links})
            if parsed_doc['tags']:
              components[-1].update({'icon': 'fas fa-tags', 'url': ", ".join(parsed_doc['tags'])})
        else:
          links = [{"url": t, 'val': t} for t in parsed_doc.get("templates", [])]
          components.append({"title": k, "urlTitle": '/search/component?v=%s' % k,
                             'dsc': parsed_doc['dsc'], 'links': links})
          if parsed_doc['tags']:
            components[-1].update({'icon': 'fas fa-tags', 'url': ", ".join(parsed_doc['tags'])})

    #print(data)
    #parse_doc(data)
    self.write({'status': "%s Results retrieved in %s" % (len(result), time.time() - start), 'results': components})


class MainHandlerSearchResult(tornado.web.RequestHandler):

  def initialize(self, current_path, page):
    self.current_path = current_path
    self.page = page

  def get(self):
    """
    Description:
    ------------

    """
    from epyk_studio.interfaces import Interface

    mod = __import__("epyk_studio.static.pages.%s" % self.page, fromlist=['object'])
    importlib.reload(mod)

    name = 'shop.rating'
    components = Interface.Studio()
    result = {}
    get_components(components, result)
    parsed_doc = parse_doc(result[name])
    mod.page.ui.title("Documentation (%s)" % name)
    mod.page.ui.texts.paragraph("\n".join(parsed_doc.get("dsc", [])))

    mod.page.ui.title("Categories")
    mod.page.ui.div("', '".join(parsed_doc.get('categories', [])))

    mod.page.ui.title("Tags")
    mod.page.ui.chips(parsed_doc.get('tags', []), options={"delete": False})

    mod.page.ui.title("Parameters")

    mod.page.ui.title("Demo")

    mod.page.ui.title("Github examples")

    mod.page.ui.title("Underlyings Modules")
    self.write(mod.page.outs.html())


class MainHandlerCodeFrame(StudioHandler):

  def get(self):
    """
    Description:
    -----------

    :return:
    """

    # TODO find a way to segregate the loading of the imports
    script = self.get_argument("script")
    classpath = self.get_argument("classpath", "")
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
        url = contents.add_url(page.ui.text(fp), r"/code_frame?classpath=&script=%s\%s\__init__.py" % (script_path, fp))
        if os.path.join(parent_folder, fp) == script_path:
          url.style.css.color = page.theme.colors[-1]
          url.style.css.bold()

    doc_link = page.ui.icon("fas fa-book-reader")
    doc_link.style.css.fixed(bottom=20, right=20)
    doc_link.goto("/docs")
    doc_link.style.add_classes.div.border_hover()
    doc_link.style.css.border_radius = 15
    doc_link.style.css.padding = 8
    doc_link.style.css.z_index = 900
    doc_link.style.css.background = page.theme.colors[0]

    if next_url is not None:
      doc_next = page.ui.icon("fas fa-caret-right")
      doc_next.style.css.fixed(bottom=80, right=20)
      doc_next.style.add_classes.div.border_hover()
      doc_next.goto(next_url)
      doc_next.style.css.border_radius = 15
      doc_next.style.css.min_width = 15
      doc_next.style.css.text_align = "center"
      doc_next.style.css.padding = 8
      doc_next.style.css.z_index = 900
      doc_next.style.css.background = page.theme.colors[0]

    if hasattr(mod, "INFOS"):
      doc_info = page.ui.icon("fas fa-info")
      doc_info.style.css.fixed(bottom=60, right=20)
      doc_info.style.css.color = page.theme.colors[5]
      doc_info.style.css.margin = "8px 15px"
      doc_info.click([
        page.js.msg.text(mod.INFOS, cssAttrs={"right": "60px", "bottom": "60px"}, options={"markdown": True})
      ])
    output = page.outs.html()
    self.write(output)

    temp_file = os.path.join(self.current_path, 'temps', TEMPS_FILE_HISTORY)
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

    :return:
    """
    from epyk.core.py import PyRest

    data = tornado.escape.json_decode(self.request.body)
    if 'rpt_path' in data:
      url = data['rpt_path']
      if data['rpt_path'].startswith("http"):
        if data['rpt_path'].startswith("https://github.com/epykure/epyk-templates"):
          url = data['rpt_path'].replace("https://github.com/epykure/epyk-templates/blob/master",
                                         "https://raw.githubusercontent.com/epykure/epyk-templates/master")
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


class MainHandlerDocs(StudioHandler):

  def get(self):
    """
    Description:
    -----------

    :return:
    """
    from epyk_studio.static import lang

    rubric = self.get_argument("r", "home")
    md_path = os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'docs', "%s_%s.md" % (rubric, lang.get_alias()))
    if not os.path.exists(md_path):
      # Default to the english version
      md_path = os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'docs', "%s_eng.md" % (rubric))
    if os.path.exists(md_path):
      from epyk_studio.core.Page import Report
      from epyk_studio.static.pages import add_code, nav_bar

      page = Report()
      nav_bar(page, "EpykDocs: %s" % rubric)
      with open(md_path) as fp:
        components = page.py.markdown.resolve(fp.read())
        box = page.studio.containers.box()
        box.extend(components)
        box.style.standard()
      add_code(page, doc_only=True)
      page.ui.banners.disclaimer()
      self.write(page.outs.html())


class MainHandlerTmpls(StudioHandler):

  def get(self):
    data = {"current_path": self.current_path}
    if self.request.query_arguments:
      arguments = self.request.query_arguments
      data.update({arg: self.get_argument(arg) for arg in arguments.keys()})
      if 'theme' in data:
        os.environ["THEME"] = data['theme']
        del data['theme']

      if 'lang' in data:
        os.environ["LANG"] = data['lang']
        del data['lang']
    mod = __import__("epyk_studio.static.pages.template", fromlist=['object'])
    importlib.reload(mod)
    if data and hasattr(mod, 'add_inputs'):
      if hasattr(mod, 'add_inputs'):
        mod.add_inputs(data)
    self.write(mod.page.outs.html())

  def post(self):
    print("Ok")


def make_app(current_path, debug=True):
  """
  Description:
  ------------
  Make the app and define the routes.

  Attributes:
  ----------
  :param current_path: String. Mandatory. The path for the project
  :param debug: Boolean. Optional. The debug command. Default True
  """
  pages_path = os.path.dirname(__file__)
  return tornado.web.Application([
      (r"/", MainHandlerPage, dict(current_path=current_path, page="home")),
      (r"/test", MainHandlerAdd, dict(current_path=current_path)),
      (r"/exts", MainHandlerExts, dict(current_path=current_path)),

      #(r"/static/configs/(.*).json", tornado.web.StaticFileHandler, {"path": "./TestStudio/Studio/configs/eng/blotter.json"},),
      #(r'/static/(.*).json', MyFileHandler, dict(path="/Studio/static/", current_path=current_path)),

      #
      (r"/docs", MainHandlerDocs, dict(current_path=current_path)),

      #
      (r"/catalog", MainHandlerPage, dict(current_path=current_path, page="catalog")),

      #
      (r"/search", MainHandlerPage, dict(current_path=current_path, page="search")),
      (r"/search_result", MainHandlerSearchResult, dict(current_path=current_path, page="search_result")),
      (r"/search_post", MainHandlerSearch, dict(current_path=current_path)),

      #
      (r"/ext_packages", MainHandlerPage, dict(current_path=current_path, page="ext_packages")),
      (r"/get/packages", MainHandlerPackages, dict(current_path=current_path)),

      #
      (r"/analytics", MainHandlerPage, dict(current_path=current_path, page="analytics")),
      (r"/tutorials", MainHandlerPage, dict(current_path=current_path, page="tutorials")),
      (r"/servers", MainHandlerPage, dict(current_path=current_path, page="servers")),
      (r"/databases", MainHandlerPage, dict(current_path=current_path, page="databases")),
      (r"/code", MainHandlerCode, dict(current_path=current_path)),

      #
      (r"/templates", MainHandlerPage, dict(current_path=current_path, page="templates")),
      (r"/template", MainHandlerTmpls, dict(current_path=current_path)),

      #
      (r"/project", MainHandlerPage, dict(current_path=current_path, page="project")),
      (r"/project_page", MainHandlerPage, dict(current_path=current_path, page="project_page")),
      (r"/projects_page_add", MainHandlerPageAdd, dict(current_path=current_path)),
      (r"/projects_get_packages", MainHandlerPageGetExt, dict(current_path=current_path)),
      (r"/projects_transpile", MainHandlerPageTranspile, dict(current_path=current_path)),
      (r"/projects_add_server", MainHandlerPageAddServer, dict(current_path=current_path)),
      (r"/projects_get", MainHandlerProjects, dict(current_path=current_path)),

      #
      (r"/code_editor", MainHandlerPage, dict(current_path=current_path, page="code_editor")),
      (r"/code_frame", MainHandlerCodeFrame, dict(current_path=current_path)),
  ], debug=debug, static_path=os.path.join(pages_path, '..', '..', 'static', 'images')
  )



