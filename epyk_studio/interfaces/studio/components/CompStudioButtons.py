#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.interfaces.components.CompButtons import Buttons
from epyk_studio.lang import get_lang


class StudioButtons(Buttons):

  def more(self, items, text=None, width=("auto", ""), height=(None, "px"), align="left", html_code=None, tooltip=None,
           profile=None, options=None):
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
    :param items: List. List of items to be added to the menu.
    :param text: String. Optional. The text visible in the button.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. The text-align property within this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    options = options or {}
    show_more = self.page.ui.text(
      text or get_lang(options.get("lang")).BUTTON_SHOW_MORE, width=("auto", ''), profile=profile)
    show_more.style.css.font_factor(-4)
    show_more.style.css.italic()
    show_more.style.css.display = "inline-block"
    show_more.style.css.text_align = "center"
    html_button = self.button(text=show_more, icon="fas fa-chevron-down", width=width, height=height, align=align,
                              html_code=html_code, tooltip=tooltip, profile=profile, options=options)
    html_button.style.css.border_radius = 5
    html_button.style.css.text_align = 'left'
    html_button.icon.style.add_classes.div.border_hover()
    html_button.style.css.padding = "0 5px"
    text_popup = self.page.ui.lists.items(items, 'link', profile=profile)
    text_popup.style.css.background = "white"
    text_popup.style.css.border = "1px solid %s" % self.page.theme.greys[3]
    text_popup.attr["data-anchor"] = "test_filter"
    text_popup.style.css.invisible()
    text_popup.style.css.position = "absolute"
    text_popup.style.css.top = 25
    text_popup.style.css.left = 5
    text_popup.style.css.padding = "2px 5px"
    text_popup.attr["tabIndex"] = 0
    html_button.icon.click([
      self.page.js.objects.event.stopPropagation(), text_popup.dom.visible(), text_popup.dom.events.trigger("focus")])
    container = self.page.ui.div([html_button, text_popup], width="auto", profile=profile)
    container.style.css.position = "relative"
    container.button = html_button
    container.menu = text_popup
    text_popup.focusout([
      self.page.js.objects.event.stopPropagation(),
      self.page.js.objects.event.preventDefault(),
      text_popup.dom.invisible()])
    return container

  def clipboard(self, click_funcs=None, profile=None, source_event=None, on_ready=False, options=None):
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
    :param click_funcs: List | String. A Javascript Python function.
    :param profile: Boolean. Optional. Set to true to get the profile for the function on the Javascript console.
    :param source_event: String. Optional. The source target for the event.
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    component = self.page.ui.icon("far fa-clipboard", options=options, profile=profile)
    component.style.add_classes.div.color_hover()
    if click_funcs is not None:
      component.click(click_funcs, profile=profile, source_event=source_event, on_ready=on_ready)
    return component

  def picture(self, click_funcs=None, profile=None, source_event=None, on_ready=False, options=None):
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
    :param click_funcs: List | String. A Javascript Python function.
    :param profile: Boolean. Optional. Set to true to get the profile for the function on the Javascript console.
    :param source_event: String. Optional. The source target for the event.
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    component = self.page.ui.icon("fas fa-camera", options=options, profile=profile)
    component.style.add_classes.div.color_hover()
    if click_funcs is not None:
      component.click(click_funcs, profile=profile, source_event=source_event, on_ready=on_ready)
    return component
