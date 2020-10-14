#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.html import HtmlList

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
    self.text = self._report.ui.text(text, "%s_text" % self.htmlCode)
    self.text.options.managed = False
    self.add(self.icon)
    self.add(self.text)
    self._jsStyles['colors'] = {"COMPLETED": self._report.theme.success[1], "RUNNING": self._report.theme.warning[1],
                                "WAITING": self._report.theme.greys[5], "FAILED": self._report.theme.danger[1]}

  @property
  def _js__builder__(self):
    return ''' console.log(htmlObj);
      var iconObj = document.getElementById(htmlObj.id  + "_icon") ;
      iconObj.classList = []; options[data.toLowerCase()].split(' ').forEach(function(cls){iconObj.classList.add(cls)});
      iconObj.style.color = options['colors'][data];
      '''

  @property
  def options(self):
    """
    Description:
    -----------
    Property to set all the Tasks properties

    :rtype: OptDashboards.OptionTask
    """
    return self.__options

  def __str__(self):
    return "<div %s>%s%s</div>" % (self.get_attrs(pyClassNames=self.style.get_classes()), self.icon.html(), self.text.html())


class Filters(Html.Html):
  name = 'Dashboard Filters'


class Groups(Html.Html):
  name = 'Dashboard Filters'

