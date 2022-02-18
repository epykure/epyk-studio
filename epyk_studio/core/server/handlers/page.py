
import os
import importlib
import tornado.web
import tornado.escape


# This is for the compatibility with Python 2
class Namespace:
  def __init__(self, **kwargs):
    self.__dict__.update(kwargs)


class PageHandler(tornado.web.RequestHandler):

  def data_received(self, chunk):
    pass

  def get(self):
    """
    Description:
    ------------

    TODO: Find a way to improve the reload
    """

    page = self.request.uri.split("?")[0][1:] or "home"
    data = {"current_path": self.application.settings.get('studio_path')}
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
      for f in os.listdir(self.application.settings.get('studio_path')):
        if not os.path.isfile(f):
          p_path_ui = os.path.join(self.application.settings.get('studio_path'), f, 'ui')
          p_path = os.path.join(self.application.settings.get('studio_path'), f)
          if os.path.exists(p_path_ui):
            data['count_projects'] += 1
            for p in os.listdir(p_path):
              if p.endswith("_server.py"):
                server_mod = __import__("%s.%s" % (f, p[:-3]), fromlist=['object'])
                if hasattr(server_mod, 'PORT'):
                  app_url = "%s:%s" % (":".join(self.request.full_url().split(":")[0:2]), server_mod.PORT)
                  # TODO: add ping on the server to check and allow a link to it from the studio
    mod = __import__("epyk_studio.static.pages.%s" % page, fromlist=['object'])
    importlib.reload(mod)
    if data and hasattr(mod, 'add_inputs'):
      if hasattr(mod, 'add_inputs'):
        mod.add_inputs(data)
    self.write(mod.page.outs.html())


class AddHandler(tornado.web.RequestHandler):

  def post(self):
    """
    Description:
    ------------

    """
    from epyk_studio.core.cli import cli_pages

    data = tornado.escape.json_decode(self.request.body)
    if data['name']:
      path = os.path.join(self.application.settings.get('studio_path'), data['project'], 'ui', 'reports')
      file_full_path = os.path.join(path, data['name'])
      if not os.path.exists(file_full_path):
        map_category = {"Page": 'new'}
        getattr(cli_pages, map_category.get(data['category'], data['category']).lower())(
          Namespace(path=path, name=data['name']))
      self.write("")
    else:
      self.write("")
