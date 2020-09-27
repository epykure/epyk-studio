
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar


# Create a basic report object
page = Report()

nav_bar(page, 'Tutorials')

t1 = page.ui.title("Start a new project")
t1.style.standard()

l1 = page.ui.link("Create new project", align="center")
l1.style.standard()

t2 = page.ui.title("Create a new page")
t2.style.standard()

p1 = page.ui.texts.paragraph('''
Epyk will allow you to create rich web templates using all the modern HTML5, CSS3 and JavaSript features.

''')
p1.style.standard()

l2 = page.ui.link("Create new page", align="center")
l2.style.standard()


t3 = page.ui.title("Search for examples")
t3.style.standard()

search = page.ui.inputs.search(htmlCode='input')
search.style.standard()

add_code(page)
