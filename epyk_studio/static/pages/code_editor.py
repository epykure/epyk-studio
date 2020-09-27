
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar

page = Report()

nav_bar(page, "Code Editor")

add_code(page)
