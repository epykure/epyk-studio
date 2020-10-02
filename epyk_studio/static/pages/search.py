
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar
from epyk.core.data import events


# Create a basic report object
page = Report()

nav_bar(page, "Search")

title = page.ui.title("Components search")
title.style.standard()

page.ui.chips([

])

search = page.ui.inputs.search(htmlCode='input')
search.style.standard()

pills = page.ui.panels.pills(htmlCode="category")
pills.style.css.padding_bottom = 5
pills.style.css.padding_top = 5
pills.style.standard()

pills.add_panel("All", None, icon="fas fa-shield-alt", width=(40, 'px'))
pills.add_panel("Text", None, icon="fas fa-paragraph", width=(40, 'px'))
pills.add_panel("Inputs", None, icon="fas fa-pencil-alt", width=(40, 'px'))
pills.add_panel("Image", None, icon="fas fa-images", width=(40, 'px'))
pills.add_panel("Chart", None, icon="fas fa-chart-pie", width=(40, 'px'))
pills.add_panel("Table", None, icon="fas fa-table", width=(40, 'px'))
pills.add_panel("Layout", None, icon="fas fa-border-none", width=(40, 'px'))
pills.add_panel("Studio", None, icon="fas fa-puzzle-piece", width=(40, 'px'))

button = page.ui.buttons.large("Search", align="center")
button.style.css.margin_top = 10

search_results = page.ui.rich.search_results()
search_results.style.standard()

button.click([
  page.js.post("/search_post", components=[search, pills]).onSuccess([
    search_results.build(events.data['results']),
    page.js.msg.status(),
  ])
])

search.enter(button.dom.events.trigger("click"))

code = page.ui.icon("fas fa-code")
code.style.css.absolute(bottom=20, right=20)
code.goto("/code?script=home")

add_code(page)

dis = page.ui.banners.disclaimer()
dis.style.css.margin_top = 20