
import os
import sys
import argparse
import inspect
import traceback

from epyk.core.cli import utils
from epyk.core.html import Defaults


def __write_page(path, name, template):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param path:
  :param name:
  :param template:
  """
  project_path = path or os.getcwd()
  sys.path.append(project_path)
  i = 0
  if name is None:
    while True:
      name = "%s%s" % (template, i)
      file = os.path.join(project_path, name if name.endswith(".py") else "%s.py" % name)
      if os.path.exists(file):
        i += 1
      else:
        break
  else:
    file = os.path.join(project_path, name if name.endswith(".py") else "%s.py" % name)
  return file


def new_parsers(subparser):
  """
  Description:
  ------------
  Paser for the new CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  subparser.set_defaults(func=new)
  subparser.add_argument('-p', '--path', help='''The path where the new environment will be created: -p /foo/bar''')
  subparser.add_argument('-n', '--name', help='''The name of the new environment: -n MyEnv''')


def new(args):
  """
  Description:
  ------------
  Create a new Epyk Structure.

  The project structure is as below:
  /ui
    /reports
      Folder with all the Python scripts
    /templates
      Folder with the shared report structure
    /views
      Folder with the transpiled scripts
    ui_settings.py, configuration module for the UI framework

  Attributes:
  ----------
  :param parser: -p, The path where the new environment will be created: -p /foo/bar
  :param parser: -n, The name of the new environment: -n MyEnv
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)
  page = __write_page(project_path, args.name, "new")
  with open(page, "w") as f:
    f.write('''
from epyk_studio.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()
''')


def new_template(subparser):
  """
  Description:
  ------------
  Paser for the new CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  subparser.add_argument('-p', '--path', help='''The path where the new environment will be created: -p /foo/bar''')
  subparser.add_argument('-n', '--name', help='''The name of the new environment: -n MyEnv''')


def dashboard(args):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param args:
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)
  template = inspect.stack()[0][0].f_code.co_name
  page = __write_page(project_path, args.name, template)
  with open(page, "w") as f:
    f.write('''
from epyk_studio.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()
''')


def management(args):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param args:
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)
  template = inspect.stack()[0][0].f_code.co_name
  page = __write_page(project_path, args.name, template)
  with open(page, "w") as f:
    f.write('''
from epyk_studio.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()
''')


def shop(args):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param args:
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)
  template = inspect.stack()[0][0].f_code.co_name
  page = __write_page(project_path, args.name, template)
  with open(page, "w") as f:
    f.write('''
from epyk_studio.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()
''')


def restaurant(args):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param args:
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)
  template = inspect.stack()[0][0].f_code.co_name
  page = __write_page(project_path, args.name, template)
  with open(page, "w") as f:
    f.write('''
from epyk_studio.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()
''')


def blog(args):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param args:
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)
  template = inspect.stack()[0][0].f_code.co_name
  page = __write_page(project_path, args.name, template)
  with open(page, "w") as f:
    f.write('''
from epyk_studio.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()
''')


def gallery(args):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param args:
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)
  template = inspect.stack()[0][0].f_code.co_name
  page = __write_page(project_path, args.name, template)
  with open(page, "w") as f:
    f.write('''
from epyk_studio.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()
''')


def dating(args):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param args:
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)
  template = inspect.stack()[0][0].f_code.co_name
  page = __write_page(project_path, args.name, template)
  with open(page, "w") as f:
    f.write('''
from epyk_studio.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()
''')


def wedding(args):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param args:
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)
  template = inspect.stack()[0][0].f_code.co_name
  page = __write_page(project_path, args.name, template)
  with open(page, "w") as f:
    f.write('''
from epyk_studio.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()
''')


def show(args):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param args:
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)
  template = inspect.stack()[0][0].f_code.co_name
  page = __write_page(project_path, args.name, template)
  with open(page, "w") as f:
    f.write('''
from epyk_studio.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()
''')


def vitrine(args):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param args:
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)
  template = inspect.stack()[0][0].f_code.co_name
  page = __write_page(project_path, args.name, template)
  with open(page, "w") as f:
    f.write('''
from epyk_studio.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()
''')


def news(args):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param args:
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)
  template = inspect.stack()[0][0].f_code.co_name
  page = __write_page(project_path, args.name, template)
  with open(page, "w") as f:
    f.write('''
from epyk_studio.core.Page import Report


# Create a basic report object
page = Report()
page.headers.dev()
''')


def transpile_parser(subparser):
  """
  Description:
  ------------
  Paser for the transpile CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  subparser.set_defaults(func=transpile)
  subparser.add_argument('-n', '--name', help='''The name of the page to be transpiled (without the extension)''')
  subparser.add_argument('-p', '--path', help='''The path where the new environment will be created: -p /foo/bar''')


def transpile(args):
  """
  Description:
  ------------
  Transpile a specific report

  Attributes:
  ----------
  :param parser: -p, The path where the new environment will be created: -p /foo/bar
  :param parser: -n, The name of the page to be transpiled: -n home
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)
  report_path = utils.get_report_path(project_path, raise_error=False)
  sys.path.append(report_path)
  ui_setting_path = os.path.join(report_path, '..', 'ui_settings.py')
  install_modules, split_files, view_folder, settings = False, False, '../views', None
  if os.path.exists(ui_setting_path):
    sys.path.append(os.path.join(report_path, '..'))
    settings = __import__('ui_settings')
    install_modules = settings.INSTALL_MODULES
    split_files = settings.SPLIT_FILES
    if settings.PACKAGE_PATH is not None:
      Defaults.SERVER_PATH = settings.PACKAGE_PATH
  views = []
  if args.name is None:
    for v in os.listdir(report_path):
      if v.endswith(".py"):
        views.append(v[:-3])
  else:
    views = [args.name]
  for f in views:
    try:
      print("Transpiling files: %s" % f)
      mod = __import__(f, fromlist=['object'])
      page = utils.get_page(mod)
      if settings is not None:
        page.node_modules(settings.PACKAGE_PATH, alias=settings.SERVER_PACKAGE_URL)
      output = page.outs.html_file(path=view_folder, name=f, split_files=split_files, install_modules=install_modules,
                                   options={"css_route": '/css', "js_route": '/js'})
      print(output)
    except Exception as err:
      traceback.print_exception(*sys.exc_info())
      print("Error in the script %s" % f)


def run_parsers(subparser):
  subparser.set_defaults(func=run)
  subparser.add_argument('-p', '--port', default=8080, help='''Integer with the port for the app''')
  subparser.add_argument('-l', '--localhost', default="Y", help='''Y / N flag to specify the hostname to define''')
  subparser.add_argument('-d', '--debug', default="N", help='''Y / N flag to activate the debug mode of Tornado''')


def run(args):
  import socket
  import tornado.ioloop
  import epyk_studio.core.cli.Server
  import asyncio

  # https://github.com/tornadoweb/tornado/issues/2751
  if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

  address = '127.0.0.1'
  if args.localhost.upper() == 'N':
    address = socket.gethostbyname(socket.gethostname())
  print("Server started at: %s:%s" % (address, args.port))
  print("Project path: %s" % os.getcwd())
  app = epyk_studio.core.cli.Server.make_app(os.getcwd(), debug=args.debug.upper()=="Y")
  app.listen(args.port, address=address)
  tornado.ioloop.IOLoop.current().start()


def add_server_parser(subparser):
  """
  Description:
  ------------
  Paser for the transpile CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  subparser.set_defaults(func=add_server)
  subparser.add_argument('-n', '--name', help='''The name of the page to be transpiled (without the extension)''')
  subparser.add_argument('-p', '--path', help='''The path where the new environment will be created: -p /foo/bar''')
  subparser.add_argument('-s', '--server', help='''The path where the new environment will be created: -p /foo/bar''')


def add_server(args):
  project_path = args.path or os.getcwd()
  page = os.path.join(project_path, args.name, "server_%s.py" % args.server)
  static_path = os.path.join(project_path, args.name, "static")
  if not os.path.exists(static_path):
    os.makedirs(static_path)
  if args.server == 'tornado':
    with open(page, "w") as f:
      f.write('''
import socket
import os
import importlib
import sys
import tornado.ioloop

from epyk_studio.core.Page import Report


class MainHandlerPage(tornado.web.RequestHandler):

  def get(self, name):
    """
    Description:
    ------------

    """
    sys.path.append(os.path.join(os.getcwd(), 'ui'))
    mod = __import__("ui.reports.%s" % name, fromlist=['object'])
    importlib.reload(mod)
    if self.request.query_arguments:
      arguments = self.request.query_arguments
      data = {arg: self.get_argument(arg) for arg in arguments.keys()}
      if hasattr(mod, 'add_inputs'):
        mod.add_inputs(data)
    if hasattr(mod, 'get_page'):
      page = Report()
      page.inputs.update(data)
      mod.get_page(page)
      self.write(page.outs.html())
    else:
      self.write(mod.page.outs.html())


class MainHandlerView(tornado.web.RequestHandler):

  def get(self, name):
    """
    Description:
    ------------

    """
    content = ""
    html_file = os.path.join(os.getcwd(), 'ui', 'views', "%s.html" % name)
    if os.path.exists(html_file):
      with open(html_file) as f:
        content = f.read()
    if self.request.query_arguments:
      arguments = self.request.query_arguments
      data = {arg: self.get_argument(arg) for arg in arguments.keys()}
      for k, v in data.items():
        content = content.replace("%%(%s)s" % k, v)
    self.write(content)


def make_app(debug=True):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param debug:
  """
  pages_path = os.path.dirname(__file__)
  return tornado.web.Application([
      (r"/script/(.*)", MainHandlerPage, None),
      (r"/view/(.*)", MainHandlerView, None),
  ], debug=debug, static_path=os.path.join(pages_path, 'static'))


if __name__ == '__main__':
  address = socket.gethostbyname(socket.gethostname())
  port = 8081
  print("Server started at: %s:%s" % (address, port))
  app = make_app()
  app.listen(port, address=address)
  tornado.ioloop.IOLoop.current().start()
  ''')
  if args.server == 'flask':
    with open(page, "w") as f:
      f.write('''
import socket
import os
import sys
import importlib

from epyk_studio.core.Page import Report

from flask import Flask
from flask import request

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
  return 'Your project running with Flask!'


@app.route('/script/<script>')
def script(script):
  sys.path.append(os.path.join(os.getcwd(), 'ui'))
  mod = __import__("ui.reports.%s" % script, fromlist=['object'])
  importlib.reload(mod)
  data = dict(request.args)
  if hasattr(mod, 'get_page'):
    page = Report()
    page.inputs.update(data)
    mod.get_page(page)
    return page.outs.html()
  else:
    if data:
      if hasattr(mod, 'add_inputs'):
        mod.add_inputs(data)
    return mod.page.outs.html()


@app.route('/view/<page>')
def view(page):
  content = ""
  html_file = os.path.join(os.getcwd(), 'ui', 'views', "%s.html" % page)
  data = dict(request.args)
  if os.path.exists(html_file):
    with open(html_file) as f:
      content = f.read()
  for k, v in data.items():
    content = content.replace("%%(%s)s" % k, v)
  return content


if __name__ == '__main__':
  address = socket.gethostbyname(socket.gethostname())
  app.run(host=address, port=8081, debug=True)

''')


def main():
  """
  Description:
  ------------
  Main entry point for the various project command lines
  """
  parser_map = {
    'new': (new_parsers, '''Create new environment'''),
    'run': (run_parsers, '''start the internal tornado server'''),
    'transpile': (transpile_parser, '''Transpile a script to web objects'''),
    'dashboard': (new_template, '''Create new dashboard'''),
    'management': (new_template, '''Create new Management report'''),
    'shop': (new_template, '''Create new shop'''),
    'restaurant': (new_template, '''Create new restaurant'''),
    'blog': (new_template, '''Create new blog'''),
    'gallery': (new_template, '''Create new gallery'''),
    'dating': (new_template, '''Create new dating page'''),
    'wedding': (new_template, '''Create new wedding page'''),
    'show': (new_template, '''Create new show main page'''),
    'vitrine': (new_template, '''Create new vitrine / demo page'''),
    'news': (new_template, '''Create new news page'''),
  }
  arg_parser = argparse.ArgumentParser(prog='epyk_studio')
  subparser = arg_parser.add_subparsers(title='Commands', dest='command')
  subparser.required = True
  for func, parser_init in parser_map.items():
    new_parser = subparser.add_parser(func, help=parser_init[1])
    if func not in ['new', 'transpile']:
      new_parser.set_defaults(func=globals()[func])
    parser_init[0](new_parser)
  args = arg_parser.parse_args(sys.argv[1:])
  return args.func(args)
