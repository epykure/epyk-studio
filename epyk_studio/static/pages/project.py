
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar
from epyk.core.data import events


# Create a basic report object
page = Report()
page.body.style.css.margin = "0 10%"

nav_bar(page, "Project")

page.ui.title("Start new project")
page.ui.texts.paragraph('''
Create a brand new project
''')

inp = page.ui.input(htmlCode="name")
inp.style.css.text_align = "left"
inp.style.css.padding_left = 5
inp.style.css.padding_right = 5

get_started = page.ui.buttons.large("Create")
get_started.style.css.margin_right = 10
get_started.click([
  page.js.post("/test", components=[inp]).onSuccess([
    page.js.msg.status(),
  ])
])

av = page.ui.images.circular(image="dashboards.PNG", path=r"https://raw.githubusercontent.com/epykure/epyk-studio/master/static", width=(200, 'px'), height=(200, 'px'), align="center")
av.style.css.margin_top = 20
av.style.css.margin_bottom = 20


t2 = page.ui.title("Find an existing projects")

inp_pr = page.ui.input(htmlCode="project")
inp_pr.style.css.text_align = "left"
inp_pr.style.css.padding_left = 5
inp_pr.style.css.padding_right = 5

items = page.ui.lists.items()
items.style.hover_border()
items.style.hover_background()
items.options.items_type = "link"

inp_pr.enter(
  page.js.post('/projects_get', components=[inp_pr]).onSuccess([
      items.build(events.data['projects'])
  ])
)

page.ui.title("Source Control")
page.ui.texts.paragraph('''
Do not forget to use external source control for your project
''')


page.ui.menus.images([
  {"image": "https://subversion.apache.org/favicon.ico", "url": "https://subversion.apache.org/"},
  {"image": "https://github.com/favicon.ico", "url": "https://github.com/"},
  {"image": "https://bitbucket.org/favicon.ico", "url": "https://bitbucket.org/product"},
])

add_code(page)

dis = page.ui.banners.disclaimer()
dis.style.css.margin_top = 20
