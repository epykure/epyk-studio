#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.Page import Report#
from epyk_studio.interfaces import Interface


class Report(Report):

  @property
  def studio(self):
    """
    Description:
    ------------
    Group all the business configuration together.
    This module will rely on the base components available in the UI.

    This will only provide ready to use component for standard business cases.
    """
    return Interface.Studio(self)
