#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.options import Options


class OptionTask(Options):

  @property
  def completed(self):
    """
    Description:
    ------------
    Icon for a completed task status.

    Attributes:
    ----------
    :prop icon: String. The icon reference.
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
    Icon for a failed task status.

    Attributes:
    ----------
    :prop icon: String. The icon reference.
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
    Icon for a waiting task status.

    Attributes:
    ----------
    :prop icon: String. The icon reference.
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
    Icon for a running task status.

    Attributes:
    ----------
    :prop icon: String. The icon reference.
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
    Set the task status.

    Attributes:
    ----------
    :prop icon: String. A task status
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
    self._attrs["color"] = {
      "COMPLETED": self.component.page.theme.success[1],
      "RUNNING": self.component.page.theme.warning[1],
      "WAITING": self.component.page.theme.greys[5],
      "FAILED": self.component.page.theme.danger[1]}[value]
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
