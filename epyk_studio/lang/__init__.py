
from epyk_studio.lang import eng
from epyk_studio.lang import fr


def get_lang(lang="uk"):
  """

  :param lang:
  """
  lang = lang or 'uk'
  lang = lang.lower()
  if lang == 'fr':
    return fr

  return eng

