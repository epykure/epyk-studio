#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk_studio.lang import eng
from epyk_studio.lang import fr


REGISTERED_LANGS = [
  {"value": 'eng', 'name': 'eng'},
  {"value": 'fr', 'name': 'fr'},
]


def get_lang(lang="uk"):
  """
  Description:
  ------------
  Route to the corresponding lang module.
  By default the one used will be the english one.

  Attributes:
  ----------
  :param lang:
  """
  lang = lang or 'uk'
  lang = lang.lower()
  if lang == 'fr':
    return fr

  return eng

