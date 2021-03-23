
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar
from epyk.core.data import events


# Create a basic report object
page = Report()
nav_bar(page, "Designer")
anchor = page.ui.buttons.large("Templates", align="center")
page.ui.navigation.side(position="left", anchor=anchor)
t1 = page.ui.title("Quick start")
p = page.ui.texts.paragraph('''
Create your first dashboards without having anything installed.

Ideal for Manager or Product owners eagger to illustrate the renderer of the final web template quickly.
This will ensure a perfect understanding and a good basis to start the implementation.
''')

reset = page.ui.buttons.large("Reset", align="center")
title_comps = page.ui.title("Add components")

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

check = page.ui.check(True, label="Add at the end", html_code="to_end")
check.click([])

title = page.ui.title("Previews")
tabs = page.ui.panels.tabs()

editor = page.ui.codes.python('''
# Epyk Designer

from epyk_studio.core.Page import Report

page = Report()
''', html_code="editor")
editor.addon.search()
editor.addon.foldcode()
editor.options.hintOptions.hint([[
  "text", "paragraph", "image"
]])

editor.addon.highlighter()
editor.addon.trailingspace()
editor.addon.fullscreen()
editor.placeholder("Put your python code here...")

iframe = page.ui.layouts.iframe(height=(600, 'px'))
iframe.style.css.border = "1px solid %s" % page.theme.greys[2]
iframe.style.css.padding = 5
iframe.scrolling()

rem_last_cange = page.ui.button("Undo", icon="fas fa-caret-left")
rem_last_cange.style.border = None

redo_last_cange = page.ui.button("Redo", icon="fas fa-caret-right")
redo_last_cange.style.border = None
redo_last_cange.style.margin_left = 15

rpt_classpath = page.ui.input(placeholder="extra classpath for this report", html_code="rpt_classpath")
rpt_classpath.style.css.text_align = "left"
rpt_classpath.style.css.padding_left = 5
rpt_link = page.ui.rich.search_input(placeholder="put the link to the report, e.g: https://raw.githubusercontent.com/epykure/epyk-templates/master/locals/texts/editor.py", html_code="rpt_path")
rpt_page = page.ui.links.colored("Full page")

ext_rpt = page.ui.panels.sliding([rpt_classpath, rpt_link, rpt_page], "External report")
ext_rpt.options.expanded = False

tabs.add_panel("Editor", page.ui.col([
  page.ui.div([rem_last_cange, redo_last_cange]).css({"margin-top": '10px'}),
  editor]), selected=True)
tabs.add_panel("Web", [ext_rpt, page.ui.div(iframe)])

rem_last_cange.click([editor.js.undo()])
redo_last_cange.click([editor.js.redo()])

for i, items in enumerate(components.items()):
  pills[i].click([
    tabs.tab("Editor").dom.events.trigger("click"),
    editor.dom.appendText(items[1], check.dom.content)
  ])

tabs.tab("Web").click([
  page.js.post("/code_frame", components=[editor]).onSuccess([
      iframe.dom.srcdoc(events.data["page"]),
  ])
])

reset.click([
  tabs.tab("Editor").dom.events.trigger("click"),
  editor.build('''# Epyk Designer
  
from epyk_studio.core.Page import Report

page = Report()
''')
])

rpt_link.enter([
  page.js.post("/code_frame", components=[rpt_classpath, rpt_link]).onSuccess([
    editor.build(events.data["content"]),
    iframe.dom.srcdoc(events.data["page"]),
    rpt_page.dom.url(events.data["link"]),
    rpt_page.dom.css({"display": 'inline-block'})
  ])
])
# C:\TestStudio\Studio\ui\reports\tmpl_2.py

rpt_link.input.change([rpt_page.dom.css({"display": 'none'})])

script = page.ui.icon("fab fa-python", color=page.theme.greys[0])
script.style.css.fixed(top=60, right=20)
script.style.add_classes.div.border_hover()
script.style.css.border_radius = 15
script.style.css.padding = 8
script.style.css.background = page.theme.colors[-1]

html = page.ui.icon("fab fa-html5", color=page.theme.greys[0])
html.style.css.fixed(top=100, right=20)
html.style.add_classes.div.border_hover()
html.style.css.border_radius = 15
html.style.css.padding = 8
html.style.css.background = page.theme.colors[-1]

box = page.studio.containers.box()
box.extend([
  t1, p, page.ui.row([reset, anchor], options={"responsive": False}), title_comps, pills, check, title, tabs
])
box.style.standard()

add_code(page)


dis = page.ui.banners.disclaimer()
dis.style.css.margin_top = 20

