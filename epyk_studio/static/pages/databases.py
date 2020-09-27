
from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar


# Create a basic report object
page = Report()

nav_bar(page, "Database")

page.ui.texts.paragraph('''
Epyk is based on Python so it can interact with any databases available in Python.
Among the most popular ones you can have a look at: 
''').style.standard()

page.ui.text("Do not hesitate to look at the SqlAlchemy and Alembic").style.standard()

page.ui.texts.paragraph('''
Can be used with the most popular modules for Data Sciences (Pandas, Numpy...)
''').style.standard()

page.ui.texts.paragraph('''
An embedded SQL interface to share easily data between the Database and the Framework
''').style.standard()

add_code(page)
