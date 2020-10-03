

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

search = page.ui.inputs.search(htmlCode='input')
search.style.standard()

gallery = page.studio.gallery.images(pictures, columns=4, options={"responsive": False})
gallery.style.standard()
for i in gallery.images:
  i.goto(os.path.join(repo_templates.main, 'locals', 'studio'))

add_code(page)

