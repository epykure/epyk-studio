#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import locale
import os

from epyk.core.css import Defaults as defaultCss
from epyk.core.css.themes import ThemeBlue
from epyk_studio.lang import get_lang
from epyk.core.html import Html


class Blog:

  def __init__(self, ui):
    self.page = ui.page

  def theme(self):
    """
    Description:
    ------------
    Set the default theme for a blog.
    This will add a template to the body in order to have a header, template and footer.
    """
    self.page.theme = ThemeBlue.Blue()
    defaultCss.Font.size = 16
    defaultCss.Font.header_size = defaultCss.Font.size + 4
    self.page.body.add_template({"margin": '0 10%'})

  def delimiter(self, size=5, count=1, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Add a line delimiter to the page.

    :tags: Layout, Delimiter
    :categories: studio

    Usage:
    -----

      page.studio.blog.delimiter()

    Related Pages:

      https://www.w3schools.com/tags/tag_hr.asp
      https://www.w3schools.com/howto/howto_css_style_hr.asp

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlOthers.Hr`

    Templates:

      blog.py

    Attributes:
    ----------
    :param size: Integer. Optional. The size of the line.
    :param count: Integer. Optional. The number of lines.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    hr = self.page.ui.layouts.hr(
      count, width=width, height=height, align=None, options=options, profile=profile)
    hr.style.css.padding = "0 20%"
    hr.hr.style.css.border_top = "%spx double %s" % (size, self.page.theme.colors[5])
    return hr

  def title(self, text, html_code=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Add a title to the page.
    Text will be automatically encoded to HTML in order to ensure a correct formatting in the page.

    :tags: Text
    :categories: studio

    Usage:
    -----

      page.studio.blog.title("This is a title")

    Related Pages:

      https://www.w3schools.com/tags/tag_hn.asp

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Title`

    Templates:

      blog.py

    Attributes:
    ----------
    :param text: String. Optional. The text for the title.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    text = self.page.py.encode_html(text)
    title = self.page.ui.title(
      text, html_code=html_code, width=width, height=height, options=options, profile=profile)
    title.style.css.white_space = 'normal'
    return title

  def link(self, text, url, html_code=None, height=(30, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Add a link to the page.
    Text will be automatically encoded to HTML in order to ensure a correct formatting in the page.

    :tags: Text, Link
    :categories: Studio, Text

    Usage:
    -----

      page.studio.blog.title("google", "www.google.com")

    Related Pages:

      https://www.w3schools.com/tags/att_a_href.asp

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlLinks.ExternalLink`

    Templates:

      blog.py

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param url: String. Optional. The underlying url for the link.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    text = self.page.py.encode_html(text)
    return self.page.ui.link(text, url, html_code=html_code, height=height, options=options, profile=profile)

  def italic(self, text, html_code=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Add a text in italic to the page.
    Text will be automatically encoded to HTML in order to ensure a correct formatting in the page.

    :tags: Text
    :categories: Studio, Text

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

      blog.py

    Attributes:
    ----------
    :param text: String. Optional. The text to be displayed.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    text = self.page.py.encode_html(text)
    return self.page.ui.tags.i(
      text, html_code=html_code, width=width, height=height, options=options, profile=profile)

  def center(self, text, width=(100, '%'), height=(30, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

      blog.py

    Attributes:
    ----------
    :param text: String. The text to be displayed.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    text = self.page.py.encode_html(text)
    return self.page.ui.text(
      text, align="center", width=width, height=height, options=options, profile=profile)

  def breadcrumb(self, values, selected=None, width=(100, '%'), height=(30, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

      blog.py

    Attributes:
    ----------
    :param values: List. The values in the breadcrumb.
    :param selected: String. Optional. The highlighted current value.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    bcrumb = self.page.ui.breadcrumb(values, selected, width, height, options, profile)
    return bcrumb

  def paragraph(self, text, css=None, align="left", width=(100, '%'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

      blog.py

    Attributes:
    ----------
    :param text: String. The text to be displayed.
    :param css: Dictionary. Optional. The CSS attributes to be added.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    text = self.page.py.encode_html(text)
    text = self.page.py.markdown.resolve(text, css_attrs=css)
    container = self.page.ui.div(
      text, align=align, width=width, height=height, options=options, profile=profile)
    return container

  def quote(self, text, author, job=None, align="left", width=(100, '%'), height=("auto", ''), options=None,
            profile=None):
    """
    Description:
    ------------
    Add a quote on the page.

    :tags: Text, Feedbacks, Comment
    :categories: Text, Studio

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

      blog.py

    Attributes:
    ----------
    :param text: String. Teh quote.
    :param author: String. Text the author for the quote.
    :param job: String. Optional. The job of the author.
    :param align:  String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    component = self.page.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    component.style.padding_left = 30
    component.style.padding_right = 30
    component.style.css.margin_bottom = 5
    quote = self.page.ui.pictos.quote()
    quote.style.css.margin_left = - 30
    quote.style.css.margin_bottom = -20
    quote.style.css.margin_top = 0
    component.add(quote)
    component.text = self.page.ui.text(self.page.py.encode_html(text), profile=profile)
    component.text.style.css.font_factor(10)
    component.text.style.css.display = 'block'
    component.text.style.css.font_style = 'italic'
    component.author = self.page.ui.text(self.page.py.encode_html(author), profile=profile)
    component.author.style.css.bold()
    if job:
      component.job = self.page.ui.text(self.page.py.encode_html(job), profile=profile)
      component.add(self.page.ui.div([
        component.text, component.author, self.page.ui.text(",&nbsp;", profile=profile),
        component.job], width=("auto", ''), align="right", profile=profile))
    else:
      component.add(self.page.ui.div(
        [component.text, component.author], width=("auto", ''), align="right", profile=profile))
    component[-1].style.css.padding_bottom = 10
    component[-1].style.css.border_bottom = "1px solid %s" % self.page.theme.greys[6]
    if align == "center":
      component.style.css.margin_left = "auto"
      component.style.css.margin_right = "auto"
      component.style.css.display = "block"
    return component

  def button(self, text, icon=None, width=(100, '%'), align="center", height=(None, 'px'),
             options=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

      blog.py

    Attributes:
    ----------
    :param text: String. The text to be displayed.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    button = self.page.ui.button(
      text, icon=icon, width=width, align=align, height=height, options=options, profile=profile)
    button.style.clear()
    button.style.css.padding = "0 10px"
    button.style.css.background = self.page.theme.greys[0]
    button.style.hover({"color": self.page.theme.colors[-1]})
    return button

  def picture(self, image, label=None, path=None, width=(300, 'px'), align="center", height=(None, 'px'),
              html_code=None, options=None, profile=False):
    """
    Description:
    ------------
    Add a picture to the page

    :tags: Picture
    :categories: Studio, Image

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

      blog.py

    Attributes:
    ----------
    :param image: String. The picture name.
    :param label: String. Optional. The text to be displayed with the picture.
    :param path: String. Optional. The picture path.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if label is None:
      img = self.page.ui.img(
        image, path=path, width=width, height=height, align=align, html_code=html_code, options=options,
        profile=profile)
      img.style.css.margin_top = 5
      img.style.css.margin_bottom = 5
      return img

    component = self.page.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    component.image = self.page.ui.img(
      image, path=path, width=width, height=height, options=options, profile=profile)
    component.style.css.position = "relative"
    component.add(component.image)
    if not hasattr(label, 'options'):
      component.label = self.page.ui.div(label)
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

  def video(self, video, label=None, width=(300, 'px'), align="center", height=(None, 'px'), html_code=None,
            profile=None, options=None):
    """
    Description:
    ------------
    Add a video to the page.

    :tags: Video
    :categories: Studio

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

      blog.py

    Attributes:
    ----------
    :param video: String. The video path.
    :param label: String. Optional. The text of label to be added to the component.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if label is None:
      return self.page.ui.media.video(video, width=width, height=height, align=align, html_code=html_code)

    component = self.page.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    component.video = self.page.ui.media.video(
      video, width=width, height=height, html_code=html_code, options=options, profile=profile)
    component.style.css.position = "relative"
    component.add(component.video)
    if not hasattr(label, 'options'):
      component.label = self.page.ui.div(label)
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

  def youtube(self, link, width=(100, '%'), height=(None, 'px'), html_code=None, profile=None, options=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

      blog.py

    Attributes:
    ----------
    :param link: String. The youtube video path.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    return self.page.ui.media.youtube(
      link, width=width, height=height, html_code=html_code, profile=profile, options=options)

  def time(self, date, icon="fas fa-circle", align="left", width=("auto", ''), height=(None, "px"), options=None,
           profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

      blog.py

    Attributes:
    ----------
    :param date: String. A date time format: %Y-%m-%d %H:%M:%S.%f.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param align: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    options = options or {}
    country = get_lang(options.get("lang")).country(options.get("country"))
    locale.setlocale(locale.LC_TIME, '%s_%s' % (country, country.upper()))
    date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    current = datetime.datetime.now()
    delta_time = current - date_time_obj
    component = self.page.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    icon = self.page.ui.icons.awesome(icon)
    icon.icon.style.css.font_factor(-3)
    icon.icon.style.css.color = self.page.theme.colors[5]
    component.add(icon)
    if delta_time.days == 0:
      if date_time_obj.day != current.day:
        text = self.page.ui.text(get_lang(options.get("lang")).LABEL_YESTERDAY)
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
        component.add(self.page.ui.text(" ".join(tooltip_value)))
    else:
      text = self.page.ui.text(self.page.py.encode_html(date_time_obj.strftime("%d %B %Y")))
      elapsed_time = self.page.py.dates.elapsed(delta_time)
      tooltip_value = []
      for lbl in ['years', 'months', 'days']:
        if elapsed_time.get(lbl, 0) > 0:
          tooltip_value.append("%s %s" % (elapsed_time[lbl], get_lang(options.get("lang")).LABEL_TIME[lbl]))
      text.tooltip(" ".join(tooltip_value))
      component.add(text)
    return component

  def by(self, name, url=None, date=None, align="center", width=("100", '%'), height=(None, "px"), options=None,
         html_code=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

      blog.py

    Attributes:
    ----------
    :param name: String. Optional. The name.
    :param url: String. Optional. The url link.
    :param date: String. Optional. The date.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    component = self.page.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    options = options or {}
    lang_obj = get_lang(options.get('lang'))
    if date is not None:
      component.text = self.page.ui.text(lang_obj.BY_WITH_NAME % date, html_code=html_code)
    else:
      component.text = self.page.ui.text(lang_obj.BY, html_code=html_code)
    component.add(component.text)
    component.name = self.page.ui.link(name, url)
    component.name.style.css.color = self.page.theme.colors[6]
    component.add(component.name)
    return component

  def typeWriter(self, text, width=('auto', ""), height=(None, "px"), align="center", html_code=None, profile=None,
                 options=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

      blog.py

    Related Pages:

      https://www.w3schools.com/howto/howto_js_typewriter.asp

    Attributes:
    ----------
    :param text: String. The text to be displayed.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    t = self.page.ui.text(
      text, width=width, height=height, align=align, html_code=html_code, profile=profile, options=options)
    t.write()
    return t

  def sliding(self, text, width=('auto', ""), height=(None, "px"), align="center", html_code=None, profile=None,
              options=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

      https://nosmoking.developpez.com/demos/css/css-marque-rtl.html

    Underlying HTML Objects:

    Templates:

      blog.py

    Attributes:
    ----------
    :param text: String. The text to be displayed.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    t = self.page.ui.div(
      text, width=width, height=height, align=align, html_code=html_code, profile=profile, options=options)
    t.style.effects.sliding()
    #t.style.hover({"animation-play-state": 'paused', "-webkit-animation-play-state": 'paused', '-moz-animation-play-state': 'paused', '-o-animation-play-state': 'paused'})
    cont = self.page.ui.div(t, width=(100, "%"), height=("auto", ''))
    cont.style.css.overflow_x = "hidden"
    cont.style.css.overflow_y = "hidden"
    return cont

  def absolute(self, text, top=None, right=None, bottom=None, left=None, font_family=None, html_code=None, profile=None,
               options=None):
    """
    Description:
    ------------
    Add a text on the page at a specific position.

    :tags: Text, Layout
    :categories: Text, Studio

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

      blog.py

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param top: Tuple. Optional. A tuple with the integer for the component's distance to the top of the page.
    :param right: Tuple. Optional. A tuple with the integer for the component's distance to the right of the page.
    :param bottom: Tuple. Optional. A tuple with the integer for the component's distance to the bottom of the page.
    :param left: Tuple. Optional. A tuple with the integer for the component's distance to the left of the page.
    :param font_family: String. Optional. Specify the CSS font family.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    text = self.page.studio.text(text, html_code=html_code, profile=profile, options=options)
    if right is not None:
      text.style.css.right = right
    if bottom is not None:
      text.style.css.bottom = bottom
    if top is not None:
      text.style.css.top = top
    if left is not None:
      text.style.css.left = left
    if font_family is not None:
      text.style.css.font_family = font_family
    text.style.css.position = "absolute"
    return text

  def like(self, value=0, icon="far fa-heart", top=(60, "px"), right=(10, "px"), tooltip="Like the page",
           html_code=None, options=None, profile=None):
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
    :param value: Integer. Optional. The count of likes.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param top: Tuple. Optional. A tuple with the integer for the component's distance to the top of the page.
    :param right: Tuple. Optional. A tuple with the integer for the component's distance to the right of the page.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    like = self.page.ui.icon(icon, options=options, profile=profile)
    ike_counter = self.page.ui.text(
      "(%s)" % (value or 0), html_code=html_code, options=options, profile=profile)
    ike_counter.style.css.margin_left = 5
    like.tooltip(tooltip)
    like.style.css.remove("color")
    like.style.css.cursor = "pointer"
    like.style.add_classes.div.color_hover()
    container = self.page.ui.div([like, ike_counter], options=options, profile=profile, width="auto")
    container.style.css.fixed(top=top[0], right=right[0])
    container.text = ike_counter
    container.icon = like
    return container


class Gallery(Blog):

  def mosaic(self, pictures=None, columns=6, path=None, width=(None, '%'), height=('auto', ''), options=None,
             profile=None):
    """
    Description:
    ------------
    Mosaic of pictures.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Attributes:
    ----------
    :param pictures: List. Optional. The list with the pictures.
    :param columns: Integer. Optional. The number of column for the mosaic component.
    :param path: String. Optional. The path for the picture.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    dflt_options = {"extensions": ['jpg']}
    if options is not None:
      dflt_options.update(options)
    grid = self.page.ui.grid(width=width, height=height, options=dflt_options, profile=profile)
    grid.style.css.margin_top = 20
    grid.style.css.overflow = 'hidden'
    grid.style.css.margin_bottom = 20
    row = self.page.ui.row(options=dflt_options)
    grid.pictures = []
    if path is not None and pictures is None:
      pictures = []
      for img in os.listdir(path):
        ext_img = img.split(".")[-1]
        if ext_img.lower() in dflt_options["extensions"]:
          pictures.append(img)
      if 'static' in dflt_options:
        path = dflt_options['static']
    pictures = pictures or []
    for i, picture in enumerate(pictures):
      if dflt_options.get("max") is not None and len(grid.pictures) > dflt_options.get("max"):
        break

      if i % columns == 0:
        grid.add(row)
        row = self.page.ui.row(options=dflt_options)
      if not hasattr(picture, 'options'):
        picture = self.page.ui.img(
          self.page.py.encode_html(picture), path=self.page.py.encode_html(path),
          html_code="%s_%s" % (grid.htmlCode, i))
        picture.attr["data-next"] = "%s_%s" % (grid.htmlCode, min(i + 1, len(pictures) - 1))
        picture.attr["data-previous"] = "%s_%s" % (grid.htmlCode, max(i - 1, 0))
        picture.style.css.max_height = 200
        picture.style.css.margin = 5
        grid.pictures.append(picture)
        if dflt_options.get('zoom', True):
          picture.style.effects.zoom()
      row.add(picture)
      picture.parent = row[-1]
    if dflt_options.get('focus', True):
      grid.image = self.page.studio.blog.picture("", path=path, align="center")
      grid.image.style.css.width = "calc(90% - 20px)"
      grid.image.style.css.max_height = 450
      grid.image.style.css.border_radius = 20
      grid.image.style.css.position = "absolute"
      grid.image.style.css.margin = "auto"
      grid.image.style.css.top = 0
      grid.image.style.css.bottom = 0
      grid.image.style.css.left = 0
      grid.image.style.css.right = 0
      if dflt_options.get('arrows', True):
        grid.next = self.page.ui.icon(dflt_options.get("arrows-right", "fas fa-chevron-right")).css(
          {"position": 'absolute', 'background': 'white', 'cursor': 'pointer', 'z-index': '1010',
           "font-size": '35px', "padding": '8px', "right": '10px', 'top': '50%'})
        grid.next.options.managed = False
        grid.previous = self.page.ui.icon(dflt_options.get("arrows-left", "fas fa-chevron-left")).css(
          {"position": 'absolute', 'background': 'white', 'cursor': 'pointer',  'z-index': '1010',
           "font-size": '35px', "padding": '8px', "left": '10px', 'top': '50%'})
        grid.previous.options.managed = False
        grid.next.click([
          grid.image.build(
            self.page.js.getElementById(grid.next.dom.getAttribute("value")).getAttribute("src")),
          grid.previous.dom.setAttribute("value", self.page.js.getElementById(
            grid.next.dom.getAttribute("value")).getAttribute("data-previous")),
          grid.next.dom.setAttribute("value", self.page.js.getElementById(
            grid.next.dom.getAttribute("value")).getAttribute("data-next"))
        ])

        grid.previous.click([
          grid.image.build(
            self.page.js.getElementById(grid.previous.dom.getAttribute("value")).getAttribute("src")),
          grid.next.dom.setAttribute("value", self.page.js.getElementById(
            grid.previous.dom.getAttribute("value")).getAttribute("data-next")),
          grid.previous.dom.setAttribute("value", self.page.js.getElementById(
            grid.previous.dom.getAttribute("value")).getAttribute("data-previous"))
        ])
        grid.popup = self.page.ui.layouts.popup([grid.previous, grid.image, grid.next])
      else:
        grid.popup = self.page.ui.layouts.popup([grid.image])

      if dflt_options.get("keyboard", True) and dflt_options.get('arrows', True):
        self.page.body.keyup.left([grid.previous.dom.events.trigger("click")])
        self.page.body.keyup.right([grid.next.dom.events.trigger("click")])

      grid.popup.options.top = 0
      for i, r in enumerate(grid.pictures):
        r.click([
          grid.next.dom.setAttribute("value", r.dom.getAttribute("data-next")),
          grid.previous.dom.setAttribute("value", r.dom.getAttribute("data-previous")),
          grid.image.build(r.dom.content),
          grid.popup.dom.show()])
    if len(row):
      for c in row:
        c.set_size(12 // columns)
      grid.add(row)
    return grid

  def carousel(self, images=None, path=None, selected=0, width=(100, "%"), height=(300, "px"), options=None,
               profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Attributes:
    ----------
    :param images: List. Optional. The list with the pictures.
    :param path: String. Optional. The path for the picture.
    :param selected: Integer. Optional. The selected index.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    dfl_options = {"extensions": ['jpg']}
    if options is not None:
      dfl_options.update(options)
    if path is not None and images is None:
      images = []
      for img in os.listdir(path):
        ext_img = img.split(".")[-1]
        if ext_img.lower() in dfl_options["extensions"]:
          images.append({"image": img, 'title': ''})
      if len(images) > 5:
        dfl_options.update({'points': False, "arrows": True, "keyboard": True})
    images = images or []
    c = self.page.ui.images.carousel(images, path, selected, width, height, dfl_options, profile)
    return c

  def pagination(self, count, selected=1, width=(100, '%'), height=(None, 'px'), html_code=None, options=None,
                 profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Attributes:
    ----------
    :param count: Integer. The pagination count of items.
    :param selected: Integer. Optional. The selected value.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    p = self.page.ui.navigation.indices(
      count, selected=selected, width=width, height=height, options=options, html_code=html_code, profile=profile)
    p.style.css.text_align = "center"
    return p

  def heroes(self, url, path=None, width=(100, "%"), height=(500, "px"), align="center", html_code=None, options=None,
             profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Related Pages:

      https://www.w3schools.com/cssref/pr_background-image.asp

    Attributes:
    ----------
    :param url: String. Optional. The picture url.
    :param path: String. Optional. The picture path.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. The text-align property within this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {}
    img = self.page.ui.div(
      width=width, height=height, align=align, html_code=html_code, options=options, profile=profile)
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

  def fixed(self, url, path=None, width=(100, "%"), height=(300, "px"), align="center", html_code=None, options=None,
            profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Attributes:
    ----------
    :param url: String. Optional. The url link.
    :param path: String. Optional.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. The text-align property within this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {}
    img = self.page.ui.div(
      width=width, height=height, align=align, html_code=html_code, options=options, profile=profile)
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

  def image(self, url, path=None, width=(100, "%"), height=(300, "px"), align="center", html_code=None, options=None,
            profile=None):
    """
    Description:
    ------------
    Set a background as an image.
    This is wrapping the image.background base component.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Attributes:
    ----------
    :param url: String. Optional. The url link.
    :param path: String. Optional. The picture path.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. The text-align property within this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    img = self.page.ui.images.img(
      url, path=path, width=width, height=height, align=align, options=options, html_code=html_code, profile=profile)
    return img

  def link(self, img, url="#", path=None, width=(100, "%"), height=(None, "px"), align="center", options=None,
           html_code=None, profile=None):
    """
    Description:
    ------------
    Set a background as an image.
    This is wrapping the image.background base component.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Attributes:
    ----------
    :param img:
    :param url: String. Optional. The url link.
    :param path: String. Optional. The picture path.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. The text-align property within this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    img = self.page.ui.images.img(
      img, path=path, width=width, height=height, align=align, html_code=html_code, options=options, profile=profile)
    img.style.effects.reduce()
    img.style.css.cursor = "pointer"
    img.goto(url)
    return img

  def overlay(self, img, text=None, path=None, width=(100, "%"), height=(None, "px"), align="center", options=None,
              profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Related Pages:

      https://www.w3schools.com/howto/howto_css_image_overlay_slide.asp

    Attributes:
    ----------
    :param img:
    :param text: String. Optional. The content.
    :param path: String. Optional. The picture path.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. The text-align property within this component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {}
    container = self.page.ui.div(width=width, height=height, align=align, options=options, profile=profile)
    container.style.css.position = "relative"
    container.style.css.box_sizing = "border-box"
    container.img = self.page.ui.images.img(
      img, path=path, width=(100, "%"), height=(None, "px"), align="center", options=options, profile=profile)
    container.img.style.css.display = "block"
    container.img.style.css.width = "100%"
    container.add(container.img)
    container.attr['class'].clear()
    container.attr['class'].add("container_overlay")
    container.overlay = self.page.ui.div(
      width=width, height=height, align=align, options=options, profile=profile)
    if text is not None:
      if hasattr(text, 'options'):
        container.text = text
      else:
        container.text = self.page.ui.div(
          text, width=(100, "%"), height=height, align=align, options=options, profile=profile)
      if options.get("direction") is None:
        container.overlay.attr['class'].clear()
        container.overlay.attr['class'].add("test_overlay_title")
        container.overlay.style.css.opacity = 0
        container.overlay.style.css.position = "absolute"
        container.overlay.style.css.bottom = 0
        container.overlay.style.css.color = self.page.theme.greys[0]
        container.overlay.style.css.background = "rgba(0, 0, 0, 0.5)"
        self.page.css.customText(".container_overlay:hover .test_overlay_title {opacity: 1 !IMPORTANT;}")
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
        container.overlay.style.css.color = self.page.theme.greys[0]
        container.overlay.style.css.background = "rgba(0, 0, 0, 0.5)"
        self.page.css.customText(".container_overlay:hover .test_overlay_top {height: 100% !IMPORTANT;}")
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
        container.overlay.style.css.color = self.page.theme.greys[0]
        container.overlay.style.css.background = "rgba(0, 0, 0, 0.5)"
        self.page.css.customText(
          ".container_overlay:hover .test_overlay_bottom {height: 100% !IMPORTANT; bottom: 0 !IMPORTANT}")
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
        container.overlay.style.css.color = self.page.theme.greys[0]
        container.overlay.style.css.background = "rgba(0, 0, 0, 0.5)"
        self.page.css.customText(
          ".container_overlay:hover .test_overlay_right {width: 100% !IMPORTANT; left: 0 !IMPORTANT}")
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
        container.overlay.style.css.color = self.page.theme.greys[0]
        container.overlay.style.css.background = "rgba(0, 0, 0, 0.5)"
        self.page.css.customText(
          ".container_overlay:hover .test_overlay_left {width: 100% !IMPORTANT; right: 0 !IMPORTANT}")
      container.style.css.cursor = 'pointer'
      container.overlay.add(container.text)
    container.add(container.overlay)
    return container

  def wallpaper(self, url, width=(100, "%"), height=(300, "px"), size="cover", margin=0, align="center",
                position="middle", options=None, profile=False):
    """
    Description:
    ------------
    Set a background as an image.
    This is wrapping the image.background base component.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Attributes:
    ----------
    :param url: String. Optional. The url link.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param size:
    :param margin:
    :param align: String. The text-align property within this component.
    :param position: String. Optional. The position compared to the main component tag.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    background = self.page.ui.images.wallpaper(
      url, width=width, height=height, size=size, margin=margin, align=align, position=position, options=options,
      profile=profile)
    return background

  def animated(self, image=None, text="", title="", url=None, path=None, width=(200, "px"), height=(200, "px"),
               html_code=None, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Attributes:
    ----------
    :param image: String. Optional.
    :param text: String. Optional. The value to be displayed to the component.
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param url: String. Optional. The url link.
    :param path: String. Optional. The picture path.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    a = self.page.ui.images.animated(
      image, text=text, title=title, url=url, path=path, width=width, height=height, html_code=html_code,
      options=options, profile=profile)
    return a

  def folders(self, path, columns=6, images=None, position="top", width=(None, '%'), height=('auto', ''), options=None,
              profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Attributes:
    ----------
    :param path: String. Optional. The picture path.
    :param columns:
    :param images:
    :param position:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    dflt_options = {"extensions": ['jpg']}
    if options is not None:
      dflt_options.update(options)
    grid = self.page.ui.grid(width=width, height=height, options=dflt_options, profile=profile)
    pictures = []
    for f in os.listdir(path):
      folder_path = os.path.join(path, f)
      if not os.path.isfile(folder_path):
        for i in os.listdir(folder_path):
          ext_img = i.split(".")[-1]
          if ext_img.lower() in dflt_options["extensions"]:
            pictures.append({"name": self.page.py.encode_html(i),
                             'path': self.page.py.encode_html(folder_path),
                             'title': self.page.py.encode_html(f)})
            if images is not None and f in images:
              pictures[-1].update(images[f])
            break
    grid.pictures = []
    row = self.page.ui.row(position=position)
    viewer = self.page.ui.img(
      pictures[0]["name"], path=pictures[0]["path"], width=(100, '%'), height=('auto', ''))
    viewer.style.css.border = "1px solid %s" % self.page.theme.greys[7]
    for i, picture in enumerate(pictures):
      if i % columns == 0:
        grid.add(row)
        row = self.page.ui.row(position=position)
      pic = self.page.ui.img(picture["name"], path=picture["path"])
      pic.style.css.cursor = "pointer"
      pic.click([
        viewer.build(pic.dom.content)
      ])
      pic.tooltip(picture["title"])
      pic.style.css.max_height = 200
      pic.style.css.margin = 5
      pic.style.css.z_index = 0
      grid.pictures.append(pic)
      row.add(pic)
      pic.parent = row[-1]

    grid.style.css.margin_top = 20
    grid.style.css.overflow = 'hidden'
    grid.style.css.margin_bottom = 20
    if len(row):
      for c in row:
        c.set_size(12 // columns)
      grid.add(row)

    if len(grid.pictures) > 4 * columns:
      grid.style.css.height = 300
      text = self.page.ui.text("See more", align="right")
      text.click([
        grid.dom.css({"height": 'auto'}),
        text.dom.css({"display": 'none'}),
      ])
      col = self.page.ui.div([grid, text])
      col.options.managed = False
      viewer.style.css.margin_top = 25
      container = self.page.ui.row([col, viewer], position="top")
    else:
      container = self.page.ui.row([grid, viewer])
    container.style.css.display = "flex"
    container.style.css.align_items = "flex-start"
    container.options.autoSize = False
    container[1].style.css.top = 30
    container[1].style.css.position = 'sticky'

    container[0].attr['class'].add("col-8")
    container[1].attr['class'].add("col-4")
    return container

  def list(self, path, urls=None, width=('auto', ''), height=('auto', ''), options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Attributes:
    ----------
    :param path: String. Optional. The picture path.
    :param urls: Dictionary. Optional.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    rows = []
    for f in os.listdir(path):
      folder_path = os.path.join(path, f)
      if not os.path.isfile(folder_path):
        div = self.page.ui.div(self.page.py.encode_html(f))
        div.style.css.padding = "5px 0 0 10px"
        div.style.add_classes.div.color_hover()
        if urls is not None and f in urls:
          url = urls[f]
        else:
          url = "%s.html" % Html.cleanData(f)
        div.click([self.page.js.navigateTo(url)])
        hr = self.page.ui.layouts.hr(background_color=self.page.theme.greys[3])
        hr.style.css.margin = "0 5px"
        hr.style.css.width = "calc(100% - 10px)"
        rows.append(self.page.ui.col([div, hr]))
    return self.page.ui.list(rows, width=width, height=height, options=options, profile=profile)

  def icons(self, icons=None, columns=6, width=(None, '%'), height=('auto', ''), options=None, profile=None):
    """
    Description:
    ------------
    Mosaic of pictures.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Attributes:
    ----------
    :param icons: List. Optional. The list with the pictures.
    :param columns: Integer. Optional. The number of column for the mosaic component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    dflt_options = {}
    if options is not None:
      dflt_options.update(options)
    grid = self.page.ui.grid(width=width, height=height, options=dflt_options, profile=profile)
    grid.style.css.margin_top = 20
    grid.style.css.overflow = 'hidden'
    grid.style.css.margin_bottom = 20
    row = self.page.ui.row(options=dflt_options)
    grid.icons = []
    grid.texts = {}
    for i, icon in enumerate(icons):
      if dflt_options.get("max") is not None and len(grid.icons) > dflt_options.get("max"):
        break

      if i % columns == 0:
        grid.add(row)
        row = self.page.ui.row(options=dflt_options)
      text = None
      if not hasattr(icon, 'options'):
        if isinstance(icon, dict):
          if 'html_code' not in icon:
            icon["html_code"] = "%s_%s" % (grid.htmlCode, i)
          if 'align' not in icon:
            icon['align'] = "center"
          if "text" in icon:
            text = self.page.ui.text(icon["text"], options=dflt_options)
            text.style.css.bold()
            text.style.css.white_space = "nowrap"
            grid.texts[i] = text
            del icon["text"]

          icon = self.page.ui.icon(**icon)
        else:
          icon = self.page.ui.icon(icon, html_code="%s_%s" % (grid.htmlCode, i), align="center")
        icon.style.css.font_factor(15)
        icon.style.css.text_align = "center"
        grid.icons.append(icon)
      if text is not None:
        text.style.css.display = "inline-block"
        text.style.css.width = "100%"
        text.style.css.text_align = "center"
        row.add(self.page.ui.col([icon, text], align="center", options=dflt_options))
      else:
        row.add(icon)
      row.attr["class"].add("mt-3")
      icon.parent = row[-1]
    if len(row):
      for i in range(columns - len(row)):
        row.add(self.page.ui.text("&nbsp;"))
      row.attr["class"].add("mt-3")
      grid.add(row)
    grid.style.css.color = self.page.theme.greys[6]
    grid.style.css.padding_top = 5
    grid.style.css.padding_bottom = 5
    return grid

  def images(self, images=None, columns=6, width=(None, '%'), height=('auto', ''), options=None, profile=None):
    """
    Description:
    ------------
    Mosaic of pictures.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Attributes:
    ----------
    :param images: List. Optional. The list with the pictures.
    :param columns: Integer. Optional. The number of column for the mosaic component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    dflt_options = {}
    if options is not None:
      dflt_options.update(options)
    grid = self.page.ui.grid(width=width, height=height, options=dflt_options, profile=profile)
    grid.style.css.margin_top = 20
    grid.style.css.overflow = 'hidden'
    grid.style.css.margin_bottom = 20
    row = self.page.ui.row(options=dflt_options)
    grid.images = []
    grid.texts = {}
    for i, image in enumerate(images):
      if dflt_options.get("max") is not None and len(grid.images) > dflt_options.get("max"):
        break

      if i % columns == 0:
        grid.add(row)
        row = self.page.ui.row(options=dflt_options)
      text = None
      if not hasattr(image, 'options'):
        if isinstance(image, dict):
          if 'htmlCode' not in image:
            image["htmlCode"] = "%s_%s" % (grid.htmlCode, i)
          if 'align' not in image:
            image['align'] = "center"
          if "text" in image:
            text = self.page.ui.text(image["text"], options=dflt_options)
            text.style.css.bold()
            text.style.css.white_space = "nowrap"
            grid.texts[i] = text
            del image["text"]

          image = self.page.ui.img(**image)
        else:
          image = self.page.ui.img(image, html_code="%s_%s" % (grid.htmlCode, i), align="center")
        image.style.css.font_factor(15)
        image.style.add_classes.div.border_hover()
        image.style.css.text_align = "center"
        grid.images.append(image)
      if text is not None:
        text.style.css.display = "inline-block"
        text.style.css.width = "100%"
        text.style.css.text_align = "center"
        row.add(self.page.ui.col([image, text], align="center", options=dflt_options))
      else:
        row.add(image)
      row.attr["class"].add("mt-3")
      for r in row:
        r.attr["class"].add("px-1")
      image.parent = row[-1]
    if len(row):
      for i in range(columns - len(row)):
        row.add(self.page.ui.text("&nbsp;"))
      for r in row:
        r.attr["class"].add("px-1")
      row.attr["class"].add("mt-3")
      grid.add(row)
    grid.style.css.color = self.page.theme.greys[6]
    return grid
