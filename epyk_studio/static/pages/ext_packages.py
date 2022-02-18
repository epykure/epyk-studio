
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar
from epyk.core.js import Imports


# Create a basic report object
page = Report()
nav_bar(page, "JavaScript")

title = page.ui.title("Get all packages")
title.style.standard()

paragraph = page.ui.texts.paragraph('''
Get all the external packages locally to be able to run your
framework without internet connection.

This will allow you to get a stable and efficient response time
''')
paragraph.style.standard()

button = page.ui.buttons.large("Download all", align="center")
button.click([
  page.js.post("/get/packages").onSuccess([
    page.js.msg.status()
  ]),
])

package = page.ui.title("Find Package")
package.style.standard()
page.ui.texts.paragraph('''
Not all the packages available on the JavaScript ecosystem are available. You can check here if a package existing.
This will search in the module Imports.py installed and tell you all the possible matched.
''').style.standard()
search = page.ui.inputs.search(html_code='input')
search.style.standard()

page.ui.texts.paragraph('''
If your package is not available you can add it and propose this to the community
''').style.standard()

link = page.ui.link("Framework Extension", "https://nbviewer.jupyter.org/github/epykure/epyk-templates-notebooks/blob/master/tutorials/extensions/01_framework_ext.ipynb", align="center")
link.style.css.font_factor(8)
link.style.standard()

title = page.ui.title("All packages available")
title.style.standard()

records = [{"pkg": pkg, "vr": dtl[0]['version'],
            "get": "<button class='cssbuttonbasic' style='padding:0 5px;line-height:15px!IMPORTANT' onclick='(function(){var xhttp = new XMLHttpRequest(); xhttp.open(\"GET\", \"/get/packages?p=%s\", true); xhttp.send()})()'>get</button>" % pkg} for pkg, dtl in Imports.ImportManager(page).show(all=True).items()]
tb = page.ui.table(records, cols=['pkg'], rows=['vr', 'get'])
tb.get_column("get").formatters.html()
tb.style.standard()

dis = page.ui.banners.disclaimer()
dis.style.css.margin_top = 20

add_code(page)
