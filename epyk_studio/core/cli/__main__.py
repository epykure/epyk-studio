import sys
import os
import socket
import tornado.ioloop
import epyk_studio.core.server.app
from epyk.core.js import Imports
from epyk.core.css import themes
import asyncio
import json

from epyk_studio.utils import sys_files

PORT = 8080
LOCALHOST = False
DEBUG = True


def set_app(port, local, debug):
  """
  Description:
  ------------
  Entry point to start the local app used by the run command in the CLI.
  This will then run the start method to start the internal Tornado server.

  Attributes:
  ----------
  :param port: Integer. The port for the server.
  :param local: String. The URL / hostname.
  :param debug: Boolean. Flag to set the app in debug mode.
  """
  global PORT
  global LOCALHOST
  global DEBUG

  LOCALHOST = local
  DEBUG = debug
  PORT = port
  start()


def set_env():
  """
  Description:
  ------------
  Main entry point for the Tornado server in charge of building the Studio workspace.
  The Studio will get multiple projects and each project will be using multiple web pages.

  The servers used by the various projects can be different. The studio purpose is to help on the implementation
  and also to simplify the testing and integration with a web project.
  """
  temps_folder = os.path.join(os.getcwd(), sys_files.STUDIO_FILES["history"]["path"])
  is_env_updated = False
  if not os.path.exists(temps_folder):
    os.mkdir(temps_folder)
    with open(os.path.join(temps_folder, sys_files.STUDIO_FILES["history"]["file"]), "w") as fp:
      fp.write("[]")
    is_env_updated = True

  styles_folder = os.path.join(os.getcwd(), sys_files.STUDIO_FILES["cls"]["path"])
  if not os.path.exists(styles_folder):
    os.mkdir(styles_folder)
    with open(os.path.join(styles_folder, sys_files.STUDIO_FILES["cls"]["file"]), "w") as fp:
      json.dump({
        "CLS_OVERRIDES": {}, "COMPONENTS_OVERRIDES": {}, "DARK_MODE": False, "BASE_COLOR_INDEX": 5,
        "THEME": "ThemeRed.Red", "THEMES": {}, "CHART_COLORS": [], "SKIN": "",
      }, fp, indent=4)
    with open(os.path.join(styles_folder, sys_files.STUDIO_FILES["packages"]["file"]), "w") as fp:
      json.dump({"FORBIDDEN": [], "PACKAGE_VERSIONS": {}}, fp, indent=4)
    is_env_updated = True
  sandbox_folder = os.path.join(os.getcwd(), sys_files.STUDIO_FILES["sandbox"]["path"])
  if not os.path.exists(sandbox_folder):
    os.mkdir(sandbox_folder)
  return is_env_updated


def start():
  """
  Description:
  ------------
  Start the local server.
  """
  if sys.platform == 'win32' and hasattr(asyncio, 'WindowsSelectorEventLoopPolicy'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  address = socket.gethostbyname(socket.gethostname()) if not LOCALHOST else '127.0.0.1'
  print("Server started at: %s:%s" % (address, PORT))
  print("Project path: %s" % os.getcwd())
  if set_env():
    print("Env files created / updated !")
  styles_folder = os.path.join(os.getcwd(), sys_files.STUDIO_FILES["cls"]["path"])
  with open(os.path.join(styles_folder, sys_files.STUDIO_FILES["cls"]["file"]), "r") as fp:
    content = json.load(fp)
    os.environ["DARK_MODE"] = 'Y' if content["DARK_MODE"] else 'N'
    os.environ["THEME"] = content["THEME"]
    os.environ["SKIN"] = content["SKIN"]
    os.environ["BASE_COLOR_INDEX"] = str(content["BASE_COLOR_INDEX"])
    for k, v in content["THEMES"].items():
      themes.REGISTERED_THEMES.append({
        "value": 'Theme.Theme%s' % k, 'name': '', 'content': themes.DIV_STYLE % (v[content["BASE_COLOR_INDEX"]], k),
      })
      dyn_cls = type('Theme%s' % k, (themes.Theme.ThemeDefault,), {})
      dyn_cls._colors = v
      setattr(themes.Theme, 'Theme%s' % k, dyn_cls)
  with open(os.path.join(styles_folder, sys_files.STUDIO_FILES["packages"]["file"]), "r") as fp:
    content = json.load(fp)
    if content["FORBIDDEN"]:
      Imports.PACKAGE_STATUS = {m: {"allowed": False} for m in content["FORBIDDEN"]}
    if content["PACKAGE_VERSIONS"]:
      for k, v in content["PACKAGE_VERSIONS"].items():
        Imports.JS_IMPORTS[k]["version"] = v
  app = epyk_studio.core.server.app.make_app(os.getcwd(), debug=DEBUG)
  app.listen(PORT, address=address)
  tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
  start()
