#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.html import HtmlList
from epyk.core.html import Defaults as default_html

from epyk.core.js import JsUtils

from epyk_studio.core.js.html import JsHtmlDashboard
from epyk_studio.core.html.options import OptDashboards


class Pivots(Html.Html):
  name = 'Dashboard Pivots'

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(Pivots, self).__init__(report, [], htmlCode=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self.container = self._report.ui.row(position="top", options={"responsive": False})
    self.container.options.managed = False

  def clear(self):
    return JsUtils.jsConvertFncs([self.rows.dom.clear(), self.columns.dom.clear()], toStr=True)

  def __str__(self):
    self.container._vals = []
    self.container.add([self._report.ui.titles.rubric("Rows"), self.rows])
    self.container.add([self._report.ui.titles.rubric("Values"), self.columns])
    html = [h.html() for h in self._vals]
    return "<div %s>%s%s</div>" % (self.get_attrs(pyClassNames=self.style.get_classes()), self.container.html(), "".join(html))


class Columns(HtmlList.List):
  name = 'Dashboard Columns'

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsHtmlDashboard.JsHtmlColumns
    """
    if self._dom is None:
      self._dom = JsHtmlDashboard.JsHtmlColumns(self, report=self._report)
    return self._dom

  def fixed(self, top, right, z_index=200, tooltip="List of columns in the data source"):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param top:
    :param right:
    :param z_index:
    """
    self.anchor = self._report.ui.icon("fas fa-chevron-right")
    self.anchor.style.css.position = "fixed"
    self.anchor.style.css.cursor = "pointer"
    self.anchor.style.css.top = top + 8
    self.anchor.style.css.right = 18
    self.anchor.tooltip(tooltip)
    self.anchor.style.css.z_index = z_index + 10
    self.anchor.click([
      self.anchor.dom.switchClass("fa-chevron-left", "fa-chevron-right"),
      self.dom.toggle()
    ])
    self.style.css.overflow = "auto"
    self.style.css.max_height = "calc(100vh - %spx)" % top
    self.style.css.fixed(top=top, right=right, transform=False)
    self.style.css.z_index = z_index
    return self


class Task(Html.Html):
  name = 'Dashboard Task'

  def __init__(self, report, text, width, height, htmlCode, options, profile):
    super(Task, self).__init__(report, [], htmlCode=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self.__options = OptDashboards.OptionTask(self, options)
    self.icon = self._report.ui.icon(self.options.icon, htmlCode="%s_icon" % self.htmlCode)
    self.icon.style.css.margin_right = 5
    self.icon.style.css.font_factor(3)
    self.icon.style.css.color = self.options.color
    self.icon.options.managed = False
    self.text = self._report.ui.text(text, htmlCode="%s_text" % self.htmlCode)
    self.text.options.managed = False
    self.text.style.css.vertical_align = "middle"
    self.text.style.css.line_height = default_html.LINE_HEIGHT
    self.add(self.icon)
    self.add(self.text)
    self._jsStyles['colors'] = {"COMPLETED": self._report.theme.success[1], "RUNNING": self._report.theme.warning[1],
                                "WAITING": self._report.theme.greys[5], "FAILED": self._report.theme.danger[1]}

  @property
  def _js__builder__(self):
    return ''' 
      if(typeof data === 'string'){
        if (data === true){ data.status = 'completed'}
        else if (data === false){ data.status = 'FAILED'}
        var iconObj = document.getElementById(htmlObj.id  + "_icon") ;
        iconObj.classList = []; options[data.toLowerCase()].split(' ').forEach(function(cls){iconObj.classList.add(cls)});
        iconObj.style.color = options['colors'][data.toUpperCase()];
      } else {
        if (data.status === true){ data.status = 'completed'}
        else if (data.status === false){ data.status = 'FAILED'}
        var iconObj = document.getElementById(htmlObj.id  + "_icon") ;
        var textObj = document.getElementById(htmlObj.id  + "_text") ;
        iconObj.classList = []; options[data.status.toLowerCase()].split(' ').forEach(function(cls){iconObj.classList.add(cls)});
        iconObj.style.color = options['colors'][data.status.toUpperCase()];
        textObj.innerText = data.text
      }'''

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsHtmlDashboard.JsHtmlTask
    """
    if self._dom is None:
      self._dom = JsHtmlDashboard.JsHtmlTask(self, report=self._report)
    return self._dom

  @property
  def options(self):
    """
    Description:
    -----------
    Property to set all the Tasks properties

    :rtype: OptDashboards.OptionTask
    """
    return self.__options

  def loading(self, label="Processing data"):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param label:
    """
    return self.icon.dom.setAttribute("class", "fas fa-spinner fa-spin")

  def click(self, jsFncs, profile=False, source_event=None, onReady=False):
    self.style.css.cursor = "pointer"
    if onReady:
      self._report.body.onReady([self.dom.events.trigger("click")])
    return self.on("click", jsFncs, profile, source_event)

  def __str__(self):
    return "<div %s>%s%s</div>" % (self.get_attrs(pyClassNames=self.style.get_classes()), self.icon.html(), self.text.html())

