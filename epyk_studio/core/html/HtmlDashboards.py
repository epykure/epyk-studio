#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.html import HtmlList
from epyk.core.html import Defaults as defaultHtml
from epyk.core.js import JsUtils

from epyk_studio.core.js.html import JsHtmlDashboard
from epyk_studio.core.html.options import OptDashboards


class Pivots(Html.Html):
  name = 'Dashboard Pivots'

  def __init__(self, page, width, height, html_code, options, profile):
    super(Pivots, self).__init__(page, [], html_code=html_code, css_attrs={"width": width, "height": height},
                                 profile=profile, options=options)
    self.container = self.page.ui.row(position="top", options={"responsive": False})
    self.container.options.managed = False

  @property
  def dom(self):
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage:
    -----

    :rtype: JsHtmlDashboard.JsHtmlPivot
    """
    if self._dom is None:
      self._dom = JsHtmlDashboard.JsHtmlPivot(self, page=self.page)
    return self._dom

  def items_style(self, style_type):
    """
    Description:
    ------------
    Function to load a predefined style for the items of the components.

    Usage:
    -----

    Attributes:
    ----------
    :param style_type. String. Mandatory. The alias of the style to apply.
    """
    if style_type == "bullets":
      bullter_style = {"display": 'inline-block', 'padding': '0 5px', 'margin-right': '2px',
                       'background': self.page.theme.greys[2], 'border-radius': '10px',
                       'border': '1px solid %s' % self.page.theme.greys[2]}
      self.columns.options.li_css = bullter_style
      self.columns.set_items()
      self.rows.options.li_css = bullter_style
      if self.sub_rows is not None:
        self.sub_rows.options.li_css = bullter_style
    return self

  def clear(self, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

    """
    return JsUtils.jsConvertFncs([self.rows.dom.clear(), self.columns.dom.clear()], toStr=True, profile=profile)

  def __str__(self):
    self.container._vals = []
    if "ondrop" not in self.rows.attr:
      self.rows.drop()
    if "ondrop" not in self.columns.attr:
      self.columns.drop()
    if self.sub_rows is not None:
      self.container.add([
        self.page.ui.text(
          "Rows <i style='font-size:%s'>(unique field)</i>" % self.page.body.style.globals.font.normal(-3)), self.rows,
        self.page.ui.text(
          "Sub Rows <i style='font-size:%s'>(unique field)</i>" % self.page.body.style.globals.font.normal(-3)),
        self.sub_rows])
    else:
      if self.rows.options.max == 1:
        self.container.add([
          self.page.ui.text(
            "Rows <i style='font-size:%s'>(unique field)</i>" % self.page.body.style.globals.font.normal(-3)), self.rows])
      else:
        self.container.add([
          self.page.ui.text(
            "Rows <i style='font-size:%s'>(multiple field)</i>" % self.page.body.style.globals.font.normal(-3)), self.rows])
    self.container.add([
      self.page.ui.text(
        "Values <i style='font-size:%s'>(multiple fields)</i>" % self.page.body.style.globals.font.normal(-3)), self.columns])
    html = [h.html() for h in self._vals]
    return "<div %s>%s%s</div>" % (
      self.get_attrs(css_class_names=self.style.get_classes()), self.container.html(), "".join(html))


class Columns(HtmlList.List):
  name = 'Dashboard Columns'
  requirements = ('font-awesome',)

  @property
  def dom(self):
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage:
    -----

    :rtype: JsHtmlDashboard.JsHtmlColumns
    """
    if self._dom is None:
      self._dom = JsHtmlDashboard.JsHtmlColumns(self, page=self.page)
    return self._dom

  def fixed(self, top, right, z_index=200, tooltip="List of columns in the data source"):
    """
    Description:
    ------------
    Display a tooltip message at a specific location.

    Usage:
    -----

    Attributes:
    ----------
    :param top: Tuple. Optional. A tuple with the integer for the component's distance to the top of the page.
    :param right: Tuple. Optional. A tuple with the integer for the component's distance to the right of the page.
    :param z_index: Integer. Optional. The CSS Z-index property.
    :param tooltip: String. Optional. The tooltip value.
    """
    self.anchor = self.page.ui.icon("fas fa-chevron-right")
    self.anchor.style.css.position = "fixed"
    self.anchor.style.css.cursor = "pointer"
    self.anchor.style.css.top = top + 10
    self.anchor.style.css.right = 18
    self.anchor.tooltip(tooltip)
    self.anchor.style.css.z_index = z_index + 10
    self.anchor.click([
      self.anchor.dom.switchClass("fa-chevron-left", "fa-chevron-right"),
      self.dom.toggle()
    ])
    self.style.css.overflow = "auto"
    self.style.css.background = self.page.theme.colors[0]
    self.style.css.max_height = "calc(100vh - %spx)" % top
    self.style.css.fixed(top=top, right=right, transform=False)
    self.style.css.z_index = z_index
    return self


class Task(Html.Html):
  name = 'Dashboard Task'
  _option_cls = OptDashboards.OptionTask

  def __init__(self, page, text, width, height, html_code, options, profile):
    super(Task, self).__init__(
      page, [], html_code=html_code, profile=profile, options=options, css_attrs={"width": width, "height": height})
    self.icon = self.page.ui.icon(self.options.icon, htmlCode="%s_icon" % self.htmlCode)
    self.icon.style.css.margin_right = 5
    self.icon.style.css.font_factor(3)
    self.icon.style.css.color = self.options.color
    self.icon.options.managed = False
    self.text = self.page.ui.text(text, htmlCode="%s_text" % self.htmlCode)
    self.text.options.managed = False
    self.text.style.css.vertical_align = "middle"
    self.text.style.css.line_height = defaultHtml.LINE_HEIGHT
    self.add(self.icon)
    self.add(self.text)
    self._jsStyles['colors'] = {
      "COMPLETED": self.page.theme.success[1],
      "RUNNING": self.page.theme.warning[1],
      "WAITING": self.page.theme.greys[5],
      "FAILED": self.page.theme.danger[1]}

  _js__builder__ = ''' 
      if(typeof data === 'string'){
        if (data === true){ data.status = 'completed'}
        else if (data === false){ data.status = 'FAILED'}
        var iconObj = document.getElementById(htmlObj.id  + "_icon") ;
        iconObj.classList = []; 
        options[data.toLowerCase()].split(' ').forEach(function(cls){iconObj.classList.add(cls)});
        iconObj.style.color = options['colors'][data.toUpperCase()];
      } else {
        if (data.status === true){ data.status = 'completed'}
        else if (data.status === false){ data.status = 'FAILED'}
        var iconObj = document.getElementById(htmlObj.id  + "_icon") ;
        var textObj = document.getElementById(htmlObj.id  + "_text") ;
        iconObj.classList = []; options[data.status.toLowerCase()].split(' ').forEach(function(cls){
          iconObj.classList.add(cls)});
        iconObj.style.color = options['colors'][data.status.toUpperCase()];
        textObj.innerText = data.text
      }'''

  @property
  def dom(self):
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage:
    -----

    :rtype: JsHtmlDashboard.JsHtmlTask
    """
    if self._dom is None:
      self._dom = JsHtmlDashboard.JsHtmlTask(self, page=self.page)
    return self._dom

  @property
  def options(self):
    """
    Description:
    -----------
    Property to set all the Tasks properties.

    Usage:
    -----

    :rtype: OptDashboards.OptionTask
    """
    return super().options

  def loading(self, icon="fas fa-spinner"):
    """
    Description:
    -----------
    Set the loading state for this component.

    Usage:
    -----

    Attributes:
    ----------
    :param icon: String. Optional. The icon reference,
    """
    return self.icon.dom.setAttribute("class", "%s fa-spin" % icon)

  def click(self, js_funcs, profile=None, source_event=None, on_ready=False):
    """
    Description:
    -----------
    The onclick event occurs when the user clicks on an element.

    Usage:
    -----

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    self.style.css.cursor = "pointer"
    if on_ready:
      self.page.body.onReady([self.dom.events.trigger("click")])
    return self.on("click", js_funcs, profile, source_event)

  def __str__(self):
    return "<div %s>%s%s</div>" % (
      self.get_attrs(css_class_names=self.style.get_classes()), self.icon.html(), self.text.html())

