
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar
from epyk.core.data import events


# Create a basic report object
page = Report()

nav = nav_bar(page, "Project")

c = page.ui.title("Create new report")
c.style.standard()

s_new = page.ui.input(htmlCode="name")
s_new.style.css.text_align = "left"
s_new.style.css.padding_left = 5
s_new.style.standard()

pills = page.ui.panels.pills(htmlCode="category")
pills.style.css.padding_bottom = 5
pills.style.css.padding_top = 5
pills.style.standard()

pills.add_panel("Page", None, selected=True)
pills.add_panel("Blog", None)
pills.add_panel("Gallery", None)
pills.add_panel("Dashboard", None)

b_new = page.ui.buttons.large("New Report", align="center")

wa = page.ui.title("Get web artifacts", align="center")
wa.style.css.margin_top = 30
wa.style.standard()
wp = page.ui.texts.text('''
Produce rich HTML pages from your Python code
''', align="center")
wp.style.standard()
wp.style.css.margin_bottom = 10

radios = page.ui.radio(['Single', 'Multiple'], htmlCode="trans_type", checked="Single", align="center")
radios.style.standard()

b_transpile = page.ui.buttons.large("Transpile Project", align="center")
b_transpile.style.css.margin_top = 10

s = page.ui.title("Attach a server", align="center")
s.style.css.margin_top = 30
s.style.standard()

pim = page.studio.pills.images([
  {"image": "flask.jpg", 'path': '/static', 'text': 'Flask'},
  {"image": "tornado.jpg", 'path': '/static', 'text': 'Tornado', 'selected': True},
  {"image": "fastapi-logo.png", 'path': '/static', 'text': 'FastAPI'},
  #{"image": "django-logo.png", 'path': '/static', 'text': 'Django'},
], radius=False, htmlCode="server", align="center")
pim.style.standard()

b_server = page.ui.buttons.large("Server", align="center")

t = page.ui.title("Scan external packages", align="center")
t.style.css.margin_top = 35
t.style.standard()
pr = page.ui.texts.text('''
Find an existing report in the project
''', align="center")
pr.style.standard()

p_packages = page.ui.buttons.large("Scan Packages", align="center")
p_packages.style.css.margin_bottom = 15
p_packages.style.css.margin_top = 10

table = page.ui.table(cols=['pkg'], rows=['vr', 'get'])
table.get_column('pkg').title = "Package"
table.get_column('vr').title = "Version"
table.get_column('get').title = "Install"
table.get_column('get').formatters.html()
table.style.standard()

add_code(page)

dis = page.ui.banners.disclaimer()
dis.style.css.margin_top = 20


def add_inputs(inputs):
  nav.title._vals = inputs.get('name', '')
  b_new.click([
    page.js.post("/projects_page_add", {'project': inputs.get('name', '')}, components=[s_new, pills])
  ])

  b_transpile.click([
    page.js.post("/projects_transpile", {'project': inputs.get('name', '')}, components=[radios]).onSuccess([
      page.js.msg.status()
    ])
  ])

  b_server.click([
    page.js.post("/projects_add_server", {'project': inputs.get('name', '')}, components=[pim])
  ])

  p_packages.click([
    page.js.post("/projects_get_packages", {'project': inputs.get('name', '')}).onSuccess([
      table.build(events.data["packages"])
    ])
  ])
