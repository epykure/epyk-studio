#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import HtmlButton
from epyk_studio.core.js.html import JsHtmlClipboard


class Clipboard(HtmlButton.IconEdit):
  name = 'Clipboard'

  def __init__(self, report, position, icon, text, tooltip, width, height, htmlCode, options, profile):
    super(Clipboard, self).__init__(report, position, icon, text, tooltip, width, height, htmlCode, options, profile)
    del self.icon.attr['css']["color"]
    self.style.add_classes.icon.selected()
    self.text = report.ui.input(width=("60", "px"))
    self.text.style.css.background = report.theme.greys[0]
    self.text.style.css.font_size = 10
    self.text.style.css.text_align = "left"
    self.text.style.display = False
    self.click([
      self.text.dom.css({"display": "inline-block"}),
      self.text.build("Paste Data"),
      self.text.dom.events.trigger("focus"),
    ])
    self.text.on("blur", [self.text.dom.hide()])

  def paste(self, jsFncs):
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    jsFncs.append(self.text.dom.hide())
    self.text.paste(jsFncs)

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsHtmlClipboard.JsClipboard
    """
    if self._dom is None:
      self._dom = JsHtmlClipboard.JsClipboard(self, report=self._report)
    return self._dom

