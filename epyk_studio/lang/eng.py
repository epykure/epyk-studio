#!/usr/bin/python
# -*- coding: utf-8 -*-

DAYS = ['Monday']
MONTHS = [
  "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
  "November", "December"]

BY_WITH_NAME = "The %s, by&nbsp;"
BY = "by&nbsp;"

SPONSORS = 'Sponsors'

CLIENTS_LABEL = "Client we have worked with..."

PLACEHOLDER_EMAIL = "Enter email address"
PLACEHOLDER_COMMENT = "Let a comment"
PLACEHOLDER_SEARCH = "Search..."

BUTTON_SUBSCRIBE = "Subscribe"
BUTTON_SHOW_MORE = "More results"

LABEL_YESTERDAY = "Yesterday"
LABEL_TIME = {
  'years': 'year', 'months': 'months', 'days': 'days', 'hours': 'hours', 'minutes': 'minutes', 'seconds': 'seconds'
}
LABEL_TIME_SHORT = {
  'years': 'y', 'months': 'm', 'days': 'd', 'hours': 'h', 'minutes': 'min', 'seconds': 's'
}

RATES_HEADER = ["Symbol", 'Last Price', 'Change', '% Change']


LABEL_YESNO = ["True", "False"]

COLUMNS = "Columns"
VALUES = 'Values'


def country(cty='us'):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param cty: String. Optional. The country code.
  """
  return "us"


def distance_unit(cty='us'):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param cty: String. Optional. The country code.
  """
  cty = cty or 'us'
  cty = cty.lower()
  if cty == 'uk':
    return "mi"

  return "km"


def currency(cty='uk'):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param cty: String. Optional. The country code.
  """
  cty = cty or 'us'
  cty = cty.lower()
  if cty == 'uk':
    return "£"

  return "$"
