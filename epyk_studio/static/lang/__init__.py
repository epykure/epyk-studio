#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk_studio.static.lang import eng
from epyk_studio.static.lang import fr
import os


def get_alias(lang="eng"):
  """
  Description:
  ------------
  Return the current alias used for the lang.
  This could allow to display different pages (markdown pages) in the documentation section.

  TODO: Improve this section.

  Attributes:
  ----------
  :param lang: String. Optional. The alias to be used
  """
  lang = os.environ.get('LANG') or lang or 'eng'
  return lang.lower()


def get_lang(lang="eng"):
  """
  Description:
  ------------
  Route to the corresponding lang module.
  By default the one used will be the english one.

  Attributes:
  ----------
  :param lang: String. Optional. The alias to be used.
  """
  lang = get_alias(lang)
  if lang == 'fr':
    return fr

  return eng
