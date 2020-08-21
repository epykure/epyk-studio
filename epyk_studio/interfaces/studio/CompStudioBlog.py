#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import locale

from epyk.core.css import Defaults_css
from epyk.core.css.themes import ThemeBlue
from epyk_studio.lang import get_lang


class Blog(object):

  def __init__(self, context):
    self.context = context

  def theme(self):
    """
    Description:
    ------------
    Set the default theme for a blog.
    This will add a template to the body in order to have a header, template and footer
    """
    self.context.rptObj.theme = ThemeBlue.Blue()
    Defaults_css.Font.size = 16
    Defaults_css.Font.header_size = Defaults_css.Font.size + 4
    self.context.rptObj.body.add_template({"margin": '0 10%'})

  def delimiter(self, size=5, count=1, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Add a line delimiter to the page

    Attributes:
    ----------
    :param size: Integer. The size of the line.
    :param count: Integer. The number of lines
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    hr = self.context.rptObj.ui.layouts.hr(count, width=width, height=height, align=None, options=options, profile=profile)
    hr.style.css.padding = "0 20%"
    hr.hr.style.css.border_top = "%spx double %s" % (size, self.context.rptObj.theme.colors[5])
    return hr

  def title(self, text, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Add a title to the page

    Attributes:
    ----------
    :param text: String.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options:
    :param profile:
    """
    text = self.context.rptObj.py.encode_html(text)
    title = self.context.rptObj.ui.title(text, width=width, height=height, options=options, profile=profile)
    title.style.css.white_space = 'normal'
    return title

  def link(self, text, url, width=(100, '%'), height=(30, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param url:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options:
    :param profile:
    """
    text = self.context.rptObj.py.encode_html(text)
    return self.context.rptObj.ui.link(text, url, width=width, height=height, options=options, profile=profile)

  def italic(self, text, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options:
    :param profile:
    """
    text = self.context.rptObj.py.encode_html(text)
    return self.context.rptObj.ui.tags.i(text, width=width, height=height, options=options, profile=profile)

  def center(self, text, width=(100, '%'), height=(30, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options:
    :param profile:
    """
    text = self.context.rptObj.py.encode_html(text)
    return self.context.rptObj.ui.text(text, align="center", width=width, height=height, options=options, profile=profile)

  def breadcrumb(self, values, selected=None, width=(100, '%'), height=(30, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param values:
    :param selected:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options:
    :param profile:
    """
    bcrumb = self.context.rptObj.ui.breadcrumb(values, selected, width, height, options, profile)
    return bcrumb

  def paragraph(self, text, css=None, align="left", width=(100, '%'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param css:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    text = self.context.rptObj.py.encode_html(text)
    text = self.context.rptObj.py.markdown.resolve(text, css_attrs=css)
    container = self.context.rptObj.ui.div(text, align=align, width=width, height=height, options=options, profile=profile)
    return container

  def quote(self, text, author, job=None, align="left", width=(100, '%'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param author:
    :param job:
    :param align:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options:
    :param profile:
    """
    component = self.context.rptObj.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    component.style.padding_left = 30
    component.style.padding_right = 30
    component.style.css.margin_bottom = 5
    quote = self.context.rptObj.ui.pictos.quote()
    quote.style.css.margin_left = - 30
    quote.style.css.margin_bottom = -20
    quote.style.css.margin_top = 0
    component.add(quote)
    component.text = self.context.rptObj.ui.text(self.context.rptObj.py.encode_html(text))#.css({"margin-left": '30px'})
    component.text.style.css.font_factor(10)
    component.text.style.css.display = 'block'
    component.text.style.css.font_style = 'italic'
    component.author = self.context.rptObj.ui.text(self.context.rptObj.py.encode_html(author))
    component.author.style.css.bold()
    if job:
      component.job = self.context.rptObj.ui.text(self.context.rptObj.py.encode_html(job))
      component.add(self.context.rptObj.ui.div([component.text, component.author, self.context.rptObj.ui.text(",&nbsp;"), component.job], width=("auto", ''), align="right"))
    else:
      component.add(self.context.rptObj.ui.div([component.text, component.author], width=("auto", ''), align="right"))
    component[-1].style.css.padding_bottom = 10
    component[-1].style.css.border_bottom = "1px solid %s" % self.context.rptObj.theme.greys[6]
    if align == "center":
      component.style.css.margin_left = "auto"
      component.style.css.margin_right = "auto"
      component.style.css.display = "block"
    return component

  def button(self, text, icon=None, border=True, background=True, width=(100, '%'), align="center", height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param icon:
    :param border:
    :param background:
    :param align:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options:
    :param profile:
    """
    button = self.context.rptObj.ui.button(text, icon=icon, width=width, align=align, height=height, options=options, profile=profile)
    button.style.clear()
    button.style.css.padding = "0 10px"
    button.style.css.background = self.context.rptObj.theme.greys[0]
    button.style.hover({"color": self.context.rptObj.theme.colors[-1]})
    return button

  def picture(self, image, label=None, path=None, width=(300, 'px'), align="center", height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param image:
    :param label:
    :param path:
    :param align:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options:
    :param profile:
    """
    if label is None:
      img = self.context.rptObj.ui.img(image, path=path, width=width, height=height, align=align, options=options, profile=profile)
      img.style.css.margin_top = 5
      img.style.css.margin_bottom = 5
      return img

    component = self.context.rptObj.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    component.image = self.context.rptObj.ui.img(image, path=path, width=width, height=height, options=options, profile=profile)
    component.style.css.position = "relative"
    component.add(component.image)
    if not hasattr(label, 'options'):
      component.label = self.context.rptObj.ui.div(label)
      component.label.style.css.position = "absolute"
      component.label.style.css.background = "white"
      component.label.style.css.width = "auto"
      component.label.style.css.max_width = "calc(100%% - %spx)" % (width[0] / 10)
      component.label.style.css.padding = "0 10px"
      component.label.style.css.bottom = 35
    else:
      component.label = label
      component.label.style.css.position = "absolute"
    component.add(component.label)
    component.style.css.margin_top = 10
    component.style.css.margin_bottom = 10
    if align == 'center':
      component.style.css.margin_left = "auto"
      component.style.css.margin_right = "auto"
      component.style.css.display = "block"
    return component

  def video(self, video, label=None, width=(300, 'px'), align="center", height=(None, 'px'), htmlCode=None, profile=None, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param video:
    :param label:
    :param align:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode:
    :param profile:
    :param options:
    """
    if label is None:
      return self.context.rptObj.ui.media.video(video, width=width, height=height, align=align)

    component = self.context.rptObj.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    component.video = self.context.rptObj.ui.media.video(video, width=width, height=height, options=options, profile=profile)
    component.style.css.position = "relative"
    component.add(component.video)
    if not hasattr(label, 'options'):
      component.label = self.context.rptObj.ui.div(label)
      component.label.style.css.position = "absolute"
      component.label.style.css.background = "white"
      component.label.style.css.opacity = 0.6
      component.label.style.css.width = "auto"
      component.label.style.css.padding = "0 10px"
      component.label.style.css.top = 0
      component.label.style.css.right = 0
    else:
      component.label = label
    component.add(component.label)
    component.style.css.margin_top = 5
    component.style.css.margin_bottom = 5
    if align == 'center':
      component.style.css.margin = "auto"
      component.style.css.display = "block"
    return component

  def youtube(self, link, width=(100, '%'), height=(None, 'px'), htmlCode=None, profile=None, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param link:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode:
    :param profile:
    :param options:
    """
    return self.context.rptObj.ui.media.youtube(link, width=width, height=height, htmlCode=htmlCode, profile=profile, options=options)

  def time(self, date, icon="fas fa-circle", align="left", width=("auto", ''), height=(None, "px"), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param date:
    :param icon:
    :param align:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
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
    icon.icon.style.css.font_factor(-3)
    icon.icon.style.css.color = self.context.rptObj.theme.colors[5]
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

  def by(self, name, url=None, date=None, align="center", width=("100", '%'), height=(None, "px"), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    :param url:
    :param date:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    component = self.context.rptObj.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    options = options or {}
    lang_obj = get_lang(options.get('lang'))
    if date is not None:
      component.add(self.context.rptObj.ui.text(lang_obj.BY_WITH_NAME % date))
    else:
      component.add(self.context.rptObj.ui.text(lang_obj.BY))
    component.name = self.context.rptObj.ui.link(name, url)
    component.name.style.css.color = self.context.rptObj.theme.colors[6]
    component.add(component.name)
    return component

  def typeWriter(self, text, width=('auto', ""), height=(None, "px"), align="center", htmlCode=None, profile=None, options=None):
    """
    Description:
    ------------

    https://www.w3schools.com/howto/howto_js_typewriter.asp

    Attributes:
    ----------
    :param text:
    :param width:
    :param height:
    :param align:
    :param htmlCode:
    :param profile:
    :param options:
    """
    t = self.context.rptObj.ui.text(text, width=width, height=height, align=align, htmlCode=htmlCode, profile=profile, options=options)
    t.write()
    return t

  def sliding(self, text, width=('auto', ""), height=(None, "px"), align="center", htmlCode=None, profile=None, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param width:
    :param height:
    :param align:
    :param htmlCode:
    :param profile:
    :param options:
    """
    t = self.context.rptObj.ui.text(text, width=width, height=height, align=align, htmlCode=htmlCode, profile=profile, options=options)
    t.style.effects.sliding()
    t.style.hover({"animation-play-state": 'paused', "-webkit-animation-play-state": 'paused',
                   '-moz-animation-play-state': 'paused', '-o-animation-play-state': 'paused'})
    return t


class Gallery(Blog):

  def mosaic(self, pictures, columns=6, path=None, width=(None, '%'), height=('auto', ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param pictures:
    :param columns:
    :param path:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options:
    :param profile:
    """
    options = options or {}
    grid = self.context.rptObj.ui.grid(width=width, height=height, options=options, profile=profile)
    grid.style.css.margin_top = 20
    grid.style.css.overflow = 'hidden'
    grid.style.css.margin_bottom = 20
    row = self.context.rptObj.ui.row()
    for i, picture in enumerate(pictures):
      if i % columns == 0:
        grid.add(row)
        row = self.context.rptObj.ui.row()
      if not hasattr(picture, 'options'):
        picture = self.context.rptObj.ui.img(picture, path=path)
        picture.style.css.max_height = 200
        picture.style.css.margin = 5
        if options.get('zoom', True):
          picture.style.effects.zoom()
      row.add(picture)

    if len(row):
      for c in row:
        c.set_size(12 // columns)
      grid.add(row)
    return grid

  def carousel(self, images, path=None, selected=0, width=(100, "%"), height=(300, "px"), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param images:
    :param path:
    :param selected:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    c = self.context.rptObj.ui.images.carousel(images, path, selected, width, height, options, profile)
    return c

  def pagination(self, count, selected=1, width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param count:
    :param selected:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    p = self.context.rptObj.ui.navigation.indices(count, selected=selected, width=width, height=height,
                                                  options=options, profile=profile)
    p.style.css.text_align = "center"
    return p

  def heroes(self, url, path=None, width=(100, "%"), height=(500, "px"), align="center", options=None, profile=None):
    """

    https://www.w3schools.com/cssref/pr_background-image.asp

    :param url:
    :param path:
    :param width:
    :param height:
    :param align:
    :param options:
    :param profile:
    """
    options = options or {}
    img = self.context.rptObj.ui.div(width=width, height=height, align=align, options=options, profile=profile)
    if path is not None:
      img.style.css.background_image = "url(%s/%s)" % (path.replace("\\", "/"), url)
    else:
      img.style.css.background_image = "url(%s)" % url
    img.style.css.background_position = "center center"
    img.style.css.background_repeat = "no-repeat"
    img.style.css.background_size = "cover"
    if options.get("fixed", True):
      img.style.css.background_attachment = "fixed"
    img.style.css.position = "relative"
    return img

  def fixed(self, url, path=None, width=(100, "%"), height=(300, "px"), align="center", options=None, profile=None):
    """

    :param url:
    :param path:
    :param width:
    :param height:
    :param align:
    :param options:
    :param profile:
    """
    options = options or {}
    img = self.context.rptObj.ui.div(width=width, height=height, align=align, options=options, profile=profile)
    if path is not None:
      img.style.css.background_image = "url(%s/%s)" % (path.replace("\\", "/"), url)
    else:
      img.style.css.background_image = "url(%s)" % url
    img.style.css.background_position = "center center"
    img.style.css.background_repeat = "no-repeat"
    img.style.css.background_size = "cover"
    if options.get("fixed", True):
      img.style.css.background_attachment = "fixed"
    return img

  def image(self, url, path=None, width=(100, "%"), height=(300, "px"), align="center", options=None, profile=None):
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
    :param align:
    :param options:
    :param profile:
    """
    img = self.context.rptObj.ui.images.img(url, path=path, width=width, height=height, align=align, options=options, profile=profile)
    return img

  def link(self, img, url="#", path=None, width=(100, "%"), height=(None, "px"), align="center", options=None, profile=None):
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
    :param align:
    :param options:
    :param profile:
    """
    img = self.context.rptObj.ui.images.img(img, path=path, width=width, height=height, align=align, options=options, profile=profile)
    img.style.effects.reduce()
    img.style.css.cursor = "pointer"
    img.goto(url)
    return img

  def overlay(self, img, text=None, path=None, width=(100, "%"), height=(None, "px"), align="center", options=None, profile=None):
    """
    Description:
    ------------

    https://www.w3schools.com/howto/howto_css_image_overlay_slide.asp

    Attributes:
    ----------
    :param img:
    :param text:
    :param path:
    :param width:
    :param height:
    :param align:
    :param options:
    :param profile:
    """
    options = options or {}
    container = self.context.rptObj.ui.div(width=width, height=height, align=align, options=options, profile=profile)
    container.style.css.position = "relative"
    container.style.css.box_sizing = "border-box"
    container.img = self.context.rptObj.ui.images.img(img, path=path, width=(100, "%"), height=(None, "px"), align="center", options=options, profile=profile)
    container.img.style.css.display = "block"
    container.img.style.css.width = "100%"
    container.add(container.img)
    container.attr['class'].clear()
    container.attr['class'].add("container_overlay")
    container.overlay = self.context.rptObj.ui.div(width=width, height=height, align=align, options=options, profile=profile)
    if text is not None:
      if hasattr(text, 'options'):
        container.text = text
      else:
        container.text = self.context.rptObj.ui.div(text, width=(100, "%"), height=height, align=align, options=options, profile=profile)

      if options.get("direction") is None:
        container.overlay.attr['class'].clear()
        container.overlay.attr['class'].add("test_overlay_title")
        container.overlay.style.css.opacity = 0
        container.overlay.style.css.position = "absolute"
        container.overlay.style.css.bottom = 0
        container.overlay.style.css.color = self.context.rptObj.theme.greys[0]
        container.overlay.style.css.background = "rgba(0, 0, 0, 0.5)"
        self.context.rptObj.css.customText(".container_overlay:hover .test_overlay_title {opacity: 1 !IMPORTANT;}")
      elif options.get("direction") == 'top':
        container.overlay.attr['class'].clear()
        container.overlay.attr['class'].add("test_overlay_top")
        container.overlay.style.css.position = "absolute"
        container.overlay.style.css.width = "100%"
        container.overlay.style.css.height = 0
        container.overlay.style.css.transition = ".5s ease"
        container.overlay.style.css.overflow = "hidden"
        container.overlay.style.css.bottom = 0
        container.overlay.style.css.right = 0
        container.overlay.style.css.left = 0
        container.overlay.style.css.color = self.context.rptObj.theme.greys[0]
        container.overlay.style.css.background = "rgba(0, 0, 0, 0.5)"
        self.context.rptObj.css.customText(".container_overlay:hover .test_overlay_top {height: 100% !IMPORTANT;}")
      elif options.get("direction") == 'bottom':
        container.overlay.attr['class'].clear()
        container.overlay.attr['class'].add("test_overlay_bottom")
        container.overlay.style.css.position = "absolute"
        container.overlay.style.css.width = "100%"
        container.overlay.style.css.height = 0
        container.overlay.style.css.transition = ".5s ease"
        container.overlay.style.css.overflow = "hidden"
        container.overlay.style.css.bottom = "100%"
        container.overlay.style.css.right = 0
        container.overlay.style.css.left = 0
        container.overlay.style.css.color = self.context.rptObj.theme.greys[0]
        container.overlay.style.css.background = "rgba(0, 0, 0, 0.5)"
        self.context.rptObj.css.customText(".container_overlay:hover .test_overlay_bottom {height: 100% !IMPORTANT; bottom: 0 !IMPORTANT}")
      elif options.get("direction") == 'right':
        container.overlay.attr['class'].clear()
        container.overlay.attr['class'].add("test_overlay_right")
        container.overlay.style.css.position = "absolute"
        container.overlay.style.css.width = 0
        container.overlay.style.css.height = "100%"
        container.overlay.style.css.transition = ".5s ease"
        container.overlay.style.css.overflow = "hidden"
        container.overlay.style.css.bottom = 0
        container.overlay.style.css.right = 0
        container.overlay.style.css.left = "100%"
        container.overlay.style.css.color = self.context.rptObj.theme.greys[0]
        container.overlay.style.css.background = "rgba(0, 0, 0, 0.5)"
        self.context.rptObj.css.customText(".container_overlay:hover .test_overlay_right {width: 100% !IMPORTANT; left: 0 !IMPORTANT}")
      elif options.get("direction") == 'left':
        container.overlay.attr['class'].clear()
        container.overlay.attr['class'].add("test_overlay_left")
        container.overlay.style.css.position = "absolute"
        container.overlay.style.css.width = 0
        container.overlay.style.css.height = "100%"
        container.overlay.style.css.transition = ".5s ease"
        container.overlay.style.css.overflow = "hidden"
        container.overlay.style.css.bottom = 0
        container.overlay.style.css.right = "100%"
        container.overlay.style.css.left = 0
        container.overlay.style.css.color = self.context.rptObj.theme.greys[0]
        container.overlay.style.css.background = "rgba(0, 0, 0, 0.5)"
        self.context.rptObj.css.customText(".container_overlay:hover .test_overlay_left {width: 100% !IMPORTANT; right: 0 !IMPORTANT}")
      container.style.css.cursor = 'pointer'
      container.overlay.add(container.text)
    container.add(container.overlay)
    return container

  def wallpaper(self, url, width=(100, "%"), height=(300, "px"), size="cover", margin=0, align="center", position="middle"):
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
    background = self.context.rptObj.ui.images.wallpaper(url, width=width, height=height, size=size, margin=margin, align=align, position=position)
    return background

  def animated(self, image=None, text="", title="", url=None, path=None, width=(200, "px"), height=(200, "px"),
               options=None, profile=None):
    """

    :param image:
    :param text:
    :param title:
    :param url:
    :param path:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    a = self.context.rptObj.ui.images.animated(image, text=text, title=title, url=url, path=path, width=width,
                                               height=height, options=options, profile=profile)
    return a
