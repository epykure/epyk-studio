
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

#  page.js.post("/get/packages", {"packages": "jqueryui"})

title = page.ui.title("All packages available")
title.style.standard()

records = [{"pkg": pkg, "vr": dtl[0]['version'], "get": "<button class='cssbuttonbasic' style='padding:0 5px;line-height:15px!IMPORTANT' onclick='(function(){var xhttp = new XMLHttpRequest(); xhttp.open(\"GET\", \"/get/packages?p=%s\", true); xhttp.send()})()'>get</button>" % pkg} for pkg, dtl in Imports.ImportManager(page).show(all=True).items()]
tb = page.ui.table(records, cols=['pkg'], rows=['vr', 'get'])
tb.get_column("get").formatters.html()
tb.style.standard()

dis = page.ui.banners.disclaimer()
dis.style.css.margin_top = 20

add_code(page)
