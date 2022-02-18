"""
Internal module to start the webserver which will drive the creation of a project locally.
"""

import tornado.web
import os

from epyk_studio.core.server import handlers


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
      (r"/", handlers.page.PageHandler),
      (r"/test", handlers.project.CreateHandler),

      #(r"/static/configs/(.*).json", tornado.web.StaticFileHandler, {"path": "./TestStudio/Studio/configs/eng/blotter.json"},),
      #(r'/static/(.*).json', MyFileHandler, dict(path="/Studio/static/", current_path=current_path)),

      #
      (r"/docs", handlers.doc.DocHandler),

      #
      (r"/catalog", handlers.page.PageHandler),

      #
      (r"/search", handlers.page.PageHandler),
      (r"/search_result", handlers.search.SearchResultHandler),
      (r"/search_post", handlers.search.SearchHandler),

      #
      (r"/ext_packages", handlers.page.PageHandler),
      (r"/get/packages", handlers.package.Packages),

      #
      (r"/analytics", handlers.page.PageHandler),
      (r"/tutorials", handlers.page.PageHandler),
      (r"/servers", handlers.page.PageHandler),
      (r"/databases", handlers.page.PageHandler),

      #
      (r"/templates", handlers.page.PageHandler),
      (r"/template", handlers.page.PageHandler),
      (r"/themes", handlers.page.PageHandler),

      #
      (r"/project", handlers.page.PageHandler),
      (r"/project_page", handlers.page.PageHandler),
      (r"/projects_page_add", handlers.page.AddHandler),
      (r"/projects_get_packages", handlers.project.GetExtHandler),
      (r"/projects_transpile", handlers.project.TranspileHandler),
      (r"/projects_add_server", handlers.project.AddServerHandler),
      (r"/projects_get", handlers.project.GetAllHandler),

      #
      (r"/code", handlers.code.CodeHandler),
      (r"/code_editor", handlers.page.PageHandler),
      (r"/code_frame", handlers.code.CodeFrameHandler),
  ], debug=debug,
    static_path=os.path.join(pages_path, '..', '..', 'static', 'images'),
    studio_path=current_path
  )



