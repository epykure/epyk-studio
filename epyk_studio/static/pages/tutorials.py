
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar


# Create a basic report object
page = Report()

nav_bar(page, 'Tutorials')

t1 = page.ui.title("How to start?")

p = page.ui.texts.paragraph('''
First have a look at the [example](/examples) section to get a technical overview of the components and function in the framework.

The below will detail how to use the Framework from around 15 examples.
Those examples are trying to show cases significant use cases in order to have an overview on the features and
the available external libraries.

All those use cases are available in the [Github](https://github.com/epykure/epyk-templates/tree/master/tutos) main repository.
''', options={"markdown": True})

st1 = page.ui.titles.section("1. Display data in dynamic charts")

ps1 = page.ui.texts.paragraph('''
This report will use external JavaScript data and link it to ChartJs containers wrapped with Python.
This use case will demonstrate how to use some components and generate interactive chart.

Few variable of this example are available in order to show how to user the other charting libraries.
Epyk is wrapping the most popular Framework some **ChartJs**, C3, Billboard, NVD3, DC, D3, Plotly.Js, APexCharts and Vis are available. 
''', options={"markdown": True})

st2 = page.ui.titles.section("2. Display data in dynamic tables")


st3 = page.ui.titles.section("3. Display static HTML texts / Blogs")

ps3 = page.ui.texts.paragraph('''

More details on static web page will be available in the web site templates section
''')

box = page.studio.containers.box()
box.extend([t1, p, st1, ps1, st2, st3, ps3])
box.style.standard()

dis = page.ui.banners.disclaimer()
dis.style.css.margin_top = 20
