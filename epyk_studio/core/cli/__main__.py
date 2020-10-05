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

  :param port:
  :param local:
  :param debug:
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

  """
  if sys.platform == 'win32' and hasattr(asyncio, 'WindowsSelectorEventLoopPolicy'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

  address = '127.0.0.1'
  if not LOCALHOST:
    address = socket.gethostbyname(socket.gethostname())
  print("Server started at: %s:%s" % (address, PORT))
  print("Project path: %s" % os.getcwd())
  app = epyk_studio.core.cli.Server.make_app(os.getcwd(), debug=DEBUG)
  app.listen(PORT, address=address)
  tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
  start()
