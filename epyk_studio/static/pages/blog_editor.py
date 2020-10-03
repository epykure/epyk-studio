
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar


# Create a basic report object
page = Report()

nav_bar(page, "Designer Mode")

title = page.ui.title("Add components")
title.style.standard()

pills = page.ui.menus.pills(["Title", 'Paragraph', 'Link', 'Wallpaper', 'Image', 'Delimiter'])
pills.style.standard()

title = page.ui.title("Previews")
title.style.standard()

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

