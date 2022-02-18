
import os
import tornado.web


class DocHandler(tornado.web.RequestHandler):

  def data_received(self, chunk):
    pass

  def get(self):
    """
    Description:
    -----------

    """
    from epyk_studio.static import lang

    rubric = self.get_argument("r", "home")
    md_path = os.path.join(
      os.path.dirname(__file__), '..', '..', '..', 'static', 'docs', "%s_%s.md" % (rubric, lang.get_alias()))
    if not os.path.exists(md_path):
      md_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'static', 'docs', "%s_eng.md" % rubric)
    if os.path.exists(md_path):
      from epyk_studio.core.Page import Report
      from epyk_studio.static.pages import add_code, nav_bar

      page = Report()
      nav_bar(page, "EpykDocs: %s" % rubric)
      with open(md_path) as fp:
        components = page.py.markdown.resolve(fp.read())
        box = page.studio.containers.box()
        box.extend(components)
        box.style.standard()
      add_code(page, doc_only=True)
      page.ui.banners.disclaimer()
      self.write(page.outs.html())
