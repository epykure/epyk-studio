
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar
from epyk.core.data import events


# Create a basic report object
page = Report()
nav_bar(page, "Project")

title = page.ui.title("Start new project")
title.style.standard()
p_1 = page.ui.texts.paragraph('''
Create a brand new project. The project name will be used to defined the folder so please make sure it is not using some
special characters.
''')
p_1.style.standard()

inp = page.ui.input(placeholder="project's name", html_code="name")
inp.style.css.text_align = "left"
inp.style.css.padding_left = 5
inp.style.css.padding_right = 5
inp.style.standard()

get_started = page.ui.buttons.colored("Create", align="center")
get_started.style.css.margin_top = 10
get_started.click([
  page.js.post("/test", components=[inp]).onSuccess([
    page.js.msg.status(),
  ])
])

p = page.ui.texts.number(0, 'Projects', align="center")
p.style.css.font_factor(40)
p.title.style.css.font_factor(20)
p.title.style.css.color = page.theme.colors[-1]
p.style.css.margin_top = 20

t2 = page.ui.title("Find an existing projects")
t2.style.standard()

inp_pr = page.ui.input(placeholder="project's name", html_code="project")
inp_pr.style.css.text_align = "left"
inp_pr.style.css.padding_left = 5
inp_pr.style.css.padding_right = 5
inp_pr.style.standard()

find_project = page.ui.buttons.colored("Find", align="center")
find_project.style.css.margin_top = 10
find_project.style.css.margin_bottom = 10

items = page.ui.lists.items()
items.style.hover_border()
items.style.hover_background()
items.options.items_type = "link"
items.style.standard()

find_project.click([
  page.js.post('/projects_get', components=[inp_pr]).onSuccess([
    items.build(events.data['projects'])
  ])
])

inp_pr.enter([find_project.dom.events.trigger('click')])

d = page.studio.blog.delimiter()
d.style.css.margin_top = 30

t_3 = page.ui.title("Source Control")
t_3.style.standard()

p_3 = page.ui.texts.paragraph('''
Do not forget to use external source control for your project
''')
p_3.style.standard()

imgs = page.ui.menus.images([
  {"image": "https://subversion.apache.org/favicon.ico", "url": "https://subversion.apache.org/"},
  {"image": "https://github.com/favicon.ico", "url": "https://github.com/"},
  {"image": "https://bitbucket.org/favicon.ico", "url": "https://bitbucket.org/product"},
])
imgs.style.standard()

add_code(page)
dis = page.ui.banners.disclaimer()
dis.style.css.margin_top = 20


def add_inputs(inputs):
  p._vals = inputs.get('count_projects', 0)
