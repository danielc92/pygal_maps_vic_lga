# -*- coding: utf-8 -*-
# This file is part of pygal
#
# A python svg graph plotting library
# Copyright © 2012-2014 Kozea
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.
"""
French departments and regions maps

"""

from __future__ import division
from collections import defaultdict
from pygal.graph.map import BaseMap
from pygal._compat import u
from numbers import Number
import os

LGAS = {
    'yarriambiack': u('Yarriambiack (S)'),
    'yarra-ranges': u('Yarra Ranges (S)'),
    'yarra': u('Yarra (C)'),
    'wyndham': u('Wyndham (C)'),
    'wodonga': u('Wodonga (C)'),
    'whittlesea': u('Whittlesea (C)'),
    'whitehorse': u('Whitehorse (C)'),
    'west-wimmera': u('West Wimmera (S)'),
    'wellington': u('Wellington (S)'),
    'warrnambool': u('Warrnambool (C)'),
    'wangaratta': u('Wangaratta (RC)'),
    'unincorporated-vic': u('Unincorporated Vic'),
    'towong':('Towong (S)'),
    'swan-hill': u('Swan Hill (RC)'),
    'surf-coast': u('Surf Coast (S)'),
    'strathbogie': u('Strathbogie (S)'),
    'stonnington': u('Stonnington (C)'),
    'southern-grampians': u('Southern Grampians (S)'),
    'south-gippsland': u('South Gippsland (S)'),
    'queenscliffe': u('Queenscliffe (B)'),
    'pyrenees': u('Pyrenees (S)'),
    'port-phillip': u('Port Phillip (C)'),
    'northern-grampians': u('Northern Grampians (S)'),
    'nillumbik': u('Nillumbik (S)'),
    'murrindindi': u('Murrindindi (S)'),
    'moyne': u('Moyne (S)'),
    'mount-alexander': u('Mount Alexander (S)'),
    'mornington-peninsula': u('Mornington Peninsula (S)'),
    'moreland': u('Moreland (C)'),
    'moorabool': u('Moorabool (S)'),
    'moonee-valley': u('Moonee Valley (C)'),
    'monash': u('Monash (C)'),
    'moira': u('Moira (S)'),
    'mitchell': u('Mitchell (S)'),
    'mildura': u('Mildura (RC)'),
    'melton': u('Melton (C)'),
    'melbourne': u('Melbourne (C)'),
    'maroondah': u('Maroondah (C)'),
    'maribyrnong': u('Maribyrnong (C)'),
    'mansfield': u('Mansfield (S)'),
    'manningham': u('Manningham (C)'),
    'macedon-ranges': u('Macedon Ranges (S)'),
    'loddon': u('Loddon (S)'),
    'latrobe': u('Latrobe (C) (Vic.)'),
    'knox': u('Knox (C)'),
    'kingston': u('Kingston (C) (Vic.)'),
    'indigo': u('Indigo (S)'),
    'hume': u('Hume (C)'),
    'horsham': u('Horsham (RC)'),
    'hobsons-bay': u('Hobsons Bay (C)'),
    'hindmarsh': u('Hindmarsh (S)'),
    'hepburn': u('Hepburn (S)'),
    'greater-shepparton': u('Greater Shepparton (C)'),
    'greater-geelong': u('Greater Geelong (C)'),
    'greater-dandenong': u('Greater Dandenong (C)'),
    'greater-bendigo': u('Greater Bendigo (C)'),
    'golden-plains': u('Golden Plains (S)'),
    'glenelg': u('Glenelg (S)'),
    'glen-eira': u('Glen Eira (C)'),
    'gannawarra': u('Gannawarra (S)'),
    'frankston': u('Frankston (C)'),
    'east-gippsland': u('East Gippsland (S)'),
    'darebin': u('Darebin (C)'),
    'corangamite': u('Corangamite (S)'),
    'colac-otway': u('Colac-Otway (S)'),
    'central-goldfields': u('Central Goldfields (S)'),
    'casey': u('Casey (C)'),
    'cardinia': u('Cardinia (S)'),
    'campaspe': u('Campaspe (S)'),
    'buloke': u('Buloke (S)'),
    'brimbank': u('Brimbank (C)'),
    'boroondara': u('Boroondara (C)'),
    'benalla': u('Benalla (RC)'),
    'bayside': u('Bayside (C)'),
    'baw-baw': u('Baw Baw (S)'),
    'bass-coast': u('Bass Coast (S)'),
    'banyule': u('Banyule (C)'),
    'ballarat': u('Ballarat (C)'),
    'ararat': u('Ararat (RC)'),
    'alpine': u('Alpine (S)'),
}



with open(os.path.join(
        os.path.dirname(__file__),
        'lga_vic.svg')) as file:
    DPT_MAP = file.read()


class IntCodeMixin(object):
    def adapt_code(self, area_code):
        if isinstance(area_code, Number):
            return '%02d' % area_code
        return super(IntCodeMixin, self).adapt_code(area_code)


class LocalGovernmentAreas(IntCodeMixin, BaseMap):
    """French department map"""
    x_labels = list(LGAS.keys())
    area_names = LGAS
    area_prefix = ''
    kind = 'lga'
    svg_map = DPT_MAP


with open(os.path.join(
        os.path.dirname(__file__),
        'lga_vic.svg')) as file:
    REG_MAP = file.read()


# class Regions(IntCodeMixin, BaseMap):
#     """French regions map"""
#     x_labels = list(REGIONS.keys())
#     area_names = REGIONS
#     area_prefix = 'a'
#     svg_map = REG_MAP
#     kind = 'region'


# DEPARTMENTS_REGIONS = {
#     "01": "82",
#     "02": "22",
#     "03": "83",
#     "04": "93",
#     "05": "93",
#     "06": "93",
#     "07": "82",
#     "08": "21",
#     "09": "73",
#     "10": "21",
#     "11": "91",
#     "12": "73",
#     "13": "93",
#     "14": "25",
#     "15": "83",
#     "16": "54",
#     "17": "54",
#     "18": "24",
#     "19": "74",
#     "21": "26",
#     "22": "53",
#     "23": "74",
#     "24": "72",
#     "25": "43",
#     "26": "82",
#     "27": "23",
#     "28": "24",
#     "29": "53",
#     "2A": "94",
#     "2B": "94",
#     "30": "91",
#     "31": "73",
#     "32": "73",
#     "33": "72",
#     "34": "91",
#     "35": "53",
#     "36": "24",
#     "37": "24",
#     "38": "82",
#     "39": "43",
#     "40": "72",
#     "41": "24",
#     "42": "82",
#     "43": "83",
#     "44": "52",
#     "45": "24",
#     "46": "73",
#     "47": "72",
#     "48": "91",
#     "49": "52",
#     "50": "25",
#     "51": "21",
#     "52": "21",
#     "53": "52",
#     "54": "41",
#     "55": "41",
#     "56": "53",
#     "57": "41",
#     "58": "26",
#     "59": "31",
#     "60": "22",
#     "61": "25",
#     "62": "31",
#     "63": "83",
#     "64": "72",
#     "65": "73",
#     "66": "91",
#     "67": "42",
#     "68": "42",
#     "69": "82",
#     "70": "43",
#     "71": "26",
#     "72": "52",
#     "73": "82",
#     "74": "82",
#     "75": "11",
#     "76": "23",
#     "77": "11",
#     "78": "11",
#     "79": "54",
#     "80": "22",
#     "81": "73",
#     "82": "73",
#     "83": "93",
#     "84": "93",
#     "85": "52",
#     "86": "54",
#     "87": "74",
#     "88": "41",
#     "89": "26",
#     "90": "43",
#     "91": "11",
#     "92": "11",
#     "93": "11",
#     "94": "11",
#     "95": "11",
#     "971": "01",
#     "972": "02",
#     "973": "03",
#     "974": "04",
#     "975": "05",
#     "976": "06"
# }


# def aggregate_regions(values):
#     if isinstance(values, dict):
#         values = values.items()
#     regions = defaultdict(int)
#     for department, value in values:
#         regions[DEPARTMENTS_REGIONS[department]] += value
#     return list(regions.items())
