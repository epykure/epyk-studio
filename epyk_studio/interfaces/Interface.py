#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from epyk_studio.interfaces.studio import CompStudioBlog
from epyk_studio.interfaces.studio import CompStudioShopping
from epyk_studio.interfaces.studio import CompStudioNews
from epyk_studio.interfaces.studio import CompStudioDashboard
from epyk_studio.interfaces.studio import CompStudioVitrine
from epyk_studio.interfaces.studio import CompStudioEvent
from epyk_studio.interfaces.studio import CompStudioQuiz

from epyk.interfaces import Interface
from epyk.core.css import Defaults as Defaults_css
from epyk.core.html import Defaults as Defaults_html
from epyk.core.css import themes
from epyk_studio.lang import get_lang, REGISTERED_LANGS
from epyk.core.js.primitives import JsObjects


class Studio(Interface.Components):

  def __init__(self, rptObj):
    super(Studio, self).__init__(rptObj)

  def locked(self, component, day, month, year, hour=0, minute=0, second=0, options=None):
    """
    Description:
    ------------

    This item is only working if the page is generated on demand

    Attributes:
    ----------
    :param component:
    :param day:
    :param month:
    :param year:
    :param hour:
    :param minute:
    :param second:
    :param options:
    """
    options = options or {}
    event_time = datetime.datetime(year, month, day, hour, minute, second)
    now = datetime.datetime.now()
    if now > event_time:
      return component

    # Delete the items on the backend side
    del self.rptObj.components[component.htmlCode]
    component = self.rptObj.ui.div()
    component.style.css.line_height = Defaults_css.font(25)
    component.style.css.border = "1px solid %s" % self.rptObj.theme.greys[3]
    component.style.css.border_radius = 10
    component.style.css.margin = "5px 0"
    component.style.css.padding = 5
    icon = self.rptObj.ui.icons.awesome("fas fa-lock")
    icon.icon.style.css.font_factor(10)
    icon.icon.style.css.vertical_align = None
    icon.icon.style.css.color = self.rptObj.theme.greys[5]
    icon.icon.style.css.line_height = Defaults_css.font(25)
    component.add(icon)
    component.text = self.rptObj.ui.text("Event Locked")
    component.text.style.css.font_factor(8)
    component.text.style.css.vertical_algin = 'bottom'
    component.text.style.css.color = self.rptObj.theme.greys[5]
    component.add(component.text)
    component.countdown = self.rptObj.ui.rich.countdown(day, month, year, hour, minute, second, width=(None, ''))
    component.countdown._jsStyles['reload'] = False
    component.countdown.style.css.display = 'inline-block'
    component.countdown.style.css.float = 'right'
    component.countdown.style.css.margin_right = 5
    component.add(component.countdown)
    if not options.get("countdown", True):
      component.countdown.style.css.display = False
    return component

  def secured(self, component, authorized=False, options=None):
    """
    Description:
    ------------

    This item is only working if the page is generated on demand

    Attributes:
    ----------
    :param component:
    :param authorized:
    :param options:
    """
    options = options or {}
    if authorized:
      return component

    # Delete the items on the backend side
    del self.rptObj.components[component.htmlCode]
    component = self.rptObj.ui.div()
    component.style.css.line_height = Defaults_css.font(25)
    component.style.css.border = "1px solid %s" % self.rptObj.theme.greys[3]
    component.style.css.border_radius = 10
    component.style.css.margin = "5px 0"
    component.style.css.padding = 5
    icon = self.rptObj.ui.icons.awesome("fas fa-key")
    icon.icon.style.css.font_factor(10)
    icon.icon.style.css.vertical_align = None
    icon.icon.style.css.color = self.rptObj.theme.greys[5]
    icon.icon.style.css.line_height = Defaults_css.font(25)
    component.add(icon)
    component.text = self.rptObj.ui.text("Not available")
    component.text.style.css.font_factor(8)
    component.text.style.css.vertical_algin = 'bottom'
    component.text.style.css.color = self.rptObj.theme.greys[5]
    component.add(component.text)
    return component

  def nav(self, logo=None, title=None, width=(100, '%'), height=(40, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param logo:
    :param title:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    bar = self.rptObj.ui.navigation.bar(logo=logo, title=title, width=width, height=height, options=options, profile=profile)
    return bar

  def row(self, components=None, position='middle', width=(100, '%'), height=(None, 'px'), align=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param components:
    :param position:
    :param width:
    :param height:
    :param align:
    :param helper:
    :param options:
    :param profile:
    """
    row = self.rptObj.ui.layouts.row(components, position=position, width=width, height=height, align=align, helper=helper,
                                     options=options, profile=profile)
    return row

  def col(self, components=None, position='middle', width=(100, '%'), height=(None, 'px'), align=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param components:
    :param position:
    :param width:
    :param height:
    :param align:
    :param helper:
    :param options:
    :param profile:
    """
    col = self.rptObj.ui.layouts.col(components, position=position, width=width, height=height, align=align, helper=helper,
                                     options=options, profile=profile)
    return col

  def grid(self, rows=None, width=(100, '%'), height=(None, 'px'), align=None, position=None, options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param rows:
    :param width:
    :param height:
    :param align:
    :param position:
    :param options:
    :param profile:
    """
    grid = self.rptObj.ui.layouts.grid(rows, position=position, width=width, height=height, align=align, options=options, profile=profile)
    return grid

  def table(self, components=None, width=(100, '%'), height=(None, 'px'), helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param components:
    :param width:
    :param height:
    :param helper:
    :param options:
    :param profile:
    """
    table = self.rptObj.ui.layouts.table(components=components, width=width, height=height, helper=helper, options=options, profile=profile)
    return table

  def sliding(self, htmlObjs, title, color=None, align="center", width=(100, "%"), height=(None, "px"), htmlCode=None, helper=None, options=None, profile=False):
    """

    :param htmlObjs:
    :param title:
    :param color:
    :param align:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param options:
    :param profile:
    """
    panel = self.rptObj.ui.panels.sliding(htmlObjs, title, color=color, align=align, width=width, height=height,
                                          htmlCode=htmlCode, helper=helper, options=options, profile=profile)
    return panel

  def tabs(self, color=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None, options=None,
           profile=False):
    """

    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param options:
    :param profile:
    """
    panel = self.rptObj.ui.panels.tabs(color=color, width=width, height=height, htmlCode=htmlCode, helper=helper, options=options, profile=profile)
    return panel

  def container(self, component=None, max_width=(900, 'px'), align="center", profile=None, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param component:
    :param max_width:
    :param align:
    :param profile:
    :param options:
    """
    container = self.rptObj.ui.div(component, profile=profile, options=options)
    container.style.css.max_width = max_width[0]
    container.style.css.text_align = align
    if align == 'center':
      container.style.css.margin = "0 auto"
    return container

  def banner(self, data, background=True, width=(100, '%'), align="center", height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data:
    :param background:
    :param width:
    :param align:
    :param height:
    :param options:
    :param profile:
    """
    if background is True:
      background = self.rptObj.theme.colors[1]
    banner = self.rptObj.ui.banners.text(data=data, background=background, width=width, align=align, height=height, options=options, profile=profile)
    return banner

  def vignet(self, title, content, icon=None, render="col", align="center", width=(200, 'px'), options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param title:
    :param content:
    :param icon:
    :param render:
    :param align:
    :param width:
    :param options:
    """
    vignet = self.rptObj.ui.vignets.vignet(title=title, content=content, icon=icon, render=render, align=align, width=width, options=options)
    return vignet

  def background(self, url, width=(100, "%"), height=(300, "px"), size="cover", margin=0, align="center", position="middle"):
    """
    Description:
    ------------
    Set a background as an image.
    This is wrapping the image.background base component

    Attributes:
    ----------
    :param url:
    :param width:
    :param height:
    :param size:
    :param margin:
    :param align:
    :param position:
    """
    background = self.rptObj.ui.images.background(url, width=width, height=height, size=size, margin=margin, align=align, position=position)
    return background

  def button(self, text, icon=None, border=False, background=True, width=('auto', ''), align="center", height=(None, 'px'),
             options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param icon:
    :param border:
    :param background:
    :param width:
    :param align:
    :param height:
    :param options:
    :param profile:
    """
    button = self.rptObj.ui.button(text, icon=icon, width=width, align=align, height=height,
                                                  options=options, profile=profile)
    button.style.clear()
    button.style.add_classes.div.no_focus_outline()
    button.style.css.padding = "0 10px"
    button.style.css.display = "inline-block"
    button.style.css.color = self.rptObj.theme.greys[-1]
    button.style.css.background = self.rptObj.theme.greys[0]
    button.style.css.border_radius = 4
    if border:
      button.style.css.border = '1px solid %s' % self.rptObj.theme.greys[4]
    if background:
      button.style.hover({"background": self.rptObj.theme.colors[6], "color": self.rptObj.theme.greys[0]})
    else:
      button.style.hover({"color": self.rptObj.theme.greys[0]})
    return button

  def carousel(self, components=None, selected=0, width=('100', '%'), height=(None, 'px'), left="fas fa-angle-left", right="fas fa-angle-right", options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param components:
    :param selected:
    :param width:
    :param height:
    :param left:
    :param right:
    :param options:
    :param profile:
    """
    dfl_options = {"arrows-right": right, "arrows-left": left, 'points': False, 'arrows': True, 'inifity': True}
    if options is not None:
      dfl_options.update(options)
    c = self.rptObj.ui.images.carousel(components, None, selected, width, height, dfl_options, profile)
    if dfl_options['arrows']:
      c.next.style.css.margin_top = -Defaults_html.LINE_HEIGHT
      c.previous.style.css.margin_top = -Defaults_html.LINE_HEIGHT
      c.container.style.css.margin = "auto 45px"
      c.container.style.css.width = "calc(100% - 90px)"
    if 'timer' in dfl_options:
      self.rptObj.body.onReady([c.next.dom.events.trigger("click", withFocus=False, options={"timer": dfl_options['timer']})])
      c.clear_timer = JsObjects.JsVoid("clearInterval(window['%s_timer'])" % c.next.htmlCode)
    return c

  def clients(self, logos, title=None, content='', width=(100, '%'), height=("auto", ''), align="center", options=None,
               profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param logos:
    :param title:
    :param content:
    :param width:
    :param height:
    :param align:
    :param options:
    :param profile:
    """
    options = options or {}
    title = title or get_lang(options.get('lang')).CLIENTS_LABEL
    banner = self.rptObj.ui.banners.sponsor(logos, title, content, width=width, height=height, align=align,
                                                           options=options, profile=profile)
    banner.title.style.css.color = self.rptObj.theme.colors[0]
    banner.style.css.background = self.rptObj.theme.colors[6]
    return banner

  def sponsors(self, logos, title=None, content='', width=(100, '%'), height=("auto", ''), align="center", options=None,
               profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param logos:
    :param title:
    :param content:
    :param width:
    :param height:
    :param align:
    :param options:
    :param profile:
    """
    options = options or {}
    title = title or get_lang(options.get('lang')).SPONSORS
    banner = self.rptObj.ui.banners.sponsor(logos, title, content, width=width, height=height, align=align,
                                                           options=options, profile=profile)
    banner.style.css.background = self.rptObj.theme.colors[2]
    return banner

  def langs(self, selected=None, width=(45, 'px'), height=(None, "%"), options=None, profile=None):
    """
    Description:
    ------------
    Display a dropdown list with all the various langs

    Attributes:
    ----------
    :param selected: String. The selected value
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile:
    """
    dftl_options = {'empty_selected': False, 'button-bg': False}
    if options is not None:
      dftl_options.update(options)
    dftl_options["width"] = width[0]
    select = self.rptObj.ui.select(REGISTERED_LANGS, width=width, selected=selected or REGISTERED_LANGS[0]['value'], options=dftl_options, htmlCode="lang", height=height, profile=profile)
    return select

  def themes(self, selected=None, width=(45, 'px'), height=(None, "%"), options=None, profile=None):
    """
    Description:
    ------------
    Display a dropdown list with all the various themes

    Attributes:
    ----------
    :param selected: String. The selected value
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile:
    """
    values = themes.REGISTERED_THEMES
    dftl_options = {'empty_selected': False, 'button-bg': False}
    if options is not None:
      dftl_options.update(options)
    dftl_options["width"] = width[0]
    select = self.rptObj.ui.select(values, width=width, selected=selected or values[0]['value'], options=dftl_options, height=height, htmlCode="theme", profile=profile)
    mod_name, class_name = select.options.selected.split(".")
    theme = getattr(getattr(themes, mod_name), class_name)
    self.rptObj.theme = theme()
    return select

  def footers(self, components=None, logo=None, width=(100, '%'), height=('auto', ''), options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param components:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    if logo is None:
      logo = self.rptObj.ui.icons.epyk()
    logo.style.css.width = "80px"
    logo.style.css.height = "80px"
    if components is None:
      components = self.rptObj.ui.row([
        self.rptObj.ui.col([
          logo, self.rptObj.ui.banners.follow("Follow us")
        ], position="top"),
        self.rptObj.ui.col([
          self.rptObj.ui.text("À Propos").css({"font-weight": 'bold'})
        ], position="top"),
        self.rptObj.ui.col([
          self.rptObj.ui.text("Resources").css({"font-weight": 'bold'})
        ], position="top"),
        self.rptObj.ui.col([
          self.rptObj.ui.text("News").css({"font-weight": 'bold'})
        ], position="top")
      ], position="top")
      components.style.css.padding = 5
    foot = self.rptObj.ui.navigation.footer(components, width, height, False, options, profile)
    foot.style.css.background_color = self.rptObj.theme.greys[2]
    disc = self.rptObj.ui.banners.disclaimer()
    disc.style.css.background_color = self.rptObj.theme.greys[4]
    col = self.col([foot, disc])
    col.style.css.padding_top = 20
    return col

  def tags(self, items):
    div = self.rptObj.ui.div()
    for i in items:
      if not hasattr(items, 'options'):
        it = self.rptObj.ui.text(i)
        it.style.css.font_weight = "bold"
        it.style.css.padding = "0 2px"
        div.add(it)
      else:
        div.add(i)
    return div

  @property
  def shop(self):
    """
    Description:
    ------------
    Property for all the components designed to be used in a e-commerce website
    """
    return CompStudioShopping.Shopping(self)

  @property
  def restaurant(self):
    """
    Description:
    ------------
    Property for all the components designed to be used in a e-commerce website
    """
    return CompStudioShopping.Resto(self)

  @property
  def blog(self):
    """
    Description:
    ------------
    Property for all the components to be used in a blog website
    """
    return CompStudioBlog.Blog(self)

  @property
  def gallery(self):
    """
    Description:
    ------------
    Property for all the components to be used in a blog website
    """
    return CompStudioBlog.Gallery(self)

  @property
  def dating(self):
    """
    Description:
    ------------
    Property for all the components to be used in a dating website
    """
    return CompStudioEvent.Dating(self)

  @property
  def wedding(self):
    """
    Description:
    ------------
    Property for all the components to be used in a wedding website
    """
    return CompStudioEvent.Wedding(self)

  @property
  def birth(self):
    """
    Description:
    ------------
    """
    return CompStudioEvent.Birth(self)

  @property
  def baptism(self):
    """
    Description:
    ------------
    """
    return CompStudioEvent.Baptism(self)

  @property
  def evg(self):
    """
    Description:
    ------------
    """
    return CompStudioEvent.EVG(self)

  @property
  def seminar(self):
    """
    Description:
    ------------

    https://www.voyage-event.com/autres-themes
    """
    return CompStudioEvent.Seminar(self)

  @property
  def birthday(self):
    """
    Description:
    ------------
    Property for all the components to be used in a wedding website
    """
    return CompStudioEvent.Birthday(self)

  @property
  def show(self):
    """
    Description:
    ------------
    Property for all the components to be used in a wedding website
    """
    return CompStudioEvent.Show(self)

  @property
  def vitrine(self):
    """
    Description:
    ------------
    """
    return CompStudioVitrine.Vitrine(self)

  @property
  def events(self):
    """
    Description:
    ------------
    """
    return CompStudioEvent.Event(self)

  @property
  def quiz(self):
    """
    Description:
    ------------
    """
    return CompStudioQuiz.Quiz(self)

  @property
  def dashboard(self):
    """
    Description:
    ------------
    """
    return CompStudioDashboard.Dashboard(self)

  @property
  def calendar(self):
    """
    Description:
    ------------
    """
    return CompStudioDashboard.Calendar(self)

  @property
  def news(self):
    """
    Description:
    ------------
    """
    return CompStudioNews.News(self)

