
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar


# Create a basic report object
page = Report()
nav_bar(page, "Code Viewer")

bc = page.ui.breadcrumb([
  {"text": 'Docs', 'url': 'https://www.tornadoweb.org/en/stable/index.html'},
  {"text": 'Web framework', 'url': 'https://www.tornadoweb.org/en/stable/webframework.html'},
], selected="Docs")
bc.style.css.background = None
bc.style.css.margin = "0 10%"

container = page.ui.div()
container.style.standard()

python = page.ui.codes.python(height=(100, '%'))
python.options.readOnly = True
python.options.lineNumbers = False
container.add(python)

dis = page.ui.banners.disclaimer()
dis.style.css.margin_top = 20

add_code(page)
