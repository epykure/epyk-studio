
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar


# Create a basic report object
page = Report()

nav_bar(page, "Blog Editor")

pills = page.ui.menus.pills(["Title", 'Paragraph', 'Link', 'Wallpaper', 'Image', 'Delimiter'])
pills.style.standard()
tabs = page.ui.panels.tabs()
tabs.style.standard()

editor = page.ui.codes.python('''
def test():
  print('ok')
''')

iframe = page.ui.layouts.iframe()

tabs.add_panel("Editor", page.ui.div(editor), selected=True)
tabs.add_panel("Result", page.ui.div(iframe))

pills[0].click([
  editor.build("page.ui.title('vhbr')")
])

input = page.ui.input(placeholder="Page name")
input.style.css.margin_top = 10
input.style.standard()

save = page.ui.buttons.large("Save", align="center")
save.style.css.margin_top = 10
save.style.standard()

add_code(page)
