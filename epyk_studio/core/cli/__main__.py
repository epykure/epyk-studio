import sys
import os
import socket
import tornado.ioloop
import epyk_studio.core.cli.Server
import asyncio

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
  :param debug: Boolean. Flag to set the app in debug mode
  """
  global PORT
  global LOCALHOST
  global DEBUG

  LOCALHOST = local
  DEBUG = debug
  PORT = port
  start()


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
  app = epyk_studio.core.cli.Server.make_app(os.getcwd(), debug=DEBUG)
  app.listen(PORT, address=address)
  tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
  start()
