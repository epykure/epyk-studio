
import os
import json

from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar
from epyk_studio.static import lang


# Create a basic report object
page = Report()
nav_bar(page, "@Studio")

img = page.ui.img("epyklogo_whole_big.png", path='/static', width=(300, 'px'))
img.style.css.margin_top = 20

text = page.ui.text(lang.get_lang().TEXT_1, align="center")
text.style.css.font_factor(15)
text.style.css.bold()

content = page.ui.text(lang.get_lang().TEXT_2, align="center")
content.style.css.font_factor(5)
content.style.css.italic()

twitter = page.ui.icons.twitter()
linkedIn = page.ui.icons.linkedIn()
linkedIn.style.css.margin_left = 5
linkedIn.style.css.margin_right = 5
youtube = page.ui.icons.youtube()

text_follow = page.ui.text("Follow us on", align="center")
text_follow.style.css.italic()
page.ui.div([twitter, linkedIn, youtube], align="center")

t1 = page.ui.titles.bold("Test Script")
t1.style.css.margin = "10px 20% 0 20%"
t1.style.css.width = "60%"

# TODO
script_shortcut = page.ui.inputs.search(
  placeholder="Test script (full path)", align="center", options={
    "icon": "far fa-play-circle", "position": 'right', "autocomplete": True})
script_shortcut.enter([
  page.js.location.open_new_tab(script_shortcut.input.dom.content.string.prepend("./code_frame?classpath=&script="))
])
script_shortcut.style.css.margin = "0 20% 0 20%"
script_shortcut.style.css.width = "60%"

pg = page.ui.texts.paragraph(lang.get_lang().TEXT_3)
pg.style.css.margin = "10px 20% 0 20%"
pg.style.css.width = "60%"

get_started = page.ui.buttons.large(lang.get_lang().TEXT_4)
get_started.style.css.margin_right = 10
get_started.goto("/project", target="_self")

tutorials = page.ui.buttons.large("Tutorials")
tutorials.style.css.margin_right = 10
tutorials.goto("/tutorials", target="_self")

templates = page.ui.buttons.large("Templates")
templates.style.css.margin_right = 10
templates.goto("/templates", target="_self")

buttons_bar = page.ui.div([get_started, tutorials, templates], align="center")
buttons_bar.style.css.margin_top = 20
buttons_bar.style.css.margin_bottom = 10

im = page.ui.img("collaborative.PNG", path='/static', width=(350, 'px'), height=("auto", ""))
im.style.css.margin_top = 10
im.style.css.margin_bottom = 10

menu = page.ui.menus.bar([
  {"value": "Project", 'children': [
    {"text": "Docs", 'url': 'http://www.epyk.io/'},
    {"text": "Components", 'url': '/search'},
    {"text": "Projects", 'url': "/project"},
    {"text": "Packages", 'url': '/ext_packages'},
    #{"text": "Servers", 'url': '/servers'},
    #{"text": "Databases", 'url': '/databases'},
  ]},
  {"value": "Links", 'children': [
    {"text": "Examples", 'url': "https://github.com/epykure/epyk-templates"},
    {"text": "Tutorials", 'url': "http://www.epyk-studio.com/tutorials"},
    {"text": "Notebooks", 'url': "https://nbviewer.jupyter.org/github/epykure/epyk-templates-notebooks/blob/master/index.ipynb"},
    {"text": "Studio", 'url': "http://www.epyk-studio.com/"}
   ]},
  {"value": 'Production', 'children': [
    #{"text": "Testing"}, # local report
    #{"text": "Analytics", 'url': '/analytics'}, # local report
    #{"text": "Publish"}, # local report
    #{"text": "Link to App"}, # local report
    {"text": "Community", 'url': 'https://github.com/epykure/epyk-studio'}, # local report
    {"text": "Share issues (Studio)", 'url': 'https://github.com/epykure/epyk-studio/issues'}, # local report
    {"text": "Share issues (Core)", 'url': 'https://github.com/epykure/epyk-ui/issues'} # local report
  ]},
], options={"responsive": False})
menu.style.css.margin = "10px auto"
# add media on the margin

blog_button = page.ui.buttons.large("Start", align="center")
blog_button.goto("/code_editor", target="_self")

vignet1 = page.ui.vignets.vignet("Thousand of components available", '''
Fully documented on the Python side based on the JavaScript documentation available online. Links available to find out more on JavaScript concepts and gradually improve your UI knowledge
''', width=("auto", ""))
vignet1.style.css.margin = "0 20%"
vignet1.style.css.width = "60%"


t1 = page.ui.titles.title("For everything", align="center")
t1.style.css.color = page.theme.colors[-1]
t1.style.css.margin_bottom = 0
t1.style.css.margin_top = 15

ics = page.studio.gallery.icons([
  {"icon": "far fa-chart-bar", "text": 'Charts'},
  {"icon": "fas fa-brain", "text": 'IA / ML'},
  {"icon": "fas fa-square-root-alt", "text": 'Maths'},
  {"icon": "far fa-lightbulb", "text": 'Tutorial'},
  {"icon": "fas fa-desktop", "text": 'Vues'},
  {"icon": "fas fa-store", "text": 'E-commerce'},
  {"icon": "fas fa-comments", "text": 'Bot'},
  {"icon": "fab fa-html5", "text": 'Blog'},
  {"icon": "fas fa-user-graduate", "text": 'Learning'},
], options={"responsive": False})
ics.style.css.margins(left=(20, '%'), right=(20, '%'), top=(0, ''))
ics.style.css.width = "60%"

m = page.ui.panels.slidings.plus('''

''', 'Time to market')
m.options.expanded = False
m.style.css.margins(left=(20, '%'), right=(20, '%'))
m.title.style.css.color = page.theme.colors[-1]
m.style.css.width = "60%"

s = page.ui.panels.slidings.plus('''
Epyk is a low Code framework in the way it will allow you to deal with other languages and technology from Python.
It is fully based on Python to ensure you have all the Flexibility in improving your platform when your technical knowledge is evolving.
''', 'Low Code Framework')
s.options.expanded = False
s.style.css.margins(left=(20, '%'), right=(20, '%'))
s.style.css.width = "60%"
s.title.style.css.color = page.theme.colors[-1]

s = page.ui.panels.slidings.plus('''
Since this is based on Python you will be able to do everything you want to customise your solution. There is no dependance on any upgrade of a tool to change the core framework.
Using Epyk will give you the entire transparency and flexibility in the same way as other popular Web framework (React, Angular, Vue...).
''', 'No Dependency')
s.options.expanded = False
s.style.css.margins(left=(20, '%'), right=(20, '%'))
s.style.css.width = "60%"
s.title.style.css.color = page.theme.colors[-1]

ics.icons[0].click(page.js.alert("ok"))

content = page.ui.div([page.ui.texts.paragraph('''
Start by creating simple static pages in your projects.
This will allow you to discover the components and also have a view on the default rendering.
'''), blog_button])

vignet = page.ui.vignets.image(title="Write your first pages", content=content, width=(60, '%'),
                               image=page.ui.images.circular("blog.PNG", path='/static'))
vignet.image.style.css.margin_top = 10
vignet.image.style.css.width = "300px"
vignet.image.style.css.height = "300px"

blog = page.ui.banners.text(vignet, align="left")
blog.style.css.padding = 0

st1 = page.ui.titles.subtitle("Compatible with", align="center")
st1.style.css.color = page.theme.colors[-1]
power = page.ui.rich.powered(True)
power.style.css.margins(left=(20, '%'), right=(20, '%'))
power.style.css.width = "60%"
power.style.css.margin_bottom = "10px"

add_code(page)

page.ui.banners.disclaimer()


def add_inputs(inputs):
  temps_path = os.path.join(inputs["current_path"], "temps", "run_history.json")
  with open(temps_path) as fp:
    script_shortcut.input.options.source = json.load(fp)
