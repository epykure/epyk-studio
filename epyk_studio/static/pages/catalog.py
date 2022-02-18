
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import nav_bar


# Create a basic report object
page = Report()
nav_bar(page, "Examples Catalog")
div = page.ui.div()

for tuto in range(10):
  title = page.ui.titles.category("Test")
  text = page.ui.text("This is a text")
  author = page.ui.text("@Epykure", align="right")
  author.style.css.italic()
  author.style.css.font_factor(-2)
  author.style.css.margin_top = 5

  menu = page.ui.icons.menu([
    {"icon": "fab fa-github-square", "tooltip": "Github path", 'url': 'goo'},
    {"icon": "far fa-eye", 'url': r'/code_frame?classpath=&script='},
    {"icon": "fas fa-file-code", 'url': '/code_editor'}
  ])

  box = page.ui.div([title, text, menu, author], width="auto")
  box.style.add_classes.shapes.page()
  box.style.css.margin_left = 5
  box.style.css.margin_right = 5
  box.style.css.margin_bottom = 10
  box.style.css.margin_top = 10
  div.add(box)
