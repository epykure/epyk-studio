#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk_studio.static.lang import eng
from epyk_studio.static.lang import fr
import os


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
  lang = os.environ.get('LANG') or lang or 'uk'
  lang = lang.lower()
  if lang == 'fr':
    return fr

  return eng
