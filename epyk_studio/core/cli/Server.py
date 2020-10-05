"""
Internal module to start the webserver which will drive the creation of a project locally.
"""

import tornado.web
import os
import time
import importlib

from epyk_studio.utils import git


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
  :param alias: String. The components prefixe (for the sub categories)
  """
  for v in dir(components):
    if v == 'google':
      continue

    obj = getattr(components, v)
    if callable(obj):
      doc_string = obj.__doc__
      if doc_string is None or not "Description" in doc_string:
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
  Parse the documentation and structure this to an internal object in order to be lookup in the Studio to help on the implementation.

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


#This is for the compatibility with Python 2
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
    data = {}
    if self.request.query_arguments:
      arguments = self.request.query_arguments
      data = {arg: self.get_argument(arg) for arg in arguments.keys()}
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
    import sys
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
    import sys

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
        if not k in js_alias:
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
    self.write('Hello Get')


  def post(self):
    data = tornado.escape.json_decode(self.request.body)
    loc = {}
    exec("%s\nhtml_page = page.outs.html()" % data['editor'], globals(), loc)
    self.write({'page': loc['html_page']})


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

      #
      (r"/search", MainHandlerPage, dict(current_path=current_path, page="search")),
      (r"/search_result", MainHandlerSearchResult, dict(current_path=current_path, page="search_result")),
      (r"/search_post", MainHandlerSearch, dict(current_path=current_path)),

      #
      (r"/ext_packages", MainHandlerPage, dict(current_path=current_path, page="ext_packages")),
      (r"/get/packages", MainHandlerPackages, dict(current_path=current_path)),

      (r"/analytics", MainHandlerPage, dict(current_path=current_path, page="analytics")),
      (r"/templates", MainHandlerPage, dict(current_path=current_path, page="templates")),
      (r"/tutorials", MainHandlerPage, dict(current_path=current_path, page="tutorials")),
      (r"/servers", MainHandlerPage, dict(current_path=current_path, page="servers")),
      (r"/databases", MainHandlerPage, dict(current_path=current_path, page="databases")),
      (r"/code", MainHandlerCode, dict(current_path=current_path)),

      #
      (r"/project", MainHandlerPage, dict(current_path=current_path, page="project")),
      (r"/project_page", MainHandlerPage, dict(current_path=current_path, page="project_page")),
      (r"/projects_page_add", MainHandlerPageAdd, dict(current_path=current_path)),
      (r"/projects_get_packages", MainHandlerPageGetExt, dict(current_path=current_path)),
      (r"/projects_transpile", MainHandlerPageTranspile, dict(current_path=current_path)),
      (r"/projects_add_server", MainHandlerPageAddServer, dict(current_path=current_path)),
      (r"/projects_get", MainHandlerProjects, dict(current_path=current_path)),

      (r"/code_editor", MainHandlerPage, dict(current_path=current_path, page="code_editor")),
      (r"/code_frame", MainHandlerCodeFrame, dict(current_path=current_path)),
  ], debug=debug, static_path=os.path.join(pages_path, '..', '..', 'static', 'images'))



