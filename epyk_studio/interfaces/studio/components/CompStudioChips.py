#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css import Defaults as css_defaults
from epyk.core.css import Colors


class StudioChips(object):

  def __init__(self, context):
    self.context = context

  def icons(self, records, htmlCode=None, width=(40, 'px'), inline=True, options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param records:
    :param htmlCode:
    :param width:
    :param inline:
    :param options:
    :param profile:
    """
    pills = self.context.rptObj.ui.panels.pills(htmlCode=htmlCode, options=options, profile=profile)
    r, g, b = Colors.getHexToRgb(self.context.rptObj.theme.success[1])
    pills.options.css_tab_clicked = {'color': self.context.rptObj.theme.colors[-1], 'border': "1px solid %s" % self.context.rptObj.theme.colors[4],
                                     'box-shadow': '0 3px 5px 0 rgba(%s,%s,%s,.08)' % (r, g, b)}
    pills.options.css_tab = {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 5px 0',
                             'box-shadow': '0 3px 5px 0 rgba(0,0,0,.08)', 'border-radius': '25px',
                             "border": "1px solid %s" % self.context.rptObj.theme.greys[0], 'color': self.context.rptObj.theme.greys[-1]}
    pills.style.css.padding_bottom = 5
    pills.style.css.padding_top = 5
    records = records or []
    for i, rec in enumerate(records):
      tab_width = width
      if 'text' in rec:
        icon_comp = self.context.rptObj.ui.icon(rec['icon']).css({"font-size": css_defaults.font(4)})
        icon_comp.style.css.margin_left = 0
        icon_comp.style.css.margin_right = 10
        text = rec['text']
        if inline:
          icon_comp.style.css.display = "inline-block"
          tab_width = (width[0] * 2, width[1])
          text = self.context.rptObj.ui.text(rec['text'])
          text.style.css.bold()
          text.style.css.text_align = "center"
          text.style.css.display = "inline-block"
        icon = self.context.rptObj.ui.div([icon_comp, text])
      else:
        icon = self.context.rptObj.ui.div(self.context.rptObj.ui.icon(rec['icon']).css({"display": 'block', "width": '100%', "font-size": css_defaults.font(4)}), width=width)
        icon.attr["data-value"] = rec['icon']
      icon.style.css.text_align = "center"
      icon.options.managed = False
      pills.add_panel(icon, None, width=tab_width, selected=rec.get("selected", False))
    return pills

  def buttons(self, records, htmlCode=None, width=(40, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param records:
    :param htmlCode:
    :param width:
    :param options:
    :param profile:
    """
    pills = self.context.rptObj.ui.panels.pills(htmlCode=htmlCode, options=options, profile=profile)
    r, g, b = Colors.getHexToRgb(self.context.rptObj.theme.success[1])
    pills.options.css_tab_clicked = {'color': self.context.rptObj.theme.colors[-1], 'border': "1px solid %s" % self.context.rptObj.theme.colors[4],
                                     'box-shadow': '0 3px 5px 0 rgba(%s,%s,%s,.08)' % (r, g, b)}
    pills.options.css_tab = {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 10px 5px 0',
                             'box-shadow': '0 3px 5px 0 rgba(0,0,0,.08)', 'border-radius': '25px',
                             "border": "1px solid %s" % self.context.rptObj.theme.greys[0], 'color': self.context.rptObj.theme.greys[-1]}
    pills.style.css.padding_bottom = 5
    pills.style.css.padding_top = 5
    records = records or []
    for rec in records:
      if not isinstance(rec, dict):
        pills.add_panel(rec, None, width=width, selected=rec.get("selected", False))
      elif rec.get('text'):
        pills.add_panel(rec.get('text', ''), None, width=width, selected=rec.get("selected", False))
    return pills

  def texts(self, records, htmlCode=None, width=(40, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param records:
    :param htmlCode:
    :param width:
    :param options:
    :param profile:
    """
    pills = self.context.rptObj.ui.panels.pills(htmlCode=htmlCode, options=options, profile=profile)
    pills.style.css.padding_bottom = 5
    pills.style.css.padding_top = 5
    records = records or []
    for rec in records:
      if not isinstance(rec, dict):
        pills.add_panel(rec, None, width=width, selected=rec.get("selected", False))
      elif rec.get('text'):
        pills.add_panel(rec.get('text', ''), None, width=width, selected=rec.get("selected", False))
    return pills

  def images(self, records, htmlCode=None, radius=True, width=(45, 'px'), inline=True, options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param records:
    :param htmlCode:
    :param radius:
    :param width:
    :param inline:
    :param options:
    :param profile:
    """
    dflt_options = {"image_width": (25, 'px')}
    if radius == True:
      radius = dflt_options["image_width"][0]+10
    elif not radius:
      radius = 0
    if options is not None:
      dflt_options.update(options)
    pills = self.context.rptObj.ui.panels.pills(htmlCode=htmlCode, options=options, profile=profile)
    r, g, b = Colors.getHexToRgb(self.context.rptObj.theme.success[1])
    pills.options.css_tab_clicked = {'color': self.context.rptObj.theme.colors[-1], 'border': "1px solid %s" % self.context.rptObj.theme.colors[4],
                                     'box-shadow': '0 3px 5px 0 rgba(%s,%s,%s,.08)' % (r, g, b)}
    pills.options.css_tab = {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer',
                             'margin': '0 2px 5px 0', 'border-radius': '%spx' % radius, 'padding': '5px',
                             'box-shadow': '0 3px 5px 0 rgba(0,0,0,.08)',
                             "border": "1px solid %s" % self.context.rptObj.theme.greys[0],
                             'color': self.context.rptObj.theme.greys[-1]}
    pills.style.css.padding_bottom = 5
    pills.style.css.padding_top = 5
    records = records or []
    for i, rec in enumerate(records):
      tab_width = width
      if 'text' in rec:
        img = self.context.rptObj.ui.img(rec['image'], path=rec.get('path'), width=dflt_options["image_width"], height=dflt_options["image_width"]).css(
          {"display": 'block', 'margin-left': '5px', 'margin-right': '5px', 'border-radius': '%spx' % radius, "font-size": css_defaults.font(4)})
        text = rec['text']
        if inline:
          img.style.css.display = "inline-block"
          tab_width = (width[0] * 2, width[1])
          text = self.context.rptObj.ui.text(rec['text'], width=(100, "%"))
          text.style.css.bold()
          text.style.css.text_align = "center"
          text.style.css.padding_right = "5px"
          text.style.css.display = "inline-block"
        icon = self.context.rptObj.ui.div([img, text], width=width)
      else:
        icon = self.context.rptObj.ui.div(self.context.rptObj.ui.img(rec['image'], path=rec.get('path'), width=dflt_options["image_width"], height=dflt_options["image_width"]).css(
          {'border-radius': '%spx' % radius, "font-size": css_defaults.font(4)}))
        icon.attr["data-value"] = rec['image']
      icon.style.css.text_align = "center"
      icon.options.managed = False
      pills.add_panel(icon, None, width=tab_width, selected=rec.get("selected", False))
    return pills

