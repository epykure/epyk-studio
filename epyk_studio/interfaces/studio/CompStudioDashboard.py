#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.interfaces.components import CompFields
from epyk.interfaces.components import CompCalendars
from epyk.interfaces.graphs import CompCharts
from epyk.core.html import Defaults as defaultsHtml

from epyk_studio.core import html
from epyk_studio.lang import get_lang


class Dashboard(CompFields.Fields, CompFields.Timelines, CompCharts.Graphs):

  def __init__(self, ui):
    super(Dashboard, self).__init__(ui)

  def task(self, label, status=None, width=(100, "%"), height=(25, "px"), html_code=None, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Attributes:
    ----------
    :param label: String. Optional. The task label.
    :param status: String. Optional. The status code.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    map_status = {True: "COMPLETED", False: 'FAILED', None: 'WAITING'}.get(status, status)
    dflt_options = {"status": map_status}
    if options is not None:
      dflt_options.update(options)
    component = html.HtmlDashboards.Task(self.page, label, width, height, html_code, dflt_options, profile)
    return component

  def filters(self, items=None, button=None, width=("auto", ""), height=(60, "px"), html_code=None, helper=None,
              options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Attributes:
    ----------
    :param items:
    :param button:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. The value to be displayed to the helper icon.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {}
    container = self.page.ui.div(width=width)
    if options.get("select", 'select') == 'input':
      container.select = self.page.ui.inputs.autocomplete(
        html_code="%s_select" % html_code if html_code is not None else html_code,
        width=(defaultsHtml.TEXTS_SPAN_WIDTH, 'px'))
      container.select.style.css.text_align = "left"
      container.select.style.css.padding_left = 5
      container.select.options.liveSearch = True
    else:
      container.select = self.page.ui.select(
        html_code="%s_select" % html_code if html_code is not None else html_code)
      container.select.attr['data-width'] = '%spx' % options.get('width', defaultsHtml.TEXTS_SPAN_WIDTH)
      container.select.options.liveSearch = True
    if options.get("autocomplete"):
      container.input = self.page.ui.inputs.autocomplete(
        html_code="%s_input" % html_code if html_code is not None else html_code,
        width=(defaultsHtml.INPUTS_MIN_WIDTH, 'px'), options={"select": True})
    else:
      container.input = self.page.ui.input(
        html_code="%s_input" % html_code if html_code is not None else html_code,
        width=(defaultsHtml.INPUTS_MIN_WIDTH, 'px'), options={"select": True})
    container.input.style.css.text_align = 'left'
    container.input.style.css.padding_left = 5
    container.input.style.css.margin_left = 10
    if button is None:
      button = self.page.ui.buttons.colored("add")
      button.style.css.margin_left = 10
    container.button = button
    container.clear = self.page.ui.icon("fas fa-times")
    container.clear.style.css.color = self.page.theme.danger[1]
    container.clear.style.css.margin_left = 20
    container.clear.tooltip("Clear all filters")
    container.add(self.page.ui.div([container.select, container.input, container.button, container.clear]))
    container.filters = self.page.ui.panels.filters(
      items, container.select.dom.content, (100, '%'), height, html_code, helper, options, profile)
    container.add(container.filters)
    container.clear.click([
      container.filters.dom.clear()
    ])
    container.button.click([
      container.filters.dom.add(container.input.dom.content, container.select.dom.content)
    ])
    container.input.enter(container.button.dom.events.trigger("click"))
    return container

  def columns(self, width=('auto', ""), height=('auto', ""), html_code=None, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Attributes:
    ----------
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    component = html.HtmlDashboards.Columns(
      self.page, [], None, width, height, html_code, None, options, profile)
    component.style.css.min_height = 20
    component.style.css.min_width = 150
    component.css({"display": "inline-block", 'text-align': 'center', "margin-top": '5px', "list-style": 'none',
                   'border': "1px dashed %s" % self.page.theme.colors[-1]})
    component.style.css.padding = 5
    component.style.css.margins(left=5, right=5)
    return component

  def pivots(self, rows=None, columns=None, width=(100, "%"), height=('auto', ""), html_code=None, options=None,
             profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Attributes:
    ----------
    :param columns: List. Optional. The list of key from the record to be used as columns in the table.
    :param rows: List. Optional. The list of key from the record to be used as rows in the table.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {}
    dflt_options = {"sub_chart": False, "max": {"rows": 1}, "columns": get_lang(options.get("lang")).COLUMNS,
                    'rows': get_lang(options.get("lang")).VALUES}
    if options is not None:
      dflt_options.update(options)
    component = html.HtmlDashboards.Pivots(self.page, width, height, html_code, options, profile)
    if rows is None:
      row_options = dict(dflt_options)
      row_options["max"] = dflt_options.get("max", {}).get("rows")
      component.rows = self.page.ui.lists.drop(html_code="%s_rows" % component.htmlCode, options=row_options)
      if row_options["max"] == 1:
        component.rows.style.css.min_height = 20
      component.rows.style.css.margin_top = 0
    else:
      component.rows = rows

    if dflt_options.get("sub_chart"):
      component.sub_rows = self.page.ui.lists.drop(
        html_code="%s_sub_rows" % component.htmlCode, options={"max": 1})
      component.sub_rows.style.css.min_height = 20
      component.sub_rows.style.css.margin_top = 0
      component.sub_rows.options.managed = False
    else:
      component.sub_rows = None
    component.rows.options.managed = False
    if columns is None:
      columns_options = dict(dflt_options)
      columns_options["max"] = dflt_options.get("max", {}).get("columns")
      component.columns = self.page.ui.lists.drop(
        html_code="%s_columns" % component.htmlCode, options=columns_options)
      component.columns.style.css.margin_top = 0
    else:
      component.columns = columns
    component.columns.options.managed = False
    component.style.css.margin_top = 5
    component.style.css.margin_bottom = 5
    return component

  def reduce(self, icon="fas fa-folder-minus", tooltip="", top=(90, "px"), left=(10, "px"), options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Attributes:
    ----------
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param top: Tuple. Optional. A tuple with the integer for the component's distance to the top of the page.
    :param left: Tuple. Optional. A tuple with the integer for the component's distance to the left of the page.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    note = self.page.ui.icon(icon, options=options, profile=profile)
    note.tooltip(tooltip)
    note.style.css.remove("color")
    note.style.css.cursor = "pointer"
    note.style.add_classes.div.color_hover()
    note.style.css.fixed(top=top[0], left=left[0])
    return note

  def notes(self, icon="fas fa-pencil-alt", top=(60, "px"), left=(10, "px"), options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Attributes:
    ----------
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param top: Tuple. Optional. A tuple with the integer for the component's distance to the top of the page.
    :param left: Tuple. Optional. A tuple with the integer for the component's distance to the left of the page.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    note = self.page.ui.icon(icon, options=options, profile=profile)
    note.tooltip("Add a floating comment")
    note.style.css.remove("color")
    note.style.css.cursor = "pointer"
    note.style.add_classes.div.color_hover()
    note.style.css.fixed(top=top[0], left=left[0])
    note.click([
      '''
      var div = document.createElement("div");
      div.style.position = "absolute"; div.style.top = (window.pageYOffset + %s) + "px"; 
      div.style.left = (window.pageXOffset + %s) + "px";
      
      var divText = document.createElement("div");
      divText.innerText = "comment"; divText.setAttribute("spellcheck", false);
      divText.style.display = "inline-block"; divText.style.marginRight = "5px"; divText.style.minHeight = "18px";
      divText.style.minWidth = "30px"; div.appendChild(divText);
      
      var spanClose = document.createElement("span");
      spanClose.innerHTML = "&times;"; spanClose.style.display = "inline-block"; spanClose.style.cursor = "pointer";
      spanClose.addEventListener("click", function(){this.parentNode.remove()})
      div.appendChild(spanClose);

      divText.addEventListener("click", function(event){
        event.preventDefault(); window.getSelection().selectAllChildren(this); this.contentEditable = true});
      divText.addEventListener("onblur", function(){this.contentEditable = false});
      
      document.body.appendChild(div); dragElement(div);
      ''' % (top[0]+10, left[0]+40)
    ])

    self.page._props['js']['builders'].add('''
    function dragElement(elmnt){
        var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
        if (document.getElementById(elmnt.id + "header")) {
          document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown} 
        else {elmnt.onmousedown = dragMouseDown}
      
        function dragMouseDown(e) {
          e = e || window.event; e.preventDefault(); pos3 = e.clientX; pos4 = e.clientY;
          document.onmouseup = closeDragElement; document.onmousemove = elementDrag}
      
        function elementDrag(e) {
          e = e || window.event; e.preventDefault(); pos1 = pos3 - e.clientX; pos2 = pos4 - e.clientY;
          pos3 = e.clientX; pos4 = e.clientY; elmnt.style.top = (elmnt.offsetTop - pos2) +"px";
          elmnt.style.left = (elmnt.offsetLeft - pos1) +"px"}
      
        function closeDragElement(){document.onmouseup = null; document.onmousemove = null}
      }''')
    return note

  def process(self, fill=None, border=None, width=(30, "px"), height=(30, "px"), options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://uxwing.com/business-management-icon/

    Templates:

    Attributes:
    ----------
    :param fill:
    :param border:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    svg = self.page.ui.pictos.path(
      fill=fill, stroke=border, width=width, height=height, options=options, profile=profile,
      path="M78.37,79.91c-0.19,0.47-0.49,0.91-0.88,1.3L73.5,85.2l-0.02,0.02c-0.39,0.39-0.83,0.69-1.3,0.88 c-0.49,0.21-1,0.32-1.55,0.32c-0.55,0-1.07-0.11-1.55-0.32c-0.47-0.21-0.9-0.51-1.27-0.9l-2.6-2.57c-0.16,0.07-0.32,0.16-0.47,0.23 c-0.44,0.21-0.9,0.39-1.34,0.56c-0.02,0.02-0.04,0.02-0.07,0.02c-0.44,0.18-0.91,0.33-1.42,0.49c-0.16,0.05-0.32,0.11-0.49,0.14 l0,3.17c0,0.55-0.11,1.07-0.3,1.55c-0.19,0.47-0.49,0.9-0.88,1.28l-0.04,0.04c-0.39,0.37-0.83,0.67-1.3,0.86 c-0.48,0.19-0.99,0.3-1.51,0.3h-5.7c-0.55,0-1.06-0.11-1.55-0.3c-0.47-0.19-0.91-0.49-1.3-0.88c-0.39-0.39-0.69-0.83-0.88-1.3 c-0.19-0.48-0.3-0.99-0.3-1.55v-3.62c-0.18-0.07-0.35-0.12-0.53-0.19c-0.47-0.18-0.93-0.39-1.41-0.6 c-0.47-0.23-0.93-0.44-1.37-0.67c-0.14-0.07-0.28-0.16-0.42-0.23L41.7,84.2l-0.05,0.05c-0.39,0.37-0.83,0.65-1.3,0.84 c-0.47,0.19-0.98,0.28-1.51,0.28c-0.53,0-1.04-0.09-1.51-0.28c-0.47-0.19-0.91-0.46-1.3-0.83c-0.02-0.02-0.04-0.02-0.04-0.04 l-3.98-4.03c-0.39-0.37-0.7-0.81-0.9-1.28c-0.21-0.47-0.32-1-0.32-1.57c0-0.55,0.11-1.07,0.32-1.57c0.21-0.49,0.51-0.91,0.9-1.28 l2.55-2.55c-0.09-0.18-0.16-0.33-0.23-0.49c-0.19-0.44-0.39-0.9-0.58-1.39c-0.18-0.46-0.35-0.95-0.49-1.44 c-0.05-0.16-0.11-0.33-0.14-0.49h-3.17c-0.55,0-1.07-0.11-1.55-0.3c-0.47-0.19-0.9-0.49-1.28-0.88l-0.04-0.04 c-0.37-0.39-0.67-0.83-0.86-1.28c-0.19-0.48-0.3-0.99-0.3-1.51v-5.7c0-1.13,0.39-2.08,1.18-2.85c0.39-0.39,0.83-0.69,1.3-0.88 c0.48-0.19,0.99-0.3,1.55-0.3h3.62c0.07-0.18,0.12-0.35,0.19-0.53c0.18-0.47,0.39-0.93,0.6-1.41c0.23-0.48,0.44-0.93,0.67-1.37 c0.07-0.14,0.16-0.28,0.23-0.42l-2.27-2.23l-0.05-0.05c-0.37-0.39-0.65-0.83-0.84-1.3c-0.19-0.47-0.28-0.98-0.28-1.51 c0-0.53,0.09-1.04,0.28-1.51c0.19-0.47,0.46-0.91,0.83-1.3c0.02-0.02,0.02-0.04,0.04-0.04L37,38.73c0.39-0.39,0.83-0.69,1.3-0.88 c0.49-0.21,1-0.32,1.55-0.32s1.07,0.11,1.55,0.32c0.47,0.21,0.9,0.51,1.27,0.9l2.55,2.55c0.18-0.09,0.33-0.16,0.49-0.23 c0.44-0.19,0.9-0.39,1.39-0.58c0.46-0.18,0.95-0.35,1.44-0.49c0.18-0.05,0.33-0.11,0.49-0.14l0-3.17c0-0.55,0.11-1.07,0.3-1.55 c0.19-0.47,0.49-0.9,0.88-1.28l0.04-0.04c0.39-0.37,0.83-0.67,1.28-0.86c0.48-0.19,0.99-0.3,1.51-0.3h5.7 c0.55,0,1.06,0.11,1.55,0.3c0.47,0.19,0.91,0.49,1.3,0.88c0.39,0.39,0.69,0.83,0.88,1.3c0.19,0.48,0.3,0.99,0.3,1.55v3.62 c0.18,0.07,0.35,0.12,0.53,0.19c0.47,0.18,0.93,0.39,1.41,0.6c0.47,0.23,0.93,0.44,1.37,0.67c0.14,0.07,0.28,0.16,0.42,0.23 l2.23-2.23c0.39-0.39,0.83-0.69,1.3-0.9c0.49-0.21,1-0.32,1.55-0.32c0.55,0,1.06,0.11,1.55,0.32c0.49,0.21,0.91,0.49,1.3,0.9 l3.99,3.99l0.02,0.02c0.39,0.39,0.69,0.83,0.88,1.3c0.21,0.49,0.32,1,0.32,1.55c0,0.55-0.11,1.07-0.32,1.55 c-0.21,0.48-0.51,0.9-0.9,1.27l-2.55,2.6c0.07,0.16,0.16,0.32,0.23,0.47c0.18,0.4,0.37,0.84,0.56,1.32 c0.02,0.02,0.02,0.04,0.02,0.07c0.18,0.46,0.35,0.95,0.49,1.44c0.05,0.16,0.11,0.33,0.14,0.49h3.17c0.55,0,1.07,0.11,1.55,0.3 c0.47,0.19,0.9,0.49,1.28,0.88l0.04,0.04c0.37,0.39,0.67,0.83,0.86,1.28c0.19,0.48,0.3,0.99,0.3,1.51v5.7 c0,0.55-0.11,1.06-0.3,1.55c-0.19,0.47-0.49,0.91-0.88,1.32c-0.39,0.39-0.83,0.69-1.3,0.88c-0.48,0.19-0.99,0.3-1.55,0.3h-3.62 c-0.07,0.18-0.12,0.35-0.19,0.53c-0.18,0.47-0.37,0.93-0.6,1.41c-0.23,0.47-0.44,0.93-0.67,1.37c-0.07,0.14-0.16,0.28-0.23,0.42 l2.23,2.23c0.39,0.39,0.69,0.83,0.9,1.3c0.21,0.49,0.32,1,0.32,1.55c0,0.55-0.11,1.06-0.32,1.55L78.37,79.91L78.37,79.91z M44.99,116c-12.7-2.39-23.86-9.16-31.85-18.67C5.09,87.76,0.25,75.43,0.25,61.99c0-12.63,4.27-24.28,11.46-33.57 C19.04,18.93,29.41,11.9,41.37,8.8l1.78,6.86c-10.41,2.7-19.44,8.82-25.83,17.09c-6.24,8.08-9.95,18.22-9.95,29.24 c0,11.73,4.21,22.47,11.19,30.78c6.68,7.95,15.91,13.7,26.44,15.98v-7.33l13.39,10.99l-13.39,10.99L44.99,116L44.99,116L44.99,116z M65.44,7.99c12.58,2.37,23.65,9.03,31.63,18.41c8.17,9.6,13.1,22.03,13.1,35.59c0,11.93-3.8,22.97-10.26,31.98 c-6.63,9.25-16.06,16.35-27.06,20.08l-1.14-3.36l-1.14-3.36c0.28-0.09,0.56-0.19,0.83-0.29c9.21-3.31,17.11-9.38,22.72-17.2 c5.62-7.84,8.93-17.45,8.93-27.84c0-11.84-4.28-22.67-11.38-31.01c-6.67-7.84-15.82-13.49-26.24-15.76v7.29L52.05,11.52L65.44,0.53 L65.44,7.99L65.44,7.99L65.44,7.99z M65.16,61.97c0,0.69-0.07,1.35-0.19,1.99h-0.02c-0.12,0.65-0.32,1.27-0.56,1.86 c-0.26,0.62-0.56,1.2-0.91,1.71c-0.33,0.53-0.74,1.02-1.18,1.46c-0.46,0.46-0.93,0.84-1.46,1.2c-0.51,0.33-1.09,0.65-1.71,0.91 c-0.02,0.02-0.05,0.02-0.07,0.04c-0.56,0.23-1.16,0.4-1.78,0.53c-0.65,0.12-1.3,0.19-1.99,0.19c-0.69,0-1.35-0.07-1.99-0.19 c-0.65-0.12-1.27-0.32-1.86-0.56c-0.62-0.26-1.2-0.56-1.71-0.91c-0.53-0.35-1.02-0.76-1.46-1.2c-0.44-0.46-0.83-0.93-1.18-1.46 c-0.33-0.51-0.65-1.09-0.91-1.71c-0.02-0.02-0.02-0.05-0.04-0.07c-0.23-0.56-0.4-1.16-0.53-1.78c-0.12-0.65-0.19-1.3-0.19-1.99 c0-0.69,0.07-1.35,0.19-1.99c0.12-0.65,0.32-1.27,0.56-1.86c0.26-0.62,0.56-1.2,0.91-1.71c0.33-0.53,0.74-1.02,1.18-1.46 c0.46-0.46,0.93-0.84,1.46-1.2c0.51-0.33,1.09-0.65,1.71-0.92c0.02-0.02,0.05-0.02,0.07-0.04c0.58-0.23,1.18-0.4,1.79-0.53 c0.65-0.12,1.3-0.19,1.99-0.19c0.69,0,1.35,0.07,1.99,0.19c0.65,0.12,1.27,0.32,1.86,0.56c0.62,0.26,1.2,0.56,1.71,0.92 c0.53,0.35,1.02,0.76,1.46,1.2c0.44,0.46,0.83,0.93,1.18,1.46c0.33,0.51,0.65,1.09,0.91,1.71c0.02,0.02,0.02,0.05,0.04,0.07 c0.23,0.56,0.4,1.16,0.53,1.78C65.09,60.63,65.16,61.28,65.16,61.97L65.16,61.97z",
    )
    return svg

  def schedule(self, fill=None, border=None, width=(30, "px"), height=(30, "px"), options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://uxwing.com/daily-schedule-icon/

    Templates:

    Attributes:
    ----------
    :param fill:
    :param border:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    svg = self.page.ui.pictos.path(
      fill=fill, stroke=border, width=width, height=height, options=options, profile=profile,
      path="M69.66,4.05c0-2.23,2.2-4.05,4.94-4.05c2.74,0,4.94,1.81,4.94,4.05v17.72c0,2.23-2.2,4.05-4.94,4.05 c-2.74,0-4.94-1.81-4.94-4.05V4.05L69.66,4.05z M91.37,57.03c4.26,0,8.33,0.85,12.05,2.39c3.87,1.6,7.34,3.94,10.24,6.84 c2.9,2.9,5.24,6.38,6.84,10.23c1.54,3.72,2.39,7.79,2.39,12.05c0,4.26-0.85,8.33-2.39,12.05c-1.6,3.87-3.94,7.34-6.84,10.24 c-2.9,2.9-6.38,5.24-10.23,6.84c-3.72,1.54-7.79,2.39-12.05,2.39c-4.26,0-8.33-0.85-12.05-2.39c-3.87-1.6-7.34-3.94-10.24-6.84 c-2.9-2.9-5.24-6.38-6.84-10.24c-1.54-3.72-2.39-7.79-2.39-12.05c0-4.26,0.85-8.33,2.39-12.05c1.6-3.87,3.94-7.34,6.84-10.24 c2.9-2.9,6.38-5.24,10.23-6.84C83.04,57.88,87.1,57.03,91.37,57.03L91.37,57.03z M89.01,75.37c0-0.76,0.31-1.45,0.81-1.95l0,0l0,0 c0.5-0.5,1.19-0.81,1.96-0.81c0.77,0,1.46,0.31,1.96,0.81c0.5,0.5,0.81,1.19,0.81,1.96v14.74l11.02,6.54l0.09,0.06 c0.61,0.39,1.01,0.98,1.17,1.63c0.17,0.68,0.09,1.42-0.28,2.06l-0.02,0.03c-0.02,0.04-0.04,0.07-0.07,0.1 c-0.39,0.6-0.98,1-1.62,1.16c-0.68,0.17-1.42,0.09-2.06-0.28l-12.32-7.29c-0.43-0.23-0.79-0.58-1.05-0.99 c-0.26-0.42-0.41-0.91-0.41-1.43h0L89.01,75.37L89.01,75.37L89.01,75.37z M109.75,70.16c-2.4-2.4-5.26-4.33-8.43-5.64 c-3.06-1.27-6.42-1.96-9.95-1.96s-6.89,0.7-9.95,1.96c-3.17,1.31-6.03,3.24-8.43,5.64c-2.4,2.4-4.33,5.26-5.64,8.43 c-1.27,3.06-1.96,6.42-1.96,9.95c0,3.53,0.7,6.89,1.96,9.95c1.31,3.17,3.24,6.03,5.64,8.43c2.4,2.4,5.26,4.33,8.43,5.64 c3.06,1.27,6.42,1.96,9.95,1.96s6.89-0.7,9.95-1.96c3.17-1.31,6.03-3.24,8.43-5.64c4.71-4.71,7.61-11.2,7.61-18.38 c0-3.53-0.7-6.89-1.96-9.95C114.08,75.42,112.15,72.56,109.75,70.16L109.75,70.16z M13.45,57.36c-0.28,0-0.53-1.23-0.53-2.74 c0-1.51,0.22-2.73,0.53-2.73h13.48c0.28,0,0.53,1.23,0.53,2.73c0,1.51-0.22,2.74-0.53,2.74H13.45L13.45,57.36z M34.94,57.36 c-0.28,0-0.53-1.23-0.53-2.74c0-1.51,0.22-2.73,0.53-2.73h13.48c0.28,0,0.53,1.23,0.53,2.73c0,1.51-0.22,2.74-0.53,2.74H34.94 L34.94,57.36z M56.43,57.36c-0.28,0-0.53-1.23-0.53-2.74c0-1.51,0.22-2.73,0.53-2.73h13.48c0.28,0,0.53,1.22,0.53,2.72 c-1.35,0.84-2.65,1.76-3.89,2.75H56.43L56.43,57.36z M13.48,73.04c-0.28,0-0.53-1.23-0.53-2.74c0-1.51,0.22-2.74,0.53-2.74h13.48 c0.28,0,0.53,1.23,0.53,2.74c0,1.51-0.22,2.74-0.53,2.74H13.48L13.48,73.04z M34.97,73.04c-0.28,0-0.53-1.23-0.53-2.74 c0-1.51,0.22-2.74,0.53-2.74h13.48c0.28,0,0.53,1.23,0.53,2.74c0,1.51-0.22,2.74-0.53,2.74H34.97L34.97,73.04z M13.51,88.73 c-0.28,0-0.53-1.23-0.53-2.74c0-1.51,0.22-2.74,0.53-2.74h13.48c0.28,0,0.53,1.23,0.53,2.74c0,1.51-0.22,2.74-0.53,2.74H13.51 L13.51,88.73z M35,88.73c-0.28,0-0.53-1.23-0.53-2.74c0-1.51,0.22-2.74,0.53-2.74h13.48c0.28,0,0.53,1.23,0.53,2.74 c0,1.51-0.22,2.74-0.53,2.74H35L35,88.73z M25.29,4.05c0-2.23,2.2-4.05,4.94-4.05c2.74,0,4.94,1.81,4.94,4.05v17.72 c0,2.23-2.21,4.05-4.94,4.05c-2.74,0-4.94-1.81-4.94-4.05V4.05L25.29,4.05z M5.44,38.74h94.08v-20.4c0-0.7-0.28-1.31-0.73-1.76 c-0.45-0.45-1.09-0.73-1.76-0.73h-9.02c-1.51,0-2.74-1.23-2.74-2.74c0-1.51,1.23-2.74,2.74-2.74h9.02c2.21,0,4.19,0.89,5.64,2.34 c1.45,1.45,2.34,3.43,2.34,5.64v32.39c-1.8-0.62-3.65-1.12-5.55-1.49v-5.06h0.06H5.44v52.83c0,0.7,0.28,1.31,0.73,1.76 c0.45,0.45,1.09,0.73,1.76,0.73h44.71c0.51,1.9,1.15,3.75,1.92,5.53H7.98c-2.2,0-4.19-0.89-5.64-2.34C0.89,101.26,0,99.28,0,97.07 V18.36c0-2.2,0.89-4.19,2.34-5.64c1.45-1.45,3.43-2.34,5.64-2.34h9.63c1.51,0,2.74,1.23,2.74,2.74c0,1.51-1.23,2.74-2.74,2.74H7.98 c-0.7,0-1.31,0.28-1.76,0.73c-0.45,0.45-0.73,1.09-0.73,1.76v20.4H5.44L5.44,38.74z M43.07,15.85c-1.51,0-2.74-1.23-2.74-2.74 c0-1.51,1.23-2.74,2.74-2.74h18.36c1.51,0,2.74,1.23,2.74,2.74c0,1.51-1.23,2.74-2.74,2.74H43.07L43.07,15.85z"
    )
    return svg

  def table(self, records=None, cols=None, rows=None, width=(100, '%'), height=(None, 'px'), html_code=None,
            options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Templates:

    Attributes:
    ----------
    :param records:
    :param cols: List. Optional. The list of key from the record to be used as columns in the table.
    :param rows: List. Optional. The list of key from the record to be used as rows in the table.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    dflt_options = {"padding": 10}
    if options is not None:
      dflt_options.update(options)
    table = self.page.ui.table(
      records, cols=cols, rows=rows, width=width, height=height, html_code=html_code, options=options, profile=profile)
    ct = self.page.ui.div(table, profile=profile)
    ct.table = table
    ct.style.css.padding = '0 %spx' % dflt_options['padding']
    return ct

  def line(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
           options=None, html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Templates:

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    dflt_options = {"padding": 10}
    if options is not None:
      dflt_options.update(options)
    line = self.page.ui.charts.chartJs.line(
      record, y_columns=y_columns, x_axis=x_axis, profile=profile, width=width, height=height, options=options,
      html_code=html_code)
    ct = self.page.ui.div(line, profile=profile)
    ct.chart = line
    ct.style.css.padding = '0 %spx' % dflt_options['padding']
    return ct

  def bar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None,
          html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Templates:

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    dflt_options = {"padding": 10}
    if options is not None:
      dflt_options.update(options)
    line = self.page.ui.charts.chartJs.bar(
      record, y_columns=y_columns, x_axis=x_axis, profile=profile, width=width, height=height, options=options,
      html_code=html_code)
    ct = self.page.ui.div(line, profile=profile)
    ct.chart = line
    ct.style.css.padding = '0 %spx' % dflt_options['padding']
    return ct

  def scatter(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
              options=None, html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Templates:

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    dflt_options = {"padding": 10}
    if options is not None:
      dflt_options.update(options)
    line = self.page.ui.charts.chartJs.scatter(
      record, y_columns=y_columns, x_axis=x_axis, profile=profile, width=width, height=height, options=options,
      html_code=html_code)
    ct = self.page.ui.div(line, profile=profile)
    ct.chart = line
    ct.style.css.padding = '0 %spx' % dflt_options['padding']
    return ct

  def pie(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None,
          html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Templates:

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    dflt_options = {"padding": 10}
    if options is not None:
      dflt_options.update(options)
    line = self.page.ui.charts.chartJs.pie(
      record, y_columns=y_columns, x_axis=x_axis, profile=profile, width=width, height=height, options=options,
      html_code=html_code)
    ct = self.page.ui.div(line, profile=profile)
    ct.chart = line
    ct.style.css.padding = '0 %spx' % dflt_options['padding']
    return ct

  def radar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None,
            html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Templates:

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    dflt_options = {"padding": 10}
    if options is not None:
      dflt_options.update(options)
    line = self.page.ui.charts.chartJs.radar(
      record, y_columns=y_columns, x_axis=x_axis, profile=profile, width=width, height=height, options=options,
      html_code=html_code)
    ct = self.page.ui.div(line, profile=profile)
    ct.chart = line
    ct.style.css.padding = '0 %spx' % dflt_options['padding']
    return ct

  def box(self, record, y_columns=None, x_columns=None, profile=None, width=(100, "%"), height=(330, "px"),
          options=None, html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Templates:

    Attributes:
    ----------
    :param record: List of dict. Optional. The Python list of dictionaries.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_columns: List. Optional. The columns corresponding to a key in the dictionaries in the record.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    dflt_options = {"padding": 10}
    if options is not None:
      dflt_options.update(options)
    line = self.page.ui.charts.plotly.box(
      record, y_columns=y_columns, x_columns=x_columns, profile=profile, width=width, height=height, options=options,
      html_code=html_code)
    ct = self.page.ui.div(line, profile=profile)
    ct.chart = line
    ct.style.css.padding = '0 %spx' % dflt_options['padding']
    return ct

  def checklist(self, fill=None, border=None, width=(30, "px"), height=(30, "px"), options=None, html_code=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://uxwing.com/check-list-icon/

    Templates:

    Attributes:
    ----------
    :param fill:
    :param border:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side)
    """
    svg = self.page.ui.pictos.path(
      fill=fill, stroke=border, width=width, height=height, options=options, profile=profile,
      path="M53.4,91.75c-1.96,0-3.54-1.59-3.54-3.54s1.59-3.54,3.54-3.54h19.85c1.96,0,3.54,1.59,3.54,3.54s-1.59,3.54-3.54,3.54H53.4 L53.4,91.75z M23.23,88.24c-0.8-1.2-0.48-2.82,0.72-3.63c1.2-0.8,2.82-0.48,3.63,0.72L29,87.45l5.65-6.88 c0.92-1.11,2.56-1.27,3.68-0.36c1.11,0.92,1.27,2.56,0.36,3.68l-7.82,9.51c-0.17,0.22-0.38,0.42-0.62,0.58 c-1.2,0.8-2.82,0.48-3.63-0.72L23.23,88.24L23.23,88.24z M23.23,63.34c-0.8-1.2-0.48-2.82,0.72-3.63c1.2-0.8,2.82-0.48,3.63,0.72 L29,62.55l5.65-6.88c0.92-1.11,2.56-1.27,3.68-0.36c1.11,0.92,1.27,2.56,0.36,3.68l-7.82,9.51c-0.17,0.22-0.38,0.42-0.62,0.58 c-1.2,0.8-2.82,0.48-3.63-0.72L23.23,63.34L23.23,63.34z M23.23,38.43c-0.8-1.2-0.48-2.82,0.72-3.63c1.2-0.8,2.82-0.48,3.63,0.72 L29,37.64l5.65-6.88c0.92-1.11,2.56-1.27,3.68-0.36c1.11,0.92,1.27,2.56,0.36,3.68l-7.82,9.51c-0.17,0.22-0.38,0.42-0.62,0.58 c-1.2,0.8-2.82,0.48-3.63-0.72L23.23,38.43L23.23,38.43z M53.4,39.03c-1.96,0-3.54-1.59-3.54-3.54s1.59-3.54,3.54-3.54h36.29 c1.96,0,3.54,1.59,3.54,3.54s-1.59,3.54-3.54,3.54H53.4L53.4,39.03z M8.22,0h101.02c2.27,0,4.33,0.92,5.81,2.4 c1.48,1.48,2.4,3.54,2.4,5.81v106.44c0,2.27-0.92,4.33-2.4,5.81c-1.48,1.48-3.54,2.4-5.81,2.4H8.22c-2.27,0-4.33-0.92-5.81-2.4 C0.92,119,0,116.93,0,114.66V8.22C0,5.95,0.92,3.88,2.4,2.4C3.88,0.92,5.95,0,8.22,0L8.22,0z M109.24,7.08H8.22 c-0.32,0-0.61,0.13-0.82,0.34c-0.21,0.21-0.34,0.5-0.34,0.82v106.44c0,0.32,0.13,0.61,0.34,0.82c0.21,0.21,0.5,0.34,0.82,0.34 h101.02c0.32,0,0.61-0.13,0.82-0.34c0.21-0.21,0.34-0.5,0.34-0.82V8.24c0-0.32-0.13-0.61-0.34-0.82 C109.84,7.21,109.55,7.08,109.24,7.08L109.24,7.08z M53.4,65.39c-1.96,0-3.54-1.59-3.54-3.54s1.59-3.54,3.54-3.54h36.29 c1.96,0,3.54,1.59,3.54,3.54s-1.59,3.54-3.54,3.54H53.4L53.4,65.39z"
    )
    return svg

  def increase(self, fill=None, border=None, width=(30, "px"), height=(30, "px"), options=None, html_code=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://uxwing.com/check-list-icon/

    Templates:

    Attributes:
    ----------
    :param fill:
    :param border:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.

    """
    svg = self.page.ui.pictos.path(
      fill=fill, stroke=border, width=width, height=height, options=options, profile=profile,
      path="M2.03,56.52c-2.66,2.58-2.72,6.83-0.13,9.49c2.58,2.66,6.83,2.72,9.49,0.13l27.65-26.98l23.12,22.31 c2.67,2.57,6.92,2.49,9.49-0.18l37.77-38.22v19.27c0,3.72,3.01,6.73,6.73,6.73s6.73-3.01,6.73-6.73V6.71h-0.02 c0-1.74-0.67-3.47-2-4.78c-1.41-1.39-3.29-2.03-5.13-1.91H82.4c-3.72,0-6.73,3.01-6.73,6.73c0,3.72,3.01,6.73,6.73,6.73h17.63 L66.7,47.2L43.67,24.97c-2.6-2.5-6.73-2.51-9.33,0.03L2.03,56.52L2.03,56.52z"
    )
    return svg

  def decrease(self, fill=None, border=None, width=(30, "px"), height=(30, "px"), options=None, html_code=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://uxwing.com/check-list-icon/

    Templates:

    Attributes:
    ----------
    :param fill:
    :param border:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    svg = self.page.ui.pictos.path(
      fill=fill, stroke=border, width=width, height=height, options=options, profile=profile,
      path="M2.03,11.52C-0.63,8.94-0.68,4.69,1.9,2.03c2.58-2.66,6.83-2.72,9.49-0.13l27.65,26.98L62.16,6.57 c2.67-2.57,6.92-2.49,9.49,0.18l37.77,38.22V25.7c0-3.72,3.01-6.73,6.73-6.73s6.73,3.01,6.73,6.73v35.63h-0.02 c0,1.74-0.67,3.47-2,4.78c-1.41,1.39-3.29,2.03-5.13,1.91H82.4c-3.72,0-6.73-3.01-6.73-6.73c0-3.72,3.01-6.73,6.73-6.73h17.63 L66.7,20.84L43.67,43.07c-2.6,2.5-6.73,2.51-9.33-0.03L2.03,11.52L2.03,11.52z"
    )
    return svg

  def performance(self, fill=None, border=None, width=(30, "px"), height=(30, "px"), options=None, html_code=None,
                  profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://uxwing.com/speedometer-icon/

    Templates:

    Attributes:
    ----------
    :param fill:
    :param border:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    svg = self.page.ui.pictos.path(
      fill=fill, stroke=border, width=width, height=height, options=options, profile=profile,
      path="M58.15,52.98l28.6-18.22c0.2-0.15,0.48-0.12,0.65,0.06l2.76,2.94c0.17,0.18,0.18,0.47,0.02,0.66L68.51,63.6 c-3.08,3.31-6.37,3.96-9.02,3.1c-1.32-0.43-2.47-1.22-3.35-2.25c-0.88-1.02-1.49-2.27-1.74-3.61c-0.49-2.67,0.49-5.66,3.73-7.85 L58.15,52.98L58.15,52.98z M19.33,106.17c-3.05-2.87-5.8-6.05-8.21-9.48c-2.39-3.4-4.44-7.06-6.11-10.91 C3.38,82,2.12,78.02,1.26,73.88C0.44,69.86,0,65.7,0,61.44c0-8.32,1.66-16.25,4.65-23.49C7.77,30.43,12.33,23.66,18,18 c5.66-5.66,12.43-10.23,19.95-13.34C45.19,1.66,53.12,0,61.44,0c8.3,0,16.21,1.66,23.43,4.66c7.52,3.12,14.28,7.7,19.95,13.37 c5.68,5.68,10.26,12.46,13.38,19.97c3.01,7.24,4.68,15.16,4.68,23.44c0,4.05-0.4,8.01-1.16,11.85c-0.78,3.94-1.95,7.75-3.46,11.4 c-1.54,3.71-3.43,7.25-5.64,10.55c-2.23,3.34-4.78,6.45-7.6,9.3c-0.19,0.19-0.51,0.19-0.7,0l-3.07-3.06 c-0.06-0.02-0.12-0.06-0.17-0.11l-8.56-8.56c-0.19-0.19-0.19-0.51,0-0.7l4.49-4.49c0.19-0.19,0.51-0.19,0.7,0l6.61,6.61 c1.4-1.82,2.69-3.72,3.85-5.7c1.25-2.12,2.35-4.34,3.3-6.63c1.28-3.1,2.29-6.35,2.97-9.71c0.64-3.12,1-6.35,1.07-9.64h-9.11 c-0.27,0-0.5-0.22-0.5-0.5V55.7c0-0.27,0.22-0.5,0.5-0.5h8.76c-0.68-5.85-2.31-11.43-4.72-16.58c-2.49-5.31-5.82-10.15-9.82-14.37 l-5.86,5.86c-0.19,0.19-0.51,0.19-0.7,0l-4.49-4.49c-0.19-0.19-0.19-0.51,0-0.7l5.65-5.65c-4.44-3.57-9.45-6.46-14.87-8.5 C75.1,8.8,69.47,7.62,63.6,7.39v8.03c0,0.27-0.22,0.5-0.5,0.5h-6.36c-0.27,0-0.5-0.22-0.5-0.5V7.59 c-5.83,0.55-11.4,2.04-16.54,4.29c-5.31,2.33-10.17,5.49-14.42,9.3l5.87,5.87c0.19,0.19,0.19,0.51,0,0.7l-4.49,4.49 c-0.19,0.19-0.51,0.19-0.7,0l-5.8-5.8c-3.73,4.4-6.78,9.41-8.96,14.86C9.1,46.6,7.79,52.29,7.44,58.23h9.03 c0.27,0,0.5,0.22,0.5,0.5v6.36c0,0.27-0.22,0.5-0.5,0.5H7.5c0.22,2.94,0.68,5.8,1.35,8.58c0.72,3.01,1.7,5.92,2.91,8.72 c1.05,2.43,2.27,4.76,3.64,6.98c1.29,2.09,2.72,4.09,4.28,5.97l7.24-7.24c0.19-0.19,0.51-0.19,0.7,0l4.49,4.49 c0.19,0.19,0.19,0.51,0,0.7c-4.14,4.14-8.09,8.11-12.09,12.36C19.84,106.35,19.53,106.36,19.33,106.17L19.33,106.17z"
    )
    return svg

  def editable(self, data=None, icon="fas fa-layer-group", width=(None, 'px'), height=(None, "px"), top=(90, "px"),
               left=(10, "px"), html_code=None, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Attributes:
    ----------
    :param data:
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param top: Tuple. Optional. A tuple with the integer for the component's distance to the top of the page.
    :param left: Tuple. Optional. A tuple with the integer for the component's distance to the left of the page.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    dflt_options = {'icon_family': 'font-awesome'}
    if options is not None:
      dflt_options.update(options)
    note = html.HtmlClipboards.ConfigEditor(
      self.page, icon, data, width, height, None, "Copy to get the configuration", dflt_options, html_code,
      profile)
    note._jsStyles["top"] = top[0]
    note.style.css.remove("color")
    note.style.add_classes.div.color_hover()
    note.style.css.fixed(top=top[0], left=left[0])
    note.icon = self.page.ui.icons.toggles.lock(
      options=options, profile=profile, html_code="%s_lock" % note.htmlCode)
    note.icon.style.css.fixed(top=(120, 'px'), left=(10, "px"))
    return note

  def explorer(self, width=(None, "px"), height=(None, "px"), html_code=None, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Attributes:
    ----------
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    container = html.HtmlClipboards.DataExplorer(self.page, width, height, html_code, options, profile)
    return container


class Calendar(CompCalendars.Calendar):

  def donut(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
            options=None, html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Attributes:
    ----------
    :param record:
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    dflt_options = {"padding": 10}
    if options is not None:
      dflt_options.update(options)
    line = self.page.ui.charts.chartJs.donut(
      record, y_columns=y_columns, x_axis=x_axis, profile=profile, width=width, height=height, options=options,
      html_code=html_code)
    ct = self.page.ui.div(line)
    ct.chart = line
    ct.style.css.padding = '0 %spx' % dflt_options['padding']
    return ct

  def radar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
            options=None, html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Attributes:
    ----------
    :param record:
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    dflt_options = {"padding": 10}
    if options is not None:
      dflt_options.update(options)
    line = self.page.ui.charts.chartJs.radar(
      record, y_columns=y_columns, x_axis=x_axis, profile=profile, width=width, height=height, options=options,
      html_code=html_code)
    ct = self.page.ui.div(line)
    ct.chart = line
    ct.style.css.padding = '0 %spx' % dflt_options['padding']
    return ct
