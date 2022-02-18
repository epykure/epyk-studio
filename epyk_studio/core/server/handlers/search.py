import time
import importlib
import tornado.web
import tornado.escape


def get_components(components, results, alias=None):
  """
  Description:
  ------------
  Get the documentation dynamically from the project structure.
  This will store everything in a global dictionary.

  Attributes:
  ----------
  :param components: HTML Component. An internal HTML Component
  :param results: Dictionary. A dictionary with the documentation per component
  :param alias: String. Optional. The components prefix (for the sub categories)
  """
  for v in dir(components):
    if v == 'google':
      continue

    obj = getattr(components, v)
    if callable(obj):
      doc_string = obj.__doc__
      if doc_string is None or "Description" not in doc_string:
        continue

      if alias is None:
        results[obj.__name__] = doc_string
      else:
        results["%s.%s" % (alias, obj.__name__)] = doc_string
    else:
      if hasattr(obj, 'context'):
        if v != 'parent':
          get_components(obj, results, alias=v)
  return results


def parse_doc(doc_string):
  """
  Description:
  ------------
  Parse the documentation and structure this to an internal object in order to be lookup in the Studio to help on
  the implementation.

  Attributes:
  ----------
  :param doc_string: String. The class doctring in the Epyk format
  """
  group = None
  result = {'dsc': [], 'tags': []}
  for line in doc_string.split("\n"):
    s_line = line.strip()
    if s_line.startswith("--------") or not s_line:
      continue

    if s_line == "Description:":
      group = "dsc"
      continue
    elif s_line == "Attributes:":
      group = "params"
      continue
    elif s_line == "Underlying HTML Objects:":
      group = "underlying"
      continue
    elif s_line == "Usage::":
      group = "usage"
      continue
    elif s_line == "Templates:":
      group = "templates"
      continue

    if s_line.startswith(":tags:"):
      result['tags'] = [c.strip() for c in s_line.split(":tags:")[1].split(",")]
      group = None
      continue

    if s_line.startswith(":categories:"):
      result['categories'] = [c.strip() for c in s_line.split(":categories:")[1].split(",")]
      group = None
      continue

    if group is not None:
      result.setdefault(group, []).append(s_line)

  if 'dsc' in result:
    result['dsc'] = "".join(result['dsc'])
  return result


class SearchHandler(tornado.web.RequestHandler):

  def post(self):
    """
    Description:
    ------------

    """
    from epyk_studio.interfaces import Interface

    start = time.time()
    components = Interface.Studio()
    result = {}
    get_components(components, result)
    data = tornado.escape.json_decode(self.request.body)

    components = []
    for k, v in result.items():
      parsed_doc = parse_doc(v)
      if data['category'] == 'All' or data['category'] in parsed_doc.get("categories", []):
        if data['input']:
          if data['input'] in parsed_doc['dsc']:
            links = [{"url": t, 'val': t} for t in parsed_doc.get("templates", [])]

            components.append({"title": k, "urlTitle": '/search/component?v=%s' % k,
                               'dsc': parsed_doc['dsc'], 'links': links})
            if parsed_doc['tags']:
              components[-1].update({'icon': 'fas fa-tags', 'url': ", ".join(parsed_doc['tags'])})
        else:
          links = [{"url": t, 'val': t} for t in parsed_doc.get("templates", [])]
          components.append({"title": k, "urlTitle": '/search/component?v=%s' % k,
                             'dsc': parsed_doc['dsc'], 'links': links})
          if parsed_doc['tags']:
            components[-1].update({'icon': 'fas fa-tags', 'url': ", ".join(parsed_doc['tags'])})

    #print(data)
    #parse_doc(data)
    self.write({'status': "%s Results retrieved in %s" % (len(result), time.time() - start), 'results': components})


class SearchResultHandler(tornado.web.RequestHandler):

  def get(self):
    """
    Description:
    ------------

    """
    from epyk_studio.interfaces import Interface

    page = self.request.uri.split("?")[0][1:] or "home"
    mod = __import__("epyk_studio.static.pages.%s" % page, fromlist=['object'])
    importlib.reload(mod)

    name = 'shop.rating'
    components = Interface.Studio()
    result = {}
    get_components(components, result)
    parsed_doc = parse_doc(result[name])
    mod.page.ui.title("Documentation (%s)" % name)
    mod.page.ui.texts.paragraph("\n".join(parsed_doc.get("dsc", [])))

    mod.page.ui.title("Categories")
    mod.page.ui.div("', '".join(parsed_doc.get('categories', [])))

    mod.page.ui.title("Tags")
    mod.page.ui.chips(parsed_doc.get('tags', []), options={"delete": False})

    mod.page.ui.title("Parameters")

    mod.page.ui.title("Demo")

    mod.page.ui.title("Github examples")

    mod.page.ui.title("Underlyings Modules")
    self.write(mod.page.outs.html())
