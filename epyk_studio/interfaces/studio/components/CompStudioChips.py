#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css import Defaults as defaultCss
from epyk.core.css import Colors


class StudioChips:

  def __init__(self, ui):
    self.page = ui.page

  def icons(self, records, html_code=None, width=(40, 'px'), inline=True, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Templates:

    Related Pages:

    Attributes:
    ----------
    :param records: List. Optional. The list of dictionaries with the input data.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param inline: Boolean. Optional. A flag to set the inline-block CSS property.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    pills = self.page.ui.panels.pills(html_code=html_code, options=options, profile=profile)
    r, g, b = Colors.getHexToRgb(self.page.theme.success[1])
    pills.options.css_tab_clicked = {'color': self.page.theme.colors[-1],
                                     'border': "1px solid %s" % self.page.theme.colors[4],
                                     'box-shadow': '0 3px 5px 0 rgba(%s,%s,%s,.08)' % (r, g, b)}
    pills.options.css_tab = {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer',
                             'margin': '0 2px 5px 0', 'box-shadow': '0 3px 5px 0 rgba(0,0,0,.08)',
                             'border-radius': '25px', "border": "1px solid %s" % self.page.theme.greys[0],
                             'color': self.page.theme.greys[-1]}
    pills.style.css.padding_bottom = 5
    pills.style.css.padding_top = 5
    records = records or []
    for i, rec in enumerate(records):
      tab_width = width
      if 'text' in rec:
        icon_comp = self.page.ui.icon(rec['icon'], profile=profile).css({"font-size": defaultCss.font(4)})
        icon_comp.style.css.margin_left = 0
        icon_comp.style.css.margin_right = 10
        text = rec['text']
        if inline:
          icon_comp.style.css.display = "inline-block"
          tab_width = (width[0] * 2, width[1])
          text = self.page.ui.text(rec['text'], profile=profile)
          text.style.css.bold()
          text.style.css.text_align = "center"
          text.style.css.display = "inline-block"
        icon = self.page.ui.div([icon_comp, text], profile=profile)
      else:
        icon = self.page.ui.div(self.page.ui.icon(rec['icon'], profile=profile).css(
          {"display": 'block', "width": '100%', "font-size": defaultCss.font(4)}), width=width, profile=profile)
        icon.attr["data-value"] = rec['icon']
      icon.style.css.text_align = "center"
      icon.options.managed = False
      pills.add_panel(icon, None, width=tab_width, selected=rec.get("selected", False))
    return pills

  def buttons(self, records, html_code=None, width=(40, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Templates:

    Related Pages:

    Attributes:
    ----------
    :param records: List. Optional. The list of dictionaries with the input data.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    pills = self.page.ui.panels.pills(htmlCode=html_code, options=options, profile=profile)
    r, g, b = Colors.getHexToRgb(self.page.theme.success[1])
    pills.options.css_tab_clicked = {'color': self.page.theme.colors[-1],
                                     'border': "1px solid %s" % self.page.theme.colors[4],
                                     'box-shadow': '0 3px 5px 0 rgba(%s,%s,%s,.08)' % (r, g, b)}
    pills.options.css_tab = {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer',
                             'margin': '0 10px 5px 0', 'box-shadow': '0 3px 5px 0 rgba(0,0,0,.08)',
                             'border-radius': '25px', "border": "1px solid %s" % self.page.theme.greys[0],
                             'color': self.page.theme.greys[-1]}
    pills.style.css.padding_bottom = 5
    pills.style.css.padding_top = 5
    records = records or []
    for rec in records:
      if not isinstance(rec, dict):
        pills.add_panel(rec, None, width=width, selected=rec.get("selected", False))
      elif rec.get('text'):
        pills.add_panel(rec.get('text', ''), None, width=width, selected=rec.get("selected", False))
    return pills

  def texts(self, records, html_code=None, width=(40, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Templates:

    Related Pages:

    Attributes:
    ----------
    :param records: List. Optional. The list of dictionaries with the input data.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    pills = self.page.ui.panels.pills(html_code=html_code, options=options, profile=profile)
    pills.style.css.padding_bottom = 5
    pills.style.css.padding_top = 5
    records = records or []
    for rec in records:
      if not isinstance(rec, dict):
        pills.add_panel(rec, None, width=width, selected=rec.get("selected", False))
      elif rec.get('text'):
        pills.add_panel(rec.get('text', ''), None, width=width, selected=rec.get("selected", False))
    return pills

  def images(self, records, html_code=None, radius=True, align="left", width=(45, 'px'), inline=True, options=None,
             profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Templates:

    Related Pages:

    Attributes:
    ----------
    :param records: List. Optional. The list of dictionaries with the input data.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param radius: Boolean. Optional. Define the radius of the container angles.
    :param align: String. Optional. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param inline: Boolean. Optional. A flag to set the inline-block CSS property.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    dflt_options = {"image_width": (25, 'px')}
    if radius is True:
      radius = dflt_options["image_width"][0]+10
    elif not radius:
      radius = 0
    if options is not None:
      dflt_options.update(options)
    pills = self.page.ui.panels.pills(html_code=html_code, align=align, options=options, profile=profile)
    r, g, b = Colors.getHexToRgb(self.page.theme.success[1])
    pills.options.css_tab_clicked = {'color': self.page.theme.colors[-1],
                                     'border': "1px solid %s" % self.page.theme.colors[4],
                                     'box-shadow': '0 3px 5px 0 rgba(%s,%s,%s,.08)' % (r, g, b)}
    pills.options.css_tab = {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer',
                             'margin': '0 2px 5px 0', 'border-radius': '%spx' % radius, 'padding': '5px',
                             'box-shadow': '0 3px 5px 0 rgba(0,0,0,.08)',
                             "border": "1px solid %s" % self.page.theme.greys[0],
                             'color': self.page.theme.greys[-1]}
    pills.style.css.padding_bottom = 5
    pills.style.css.padding_top = 5
    records = records or []
    for i, rec in enumerate(records):
      tab_width = width
      if 'text' in rec:
        img = self.page.ui.img(
          rec['image'], path=rec.get('path'), width=dflt_options["image_width"],
          height=dflt_options["image_width"], profile=profile).css(
          {"display": 'block', 'margin-left': '5px', 'margin-right': '5px', 'border-radius': '%spx' % radius,
           "font-size": defaultCss.font(4)})
        text = rec['text']
        if inline:
          img.style.css.display = "inline-block"
          tab_width = (width[0] * 2, width[1])
          text = self.page.ui.text(rec['text'], width=(100, "%"), profile=profile)
          text.style.css.bold()
          text.style.css.text_align = "center"
          text.style.css.padding_right = "5px"
          text.style.css.display = "inline-block"
        icon = self.page.ui.div([img, text], width=width, profile=profile)
      else:
        icon = self.page.ui.div(
          self.page.ui.img(
            rec['image'], path=rec.get('path'), width=dflt_options["image_width"],
            height=dflt_options["image_width"]).css(
            {'border-radius': '%spx' % radius, "font-size": defaultCss.font(4)}), profile=profile)
        icon.attr["data-value"] = rec['image']
      icon.style.css.text_align = "center"
      icon.options.managed = False
      pills.add_panel(icon, None, width=tab_width, selected=rec.get("selected", False))
    return pills
