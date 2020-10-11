#!/usr/bin/python
# -*- coding: utf-8 -*-

DAYS = []
MONTHS = []

BY_WITH_NAME = "Le %s, par&nbsp;"
BY = "par&nbsp;"

SPONSORS = "Partenaires"

PLACEHOLDER_EMAIL = "Enter email address"
PLACEHOLDER_COMMENT = "Let a comment"
PLACEHOLDER_SEARCH = "Rechercher..."

BUTTON_SUBSCRIBE = "Subscribe"
BUTTON_SHOW_MORE = "Plus de resultats"

LABEL_YESTERDAY = "Hier"
LABEL_TIME = {
  'years': 'annee', 'months': 'mois', 'days': 'jours', 'hours': 'heures', 'minutes': 'minutes', 'seconds': 'secondes'
}
LABEL_TIME_SHORT = {
  'years': 'an', 'months': 'm', 'days': 'j', 'hours': 'h', 'minutes': 'min', 'seconds': 's'
}

RATES_HEADER = ["Symbol", 'Last Price', 'Change', '% Change']


LABEL_YESNO = ["Vrai", "Faux"]

COLUMNS = "Colonnes"
VALUES = 'Valeurs'


def country(cty='fr'):
  return "fr"


def distance_unit(cty='fr'):
  return "km"


def currency(cty='fr'):
  cty = cty or 'uk'
  cty = cty.lower()
  return "€"
