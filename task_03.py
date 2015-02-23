#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Mortgage Calculator"""

import decimal

NAME = raw_input('What is your name? ')
PRINCIPAL = raw_input('What is the amount being borrowed? ')
PRINCIPAL = int(PRINCIPAL)
TERM = raw_input('What is the term of the loan? ')
TERM = int(TERM)
QUAL_INPUT = raw_input('Are you pre-qualified for this loan? ')
QUAL = QUAL_INPUT[:1].lower() == 'y'
RATE = 0

if PRINCIPAL <= 199999:
    if 1 <= TERM <= 15:
        if QUAL:
            RATE = decimal.Decimal('.0363')
        else:
            RATE = decimal.Decimal('.0465')
    elif 16 <= TERM <= 20:
        if QUAL:
            RATE = decimal.Decimal('.0404')
        else:
            RATE = decimal.Decimal('.0498')
    elif 21 <= TERM <= 30:
        if QUAL:
            RATE = decimal.Decimal('.0577')
        else:
            RATE = decimal.Decimal('.0639')
elif 200000 <= PRINCIPAL <= 999999:
    if 1 <= TERM <= 15:
        if QUAL:
            RATE = decimal.Decimal('.0302')
        else:
            RATE = decimal.Decimal('.0398')
    elif 16 <= TERM <= 20:
        if QUAL:
            RATE = decimal.Decimal('.0327')
        else:
            RATE = decimal.Decimal('.0408')
    elif 21 <= TERM <= 30:
        if QUAL:
            RATE = decimal.Decimal('.0466')
        else:
            RATE is None
else:
    if 1 <= TERM <= 15:
        if QUAL:
            RATE = decimal.Decimal('.0205')
        else:
            RATE = 0
    elif 16 <= TERM <= 20:
        if QUAL:
            RATE = decimal.Decimal('.0262')
        else:
            RATE is None
    else:
        if QUAL:
            RATE is None
        else:
            RATE is None

if RATE is None:
    TOTAL = None 
else:
    TOTAL = (PRINCIPAL * (1 + (RATE / 12))) ** (12 * TERM)
    TOTAL = round(TOTAL)

LINE = '_' * 60

if TOTAL is None:
    REPORT = ('Loan report for: {}\n'
              '{} \n'
              'Principal: ${:>10,}\n'
              'Duration: {:>11}yrs\n'
              'Pre-qualified?: {:>6}\n'
              '\n'
              'Total: NO LOAN')
    print REPORT.format(NAME, LINE, PRINCIPAL, TERM, QUAL)
else:
    REPORT = ('Loan report for: {}\n'
              '{} \n'
              'Principal: ${:>10,}\n'
              'Duration: {:>9}yrs\n'
              'Pre-qualified?: {:>6}\n'
              '\n'
              'Total: ${:>14,}')

    print REPORT.format(NAME, LINE, PRINCIPAL, TERM, QUAL, TOTAL)
