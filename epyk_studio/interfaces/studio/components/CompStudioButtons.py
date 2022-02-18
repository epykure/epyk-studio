#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.interfaces.components.CompButtons import Buttons
from epyk_studio.lang import get_lang


class StudioButtons(Buttons):

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
