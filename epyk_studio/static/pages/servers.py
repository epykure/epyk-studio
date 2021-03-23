
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar


# Create a basic report object
page = Report()
nav_bar(page, "Servers")

content = page.ui.contents()

mysql = page.ui.img("https://www.iconfinder.com/data/icons/logos-3/181/MySQL-512.png", width=(60, 'px'))
msserver = page.ui.img("https://e7.pngegg.com/pngimages/515/909/png-clipart-microsoft-sql-server-computer-servers-database-microsoft-microsoft-sql-server-server-computer.png", width=(60, 'px'))
postgres = page.ui.img("https://user-images.githubusercontent.com/24623425/36042969-f87531d4-0d8a-11e8-9dee-e87ab8c6a9e3.png", width=(60, 'px'))

row = page.ui.row([mysql, msserver, postgres], options={"responsive": False})
row.style.standard()

info = page.ui.texts.highlights("This is a test", 'Title', type="success")
info.style.standard()

b = page.studio.blog.delimiter()
page.ui.layouts.new_line()

icon = page.ui.icons.large("fas fa-database", align="center")


t1 = page.ui.title("Example with Postgres")
t1.style.standard()

t2 = page.ui.title("Example with Sqlite")
t2.style.standard()

add_code(page)
