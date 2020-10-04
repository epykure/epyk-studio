
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar
from epyk.core.data import events


# Create a basic report object
page = Report()

nav_bar(page, "Designer")

anchor = page.ui.buttons.large("Templates", align="center")

page.ui.navigation.side(position="left", anchor=anchor)

p = page.ui.texts.paragraph('''
Create your first dashboards without having anything installed.

Ideal for Manager or Product owners eagger to illustrate the renderer of the final web template quickly.
This will ensure a perfect understanding and a good basis to start the implementation.
''')
p.style.standard()

reset = page.ui.buttons.large("Reset", align="center")
page.ui.row([reset, anchor], options={"responsive": False})

title = page.ui.title("Add components")
title.style.standard()

components = {
  'Title': "page.ui.title('This is a title')",
  'Paragraph': "page.ui.texts.paragraph('This is a paragraph')",
  'Link': "page.ui.link('google', 'www.google.com')",
  'Image': "page.ui.img('https://raw.githubusercontent.com/epykure/epyk-ui/master/epyk/static/images/epyklogo.ico', height=(50, 'px'))",
  'Delimiter': "page.ui.layouts.hr()",
  'New Line': "page.ui.layouts.br()",
  'Button': "page.ui.buttons.large('Button')",
  'Table': "page.ui.table([{'y': 43, 'x': 0}, {'y': 83, 'x': 0}])",
  'Pie': "page.ui.charts.chartJs.pie([{'y': 43, 'x': 0}, {'y': 83, 'x': 0}], y_columns=['y'], x_axis='x')",

}
pills = page.ui.menus.pills(list(components.keys()), height=(30, 'px'))
pills.style.css.margin_bottom = 0
pills.style.standard()

check = page.ui.check(True, label="Add at the end", htmlCode="to_end")
check.style.standard()
check.click([])

title = page.ui.title("Previews")
title.style.standard()

tabs = page.ui.panels.tabs()
tabs.style.standard()

editor = page.ui.codes.python('''
from epyk_studio.core.Page import Report

page = Report()
''', htmlCode="editor")

iframe = page.ui.layouts.iframe(height=(600, 'px'))
iframe.style.css.border = "1px solid %s" % page.theme.greys[2]
iframe.style.css.padding = 5
iframe.scrolling()

tabs.add_panel("Editor", page.ui.div(editor), selected=True)
tabs.add_panel("Web", page.ui.div(iframe))

for i, items in enumerate(components.items()):
  pills[i].click([
    tabs.tab("Editor").dom.events.trigger("click"),
    editor.dom.appendText(items[1], check.dom.content)
  ])

tabs.tab("Web").click([
  page.js.post("/code_frame", components=[editor]).onSuccess([
      iframe.dom.srcdoc(events.data["page"])
  ])
])


reset.click([
  editor.build('''from epyk_studio.core.Page import Report

page = Report()
''')
])


script = page.ui.icon("fab fa-python", color="white")
script.style.css.fixed(top=60, right=20)
script.style.add_classes.div.border_hover()
script.style.css.border_radius = 15
script.style.css.padding = 8
script.style.css.background = page.theme.colors[-1]

html = page.ui.icon("fab fa-html5", color="white")
html.style.css.fixed(top=100, right=20)
html.style.add_classes.div.border_hover()
html.style.css.border_radius = 15
html.style.css.padding = 8
html.style.css.background = page.theme.colors[-1]

add_code(page)


dis = page.ui.banners.disclaimer()
dis.style.css.margin_top = 20

