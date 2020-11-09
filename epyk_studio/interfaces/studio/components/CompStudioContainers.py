#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.interfaces.components.CompButtons import Buttons


class StudioContainers(Buttons):

  def box(self, info=None, delete=False):
    """
    Description:
    ------------
    Predefined container to help on the style of teh generated pages.

    Attributes:
    ----------
    :param info:
    :param delete:
    """
    container = self.context.rptObj.ui.div()
    container.style.css.padding = "5px 15px"
    container.style.css.background = self.context.rptObj.theme.greys[0]
    container.style.css.border = "1px solid %s" % self.context.rptObj.theme.greys[3]
    container.style.css.margin_bottom = 5
    container.style.css.margin_top = 10
    margin_right = 5
    if delete:
      remove = self.context.rptObj.ui.icons.remove(tooltip="Remove panel")
      remove.style.css.position = "absolute"
      remove.style.css.top = 2
      remove.style.css.right = 5
      remove.style.css.margin = 0
      remove.click([container.dom.remove()])
      remove.style.css.color = self.context.rptObj.theme.greys[6]
      margin_right += 25
      container.add(remove)
    if info is not None:
      container.style.css.position = "relative"
      info = self.context.rptObj.ui.rich.info(info)
      info.style.css.position = "absolute"
      info.style.css.color = self.context.rptObj.theme.greys[6]
      info.style.css.top = 5
      info.style.css.right = margin_right
      container.add(info)
    return container

