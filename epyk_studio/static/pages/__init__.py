
import inspect


def nav_bar(page, name):
  """

  :param page:
  :param name:
  """
  nav = page.ui.navbar(title=name)
  nav.add_right(page.studio.langs())
  nav.add_right(page.studio.themes(selected="ThemeRed.Red"))
  nav._right.style.css.padding_right = 60
  page.ui.banners.corner("Localhost", position="top")
  nav.logo.goto("/", name="_self")
  return nav


def add_code(page):
  """

  :param page:
  """
  frm = inspect.stack()[1]
  code = page.ui.icon("fas fa-code")
  code.style.css.fixed(bottom=20, right=20)
  code.goto("/code?script=%s" % inspect.getmodule(frm[0]).__name__.split(".")[-1], name="_self")
  code.style.add_classes.div.border_hover()
  code.style.css.border_radius = 15
  code.style.css.padding = 8
  code.style.css.background = page.theme.greys[0]
  return code

