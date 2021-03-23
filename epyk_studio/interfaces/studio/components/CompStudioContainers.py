#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.interfaces.components.CompButtons import Buttons


class StudioContainers(Buttons):

  def box(self, info=None, delete=False, background=False, options=None, html_code=None, profile=None):
    """
    Description:
    ------------
    Predefined container to help on the style of teh generated pages.

    :tags:
    :categories:

    Usage:
    -----

      title = page.ui.title("This is a title")
      box = page.studio.containers.box()
      box.extend([title])
      box.style.standard()

    Templates:

    Related Pages:

    Attributes:
    ----------
    :param info: String. Optional.
    :param delete: Boolean. Optional. Display a delete icon button.
    :param background: Boolean. Optional. Force the background to respect the theme.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    container = self.page.ui.div(html_code=html_code, options=options, profile=profile)
    container.style.css.padding = "5px 15px"
    if background:
      container.style.css.background = self.page.theme.greys[0]
    container.style.css.border = "1px solid %s" % self.page.theme.greys[3]
    container.style.css.margin_bottom = 5
    container.style.css.margin_top = 10
    margin_right = 5
    if delete:
      container.style.css.position = "relative"
      remove = self.page.ui.icons.remove(tooltip="Remove panel")
      remove.style.css.position = "absolute"
      remove.style.css.top = 2
      remove.style.css.right = 5
      remove.style.css.margin = 0
      remove.click([container.dom.remove()])
      remove.style.css.color = self.page.theme.greys[6]
      margin_right += 25
      container.add(remove)
    if info is not None:
      container.style.css.position = "relative"
      info = self.page.ui.rich.info(info, profile=profile)
      info.style.css.position = "absolute"
      info.style.css.color = self.page.theme.greys[6]
      info.style.css.top = 5
      info.style.css.right = margin_right
      container.add(info)
    return container

  def panel(self, close=True, mini=True, info="", options=None, profile=None):
    """
    Description:

    :tags:
    :categories:

    Usage:
    -----

    Templates:

    Related Pages:

    Attributes:
    ----------
    :param close: Boolean. Optional. Display a close font awesome icon.
    :param mini: Boolean. Optional. Display a minify font awesome icon.
    :param info: String. Optional. Display a info icon with a tooltip.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    container = self.page.ui.panels.panel(options=options, profile=profile)
    container.style.css.padding = "5px 15px"
    container.style.css.background = self.page.theme.greys[0]
    container.style.css.border = "1px solid %s" % self.page.theme.greys[3]
    container.style.css.margin_bottom = 5
    container.style.css.margin_top = 10
    container.add_menu(close=close, mini=mini, info=info)
    return container

