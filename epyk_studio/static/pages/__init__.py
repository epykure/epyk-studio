
import inspect
import os


def nav_bar(page, name, title=None, dark=False):
  """
  Description:
  ------------
  Add the framework navigation bar.

  Attributes:
  ----------
  :param page: Report. The page object.
  :param name: String. The current page title.
  :param title. String. Optional.
  :param dark. Boolean. Optional.
  """
  if title is not None:
    page.headers.title(title)
  nav = page.ui.navbar(title=name)
  select_themes = page.studio.themes(selected=os.environ.get("THEME", "Theme.ThemeDefault"), options={
    "dark": os.environ.get("DARK_MODE", dark) == 'Y', "base_color_index": os.environ.get("BASE_COLOR_INDEX", 5)})
  select_themes.attr["data-background"] = page.theme.colors[0]
  nav.set_theme()

  langs = page.studio.langs()
  langs.attr["data-background"] = page.theme.colors[0]

  div_lag = page.ui.div(langs, width="auto")
  div_lag.style.css.margin_right = 10
  div_lag.style.css.line_height = 20
  nav.add_right(div_lag)

  div_themes = page.ui.div(select_themes, width="auto")
  div_themes.style.css.margin_right = 30
  div_themes.style.css.line_height = 20
  nav.add_right(div_themes)

  nav._right.style.css.padding_right = 60
  page.ui.banners.corner("Beta", position="top")
  nav.logo.goto("/", target="_self")
  page.skins.set(os.environ.get("SKIN", ""))
  return nav


def add_code(page, doc_only=False):
  """
  Description:
  ------------
  Add generic framework and shortcut features.
  This will add the link to the code source or a shortcut link to the documentation.

  Attributes:
  ----------
  :param page: Report. The page object.
  :param doc_only:
  """
  frm = inspect.stack()[1]

  # Add shortcut for the documentation
  doc_link = page.ui.icon("fas fa-book-reader")
  doc_link.style.css.fixed(bottom=20 if doc_only else 60, right=20)
  doc_link.goto("/docs")
  doc_link.style.configs.rounded_icons()
  doc_link.style.css.background = page.theme.colors[0]

  if not doc_only:
    # Add shortcut to see the source code of the page
    code = page.ui.icon("fas fa-code")
    code.style.css.fixed(bottom=20, right=20)
    code.style.css.z_index = 10
    code.goto("/code?script=%s" % inspect.getmodule(frm[0]).__name__.split(".")[-1], target="_self")
    code.style.configs.rounded_icons()
    code.style.css.background = page.theme.greys[0]
    return code

  return doc_link

