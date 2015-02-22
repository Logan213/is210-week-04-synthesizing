#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Decision Tree for Colors"""

BASE = raw_input('Which base color, "Seattle Gray" or "Manatee"? ')

if BASE == 'Seattle Gray':
    ACCENT = raw_input('Which accent color, "Ceramic Glaze" or "Cumulus '
                       'Nimbus"?: ')
    if ACCENT is 'Ceramic Glaze':
        HIGHLIGHT = raw_input('Which highlight color, "Basically White" or '
                              '"White"?: ')
    else:
        HIGHLIGHT = raw_input('Which highlight color, "Off White" or "Paper '
                              'White"?: ')

else:
    ACCENT = raw_input('Which accent color, "Platinum Mist" or "Spartan '
                       'Sage"?: ')
    if ACCENT is 'Platinum Mist':
        HIGHLIGHT = raw_input('Which highlight color, "Bone White" or "Just '
                              'White"?: ')
    else:
        HIGHLIGHT = raw_input('Which highlight color, "Fractal White" or "Not '
                              'White"?: ')

RETSTR = 'Your selected colors are {}, {}, and {}.'
print RETSTR.format(BASE, ACCENT, HIGHLIGHT)
