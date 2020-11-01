#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk_studio.core.js.html import JsHtmlClipboard


class Clipboard(Html.Html):
  requirements = ('font-awesome',)
  name = 'Clipboard'

  def __init__(self, report, icon, text, tooltip, width, height, htmlCode, options, profile):
    super(Clipboard, self).__init__(report, '', htmlCode=htmlCode, profile=profile,
              css_attrs={"width": width, 'height': height})
    self.icon = report.ui.icon(icon, htmlCode="%s_icon" % self.htmlCode)
    self.icon.options.managed = False
    self.icon.style.add_classes.icon.selected()
    self.icon.style.css.remove("color")
    self.icon.style.css.font_factor(5)
    self.tooltip(tooltip)
    self.text = report.ui.text(text, width=(100, '%'), htmlCode="%s_text" % self.htmlCode)
    self.text.style.css.text_align = "right"
    self.text.style.css.italic()
    self.text.options.managed = False
    self.input = report.ui.input(width=(width[0] - 30, 'px'))
    self.input.style.css.remove("background", set_none=True)
    self.input.style.css.font_size = 10
    self.input.style.css.float = "left"
    self.input.style.css.remove("line-height", set_none=True)
    self.input.style.css.text_align = "left"
    self.input.options.managed = False
    self.icon.click([
      self.input.dom.css({"display": "inline-block"}),
      self.input.build("Paste Data"),
      self.input.dom.events.trigger("focus"),
    ])
    #self.text.on("blur", [self.text.dom.hide()])

  def paste(self, jsFncs):
    """
    Description:
    ------------
    Paste data stored in the clipboard.

    The paste is not automatic for secutity reasons on the browser to avoid stealing data.
    THis is the reason why this framework will also do not try to automate this.

    If clipboard is used it will only encourage the user to paste the data.

    :param jsFncs:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    jsFncs.append(self.input.dom.hide())
    self.input.paste([self.loading()] + jsFncs)

  def loading(self, label="Processing data"):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param label:
    """
    return self.text.build('<i style="margin-right:5px" class="fas fa-spinner fa-spin"></i>%s' % label)

  @property
  def _js__builder__(self):
    return '''
      var content = data.text;
      htmlTextObj = document.getElementById(htmlObj.id + "_text");
      htmlIconObj = document.getElementById(htmlObj.id + "_icon");
      if (!data.status) {htmlIconObj.style.color = 'red'}
      else {htmlIconObj.style.color = 'green'}
      if(options.reset){htmlTextObj.innerHTML = ""}; 
      if(data != ''){ 
        if(options.showdown){var converter = new showdown.Converter(options.showdown); content = converter.makeHtml(data)} 
        if((options.maxlength != undefined) && (data.length > options.maxlength)){
          content = data.slice(0, options.maxlength); 
          if(options.markdown){htmlTextObj.innerHTML = content +"..."} else {htmlTextObj.innerHTML = content +"..."}; 
          htmlTextObj.title = data} 
        else{
          if(options.markdown){htmlTextObj.innerHTML = content} else {htmlTextObj.innerHTML = content}}};
      if(typeof options.css !== 'undefined'){for(var k in options.css){htmlTextObj.style[k] = options.css[k]}};
      '''

  @property
  def dom(self):
    """
    Description:
    ------------
    Shortcut to the clipboard dom elment.

    :rtype: JsHtmlClipboard.JsClipboard
    """
    if self._dom is None:
      self._dom = JsHtmlClipboard.JsClipboard(self, report=self._report)
    return self._dom

  def __str__(self):
    return "<div %s><div style='display:inline-block'>%s%s</div>%s</div>" % (self.get_attrs(pyClassNames=self.style.get_classes()),
                self.icon.html(), self.input.html(), self.text.html())
