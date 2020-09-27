
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar


# Create a basic report object
page = Report()

nav_bar(page, "Analytics")

page.ui.texts.paragraph('''
Epyk is wrapper the best of the web to allow a huge range of components for Tables ahd Charts.
It is using the same design to interface all the main JavaScript Libraries.
''').style.standard()


page.ui.texts.paragraph('''
An extensible framework which can easily evolve with your need and the techs
''').style.standard()


page.ui.texts.paragraph('''
Incredibly fast for prototyping and delivering value to your business. 
''').style.standard()


dis = page.ui.banners.disclaimer()
dis.style.css.margin_top = 20

add_code(page)
