#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.interfaces.components.CompButtons import Buttons
from epyk_studio.lang import get_lang


class StudioContainers(Buttons):

  def box(self):
    container = self.context.rptObj.ui.div()
    container.style.css.padding = "5px 15px"
    container.style.css.background = self.context.rptObj.theme.greys[0]
    container.style.css.border = "1px solid %s" % self.context.rptObj.theme.greys[3]
    container.style.css.margin_bottom = 10
    return container

