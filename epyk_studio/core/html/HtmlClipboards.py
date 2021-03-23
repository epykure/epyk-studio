#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.html import HtmlImage

from epyk_studio.core.js.html import JsHtmlClipboard


class Clipboard(Html.Html):
  requirements = ('font-awesome',)
  name = 'Clipboard'

  def __init__(self, report, icon, text, tooltip, width, height, html_code, options, profile):
    super(Clipboard, self).__init__(report, '', html_code=html_code, profile=profile, options=options,
                                    css_attrs={"width": width, 'height': height})
    self.icon = report.ui.icon(icon, html_code="%s_icon" % self.htmlCode)
    self.icon.options.managed = False
    self.icon.style.add_classes.icon.selected()
    self.icon.style.css.remove("color")
    self.icon.style.css.font_factor(5)
    self.tooltip(tooltip)
    self.text = report.ui.text(text, width=(100, '%'), html_code="%s_text" % self.htmlCode)
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

  def paste(self, js_funcs, profile=False, source_event=None):
    """
    Description:
    ------------
    Paste data stored in the clipboard.

    The paste is not automatic for security reasons on the browser to avoid stealing data.
    THis is the reason why this framework will also do not try to automate this.

    If clipboard is used it will only encourage the user to paste the data.

    Usage:
    -----

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | String. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    js_funcs.append(self.input.dom.hide())
    return self.input.paste([self.loading()] + js_funcs, profile, source_event)

  def loading(self, label="Processing data"):
    """
    Description:
    -----------
    Set the loading state for this component.

    Usage:
    -----

    Attributes:
    ----------
    :param label: String. Optional. The loading message.
    """
    return self.text.build('<i style="margin-right:5px" class="fas fa-spinner fa-spin"></i>%s' % label)

  _js__builder__ = '''
      var content = data.text;
      htmlTextObj = document.getElementById(htmlObj.id + "_text");
      htmlIconObj = document.getElementById(htmlObj.id + "_icon");
      if (!data.status) {htmlIconObj.style.color = 'red'}
      else {htmlIconObj.style.color = 'green'}
      if(options.reset){htmlTextObj.innerHTML = ""}; 
      if(data != ''){ 
        if(options.showdown){
          var converter = new showdown.Converter(options.showdown); content = converter.makeHtml(data)} 
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
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage:
    -----

    :rtype: JsHtmlClipboard.JsClipboard
    """
    if self._dom is None:
      self._dom = JsHtmlClipboard.JsClipboard(self, report=self._report)
    return self._dom

  def __str__(self):
    return "<div %s><div style='display:inline-block'>%s%s</div>%s</div>" % (
      self.get_attrs(pyClassNames=self.style.get_classes()), self.icon.html(), self.input.html(), self.text.html())


class ConfigEditor(HtmlImage.Icon):
  requirements = ('font-awesome',)
  name = 'Configuration'

  def __init__(self, report, value, data, width, height, color, tooltip, options, html_code, profile):
    super(ConfigEditor, self).__init__(report, value, width, height, color, tooltip, options, html_code, profile)
    self.varName = data or "window['page_config']"
    self.components = []

  _js__builder__ = '''var position = options.top; 
      if((typeof data === 'undefined') || (!data.download)){htmlObj.remove()} 
      else {htmlObj.style.top = position + "px"; position = position + 30} 
      if((typeof data === 'undefined') || (!data.edit)){document.getElementById(htmlObj.id + "_lock").remove()} 
      else {
        document.getElementById(htmlObj.id + "_lock").click(); 
        document.getElementById(htmlObj.id + "_lock").style.top = position + "px"}'''

  def add(self, component):
    """
    Description:
    ------------
    Add an extra component to the container.

    Usage:
    -----

    Attributes:
    ----------
    :param component: HTML Component. Optional. A HTML Component to be added.
    """
    if not hasattr(component, "htmlCode"):
      component = self.page.components[component]
    self.components.append(component)
    return self

  def extend(self, components):
    """
    Description:
    ------------
    Add several components to the container.

    Usage:
    -----

    Attributes:
    ----------
    :param components: List. Optional. The various HTML Components to be added.
    """
    for component in components:
      self.add(component)
    return self

  def __str__(self):
    data_ovr = "; ".join(["configData['%s'] = %s" % (h.htmlCode, h.dom.content.toStr()) for h in self.components or []])
    self.icon.click(
      {"on": [c.dom.setAttribute("contenteditable", False).r for c in self.components],
       "off": [c.dom.setAttribute("contenteditable", True).r for c in self.components]})
    self.click(['''
      var configData = %(configData)s; %(data_ovr)s;
      var dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(configData));
      var dlAnchorElem = document.createElement('a'); dlAnchorElem.setAttribute("href", dataStr);
      dlAnchorElem.setAttribute("download", "config.json"); dlAnchorElem.click(); dlAnchorElem.remove();
      ''' % {"configData": self.varName, "data_ovr": data_ovr}])
    return super(ConfigEditor, self).__str__()


class DataExplorer(Html.Html):
  requirements = ('font-awesome',)
  name = 'Explorer'

  def __init__(self, report, width, height, html_code, options, profile):
    super(DataExplorer, self).__init__(report, '', html_code=html_code, profile=profile, options=options,
                                       css_attrs={"width": width, 'height': height})

  _js__builder__ = '''
      '''

  def __str__(self):
    return "<div %s></div>" % self.get_attrs(pyClassNames=self.style.get_classes())
