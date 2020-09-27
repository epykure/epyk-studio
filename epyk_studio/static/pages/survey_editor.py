
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar


# Create a basic report object
page = Report()
nav_bar(page, "Survey Editor")


add_code(page)
