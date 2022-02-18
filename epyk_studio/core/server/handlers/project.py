
import os
import sys
import importlib
import tornado.web
import tornado.escape

from epyk.core.cli import utils
from epyk.core.js import Imports
from epyk.core.cli import cli_project


# This is for the compatibility with Python 2
class Namespace:
  def __init__(self, **kwargs):
    self.__dict__.update(kwargs)


class GetExtHandler(tornado.web.RequestHandler):

  def post(self):
    """
    Description:
    ------------

    """
    data = tornado.escape.json_decode(self.request.body)
    modules = set()
    if data['project']:
      sys.path.append(os.path.join(self.application.settings.get('studio_path'), data['project']))
      path = os.path.join(self.application.settings.get('studio_path'), data['project'], 'ui', 'reports')
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


class AddServerHandler(tornado.web.RequestHandler):

  def post(self):
    """
    Description:
    ------------
    Shortcut event to the command to add a server to an existing project.


    """
    from epyk_studio.core.cli import cli_pages

    data = tornado.escape.json_decode(self.request.body)
    cli_pages.add_server(Namespace(
      path=self.application.settings.get('studio_path'), name=data['project'], server=data['server'].lower()))
    # create the two underlying folders reports and views
    for f in ['reports', 'views']:
      pages_path = os.path.join(self.application.settings.get('studio_path'), data['project'], 'ui', f)
      if not os.path.exists(pages_path):
        os.makedirs(pages_path)
    self.write("")


class CreateHandler(tornado.web.RequestHandler):

  def post(self):
    """
    Description:
    ------------

    """
    data = tornado.escape.json_decode(self.request.body)
    project_path = os.path.join(self.application.settings.get('studio_path'), data['name'])
    if os.path.exists(project_path):
      self.write({'status': "%s - Project already defined" % data['name'],
                  'css': {'background': 'orange', 'color': 'white', 'padding-top': '20px'}})
    else:
      cli_project.new(Namespace(path=self.application.settings.get('studio_path'), name=data['name']))
      self.write({'status': "%s - Project created" % data['name'], 'css': {'color': 'white', 'marginLeft': '20px'}})


class GetAllHandler(tornado.web.RequestHandler):

  def post(self):
    """
    Description:
    ------------

    """
    repo = []
    data = tornado.escape.json_decode(self.request.body)
    project_filter = data.get('project', '').upper()
    if not project_filter:
      for f in os.listdir(self.application.settings.get('studio_path')):
        path_dir = os.path.join(self.application.settings.get('studio_path'), f, 'ui')
        if not os.path.isdir(path_dir):
          continue

        repo.append({'text': f, 'url': '/project_page?name=%s' % f, 'button': 'get',
                     'event': {'url': '/test', 'data': {'Ok': f}}})
    else:
      for f in os.listdir(self.application.settings.get('studio_path')):
        path_dir = os.path.join(self.application.settings.get('studio_path'), f, 'ui')
        if not os.path.isdir(path_dir):
          continue

        if project_filter in f.upper():
          repo.append({'text': f, 'url': '/project_page?name=%s' % f, 'button': 'get',
                       'event': {'url': '/test', 'data': {'Ok': f}}})
    self.write({'projects': repo})


class TranspileHandler(tornado.web.RequestHandler):

  def post(self):
    """
    Description:
    ------------
    Shortcut event to the command to transpile a project.
    This command will transpile to HTML all the script in the project's reports folder.

    To be transpiled the project must get the structure defined in the epyk-ui module.
    Some CLI command are available to transpile directly a script.
    """
    data = tornado.escape.json_decode(self.request.body)
    project_path = os.path.join(self.application.settings.get('studio_path'), data['project'])
    colors = ",".join([
      "#E8F4EF", "#c8e6c9", "#a5d6a7", "#81c784", "#66bb6a", "#4caf50", "#43a047", "#388e3c", "#2e7d32", "#025C39"])
    results = cli_project.transpile_all(Namespace(
      path=project_path, split=data["trans_type"] == 'Multiple', colors=colors))
    if len(results["failed"]) > 0:
      self.write({"status": '%s scripts transpiled, %s errors' % (len(results["completed"]), len(results["failed"]))})
    else:
      self.write({"status": '%s scripts transpiled' % len(results["completed"])})
