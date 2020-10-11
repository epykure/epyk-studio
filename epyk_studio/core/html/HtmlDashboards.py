#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.html import HtmlList

from epyk_studio.core.js.html import JsHtmlDashboard


class Pivots(Html.Html):
  name = 'Dashboard Pivots'

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(Pivots, self).__init__(report, [], htmlCode=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self.container = self._report.ui.row(position="top", options={"responsive": False})
    self.container.options.managed = False

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


class Filters(Html.Html):
  name = 'Dashboard Filters'


class Groups(Html.Html):
  name = 'Dashboard Filters'

