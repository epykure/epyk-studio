
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar
from epyk.core.data import events


# Create a basic report object
page = Report()

nav_bar(page, "Designer")

p = page.ui.texts.paragraph('''
Create your first dashboards without having anything installed.

Ideal for Manager or Product owners eagger to illustrate the renderer of the final web template quickly.
This will ensure a perfect understanding and a good basis to start the implementation.
''')
p.style.standard()

title = page.ui.title("Add components")
title.style.standard()

pills = page.ui.menus.pills(["Title", 'Paragraph', 'Link', 'Wallpaper', 'Image', 'Delimiter'])
pills.style.standard()

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
tabs.add_panel("Result", page.ui.div(iframe))

pills[0].click([
  tabs.tab("Editor").dom.events.trigger("click"),
  editor.dom.appendText("page.ui.title('vhbr')")
])

tabs.tab("Result").click([
  page.js.post("/code_frame", components=[editor]).onSuccess([
      iframe.dom.srcdoc(events.data["page"])
  ])
])

title = page.ui.title("Ger result")
title.style.standard()

script = page.ui.buttons.large("Python", icon="fab fa-python", align="center")
script.style.css.margin_top = 10

html = page.ui.buttons.large("HTML", icon="fab fa-html5", align="center")
html.style.css.margin_top = 10


row = page.ui.row([
  [script, "share"],
  [html]], options={"responsive": False})
row.style.standard()

add_code(page)


dis = page.ui.banners.disclaimer()
dis.style.css.margin_top = 20

