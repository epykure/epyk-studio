#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import datetime
import locale

from epyk.core.css.themes import ThemeDark
from epyk_studio.lang import get_lang


class News(object):
  def __init__(self, context):
    self.context = context

  def theme(self):
    """
    Description:
    ------------

    """
    self.context.rptObj.theme = ThemeDark.Grey()

  def miniature(self, title, url, image, category="", time=None, align="left", width=(100, '%'), height=(None, "px"), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param title:
    :param url:
    :param image:
    :param category:
    :param align:
    :param width:
    :param height:
    :param options:
    """
    container = self.context.rptObj.ui.col(align=align, width=width, height=height, position="top")
    container.style.css.margin = "20px auto"
    container.style.css.padding = "5px"
    container.style.css.background = self.context.rptObj.theme.greys[0]
    if not hasattr(category, 'options'):
      category = self.context.rptObj.ui.text(category)
      category.style.css.display = "block"
    if not hasattr(title, 'options'):
      title = self.context.rptObj.ui.link(self.context.rptObj.py.encode_html(title), url)
      title.style.css.display = "block"
      title.style.css.color = self.context.rptObj.theme.greys[-1]
      title.style.css.bold()
      title.style.css.text_decoration = None
    if image is not None:
      if not hasattr(image, 'options'):
        split_url = os.path.split(image)
        container.image = self.context.rptObj.ui.img(split_url[1], path=split_url[0])
        container.image.style.css.margin_bottom = "10px"
        container.add(container.image)
    container.add(self.context.rptObj.ui.col([category, title]))
    return container

  def exchange(self, positive, value, align="left", width=(100, '%'), height=(None, "px"), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param positive:
    :param value:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    component = self.context.rptObj.ui.div()
    if positive:
      icon = self.context.rptObj.ui.icons.awesome("fas fa-caret-up")
      component.style.css.color = self.context.rptObj.theme.success[1]
    else:
      icon = self.context.rptObj.ui.icons.awesome("fas fa-caret-down")
      component.style.css.color = self.context.rptObj.theme.danger[1]
    icon.icon.style.css.font_factor(2)
    component.add(icon)
    number = self.context.rptObj.ui.texts.number(value, width=("auto", ""))
    component.add(number)
    return component

  def shares(self, positive, value, trend, align="left", width=(100, '%'), height=(None, "px"), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param positive:
    :param value:
    :param trend:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    component = self.context.rptObj.ui.div()
    if positive:
      icon = self.context.rptObj.ui.icons.awesome("fas fa-caret-up")
      component.style.css.color = self.context.rptObj.theme.success[1]
    else:
      icon = self.context.rptObj.ui.icons.awesome("fas fa-caret-down")
      component.style.css.color = self.context.rptObj.theme.danger[1]
    icon.icon.style.css.font_factor(2)
    component.add(icon)
    chart = self.context.rptObj.ui.charts.sparkline("line", trend)
    number = self.context.rptObj.ui.texts.number(value, width=("auto", ""))
    component.add(number)
    component.add(chart)
    return component

  def moves(self, current, previous, align="left", width=(100, '%'), height=(None, "px"), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param current:
    :param previous:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    component = self.context.rptObj.ui.div()
    if current-previous >= 0:
      icon = self.context.rptObj.ui.icons.awesome("fas fa-caret-up")
      component.style.css.color = self.context.rptObj.theme.success[1]
    else:
      icon = self.context.rptObj.ui.icons.awesome("fas fa-caret-down")
      component.style.css.color = self.context.rptObj.theme.danger[1]
    icon.icon.style.css.font_factor(2)
    component.add(icon)
    number = self.context.rptObj.ui.texts.number(current, width=("auto", ""))
    component.add(number)
    delta = self.context.rptObj.ui.texts.number(current-previous, width=("auto", ""))
    delta.style.css.margin = "0 10px"
    move = self.context.rptObj.ui.text("(%s%%)" % round((current-previous)/previous *100, 2), width=("auto", ""))
    component.add(delta)
    component.add(move)
    return component

  def rates(self, records, width=('auto', '%'), height=(None, "px"), options=None, profile=None):
    """
    Description:
    ------------

    TODO: add real time event on this component

    Attributes:
    ----------
    :param records:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    html_records = []
    options = options or {}
    for rec in records:
      if not hasattr(rec[0], 'options'):
        name = self.context.rptObj.ui.text(rec[0])
        name.style.css.color = self.context.rptObj.theme.colors[-1]
        name.style.css.padding = "5px 10px"
      else:
        name = rec[0]
      name.options.managed = False
      current = self.context.rptObj.ui.text(rec[1])
      current.style.css.color = self.context.rptObj.theme.greys[5]
      current.style.css.padding = "5px 10px"
      current.options.managed = False
      move = self.context.rptObj.ui.text("+%s" % rec[2] if rec[3] > 0 else rec[2])
      move.style.css.color = self.context.rptObj.theme.danger[1] if rec[2] < 0 else self.context.rptObj.theme.success[1]
      move.style.css.padding = "5px 10px"
      move.options.managed = False
      percent = self.context.rptObj.ui.text("+%s%%" % rec[3] if rec[3] > 0 else "-%s%%" % rec[3])
      percent.style.css.color = self.context.rptObj.theme.danger[1] if rec[3] < 0 else self.context.rptObj.theme.success[1]
      percent.style.css.padding = "5px 10px"
      percent.options.managed = False
      html_records.append([name, current, move, percent])
    table = self.context.rptObj.ui.tables.basic(html_records, rows=[0], cols=[1, 2, 3], width=width, height=height,
               options=options, profile=profile)
    for row in table:
      row.style.css.border_bottom = "1px solid %s" % self.context.rptObj.theme.colors[3]
    table.set_header(get_lang(options.get("lang")).RATES_HEADER)
    return table

  def share(self, facebook=True, messenger=True, twitter=True, mail=True):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param facebook: Boolean. Flag to mention if the facebook shortcut need to be displayed
    :param messenger: Boolean. Flag to mention if the messenger shortcut need to be displayed
    :param twitter: Boolean. Flag to mention if the twitter shortcut need to be displayed
    :param mail: Boolean. Flag to mention if the mail shortcut need to be displayed
    """
    component = self.context.rptObj.ui.div()
    if facebook:
      component.facebook = self.context.rptObj.ui.icons.facebook()
      component.facebook.icon.style.css.font_factor(2)
      component.add(component.facebook)
    if messenger:
      component.messenger = self.context.rptObj.ui.icons.messenger()
      component.messenger.icon.style.css.font_factor(2)
      component.add(component.messenger)
    if twitter:
      component.twitter = self.context.rptObj.ui.icons.twitter()
      component.twitter.icon.style.css.font_factor(2)
      component.add(component.twitter)
    if mail:
      component.mail = self.context.rptObj.ui.icons.mail()
      component.mail.icon.style.css.font_factor(2)
      component.add(component.mail)
    return component

  def time(self, date, icon="far fa-clock", align="left", width=("auto", ''), height=(None, "px"), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param date:
    :param icon:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    options = options or {}
    country = get_lang(options.get("lang")).country(options.get("country"))
    locale.setlocale(locale.LC_TIME, '%s_%s' % (country, country.upper()))
    date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    current = datetime.datetime.now()
    delta_time = current - date_time_obj
    component = self.context.rptObj.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    icon = self.context.rptObj.ui.icons.awesome(icon)
    icon.icon.style.css.font_factor(2)
    component.add(icon)
    if delta_time.days == 0:
      if date_time_obj.day != current.day:
        text = self.context.rptObj.ui.text(get_lang(options.get("lang")).LABEL_YESTERDAY)
        component.add(text)
        elapsed_time = self.context.rptObj.py.dates.elapsed(delta_time, with_time=True)
        tooltip_value = []
        for lbl in ['hours', 'minutes', 'seconds']:
          if elapsed_time.get(lbl, 0) > 0:
            tooltip_value.append("%s %s" % (elapsed_time[lbl], get_lang(options.get("lang")).LABEL_TIME[lbl]))
        text.tooltip(" ".join(tooltip_value))
      else:
        elapsed_time = self.context.rptObj.py.dates.elapsed(delta_time, with_time=True)
        tooltip_value = []
        for lbl in ['hours', 'minutes', 'seconds']:
          if elapsed_time.get(lbl, 0) > 0:
            tooltip_value.append("%s %s" % (elapsed_time[lbl], get_lang(options.get("lang")).LABEL_TIME_SHORT[lbl]))
        component.add(self.context.rptObj.ui.text(" ".join(tooltip_value)))
    else:
      text = self.context.rptObj.ui.text(self.context.rptObj.py.encode_html(date_time_obj.strftime("%d %B %Y")))
      elapsed_time = self.context.rptObj.py.dates.elapsed(delta_time)
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

    Attributes:
    ----------
    :param tags:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    container = self.context.rptObj.ui.div([], align=align, width=width, height=height, options=options, profile=profile)
    for tag in tags:
      if not hasattr(tag, 'options'):
        comp_tag = self.context.rptObj.ui.text(tag)
      else:
        comp_tag = tag
      comp_tag.style.css.border = "1px solid %s" % self.context.rptObj.theme.greys[-1]
      comp_tag.style.css.margin = "0 3px"
      comp_tag.style.css.padding = "1px 5px"
      container.add(comp_tag)
    return container

  def border(self):
    """
    Description:
    ------------

    Attributes:
    ----------

    """
    return self.context.rptObj.ui.div("&nbsp;").css({"border-left": '1px solid %s' % self.context.rptObj.theme.greys[5],
                                                     "margin": '5px 0', "display": 'inline-block', 'width': 'auto'})

  def delimiter(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    """
    hr = self.context.rptObj.ui.layouts.hr()
    hr.style.css.padding = "10px 20%"
    return hr

  def section(self, text, align="left", width=(100, '%'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    hr = self.context.rptObj.ui.layouts.hr()
    hr.style.css.padding = 0
    hr.style.css.margin_top = "-50px"
    hr.style.css.padding_left = "140px"
    hr.style.css.padding_right = "60px"
    hr.style.css.display = "inline-block"
    text = self.context.rptObj.ui.text(text, width=("auto", ""))
    text.style.css.display = "inline-block"
    text.style.css.bold()
    text.style.css.font_factor(15)
    return self.context.rptObj.ui.div([text, hr], align=align, width=width, height=height, options=options, profile=profile)

  def comments(self, count, url, icon="far fa-comment-alt", align="left", width=("auto", ''), height=(None, "px"), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param count:
    :param url:
    :param icon:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    component = self.context.rptObj.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    icon = self.context.rptObj.ui.icons.awesome(icon)
    icon.icon.style.css.font_factor(0)
    component.add(icon)
    link = self.context.rptObj.ui.link(count, url)
    link.style.css.color = self.context.rptObj.theme.greys[6]
    component.add(link)
    return component

  def live(self, icon="fas fa-circle"):
    """
    Description:
    ------------

    Attributes:
    ----------

    """
    live = self.context.rptObj.ui.icons.awesome(icon)
    live.style.css.color = self.context.rptObj.theme.danger[1]
    live.style.css.border = "1px solid %s" % self.context.rptObj.theme.danger[1]
    live.style.css.border_radius = "50px"
    live.style.css.padding = "2px"
    live.style.css.margin = 0
    live.icon.style.css.font_factor(2)
    live.icon.style.css.margin_right = 0
    live.icon.style.css.margin = 0
    live.icon.style.css.padding_bottom = "2px"
    live.icon.style.effects.blink(2)
    return live

  def button(self, text="", icon=None, width=(None, "%"), height=(None, "px"), align="left", htmlCode=None,
             tooltip=None, profile=None, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param icon:
    :param width:
    :param height:
    :param align:
    :param htmlCode:
    :param tooltip:
    :param profile:
    :param options:
    """
    button = self.context.rptObj.ui.button(text, icon, width=width, height=height, options=options, tooltip=tooltip, profile=profile, align=align)
    button.style.clear()
    button.style.css.padding = "0 10px"
    button.style.css.background = self.context.rptObj.theme.greys[0]
    button.style.hover({"color": self.context.rptObj.theme.success[1]})
    return button

  def stepper(self, records, color=None, width=(200, 'px'), height=(350, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param records:
    :param color:
    :param width:
    :param height:
    :param options:
    :param profile:
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
    svg = self.context.rptObj.ui.charts.svg.new(width=width, height=height)
    svg.line(10, 10, 10, sum(frgs) + 10, stroke=color or self.context.rptObj.theme.danger[1])
    for i, rec in enumerate(records):
      svg.circle(10, 10 + sum(frgs[0:i]), 5, fill=rec.get("fill", self.context.rptObj.theme.greys[0]),
                 stroke=color or self.context.rptObj.theme.danger[1])
      svg.text(rec["time"], 20, 15 + sum(frgs[0:i])).css({"font-weight": 'bold'})
      svg.text(rec["text"], 55, 15 + sum(frgs[0:i]))
    return svg

  def search(self, text='', placeholder='Search..', color=None, height=(None, "px"), htmlCode=None,
             tooltip='', extensible=True, options=None, profile=None):
    s = self.context.rptObj.ui.inputs.search(text=text, placeholder=placeholder, color=color, height=height,
         htmlCode=htmlCode, tooltip=tooltip, extensible=extensible, options=options, profile=profile)
    return s

  def audio(self, text, url, icon="fas fa-volume-up"):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param url:
    :param icon:
    """
    icon = self.context.rptObj.ui.icons.awesome(icon)
    icon.icon.style.css.font_factor(0)
    icon.icon.style.css.color = self.context.rptObj.theme.greys[-1]
    icon.options.managed = False
    link = self.context.rptObj.ui.link("%s %s" % (icon.html(), text), url)
    link.style.css.background = self.context.rptObj.theme.greys[0]
    link.style.css.color = self.context.rptObj.theme.greys[-1]
    link.style.css.padding = "2px 5px"
    return link

  def increase(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """

    https://uxwing.com/check-list-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M2.03,56.52c-2.66,2.58-2.72,6.83-0.13,9.49c2.58,2.66,6.83,2.72,9.49,0.13l27.65-26.98l23.12,22.31 c2.67,2.57,6.92,2.49,9.49-0.18l37.77-38.22v19.27c0,3.72,3.01,6.73,6.73,6.73s6.73-3.01,6.73-6.73V6.71h-0.02 c0-1.74-0.67-3.47-2-4.78c-1.41-1.39-3.29-2.03-5.13-1.91H82.4c-3.72,0-6.73,3.01-6.73,6.73c0,3.72,3.01,6.73,6.73,6.73h17.63 L66.7,47.2L43.67,24.97c-2.6-2.5-6.73-2.51-9.33,0.03L2.03,56.52L2.03,56.52z"
    )
    return svg

  def decrease(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """

    https://uxwing.com/check-list-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M2.03,11.52C-0.63,8.94-0.68,4.69,1.9,2.03c2.58-2.66,6.83-2.72,9.49-0.13l27.65,26.98L62.16,6.57 c2.67-2.57,6.92-2.49,9.49,0.18l37.77,38.22V25.7c0-3.72,3.01-6.73,6.73-6.73s6.73,3.01,6.73,6.73v35.63h-0.02 c0,1.74-0.67,3.47-2,4.78c-1.41,1.39-3.29,2.03-5.13,1.91H82.4c-3.72,0-6.73-3.01-6.73-6.73c0-3.72,3.01-6.73,6.73-6.73h17.63 L66.7,20.84L43.67,43.07c-2.6,2.5-6.73,2.51-9.33-0.03L2.03,11.52L2.03,11.52z"
    )
    return svg
