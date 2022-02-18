#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from epyk.core.css.themes import ThemeBlue
from epyk_studio.lang import get_lang


class Shopping:

  def __init__(self, ui):
    self.page = ui.page

  def theme(self):
    self.page.theme = ThemeBlue.Blue()

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
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    button = self.page.ui.button(
      text, icon, width=width, height=height, options=options, tooltip=tooltip, html_code=html_code, profile=profile,
      align=align)
    button.style.clear()
    button.style.css.padding = "0 10px"
    button.style.css.border = "1px solid %s" % self.page.theme.greys[-1]
    button.style.css.border_radius = 5
    button.style.css.background = self.page.theme.greys[0]
    button.style.hover({"color": self.page.theme.success[1]})
    return button

  def product(self, content, price, image, rating=None, title=None, align="left", width=(300, 'px'),
              height=("auto", ''), options=None, profile=None):
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
    :param content: String. The item description.
    :param price: Number. The item price.
    :param image: String. The image path.
    :param rating: Integer. Optional. The number of stars.
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    if title is not None:
      if not hasattr(title, 'options'):
        title = self.page.ui.titles.title(title, profile=profile)
        title.style.css.display = "block"
    if not hasattr(image, 'options'):
      split_url = os.path.split(image)
      div.image = self.page.ui.img(split_url[1], path=split_url[0])
      div.image.style.css.margin_bottom = 10
      div.add(div.image)
    if not hasattr(content, 'options'):
      content = self.page.ui.text(content, profile=profile)
      content.style.css.display = "block"
    div.add(content)
    if rating is not None:
      if not hasattr(rating, 'options'):
        div.ratings = self.page.ui.rich.stars(rating, profile=profile)
        div.add(div.ratings)
    if not hasattr(price, 'options'):
      div.price = self.price(price, profile=profile)
      div.add(div.price)
    return div

  def price(self, price, currency="€", align="left", width=(300, 'px'), height=("auto", ''), options=None,
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
    :param price: Number. The item price.
    :param currency: String. Optional. The currency reference.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {}
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    if options.get("deleted", False):
      div.price = self.page.ui.tags.delete(
        self.page.py.encode_html("%s%s" % (price, currency)), options={"type_number": 'number'}, width=(None, "px"),
        profile=profile,)
    else:
      if not hasattr(price, 'options'):
        split_price = str(price).split(".")
        if len(split_price) > 1:
          div.price = self.page.ui.texts.number(
            split_price[0], options={"type_number": 'number'}, width=(None, "px"), profile=profile)
          div.price.style.css.font_size = self.page.body.style.globals.font.normal(options.get("font_factor", 10))
          price_with_dec = self.page.ui.tags.sup(
            "%s%s" % (self.page.py.encode_html(currency), split_price[1]), width=(None, "px"), profile=profile)
          price_with_dec.style.css.font_size = self.page.body.style.globals.font.normal(options.get("font_factor", 10)/2)
        else:
          div.price = self.page.ui.texts.number(
            split_price[0], options={"type_number": 'number'}, width=(None, "px"), profile=profile)
          div.price.style.css.font_size = self.page.body.style.globals.font.normal(options.get("font_factor", 10))
          price_with_dec = self.page.ui.tags.sup(
            "%s00" % self.page.py.encode_html(currency), width=(None, "px"), profile=profile)
          price_with_dec.style.css.font_size = self.page.body.style.globals.font.normal(options.get("font_factor", 10)/2)
        div.add(self.page.ui.div([div.price, price_with_dec], align=align, profile=profile))
        div.style.css.color = self.page.theme.notch()
      else:
        div.price = price
        div.add(div.price)
    return div

  def price_from(self, price, text="from", currency="€", align="left", width=(300, 'px'), height=("auto", ''),
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
    :param price: Number. The item price.
    :param text: String. Optional. The value to be displayed to the component.
    :param currency: String. Optional. The currency reference.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    div.label = self.page.ui.text(text, profile=profile)
    div.label.style.css.display = 'block'
    div.label.style.css.margin_bottom = '-10px'
    div.add(div.label)
    if not hasattr(price, 'options'):
      split_price = str(price).split(".")
      if len(split_price) > 1:
        div.price = self.page.ui.texts.number(
          split_price[0], options={"type_number": 'number'}, width=(None, "px"), profile=profile)
        div.price.style.css.font_size = self.page.body.style.globals.font.normal(10)
        price_with_dec = self.page.ui.tags.sup(
          "%s%s" % (self.page.py.encode_html(currency), split_price[1]), width=(None, "px"), profile=profile)
        price_with_dec.style.css.font_size = self.page.body.style.globals.font.normal(4)
      else:
        div.price = self.page.ui.texts.number(
          split_price[0], options={"type_number": 'number'}, width=(None, "px"), profile=profile)
        div.price.style.css.font_size = self.page.body.style.globals.font.normal(10)
        price_with_dec = self.page.ui.tags.sup(
          "%s00" % self.page.py.encode_html(currency), width=(None, "px"), profile=profile)
        price_with_dec.style.css.font_size = self.page.body.style.globals.font.normal(4)
      div.add(self.page.ui.div([div.price, price_with_dec], profile=profile,))
    else:
      div.price = price
      div.add(div.price)
    return div

  def price_discount(self, price, discount, align="left", width=(120, 'px'), height=("auto", ''), options=None,
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
    :param price: Number. The item price.
    :param discount: Number. The discount value.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    prev_price = self.price(price, width=("auto", ""), options={"font_factor": 2, "deleted": True}, profile=profile)
    prev_price.style.css.font_factor(-5)
    prev_price.style.css.color = self.page.theme.greys[4]
    new_price = self.price("%.2f" % (price - (price * discount) / 100), width=("auto", ""), profile=profile)
    discount = self.discount(discount, profile=profile)
    div.prev_price = prev_price
    div.price = new_price
    div.discount = discount
    prices = self.page.ui.div([prev_price, new_price], width=("auto", ""), profile=profile)
    prices.style.css.display = "inline-block"
    div.add(prices)
    discount.style.css.float = "right"
    div.add(discount)
    return div

  def description(self, text, url, height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------
    Wrapped link component.

    :tags:
    :categories:

    Usage:
    -----

    Attributes:
    ----------
    :param text: String. The visible text.
    :param url: String. The link URL when click on the link.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    html_link = self.page.ui.link(text, url, height=height, options=options, profile=profile)
    html_link.style.css.color = self.page.theme.greys[-1]
    return html_link

  def order(self, quantity, align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
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
    :param quantity: Number. The quantity value.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    div.plus = self.page.ui.icon("fa fa-plus", profile=profile)
    div.minus = self.page.ui.icon("fa fa-minus", profile=profile)
    div.plus.style.css.margin = "0 5px"
    div.minus.style.css.margin = "0 5px"
    div.input = self.page.ui.inputs.d_text(quantity, width=(20, "px"), profile=profile)
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
    Add a discount tag to a component.

    :tags:
    :categories:

    Usage:
    -----

    Templates:

    Related Pages:

    Attributes:
    ----------
    :param percent: Number. Optional. The percentage value.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    comp_discount = self.page.ui.text(
      "-%s%%" % percent, align=align, width=width, height=height, options=options, profile=profile)
    comp_discount.style.css.background_color = self.page.theme.danger[1]
    comp_discount.style.css.color = "white"
    comp_discount.style.css.min_width = "30px"
    comp_discount.style.css.bold()
    comp_discount.style.css.padding = "7px 5px"
    comp_discount.style.css.margin = "5px"
    comp_discount.style.css.border_radius = "50%"
    return comp_discount

  def rating(self, rating, customers=None, label=None, url=None, align="left", width=(300, 'px'), height=("auto", ''),
             options=None, profile=None):
    """
    Description:
    ------------
    Add rating component for customers review.

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
    :param rating: Integer. Optional. The number of stars.
    :param customers:
    :param label: String. Optional. The label value.
    :param url: String. Optional. The url link.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {}
    container = self.page.ui.div([], profile=profile)
    if label is not None:
      container.label = self.page.ui.texts.label(label, width=60, options=options, profile=profile)
      container.label.style.css.line_height = False
      container.label.style.css.margin = False
      container.label.style.css.margin_right = 10
      container.add(container.label)
    container.stars = self.page.ui.rich.stars(rating, best=options.get("stars", 5), profile=profile)
    container.stars.style.display = "inline-block"
    container.stars.style.margin_right = 5
    container.add(container.stars)
    if customers is not None:
      container.link = self.page.ui.link("(%s)" % customers, url, profile=profile)
      container.add(container.link)
    return container

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
    :param tags: List. The list of tags.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    container = self.page.ui.div(
      [], align=align, width=width, height=height, options=options, profile=profile)
    for tag in tags:
      if not hasattr(tag, 'options'):
        comp_tag = self.page.ui.text(tag, profile=profile)
      else:
        comp_tag = tag
      comp_tag.style.css.background = self.page.theme.colors[4]
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

    :tags:
    :categories:

    Usage:
    -----

    Templates:

    Related Pages:

    Attributes:
    ----------
    :param component: Component. The HTML component.
    :param name: String. Optional. The label value.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    label = self.page.ui.text(name, profile=profile)
    label.style.css.background = self.page.theme.colors[-1]
    label.style.css.color = self.page.theme.greys[0]
    label.style.css.padding = "0 10px"
    label.style.css.border_radius = "0 0 20px 0"
    container = self.page.ui.div(
      [label, self.page.ui.div(component, align=align, profile=profile).css({'margin': '5px'})],
      align="left", width=width, height=height, options=options, profile=profile)
    container.style.css.border = "1px solid %s" % self.page.theme.colors[-1]
    container.label = label
    return container

  def quality(self, votes, url=None, width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------
    Return a skillbar chart for the customer review ratings.

    :tags:
    :categories:

    Usage:
    -----

    Templates:

    Related Pages:

    Attributes:
    ----------
    :param votes: Dictionary. Number of customer review per rating.
    :param url: String. Optional. Url template for product link to those customer rating comments.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    vote_records = []
    dflt_options = {"unit": '%', "values": True, "background": self.page.theme.colors[6], 'borders': True}
    if options is not None:
      dflt_options.update(options)
    customers = sum([k for k in votes.values()])
    for i in reversed(range(dflt_options.get("stars", 5))):
      if url is not None:
        vote_records.append(
          {"star": self.page.ui.link("%s stars" % i, url % i), "value":  votes.get(i, 0) / customers * 100})
      else:
        vote_records.append(
          {"star": "%s stars" % i, "value":  votes.get(i, 0) / customers * 100})
    comp = self.page.ui.charts.skillbars(
      vote_records, y_column='value', x_axis='star', options=dflt_options, profile=profile, height=height
    ).css({"width": "%s%s" % (width[0], width[1])})
    return comp

  def question(self, question, answers=None, url=None, align="left", width=(300, 'px'), height=("auto", ''),
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
    :param question: String. Optional. The question.
    :param answers:
    :param url: String. Optional. The url link.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    table = self.page.ui.layouts.table(options={"header": False}, profile=profile)
    if url is not None:
      link = self.page.ui.link(question, url, align=align, options=options, profile=profile)
      link.style.css.color = self.page.theme.colors[6]
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

  def review(self, rating, title, comment, author, date, align="left", width=(300, 'px'), height=("auto", ''),
             options=None, profile=None):
    pass

  def album(self, pictures, selected=0, align="left", width=(500, 'px'), height=("auto", ''), options=None,
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
    :param pictures: List. The list of pictures.
    :param selected: Integer. Optional. The default selected index.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    container = self.page.ui.div(
      [], align=align, width=width, height=height, options=options, profile=profile)
    left_panel = self.page.ui.div(
      [], align=align, width=(50, 'px'), height=(100, "%"), options=options, profile=profile)
    left_panel.style.css.display = "inline-block"
    left_panel.style.css.vertical_align = "top"
    right_panel = self.page.ui.div(
      [], align=align, width=("calc(100% - 60px)", ''), height=height, options=options, profile=profile)
    right_panel.style.css.display = "inline-block"
    right_panel.style.css.padding = 5
    img_selected = self.page.ui.img(pictures[selected], profile=profile)
    img_selected.style.css.float = "right"
    right_panel.add(img_selected)

    for i, pic in enumerate(pictures):
      if isinstance(pic, dict):
        picture = pic['min']
        full_picture = pic['max']
      else:
        picture = pic
        full_picture = pic
      img = self.page.ui.img(picture, width=(40, "px"), profile=profile)
      img.style.css.border = "1px solid %s" % self.page.theme.greys[-1]
      img.style.css.margin = "5px 10px"
      img.style.css.cursor = "pointer"
      img.style.hover({"border": "1px solid red"})
      img.click([img_selected.dom.src(full_picture)])
      left_panel.add(img)
    container.add(self.page.ui.div([left_panel, right_panel], profile=profile))
    return container

  def availability(self, flag, comment=None, align="left", width=('auto', ''), height=("auto", ''), options=None,
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
    :param flag: Boolean. The availability flag.
    :param comment: String. Optional. The product comment.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    comp_availability = self.page.ui.text(
      "In Stock", align=align, width=width, height=height, options=options, profile=profile)
    if flag:
      comp_availability.style.css.color = self.page.theme.success[1]
      comp_availability.style.css.bold()
      comp_availability._vals = comment or "In Stock"
    else:
      comp_availability.style.css.color = self.page.theme.danger[1]
      comp_availability.style.css.bold()
      comp_availability._vals = comment or "Not Available"
    return comp_availability

  def vote(self, number, align="center", width=('auto', ''), height=("auto", ''), options=None, profile=None):
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
    :param number: Integer. Optional. The vote count.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    container = self.page.ui.div(
      [], align=align, width=width, height=height, options=options, profile=profile)
    container.up = self.page.ui.icons.awesome("fas fa-caret-up", profile=profile)
    container.up.style.css.display = 'block'
    container.up.style.css.margin = '0 auto'
    container.add(container.up)
    container.text = self.page.ui.texts.number(number, width=width, options=options)
    container.text.style.css.font_factor(10)
    container.add(container.text)
    container.down = self.page.ui.icons.awesome("fas fa-caret-down", profile=profile)
    container.down.style.css.display = 'block'
    container.down.style.css.margin = '0 auto'
    container.add(container.down)
    return container

  def bar(self, title, price, description=None, url=None, width=(None, ''), height=("auto", ''), options=None,
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
    :param title: String. A panel title. This will be attached to the title property.
    :param price: Number. The item price.
    :param description: String. Optional. The item description.
    :param url: String. Optional. The url link.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {}
    container = self.page.ui.div([], align='left', width=width, height=height, options=options,
                                           profile=profile)
    if not hasattr(title, 'options'):
      container.title = self.page.ui.titles.title(title, profile=profile)
      container.title.style.css.display = "inline-block"
      container.title.style.css.margin_top = 0
      container.title.style.css.font_weight = 'bold'
      container.title.style.css.font_size = self.page.body.style.globals.font.normal(5)
    else:
      container.title = title
    if url is not None:
      container.style.css.cursor = "pointer"
      container.click([self.page.js.navigateTo(url)])
    container.add(container.title)
    if not hasattr(price, 'options'):
      if "font_factor" not in options:
        options["font_factor"] = 5
      container.price = self.price(price, align='right', width=(None, 'px'), options=options, profile=profile)
      container.price.style.css.position = "relative"
      container.price.style.css.font_weight = 'bold'
      container.price.style.css.margin_top = -25
      container.price.style.css.right = 0
    else:
      container.price = price
    container.add(container.price)
    if description is not None:
      if not hasattr(description, 'options'):
        container.description = self.page.ui.text(description, profile=profile)
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

    :tags:
    :categories:

    Usage:
    -----

    Templates:

    Related Pages:

    Attributes:
    ----------
    :param title: String. A panel title. This will be attached to the title property.
    :param image:
    :param location:
    :param limit:
    :param date:
    :param tags:
    :param price: Number. The item price.
    :param details:
    :param align: String. Optional. A string with the horizontal position of the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    ool = self.page.ui.col(profile=profile)
    ool.add(self.page.studio.shop.bar(title, price, details, profile=profile))
    if location:
      ool.add(self.page.ui.div([
        self.page.ui.icon("fas fa-map-marker-alt", profile=profile).css(
          {"margin-right": '10px'}), self.page.ui.text(location)], profile=profile))
    if limit:
      ool.add(self.page.ui.div([
        self.page.ui.icon("fas fa-male", profile=profile).css(
          {"margin-right": '15px'}), self.page.ui.text(limit)]))
    if tags:
      ool.add(self.page.studio.tags(tags, profile=profile))
    ool.add(self.page.ui.text("Prochaine session", profile=profile).css(
      {"display": 'block', "margin-top": '5px', "color": self.page.theme.greys[6]}))
    ool.add(self.page.ui.text(date, profile=profile).css({"display": 'block', 'font-weight': 'bold'}))
    ool.add(self.page.ui.button("Book this item", align="center", profile=profile).css(
      {"margin": '15px auto 5px'}))
    vim = self.page.ui.vignets.image(
      content=ool, align=align, width=width, height=height, options=options, render='col', profile=profile)
    vim.style.configs.shadow()
    vim.style.css.padding_top = 160
    vim.style.css.background_url(image, size="100% 150px", background_position="top")
    vim.style.css.margin_top = 10
    return vim


class Resto(Shopping):

  def compostion(self, text, weight, percentage, background=None, width=(80, 'px'), height=(120, 'px'), options=None,
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
    :param text: String. Optional. The value to be displayed to the component.
    :param weight: Tuple. Optional. A tuple with the integer for the component weight and its unit.
    :param percentage: Number. Optional. The percentage value.
    :param background: String. Optional. The background color.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    container = self.page.ui.div(width=width, height=height, options=options, profile=profile)
    container.style.css.display = "inline-block"
    container.title = self.page.ui.text(text, align="center", profile=profile)
    container.title.style.css.font_factor(-3)
    container.style.css.position = "relative"
    container.add(container.title)
    container.weight = self.page.ui.text("%s %s" % (weight[0], weight[1]), align="center", profile=profile)
    container.weight.style.css.font_factor(8)
    container.weight.style.css.bold()
    container.weight.style.css.padding_top = 10
    container.add(container.weight)
    if background is None:
      if percentage < 10:
        container.style.css.background = self.page.theme.success[0]
      elif percentage < 50:
        container.style.css.background = self.page.theme.warning[0]
      else:
        container.style.css.background = self.page.theme.danger[0]
    container.style.css.border_radius = 25
    container.style.css.padding_top = 10
    container.percentage = self.page.ui.div("%s%%" % percentage, width=(50, 'px'), profile=profile)
    container.percentage.style.css.position = "absolute"
    container.percentage.style.css.text_align = "center"
    container.percentage.style.css.bottom = 0
    container.percentage.style.css.margin_left = 15
    container.percentage.style.css.border_radius = "20px 20px 0 0"
    container.add(container.percentage)
    container.percentage.style.css.background = "white"
    return container
