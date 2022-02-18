
import os

from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar
from epyk_studio.utils import sys_files
from epyk.core.data import events


# Create a basic report object
page = Report()
nav_bar(page, "Designer")
anchor = page.ui.buttons.large("Templates", align="center")
page.ui.navigation.side(position="left", anchor=anchor)
t1 = page.ui.title("Quick start")
p = page.ui.texts.paragraph('''
Create your first dashboards without having anything installed.

Ideal for Manager or Product owners eager to illustrate the renderer of the final web template quickly.
This will ensure a perfect understanding and a good basis to start the implementation.
''')

reset = page.ui.buttons.large("Reset", align="center")
title_comps = page.ui.title("Add components")

components = {
  'Title': "page.ui.title('This is a title')",
  'Paragraph': "page.ui.texts.paragraph('This is a paragraph')",
  'Link': "page.ui.link('google', 'www.google.com')",
  'Image': "page.ui.img('%s/epykure/epyk-ui/master/epyk/static/images/epyklogo.ico', height=(50, 'px'))" % sys_files.GITHUB_PATHS["api"],
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
rpt_link = page.ui.rich.search_input(
  placeholder="put the link to the report, e.g: %s/epykure/epyk-templates/master/locals/texts/editor.py" % sys_files.GITHUB_PATHS["api"], html_code="rpt_path")
rpt_page = page.ui.links.colored("Full page")

rpt_save = page.ui.icon("fas fa-save", tooltip="Save file")
rpt_save.style.css.margin_right = 10
rpt_square = page.ui.icon("fas fa-share-square", tooltip="Open in new page")

rpt_filename = page.ui.inputs.left(placeholder="extra classpath for this report", html_code="rpt_name", width=(150, "px"))
rpt_filename.style.css.margin_right = 10
rpt_filename.style.css.background = None
rpt_filename.style.css.border = None
rpt_filename.style.css.border_radius = 0
rpt_filename.style.css.border_bottom = "1px solid %s" % page.theme.colors[-1]

ext_rpt = page.ui.panels.sliding([rpt_classpath, rpt_link], "External report")
ext_rpt.options.expanded = False

tabs.add_panel("Editor", page.ui.col([
  ext_rpt,
  page.ui.div([rem_last_cange, redo_last_cange]).css({"margin-top": '10px'}),
  editor]), selected=True)
tabs.add_panel("Web", [page.ui.div([rpt_filename, rpt_save, rpt_square]), page.ui.div(iframe)])

rpt_save.click(page.js.post("/code", components=[rpt_filename, editor]))
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


def add_inputs(inputs):
  i = 0
  while True:
    next_script = os.path.join(inputs["current_path"], sys_files.STUDIO_FILES["sandbox"]["path"], "new_page_%s.py" % i)
    if not os.path.exists(next_script):
      rpt_filename.value("new_page_%s.py" % i)
      break

    i += 1

