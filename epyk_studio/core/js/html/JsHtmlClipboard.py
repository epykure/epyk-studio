#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects
from epyk.core.js import JsUtils


class JsClipboard(JsHtml.JsHtml):

  @property
  def content(self):
    return JsObjects.JsObjects.get("(event.clipboardData || window.clipboardData).getData('text')")

  def store(self, data=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param data:
    """
    if data is None:
      return JsObjects.JsVoid(
        "window['%s'] = (event.clipboardData || window.clipboardData).getData('text')" % self.code)

    JsUtils.jsConvertData(data, None)
    return JsObjects.JsVoid("window['%s'] = %s" % (self.code, data))

  def clear(self):
    """
    Description:
    ------------
    Clear the data store in the clipboard component (not in memory in the current clipboard)

    Usage:
    -----

    """
    return JsObjects.JsVoid("window['%s'] = ''" % self.code)

  @property
  def code(self):
    """
    Description:
    ------------
    The default data reference.

    Usage:
    -----

    """
    return "%s_data" % self.component.htmlCode

  @property
  def data(self):
    """
    Description:
    ------------
    Get the data store in the clipboard component.

    Usage:
    -----

    """
    return JsObjects.JsString.JsString.get("window['%s']" % self.code)
