

from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar
from epyk_studio.utils import git

import os
import json


# Create a basic report object
page = Report()

repo_templates = git("epykure", "epyk-templates")
git_files = repo_templates.trees(tempFolder=os.path.join(os.getcwd(), "temps"))

pictures = []
for rec in git_files['tree']:
  if rec["path"].startswith("static/images/thumbnails/"):
    pictures.append(repo_templates.picture_path(rec["path"]))

nav_bar(page, 'Templates Links', "Templates")

t0 = page.ui.title("My templates folders")

f_alias = page.ui.input(placeholder="alias", width="auto")
f_path = page.ui.input(placeholder="templates full path", width="auto")
f_button = page.ui.buttons.colored("Add")
f_button.click([
  page.js.post("/template", components=[f_alias, f_path]).onSuccess([

  ])
])

items = page.ui.lists.items()
items.style.hover_border()
items.style.hover_background()
items.options.items_type = "link"

f_line = page.ui.row([f_alias, f_path, f_button])

t1 = page.ui.title("Online Static templates")

search = page.ui.inputs.search(html_code='input')

gallery = page.studio.gallery.images(pictures, columns=4, options={"responsive": False})
for i in gallery.images:
  i.goto(os.path.join(repo_templates.main, 'locals', 'studio'))

t2 = page.ui.title("Web templates")

box = page.studio.containers.box(delete=True)
box.extend([t0, f_line, page.ui.layouts.hr(), items, t1, search, gallery, t2])
box.style.standard()

add_code(page)


def add_inputs(inputs):
  tmps_folder = os.path.join(inputs['current_path'], "temps")
  if not os.path.exists(tmps_folder):
    os.mkdir(tmps_folder)

  config_folders = os.path.join(tmps_folder, "my_folders.json")
  my_folders = {}
  if os.path.exists(config_folders):
    with open(config_folders) as fp:
      my_folders = json.load(fp)
  items.record(my_folders)
