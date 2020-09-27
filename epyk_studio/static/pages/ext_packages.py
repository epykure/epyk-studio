
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar
from epyk.core.js import Imports


# Create a basic report object
page = Report()

nav_bar(page, "JavaScript")

records = [{"pkg": pkg, "vr": dtl[0]['version']} for pkg, dtl in Imports.ImportManager(page).show(all=True).items()]
tb = page.ui.table(records, cols=['pkg'], rows=['vr', 'get'])
tb.style.standard()

dis = page.ui.banners.disclaimer()
dis.style.css.margin_top = 20

add_code(page)
