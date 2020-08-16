
import os
import sys
import argparse
import inspect


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
  subparser.add_argument('-n', '--name', default='NewEnv', help='''The name of the new environment: -n MyEnv''')


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
  subparser.set_defaults(func=new)
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


def main():
  """
  Description:
  ------------
  Main entry point for the various project command lines
  """
  parser_map = {
    'new': (new_parsers, '''Create new environment'''),
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
    parser_init[0](new_parser)
  args = arg_parser.parse_args(sys.argv[1:])
  return args.func(args)

