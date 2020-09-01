#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css.themes import ThemeBlue
from epyk_studio.lang import get_lang


class Vitrine(object):

  def __init__(self, context):
    self.context = context

  def theme(self):
    """
    Description:
    ------------

    """
    self.context.rptObj.theme = ThemeBlue.BlueGrey()

  def vignet(self, title, content="", image=None, render="row", align="center", width=(90, '%'), height=(None, "px"),
             options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param title:
    :param content:
    :param image:
    :param render:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param options: Dictionary. Optional. Specific Python options available for this component
    """
    v = self.context.rptObj.ui.vignets.image(title=title, content=content, image=image, render=render, align=align,
                                                     width=width, height=height, options=options, profile=profile)
    return v

  def cover(self, url, components=None, width=(100, "%"), height=(300, "px"), size="cover", margin=0, align="center",
            position="middle", options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param url:
    :param components:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param size:
    :param margin:
    :param align: String. Optional. A string with the horizontal position of the component
    :param position: String. Optional. A string with the vertical position of the component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param options: Dictionary. Optional. Specific Python options available for this component
    """
    b = self.context.rptObj.ui.images.wallpaper(url=url, width=width, height=height, size=size, margin=margin,
                                                align=align, position=position, options=options, profile=profile)
    if components is not None:
      pass
    return b

  def background(self, url, width=(90, "%"), height=(450, "px"), size="contain", margin=0, align="center",
                 position="middle", options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param url:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param size:
    :param margin:
    :param align: String. Optional. A string with the horizontal position of the component
    :param position: String. Optional. A string with the vertical position of the component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param options: Dictionary. Optional. Specific Python options available for this component
    """
    b = self.context.rptObj.ui.images.background(url=url, width=width, height=height, size=size, margin=margin, align=align,
                                                 position=position, options=options, profile=profile)
    return b

  def image(self, image, text=None, title=None, url=None, path=None, width=(200, "px"), height=(200, "px"), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param image:
    :param text:
    :param title:
    :param url:
    :param path:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    if text is None and title is None:
      return self.context.rptObj.ui.img(image, path=path, width=width, height=height, options=options, profile=profile)

    a = self.context.rptObj.ui.images.animated(image=image, text=text, title=title, url=url, path=path,
                                                      width=width, height=height, options=options, profile=profile)
    a.style.css.border = "1px solid red"
    return a

  def picture(self, image=None, label=None, path=None, width=(100, "%"), height=(None, "px"), align="center", htmlCode=None,
              profile=None, options=None):
    """
    Description:
    ------------
    Add an HTML image to the page. The path can be defined either in a absolute or relative format.

    Tip: The absolute format does not work on servers. It is recommended to use relative starting to the root of the server

    Usage::

      rptObj.ui.img("epykIcon.PNG", path=r"../../../static/images", height=(50, "px"))


    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Image`

    Related Pages:

      https://www.w3schools.com/bootstrap/bootstrap_ref_css_images.asp
      https://www.w3schools.com/cssref/css3_pr_border-radius.asp

    Attributes:
    ----------
    :param image: String. The image file name
    :param label: String. Optional. The text of label to be added to the component
    :param path: Optional. String. The image file path
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param align: String. Optional. A string with the horizontal position of the component
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param options: Dictionary. Optional. Specific Python options available for this component
    """
    if height[0] is not None and width[1] == '%':
      width = ("auto", '')
    component = self.context.rptObj.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    component.image = self.context.rptObj.ui.img(image, path, (100, '%'), ('auto', ''), align, htmlCode, profile, "", options or {})
    component.style.css.position = "relative"
    component.add(component.image)
    if not hasattr(label, 'options'):
      component.label = self.context.rptObj.ui.div(label)
      component.label.style.css.background = "white"
      component.label.style.css.opacity = 0.6
    else:
      component.label = self.context.rptObj.ui.div()
      component.label.add(label)
    component.label.style.css.position = "absolute"
    component.label.style.css.text_align = "center"
    component.label.style.css.width = "calc(100% - 20px)"
    component.label.style.css.margin = 10
    component.label.style.css.padding = 10
    component.label.style.css.bottom = 5
    component.add(component.label)
    return component

  def delimiter(self, size=5, count=1, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Add a line delimiter to the page

    Attributes:
    ----------
    :param size: Integer. The size of the line.
    :param count: Integer. The number of lines
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    hr = self.context.rptObj.ui.layouts.hr(count, width=width, height=height, align=None, options=options, profile=profile)
    hr.style.css.padding = "0 20%"
    hr.hr.style.css.border_top = "%spx double %s" % (size, self.context.rptObj.theme.colors[5])
    return hr

  def youtube(self, link, width=(100, '%'), height=(None, 'px'), htmlCode=None, profile=None, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param link:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param options: Dictionary. Optional. Specific Python options available for this component
    """
    return self.context.rptObj.ui.media.youtube(link, width=width, height=height, htmlCode=htmlCode, profile=profile, options=options)

  def avatar(self, image="", path=None, size=80, text=None, htmlCode=None, profile=None, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param image:
    :param path:
    :param size:
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param options: Dictionary. Optional. Specific Python options available for this component
    """
    dfl_options = {"status": False}
    if options is not None:
      dfl_options.update(options)
    img = self.context.rptObj.ui.images.avatar(image=image, path=path, text=text, width=(size, 'px'), height=(size, 'px'), htmlCode=htmlCode,
                                               options=dfl_options, profile=profile)
    return img

  def price(self, value, title, items, url=None, align="center", width=(300, 'px'), currency=None, options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param value:
    :param title:
    :param items:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param currency:
    :param options: Dictionary. Optional. Specific Python options available for this component
    """
    options = options or {}
    currency = currency or get_lang(options.get('lang')).currency(options.get('country'))
    p = self.context.rptObj.ui.vignets.price(value=value, title=title, items=items, url=url, align=align, width=width, currency=currency)
    return p

  def quote(self, text, author, job=None, align="left", width=(100, '%'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param author:
    :param job:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    component = self.context.rptObj.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    component.style.css.margin_bottom = 5
    quote = self.context.rptObj.ui.pictos.quote()
    quote.style.css.margin_bottom = -20
    component.add(quote)
    component.text = self.context.rptObj.ui.text("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s" % self.context.rptObj.py.encode_html(text))
    component.add(component.text)
    component.author = self.context.rptObj.ui.text(self.context.rptObj.py.encode_html(author))
    component.author.style.css.bold()
    if job is not None:
      component.job = self.context.rptObj.ui.text(self.context.rptObj.py.encode_html(job))
      component.add(self.context.rptObj.ui.div([component.author, self.context.rptObj.ui.text(",&nbsp;"), component.job], align="right"))
    else:
      component.add(self.context.rptObj.ui.div([component.author], align="right"))
    return component

  def contact_us(self, title="Contact Us", background=None, width=(100, '%'), align="left", height=(None, 'px'),
                 htmlCode="contactus", options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param title:
    :param background:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    c = self.context.rptObj.ui.banners.contact_us(title=title, background=background, width=width, align=align,
               height=height, htmlCode=htmlCode, options=options, profile=profile)
    return c

  def disclaimer(self, copyright=None, links=None, width=(100, '%'), height=("auto", ''), align="center", options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param copyright:
    :param links:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    d = self.context.rptObj.ui.banners.disclaimer(copyright=copyright, links=links or [], width=width, height=height,
                                                            align=align, options=options, profile=profile)
    return d

  def tabs(self, color=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None, options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param color:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param helper:
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    t = self.context.rptObj.ui.panels.tabs(color=color, width=width, height=height, htmlCode=htmlCode, helper=helper,
                                                  options=options, profile=profile)
    return t

  def accordion(self, components, title, color=None, align="center", width=(100, "%"), height=(None, "px"),
                htmlCode=None, helper=None, options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param components:
    :param title:
    :param color: String. Optional. The font color in the component. Default inherit
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: String. Optional. A tooltip helper
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    s = self.context.rptObj.ui.panels.sliding(components, title=title, color=color, align=align, width=width,
      height=height, htmlCode=htmlCode, helper=helper, options=options, profile=profile)
    return s

  def card(self, title, content, icon=None, render='row', align="center", width=(200, 'px'), options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param title:
    :param content:
    :param icon:
    :param render:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    """
    v = self.context.rptObj.ui.vignets.vignet(title=title, content=content, icon=icon, render=render,
                                                     align=align, width=width, options=options)
    return v

  def up(self, icon="fas fa-arrow-up", top=20, right=20, bottom=None, tooltip=None, width=(100, '%'), options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param icon:
    :param top:
    :param right:
    :param bottom:
    :param tooltip: String. Optional. A string with the value of the tooltip
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    n = self.context.rptObj.ui.navigation.up(icon=icon, top=top, right=right, bottom=bottom, tooltip=tooltip,
                                                    width=width, options=options, profile=profile)
    return n

  def subscribe(self, value="", placeholder=None, button=None, width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param value:
    :param placeholder:
    :param button:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    options = options or {}
    placeholder = placeholder or get_lang(options.get('lang')).PLACEHOLDER_EMAIL
    button = button or get_lang(options.get('lang')).BUTTON_SUBSCRIBE
    s = self.context.rptObj.ui.forms.subscribe(value=value, placeholder=placeholder, button=button, width=width,
                                                      height=height, options=options, profile=profile)
    return s

  def list(self, data=None, color=None, width=('auto', ""), height=(None, 'px'), htmlCode=None, helper=None,
           options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data:
    :param color: String. Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: String. Optional. A tooltip helper
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :return:
    """
    l = self.context.rptObj.ui.lists.list(data=data, color=color, width=width, height=height, htmlCode=htmlCode,
                                                 helper=helper, options=options, profile=profile)
    return l
