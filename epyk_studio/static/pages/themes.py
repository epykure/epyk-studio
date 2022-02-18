
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar

# Create a basic report object
page = Report()
page.body.add_template(defined_style="doc")
nav_bar(page, 'Themes / Colors', dark=True)

t1 = page.ui.title("Themes")
page.ui.titles.underline()
p1 = page.ui.paragraph('''
Those are the colors codes predefined for this theme which can be used directly from the page.theme property.
It is possible to change or update themes.
''')
colors_container = page.ui.div([page.ui.titles.subtitle("Colors", align="center")], width=(100, 'px'))
colors_container.style.css.vertical_align = "top"
colors_container.style.css.margin = "0 2px"
for i, k in enumerate(page.theme.colors):
  div = page.ui.div(k, width=(100, 'px'))
  div.style.css.background = k
  div.style.css.text_align = "center"
  if i == page.theme.index:
    div.style.css.border = "2px solid %s" % page.theme.colors[-1]
    div.style.css.margin = "2px 0"
  colors_container.add(div)

greys_container = page.ui.div([page.ui.titles.subtitle("Greys", align="center")], width=(100, 'px'))
greys_container.style.css.vertical_align = "top"
greys_container.style.css.margin = "0 2px"
for i, k in enumerate(page.theme.greys):
  div = page.ui.div(k, width=(100, 'px'))
  div.style.css.background = k
  div.style.css.color = page.theme.greys[-1] if i == 0 else page.theme.greys[-i]
  div.style.css.text_align = "center"
  greys_container.add(div)

charts_container = page.ui.div([page.ui.titles.subtitle("Charts", align="center")], width=(100, 'px'))
charts_container.style.css.vertical_align = "top"
charts_container.style.css.margin = "0 2px"
for k in page.theme.charts:
  div = page.ui.div(k, width=(100, 'px'))
  div.style.css.background = k
  div.style.css.text_align = "center"
  charts_container.add(div)

warnings_container = page.ui.div([page.ui.titles.subtitle("Alerts", align="center")], width=(100, 'px'))
warnings_container.style.css.vertical_align = "top"
warnings_container.style.css.margin = "0 2px"
warnings_container.add(page.ui.titles.section("Success", align="center"))
for k in page.theme.success:
  div = page.ui.div(k, width=(100, 'px'))
  div.style.css.background = k
  div.style.css.text_align = "center"
  warnings_container.add(div)
warnings_container.add(page.ui.titles.section("Warning", align="center"))
for k in page.theme.warning:
  div = page.ui.div(k, width=(100, 'px'))
  div.style.css.background = k
  div.style.css.text_align = "center"
  warnings_container.add(div)
warnings_container.add(page.ui.titles.section("Danger", align="center"))
for k in page.theme.danger:
  div = page.ui.div(k, width=(100, 'px'))
  div.style.css.background = k
  div.style.css.text_align = "center"
  warnings_container.add(div)

add_code(page)
page.ui.banners.disclaimer()
