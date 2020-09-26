#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.interfaces.components.CompButtons import Buttons
from epyk_studio.lang import get_lang


class StudioButtons(Buttons):

  def more(self, width=(100, "%"), height=(None, "px"), align="left", htmlCode=None, tooltip=None, profile=None, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param width:
    :param height:
    :param align:
    :param htmlCode:
    :param tooltip:
    :param profile:
    :param options:
    """
    options = options or {}
    show_more = self.context.rptObj.ui.text(get_lang(options.get("lang")).BUTTON_SHOW_MORE, width=(100, '%'))
    show_more.style.css.display = "inline-block"
    show_more.style.css.text_align = "center"
    html_button = self.button(text=show_more, icon="fas fa-chevron-down", width=width, height=height, align=align, htmlCode=htmlCode, tooltip=tooltip,
                              profile=profile, options=options)
    html_button.style.css.border_radius = 30
    html_button.style.css.text_align = 'left'
    html_button.style.add_classes.div.border_hover()
    html_button.style.css.padding = "3px 20px"
    return html_button
