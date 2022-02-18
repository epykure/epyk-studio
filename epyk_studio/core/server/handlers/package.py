
import tornado.web
import tornado.escape

from epyk.core.js import Imports


class Packages(tornado.web.RequestHandler):

  def get(self):
    """
    Description:
    ------------

    """

    js_alias = [self.get_argument("p")]
    Imports.npm(js_alias, self.application.settings.get('studio_path'))
    self.write({'status': "%s - package downloaded" % js_alias[0]})

  def post(self):
    """
    Description:
    ------------
    Get all the JavaScript External packages with a structure similar to the one in NodeJs
    """
    if self.request.body:
      data = tornado.escape.json_decode(self.request.body)
      js_alias = data["packages"].split(",")
    else:
      js_alias = list(Imports.JS_IMPORTS.keys())
      for k in Imports.CSS_IMPORTS.keys():
        if k not in js_alias:
          js_alias.append(k)
    Imports.npm(js_alias, self.application.settings.get('studio_path'))
    self.write({'status': "All packages downloaded"})
