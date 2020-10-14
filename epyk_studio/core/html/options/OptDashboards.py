#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.options import Options


class OptionTask(Options):

  @property
  def completed(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param icon: Dictionary. CSS attributes
    """
    return self.get("fas fa-check-circle")

  @completed.setter
  def completed(self, icon):
    self._config(icon)
    self.set(icon)

  @property
  def failed(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param icon: Dictionary. CSS attributes
    """
    return self.get("fas fa-times-circle")

  @failed.setter
  def failed(self, icon):
    self._config(icon)
    self.set(icon)

  @property
  def waiting(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param icon: Dictionary. CSS attributes
    """
    return self.get("fas fa-pause")

  @waiting.setter
  def waiting(self, icon):
    self._config(icon)
    self.set(icon)

  @property
  def running(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param icon: Dictionary. CSS attributes
    """
    return self.get("fas fa-spinner")

  @running.setter
  def running(self, icon):
    self._config(icon)
    self.set(icon)

  @property
  def status(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param icon: Dictionary. CSS attributes
    """
    return self.get("")

  @status.setter
  def status(self, value):
    if not value.upper() in ("COMPLETED", "RUNNING", "WAITING", "FAILED"):
      raise Exception("Error")

    self.running = self.running
    self.waiting  = self.waiting
    self.failed = self.failed
    self.completed  = self.completed
    self._attrs["icon"] = getattr(self, value.lower())
    self._attrs["color"] = {"COMPLETED": self._report._report.theme.success[1], "RUNNING": self._report._report.theme.warning[1],
                "WAITING": self._report._report.theme.greys[5], "FAILED": self._report._report.theme.danger[1]}[value]
    self.set(value)

  @property
  def icon(self):
    """
    Description:
    ------------

    """
    return self.get(self.waiting)

  @property
  def color(self):
    """
    Description:
    ------------

    """
    return self.get("black")
