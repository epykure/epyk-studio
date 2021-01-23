

from epyk_studio.core.Page import Report
from epyk_studio.static.pages import add_code, nav_bar
from epyk_studio.utils import git

import os

# Create a basic report object
page = Report()

repo_templates = git("epykure", "epyk-templates")
git_files = repo_templates.trees()

pictures = []
for rec in git_files['tree']:
  if rec["path"].startswith("static/images/thumbnails/"):
    pictures.append(repo_templates.picture_path(rec["path"]))

nav_bar(page, 'Templates')

t1 = page.ui.title("Static templates")

search = page.ui.inputs.search(htmlCode='input')

gallery = page.studio.gallery.images(pictures, columns=4, options={"responsive": False})
for i in gallery.images:
  i.goto(os.path.join(repo_templates.main, 'locals', 'studio'))

t2 = page.ui.title("Web templates")

box = page.studio.containers.box()
box.extend([t1, search, gallery, t2])
box.style.standard()

add_code(page)

