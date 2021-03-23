
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar

# Create a basic report object
page = Report()
nav_bar(page, 'Local Templates')

icon = page.web.bs.icons.danger()
icon.style.css.invisble()

mode_switch = page.ui.fields.toggle({"off": 'hidden', "on": "visible"}, is_on=True, label="", html_code="switch")
mode_switch.input.click([
  icon.dom.visible(mode_switch.input.dom.content)
])

t1 = page.ui.title("Templates structure")
tree = page.ui.trees.folder()
box = page.studio.containers.box()
box.extend([t1, icon, tree])
box.style.standard()

add_code(page)

