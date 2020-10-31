#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects
from epyk.core.js import JsUtils


class JsClipboard(JsHtml.JsHtml):

  @property
  def content(self):
    return JsObjects.JsObjects.get("(event.clipboardData || window.clipboardData).getData('text')")

  def store(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsVoid("window[%s] = (event.clipboardData || window.clipboardData).getData('text')" % self._src.htmlCode)

  def clear(self):
    """
    Description:
    ------------
    Clear the data store in the clipboard component (not in memory in the current clipboard)
    """
    return JsObjects.JsVoid("window[%s] = ''" % self._src.htmlCode)

  @property
  def data(self):
    """
    Get the data store in the clipboard component
    """
    return JsObjects.JsString.JsString.get("window[%s]" % self._src.htmlCode)
