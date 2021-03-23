#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import datetime
import locale

from epyk.core.css.themes import ThemeDark
from epyk_studio.lang import get_lang


class News:

  def __init__(self, ui):
    self.page = ui.page

  def theme(self):
    """
    Description:
    ------------

    """
    self.page.theme = ThemeDark.Grey()

  def miniature(self, title, url, image, category="", time=None, align="left", width=(100, '%'), height=(None, "px"),
                options=None, profile=None):
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
    :param title:
    :param url:
    :param image:
    :param category:
    :param time:
    :param align: String. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    container = self.page.ui.col(
      align=align, width=width, height=height, options=options, position="top", profile=profile)
    container.style.css.margin = "20px auto"
    container.style.css.padding = "5px"
    container.style.css.background = self.page.theme.greys[0]
    if not hasattr(category, 'options'):
      category = self.page.ui.text(category)
      category.style.css.display = "block"
    if not hasattr(title, 'options'):
      title = self.page.ui.link(self.page.py.encode_html(title), url, profile=profile)
      title.style.css.display = "block"
      title.style.css.color = self.page.theme.greys[-1]
      title.style.css.bold()
      title.style.css.text_decoration = None
    if image is not None:
      if not hasattr(image, 'options'):
        split_url = os.path.split(image)
        container.image = self.page.ui.img(split_url[1], path=split_url[0], profile=profile)
        container.image.style.css.margin_bottom = "10px"
        container.add(container.image)
    container.add(self.page.ui.col([category, title], profile=profile))
    return container

  def exchange(self, positive, value, align="left", width=(100, '%'), height=(None, "px"), options=None, profile=None):
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
    :param positive:
    :param value:
    :param align: String. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    component = self.page.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    if positive:
      icon = self.page.ui.icons.awesome("fas fa-caret-up", profile=profile)
      component.style.css.color = self.page.theme.success[1]
    else:
      icon = self.page.ui.icons.awesome("fas fa-caret-down", profile=profile)
      component.style.css.color = self.page.theme.danger[1]
    icon.icon.style.css.font_factor(2)
    component.add(icon)
    number = self.page.ui.texts.number(value, width=("auto", ""), profile=profile)
    component.add(number)
    return component

  def shares(self, positive, value, trend, align="left", width=(100, '%'), height=(None, "px"), options=None,
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
    :param positive:
    :param value:
    :param trend:
    :param align: String. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    component = self.page.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    if positive:
      icon = self.page.ui.icons.awesome("fas fa-caret-up", profile=profile)
      component.style.css.color = self.page.theme.success[1]
    else:
      icon = self.page.ui.icons.awesome("fas fa-caret-down", profile=profile)
      component.style.css.color = self.page.theme.danger[1]
    icon.icon.style.css.font_factor(2)
    component.add(icon)
    chart = self.page.ui.charts.sparkline("line", trend, profile=profile)
    number = self.page.ui.texts.number(value, width=("auto", ""), profile=profile)
    component.add(number)
    component.add(chart)
    return component

  def moves(self, current, previous, align="left", width=(100, '%'), height=(None, "px"), options=None, profile=None):
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
    :param current:
    :param previous:
    :param align: String. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    component = self.page.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    if current-previous >= 0:
      icon = self.page.ui.icons.awesome("fas fa-caret-up", profile=profile)
      component.style.css.color = self.page.theme.success[1]
    else:
      icon = self.page.ui.icons.awesome("fas fa-caret-down", profile=profile)
      component.style.css.color = self.page.theme.danger[1]
    icon.icon.style.css.font_factor(2)
    component.add(icon)
    number = self.page.ui.texts.number(current, width=("auto", ""), profile=profile)
    component.add(number)
    delta = self.page.ui.texts.number(current-previous, width=("auto", ""), profile=profile)
    delta.style.css.margin = "0 10px"
    move = self.page.ui.text(
      "(%s%%)" % round((current-previous)/previous * 100, 2), width=("auto", ""), profile=profile)
    component.add(delta)
    component.add(move)
    return component

  def rates(self, records, width=('auto', '%'), height=(None, "px"), options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Templates:

    Related Pages:

    TODO: add real time event on this component

    Attributes:
    ----------
    :param records: List. A list of dictionaries.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    html_records = []
    options = options or {}
    for rec in records:
      if not hasattr(rec[0], 'options'):
        name = self.page.ui.text(rec[0], profile=profile)
        name.style.css.color = self.page.theme.colors[-1]
        name.style.css.padding = "5px 10px"
      else:
        name = rec[0]
      name.options.managed = False
      current = self.page.ui.text(rec[1], profile=profile)
      current.style.css.color = self.page.theme.greys[5]
      current.style.css.padding = "5px 10px"
      current.options.managed = False
      move = self.page.ui.text("+%s" % rec[2] if rec[3] > 0 else rec[2], profile=profile)
      move.style.css.color = self.page.theme.danger[1] if rec[2] < 0 else self.page.theme.success[1]
      move.style.css.padding = "5px 10px"
      move.options.managed = False
      percent = self.page.ui.text("+%s%%" % rec[3] if rec[3] > 0 else "-%s%%" % rec[3], profile=profile)
      percent.style.css.color = self.page.theme.danger[1] if rec[3] < 0 else self.page.theme.success[1]
      percent.style.css.padding = "5px 10px"
      percent.options.managed = False
      html_records.append([name, current, move, percent])
    table = self.page.ui.tables.basic(
      html_records, rows=[0], cols=[1, 2, 3], width=width, height=height, options=options, profile=profile)
    for row in table:
      row.style.css.border_bottom = "1px solid %s" % self.page.theme.colors[3]
    table.set_header(get_lang(options.get("lang")).RATES_HEADER)
    return table

  def share(self, facebook=True, messenger=True, twitter=True, mail=True, options=None, profile=None):
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
    :param facebook: Boolean. Optional. Flag to mention if the facebook shortcut need to be displayed.
    :param messenger: Boolean. Optional. Flag to mention if the messenger shortcut need to be displayed.
    :param twitter: Boolean. Optional. Flag to mention if the twitter shortcut need to be displayed.
    :param mail: Boolean. Optional. Flag to mention if the mail shortcut need to be displayed.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    component = self.page.ui.div(options=options, profile=profile)
    if facebook:
      component.facebook = self.page.ui.icons.facebook()
      component.facebook.icon.style.css.font_factor(2)
      component.add(component.facebook)
    if messenger:
      component.messenger = self.page.ui.icons.messenger()
      component.messenger.icon.style.css.font_factor(2)
      component.add(component.messenger)
    if twitter:
      component.twitter = self.page.ui.icons.twitter()
      component.twitter.icon.style.css.font_factor(2)
      component.add(component.twitter)
    if mail:
      component.mail = self.page.ui.icons.mail()
      component.mail.icon.style.css.font_factor(2)
      component.add(component.mail)
    return component

  def time(self, date, icon="far fa-clock", align="left", width=("auto", ''), height=(None, "px"), options=None,
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
    :param date:
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param align: String. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {}
    country = get_lang(options.get("lang")).country(options.get("country"))
    locale.setlocale(locale.LC_TIME, '%s_%s' % (country, country.upper()))
    date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    current = datetime.datetime.now()
    delta_time = current - date_time_obj
    component = self.page.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    icon = self.page.ui.icons.awesome(icon)
    icon.icon.style.css.font_factor(2)
    component.add(icon)
    if delta_time.days == 0:
      if date_time_obj.day != current.day:
        text = self.page.ui.text(get_lang(options.get("lang")).LABEL_YESTERDAY, profile=profile)
        component.add(text)
        elapsed_time = self.page.py.dates.elapsed(delta_time, with_time=True)
        tooltip_value = []
        for lbl in ['hours', 'minutes', 'seconds']:
          if elapsed_time.get(lbl, 0) > 0:
            tooltip_value.append("%s %s" % (elapsed_time[lbl], get_lang(options.get("lang")).LABEL_TIME[lbl]))
        text.tooltip(" ".join(tooltip_value))
      else:
        elapsed_time = self.page.py.dates.elapsed(delta_time, with_time=True)
        tooltip_value = []
        for lbl in ['hours', 'minutes', 'seconds']:
          if elapsed_time.get(lbl, 0) > 0:
            tooltip_value.append("%s %s" % (elapsed_time[lbl], get_lang(options.get("lang")).LABEL_TIME_SHORT[lbl]))
        component.add(self.page.ui.text(" ".join(tooltip_value), profile=profile))
    else:
      text = self.page.ui.text(self.page.py.encode_html(date_time_obj.strftime("%d %B %Y")), profile=profile)
      elapsed_time = self.page.py.dates.elapsed(delta_time)
      tooltip_value = []
      for lbl in ['years', 'months', 'days']:
        if elapsed_time.get(lbl, 0) > 0:
          tooltip_value.append("%s %s" % (elapsed_time[lbl], get_lang(options.get("lang")).LABEL_TIME[lbl]))
      text.tooltip(" ".join(tooltip_value))
      component.add(text)
    return component

  def tags(self, tags, align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
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
    :param tags:
    :param align: String. Optional. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    container = self.page.ui.div([], align=align, width=width, height=height, options=options, profile=profile)
    for tag in tags:
      if not hasattr(tag, 'options'):
        comp_tag = self.page.ui.text(tag, profile=profile)
      else:
        comp_tag = tag
      comp_tag.style.css.border = "1px solid %s" % self.page.theme.greys[-1]
      comp_tag.style.css.margin = "0 3px"
      comp_tag.style.css.padding = "1px 5px"
      container.add(comp_tag)
    return container

  def border(self, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Attributes:
    ----------
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.page.ui.div("&nbsp;", options=options, profile=profile).css({
      "border-left": '1px solid %s' % self.page.theme.greys[5],
      "margin": '5px 0', "display": 'inline-block', 'width': 'auto'})

  def delimiter(self, options=None, profile=None):
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
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    hr = self.page.ui.layouts.hr()
    hr.style.css.padding = "10px 20%"
    return hr

  def section(self, text, align="left", width=(100, '%'), height=("auto", ''), options=None, profile=None):
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
    :param text: String. Optional. The value to be displayed to the component.
    :param align: String. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    hr = self.page.ui.layouts.hr()
    hr.style.css.padding = 0
    hr.style.css.margin_top = "-50px"
    hr.style.css.padding_left = "140px"
    hr.style.css.padding_right = "60px"
    hr.style.css.display = "inline-block"
    text = self.page.ui.text(text, width=("auto", ""), profile=profile)
    text.style.css.display = "inline-block"
    text.style.css.bold()
    text.style.css.font_factor(15)
    return self.page.ui.div([text, hr], align=align, width=width, height=height, options=options, profile=profile)

  def comments(self, count, url, icon="far fa-comment-alt", align="left", width=("auto", ''), height=(None, "px"),
               options=None, profile=None):
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
    :param count:
    :param url:
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param align: String. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    component = self.page.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    icon = self.page.ui.icons.awesome(icon, profile=profile)
    icon.icon.style.css.font_factor(0)
    component.add(icon)
    link = self.page.ui.link(count, url, profile=profile)
    link.style.css.color = self.page.theme.greys[6]
    component.add(link)
    return component

  def button(self, text="", icon=None, width=(None, "%"), height=(None, "px"), align="left", html_code=None,
             tooltip=None, profile=None, options=None):
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
    :param text: String. Optional. The value to be displayed to the component.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. The text-align property within this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    button = self.page.ui.button(
      text, icon, width=width, height=height, options=options, html_code=html_code, tooltip=tooltip, profile=profile,
      align=align)
    button.style.clear()
    button.style.css.padding = "0 10px"
    button.style.css.background = self.page.theme.greys[0]
    button.style.hover({"color": self.page.theme.success[1]})
    return button

  def stepper(self, records, color=None, width=(200, 'px'), height=(350, 'px'), options=None, profile=None):
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
    :param records: List. A list of dictionaries.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    size = (height[0] - 20) / (len(records) - 1)
    frgs, dflt_size = [], 0
    for rec in records[:-1]:
      if 'size' in rec:
        frgs.append(rec['size'])
      else:
        frgs.append(size)
        dflt_size += 1
    extra_size = (height[0] - 20 - sum(frgs)) / dflt_size if dflt_size > 0 else 0
    frgs = [frg + extra_size if frg == size else frg for frg in frgs]
    svg = self.page.ui.charts.svg.new(width=width, height=height)
    svg.line(10, 10, 10, sum(frgs) + 10, stroke=color or self.page.theme.danger[1])
    for i, rec in enumerate(records):
      svg.circle(10, 10 + sum(frgs[0:i]), 5, fill=rec.get("fill", self.page.theme.greys[0]),
                 stroke=color or self.page.theme.danger[1])
      svg.text(rec["time"], 20, 15 + sum(frgs[0:i])).css({"font-weight": 'bold'})
      svg.text(rec["text"], 65, 15 + sum(frgs[0:i]))
    return svg

  def search(self, text='', placeholder=None, color=None, height=(None, "px"), html_code=None, tooltip='',
             extensible=True, options=None, profile=None):
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
    :param text: String. Optional. The value to be displayed to the component.
    :param placeholder: String. Optional. The value when the input field is empty.
    :param color: String. Optional. The color code.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param extensible: Boolean. Optional.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {}
    placeholder = placeholder or get_lang(options.get('lang')).PLACEHOLDER_SEARCH
    s = self.page.ui.inputs.search(
      text=text, placeholder=placeholder, color=color, height=height, html_code=html_code, tooltip=tooltip,
      extensible=extensible, options=options, profile=profile)
    return s

  def audio(self, text, url, icon="fas fa-volume-up", options=None, profile=None):
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
    :param text: String. Optional. The value to be displayed to the component.
    :param url: String. Optional. The url link.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    icon = self.page.ui.icons.awesome(icon)
    icon.icon.style.css.font_factor(0)
    icon.icon.style.css.color = self.page.theme.greys[-1]
    icon.options.managed = False
    link = self.page.ui.link("%s %s" % (icon.html(), text), url, options=options, profile=profile)
    link.style.css.background = self.page.theme.greys[0]
    link.style.css.color = self.page.theme.greys[-1]
    link.style.css.padding = "2px 5px"
    return link

  def increase(self, fill=None, border=None, width=(30, "px"), height=(30, "px"), options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Templates:

    Related Pages:

      https://uxwing.com/check-list-icon/

    Attributes:
    ----------
    :param fill:
    :param border:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    svg = self.page.ui.pictos.path(
      fill=fill, stroke=border, width=width, height=height, options=options, profile=profile,
      path="M2.03,56.52c-2.66,2.58-2.72,6.83-0.13,9.49c2.58,2.66,6.83,2.72,9.49,0.13l27.65-26.98l23.12,22.31 c2.67,2.57,6.92,2.49,9.49-0.18l37.77-38.22v19.27c0,3.72,3.01,6.73,6.73,6.73s6.73-3.01,6.73-6.73V6.71h-0.02 c0-1.74-0.67-3.47-2-4.78c-1.41-1.39-3.29-2.03-5.13-1.91H82.4c-3.72,0-6.73,3.01-6.73,6.73c0,3.72,3.01,6.73,6.73,6.73h17.63 L66.7,47.2L43.67,24.97c-2.6-2.5-6.73-2.51-9.33,0.03L2.03,56.52L2.03,56.52z"
    )
    return svg

  def decrease(self, fill=None, border=None, width=(30, "px"), height=(30, "px"), options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Templates:

    Related Pages:

      https://uxwing.com/check-list-icon/

    Attributes:
    ----------
    :param fill:
    :param border:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    svg = self.page.ui.pictos.path(
      fill=fill, stroke=border, width=width, height=height, options=options, profile=profile,
      path="M2.03,11.52C-0.63,8.94-0.68,4.69,1.9,2.03c2.58-2.66,6.83-2.72,9.49-0.13l27.65,26.98L62.16,6.57 c2.67-2.57,6.92-2.49,9.49,0.18l37.77,38.22V25.7c0-3.72,3.01-6.73,6.73-6.73s6.73,3.01,6.73,6.73v35.63h-0.02 c0,1.74-0.67,3.47-2,4.78c-1.41,1.39-3.29,2.03-5.13,1.91H82.4c-3.72,0-6.73-3.01-6.73-6.73c0-3.72,3.01-6.73,6.73-6.73h17.63 L66.7,20.84L43.67,43.07c-2.6,2.5-6.73,2.51-9.33-0.03L2.03,11.52L2.03,11.52z"
    )
    return svg
