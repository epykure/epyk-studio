#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from epyk.core.css import Defaults as Defaults_css
from epyk.core.css.themes import ThemeBlue
from epyk_studio.lang import get_lang


class Shopping(object):
  def __init__(self, context):
    self.context = context

  def theme(self):
    self.context.rptObj.theme = ThemeBlue.Blue()

  def button(self, text="", icon=None, width=(None, "%"), height=(None, "px"), align="left", htmlCode=None, tooltip=None, profile=None, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param icon: String. Optional. The component icon content from font-awesome references
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param align: String. Optional. A string with the horizontal position of the component
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: String. Optional. A string with the value of the tooltip
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    button = self.context.rptObj.ui.button(text, icon, width=width, height=height, options=options, tooltip=tooltip, profile=profile, align=align)
    button.style.clear()
    button.style.css.padding = "0 10px"
    button.style.css.border = "1px solid %s" % self.context.rptObj.theme.greys[-1]
    button.style.css.border_radius = 5
    button.style.css.background = self.context.rptObj.theme.greys[0]
    button.style.hover({"color": self.context.rptObj.theme.success[1]})
    return button

  def product(self, content, price, image, rating=None, title=None, align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param content:
    :param price:
    :param image:
    :param rating:
    :param title:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    if title is not None:
      if not hasattr(title, 'options'):
        title = self.context.rptObj.ui.titles.title(title)
        title.style.css.display = "block"
    if not hasattr(image, 'options'):
      split_url = os.path.split(image)
      div.image = self.context.rptObj.ui.img(split_url[1], path=split_url[0])
      div.image.style.css.margin_bottom = 10
      div.add(div.image)
    if not hasattr(content, 'options'):
      content = self.context.rptObj.ui.text(content)
      content.style.css.display = "block"
    div.add(content)
    if rating is not None:
      if not hasattr(rating, 'options'):
        div.ratings = self.context.rptObj.ui.rich.stars(rating)
        div.add(div.ratings)
    if not hasattr(price, 'options'):
      div.price = self.price(price)
      div.add(div.price)
    return div

  def price(self, price, currency="€", align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param price:
    :param currency:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    options = options or {}
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    if options.get("deleted", False):
      div.price = self.context.rptObj.ui.tags.delete(self.context.rptObj.py.encode_html("%s%s" % (price, currency)), options={"type_number": 'number'}, width=(None, "px"))
    else:
      if not hasattr(price, 'options'):
        split_price = str(price).split(".")
        if len(split_price) > 1:
          div.price = self.context.rptObj.ui.texts.number(split_price[0], options={"type_number": 'number'}, width=(None, "px"))
          div.price.style.css.font_size = Defaults_css.font(options.get("font_factor", 10))
          price_with_dec = self.context.rptObj.ui.tags.sup("%s%s" % (self.context.rptObj.py.encode_html(currency), split_price[1]), width=(None, "px"))
          price_with_dec.style.css.font_size = Defaults_css.font(options.get("font_factor", 10)/2)
        else:
          div.price = self.context.rptObj.ui.texts.number(split_price[0], options={"type_number": 'number'}, width=(None, "px"))
          div.price.style.css.font_size = Defaults_css.font(options.get("font_factor", 10))
          price_with_dec = self.context.rptObj.ui.tags.sup("%s00" % self.context.rptObj.py.encode_html(currency), width=(None, "px"))
          price_with_dec.style.css.font_size = Defaults_css.font(options.get("font_factor", 10)/2)
        div.add(self.context.rptObj.ui.div([div.price, price_with_dec], align=align))
        div.style.css.color = self.context.rptObj.theme.colors[5]
      else:
        div.price = price
        div.add(div.price)
    return div

  def price_from(self, price, text="from", currency="€", align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param price:
    :param text:
    :param currency:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    div.label = self.context.rptObj.ui.text(text)
    div.label.style.css.display = 'block'
    div.label.style.css.margin_bottom = '-10px'
    div.add(div.label)
    if not hasattr(price, 'options'):
      split_price = str(price).split(".")
      if len(split_price) > 1:
        div.price = self.context.rptObj.ui.texts.number(split_price[0], options={"type_number": 'number'}, width=(None, "px"))
        div.price.style.css.font_size = Defaults_css.font(10)
        price_with_dec = self.context.rptObj.ui.tags.sup("%s%s" % (self.context.rptObj.py.encode_html(currency), split_price[1]), width=(None, "px"))
        price_with_dec.style.css.font_size = Defaults_css.font(4)
      else:
        div.price = self.context.rptObj.ui.texts.number(split_price[0], options={"type_number": 'number'}, width=(None, "px"))
        div.price.style.css.font_size = Defaults_css.font(10)
        price_with_dec = self.context.rptObj.ui.tags.sup("%s00" % self.context.rptObj.py.encode_html(currency), width=(None, "px"))
        price_with_dec.style.css.font_size = Defaults_css.font(4)
      div.add(self.context.rptObj.ui.div([div.price, price_with_dec]))
    else:
      div.price = price
      div.add(div.price)
    return div

  def price_discount(self, price, discount, align="left", width=(120, 'px'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param price:
    :param discount:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    prev_price = self.price(price, width=("auto", ""), options={"font_factor": 2, "deleted": True})
    prev_price.style.css.font_factor(-5)
    prev_price.style.css.color = self.context.rptObj.theme.greys[4]
    new_price = self.price("%.2f" % (price - (price * discount) / 100), width=("auto", ""))
    discount = self.discount(discount)
    div.prev_price = prev_price
    div.price = new_price
    div.discount = discount
    prices = self.context.rptObj.ui.div([prev_price, new_price], width=("auto", ""))
    prices.style.css.display = "inline-block"
    div.add(prices)
    discount.style.css.float = "right"
    div.add(discount)
    return div

  def description(self, text, url, height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------
    Wrapped link component

    Attributes:
    ----------
    :param text: String. The visible text.
    :param url: String. The link URL when click on the link
    :param height: Tuple. The component height
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    html_link = self.context.rptObj.ui.link(text, url, height=height, options=options, profile=profile)
    html_link.style.css.color = self.context.rptObj.theme.greys[-1]
    return html_link

  def order(self, quantity, align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param quantity:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    div.plus = self.context.rptObj.ui.icon("fa fa-plus")
    div.minus = self.context.rptObj.ui.icon("fa fa-minus")
    div.plus.style.css.margin = "0 5px"
    div.minus.style.css.margin = "0 5px"
    div.input = self.context.rptObj.ui.inputs.d_text(quantity, width=(20, "px"))
    div.input.style.css.border_radius = "20px"
    div.input.readonly()
    div.add(div.minus)
    div.add(div.input)
    div.add(div.plus)
    div.minus.click([div.input.build(div.input.dom.content.number.add(-1).max(0))])
    div.plus.click([div.input.build(div.input.dom.content.number.add(1))])
    return div

  def discount(self, percent, align="left", width=('auto', ''), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------
    Add a discount tag to a component

    Attributes:
    ----------
    :param percent:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    comp_discount = self.context.rptObj.ui.text("-%s%%" % percent, align=align, width=width, height=height, options=options, profile=profile)
    comp_discount.style.css.background_color = self.context.rptObj.theme.danger[1]
    comp_discount.style.css.color = "white"
    comp_discount.style.css.min_width = "30px"
    comp_discount.style.css.bold()
    comp_discount.style.css.padding = "7px 5px"
    comp_discount.style.css.margin = "5px"
    comp_discount.style.css.border_radius = "50%"
    return comp_discount

  def rating(self, rating, customers, url=None, align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------
    Add rating component for customers review

    :tags: Review, Comment
    :categories: studio

    Usage::

      page.studio.shop.rating(2, 85, "")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlOthers.Stars`
      - :class:`epyk.core.html.HtmlLinks.ExternalLink`

    Templates:

      shop.py

    Attributes:
    ----------
    :param rating:
    :param customers:
    :param url:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    options = options or {}
    container = self.context.rptObj.ui.div([])
    container.stars = self.context.rptObj.ui.rich.stars(rating, best=options.get("stars", 5))
    container.stars.style.display = "inline-block"
    container.stars.style.margin_right = 5
    container.link = self.context.rptObj.ui.link("(%s)" % customers, url)
    container.add(container.stars)
    container.add(container.link)
    return container

  def tags(self, tags, align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param tags: List.
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    container = self.context.rptObj.ui.div([], align=align, width=width, height=height, options=options, profile=profile)
    for tag in tags:
      if not hasattr(tag, 'options'):
        comp_tag = self.context.rptObj.ui.text(tag)
      else:
        comp_tag = tag
      comp_tag.style.css.background = self.context.rptObj.theme.colors[4]
      comp_tag.style.css.color = "white"
      comp_tag.style.css.margin = "0 3px"
      comp_tag.style.css.padding = "1px 5px"
      comp_tag.style.css.border_radius = "20px"
      container.add(comp_tag)
    return container

  def label(self, component, name, align="center", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param component:
    :param name:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    label = self.context.rptObj.ui.text(name)
    label.style.css.background = self.context.rptObj.theme.colors[-1]
    label.style.css.color = self.context.rptObj.theme.greys[0]
    label.style.css.padding = "0 10px"
    label.style.css.border_radius = "0 0 20px 0"
    container = self.context.rptObj.ui.div([label, self.context.rptObj.ui.div(component, align=align).css({'margin': '5px'})],
                align="left", width=width, height=height, options=options, profile=profile)
    container.style.css.border = "1px solid %s" % self.context.rptObj.theme.colors[-1]
    container.label = label
    return container

  def quality(self, votes, url=None, align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------
    Return a skillbar chart for the customer review ratings

    Attributes:
    ----------
    :param votes: Dictionary. Number of customer review per rating
    :param url: String. Url template for product link to those customer rating comments
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    vote_records = []
    dflt_options = {"unit": '%', "values": True, "background": self.context.rptObj.theme.colors[6], 'borders': True}
    if options is not None:
      dflt_options.update(options)
    customers = sum([k for k in votes.values()])
    for i in reversed(range(dflt_options.get("stars", 5))):
      if url is not None:
        vote_records.append({"star": self.context.rptObj.ui.link("%s stars" % i, url % i), "value":  votes.get(i, 0) / customers * 100})
      else:
        vote_records.append({"star": "%s stars" % i, "value":  votes.get(i, 0) / customers * 100})
    comp = self.context.rptObj.ui.charts.skillbars(vote_records, y_column='value', x_axis='star', options=dflt_options).css({"width": "%s%s" % (width[0], width[1])})
    return comp

  def question(self, question, answers=None, url=None, align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param question:
    :param answers:
    :param url:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    table = self.context.rptObj.ui.layouts.table(options={"header": False})
    if url is not None:
      link = self.context.rptObj.ui.link(question, url)
      link.style.css.color = self.context.rptObj.theme.colors[6]
      table += ["Question: ", link]
    else:
      table += ["Question: ", question]
    table[-1][0].style.css.min_width = 100
    table[-1][0].style.css.bold()
    table[-1][1].style.css.width = "100%"
    table[-1][1].style.css.text_align = "left"
    table += ["Answers: ", "".join(answers or [])]
    table[-1][0].style.css.min_width = 100
    table[-1][0].style.css.bold()
    return table

  def review(self, rating, title, comment, author, date, align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    pass

  def album(self, pictures, selected=0, align="left", width=(500, 'px'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param pictures:
    :param selected:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    container = self.context.rptObj.ui.div([], align=align, width=width, height=height, options=options, profile=profile)
    left_panel = self.context.rptObj.ui.div([], align=align, width=(50, 'px'), height=(100, "%"), options=options, profile=profile)
    left_panel.style.css.display = "inline-block"
    left_panel.style.css.vertical_align = "top"
    right_panel = self.context.rptObj.ui.div([], align=align, width=("calc(100% - 60px)", ''), height=height, options=options, profile=profile)
    right_panel.style.css.display = "inline-block"
    right_panel.style.css.padding = 5
    img_selected = self.context.rptObj.ui.img(pictures[selected])
    img_selected.style.css.float = "right"
    right_panel.add(img_selected)

    for i, pic in enumerate(pictures):
      if isinstance(pic, dict):
        picture = pic['min']
        full_picture = pic['max']
      else:
        picture = pic
        full_picture = pic
      img = self.context.rptObj.ui.img(picture, width=(40, "px"))
      img.style.css.border = "1px solid %s" % self.context.rptObj.theme.greys[-1]
      img.style.css.margin = "5px 10px"
      img.style.css.cursor = "pointer"
      img.style.hover({"border": "1px solid red"})
      img.click([img_selected.dom.src(full_picture)])
      left_panel.add(img)
    container.add(self.context.rptObj.ui.div([left_panel, right_panel]))
    return container

  def availability(self, flag, comment=None, align="left", width=('auto', ''), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param flag:
    :param comment:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    comp_availability = self.context.rptObj.ui.text("In Stock", align=align, width=width, height=height, options=options, profile=profile)
    if flag:
      comp_availability.style.css.color = self.context.rptObj.theme.success[1]
      comp_availability.style.css.bold()
      comp_availability._vals = comment or "In Stock"
    else:
      comp_availability.style.css.color = self.context.rptObj.theme.danger[1]
      comp_availability.style.css.bold()
      comp_availability._vals = comment or "Not Available"
    return comp_availability

  def vote(self, number, align="center", width=('auto', ''), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param number:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    container = self.context.rptObj.ui.div([], align=align, width=width, height=height, options=options,
                                                  profile=profile)
    container.up = self.context.rptObj.ui.icons.awesome("fas fa-caret-up")
    container.up.style.css.display = 'block'
    container.up.style.css.margin = '0 auto'
    container.add(container.up)
    container.text = self.context.rptObj.ui.texts.number(number, width=width, options=options)
    container.text.style.css.font_factor(10)
    container.add(container.text)
    container.down = self.context.rptObj.ui.icons.awesome("fas fa-caret-down")
    container.down.style.css.display = 'block'
    container.down.style.css.margin = '0 auto'
    container.add(container.down)
    return container

  def bar(self, title, price, description=None, url=None, width=(None, ''), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param title:
    :param price:
    :param description:
    :param url:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    options = options or {}
    container = self.context.rptObj.ui.div([], align='left', width=width, height=height, options=options,
                                           profile=profile)
    if not hasattr(title, 'options'):
      container.title = self.context.rptObj.ui.titles.title(title)
      container.title.style.css.display = "inline-block"
      container.title.style.css.margin_top = 0
      container.title.style.css.font_weight = 'bold'
      container.title.style.css.font_size = Defaults_css.font(5)
    else:
      container.title = title
    if url is not None:
      container.style.css.cursor = "pointer"
      container.click([self.context.rptObj.js.navigateTo(url)])
    container.add(container.title)
    if not hasattr(price, 'options'):
      if not "font_factor" in options:
        options["font_factor"] = 5
      container.price = self.price(price, align='right', width=(None, 'px'), options=options)
      container.price.style.css.position = "relative"
      container.price.style.css.font_weight = 'bold'
      container.price.style.css.margin_top = -25
      container.price.style.css.right = 0
    else:
      container.price = price
    container.add(container.price)
    if description is not None:
      if not hasattr(description, 'options'):
        container.description = self.context.rptObj.ui.text(description)
        container.description.style.css.margin_bottom = 5
        container.description.style.css.margin_top = 0
      else:
        container.description = description
      container.add(container.description)
    return container

  def item(self, title, image, location="", limit="", date='N/A', tags=None, price=None, details=None, align="center",
           width=(200, 'px'), height=(None, "px"), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param title:
    :param image:
    :param location:
    :param limit:
    :param date:
    :param tags:
    :param price:
    :param details:
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    ool = self.context.rptObj.ui.col(profile=profile)
    ool.add(self.context.rptObj.studio.shop.bar(title, price, details, profile=profile))
    if location:
      ool.add(self.context.rptObj.ui.div([self.context.rptObj.ui.icon("fas fa-map-marker-alt", profile=profile).css({"margin-right": '10px'}), self.context.rptObj.ui.text(location)]))
    if limit:
      ool.add(self.context.rptObj.ui.div([self.context.rptObj.ui.icon("fas fa-male", profile=profile).css({"margin-right": '15px'}), self.context.rptObj.ui.text(limit)]))
    if tags:
      ool.add(self.context.rptObj.studio.tags(tags, profile=profile))
    ool.add(self.context.rptObj.ui.text("Prochaine session", profile=profile).css({"display": 'block', "margin-top": '5px', "color": self.context.rptObj.theme.greys[6]}))
    ool.add(self.context.rptObj.ui.text(date, profile=profile).css({"display": 'block', 'font-weight': 'bold'}))
    ool.add(self.context.rptObj.ui.button("Book this item", align="center", profile=profile).css({"margin": '15px auto 5px'}))
    vim = self.context.rptObj.ui.vignets.image(content=ool, align=align, width=width, height=height, options=options, render='col')
    # vim.image.style.css.border_radius = "20px 20px 0 0 "
    vim.style.css.shadow_box()
    vim.style.css.padding_top = 160
    vim.style.css.background_url(image, size="100% 150px", background_position="top")
    vim.style.css.margin_top = 10
    return vim


class Resto(Shopping):

  def compostion(self, text, weight, percentage, background=None, width=(80, 'px'), height=(120, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param weight:
    :param percentage:
    :param background:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    container = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile)
    container.style.css.display = "inline-block"
    container.title = self.context.rptObj.ui.text(text, align="center")
    container.title.style.css.font_factor(-3)
    container.style.css.position = "relative"
    container.add(container.title)
    container.weight = self.context.rptObj.ui.text("%s %s" % (weight[0], weight[1]), align="center")
    container.weight.style.css.font_factor(8)
    container.weight.style.css.bold()
    container.weight.style.css.padding_top = 10
    container.add(container.weight)
    if background is None:
      if percentage < 10:
        container.style.css.background = self.context.rptObj.theme.success[0]
      elif percentage < 50:
        container.style.css.background = self.context.rptObj.theme.warning[0]
      else:
        container.style.css.background = self.context.rptObj.theme.danger[0]
    container.style.css.border_radius = 25
    container.style.css.padding_top = 10
    container.percentage = self.context.rptObj.ui.div("%s%%" % percentage, width=(50, 'px'))
    container.percentage.style.css.position = "absolute"
    container.percentage.style.css.text_align = "center"
    container.percentage.style.css.bottom = 0
    container.percentage.style.css.margin_left = 15
    container.percentage.style.css.border_radius = "20px 20px 0 0"
    container.add(container.percentage)
    container.percentage.style.css.background = "white"
    return container

