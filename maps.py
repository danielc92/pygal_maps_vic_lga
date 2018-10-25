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
    '27630_yarriambiack_(s)': u('Yarriambiack (S)'),
    '27450_yarra_ranges_(s)': u('Yarra Ranges (S)'),
    '27350_yarra_(c)': u('Yarra (C)'),
    '27260_wyndham_(c)': u('Wyndham (C)'),
    '27170_wodonga_(c)': u('Wodonga (C)'),
    '27070_whittlesea_(c)': u('Whittlesea (C)'),
    '26980_whitehorse_(c)': u('Whitehorse (C)'),
    '26890_west_wimmera_(s)': u('West Wimmera (S)'),
    '26810_wellington_(s)': u('Wellington (S)'),
    '26730_warrnambool_(c)': u('Warrnambool (C)'),
    '26700_wangaratta_(rc)': u('Wangaratta (RC)'),
    '29399_unincorporated_vic': u('Unincorporated Vic'),
    '26670_towong_(s)': u('Towong (S)'),
    '26610_swan_hill_(rc)': u('Swan Hill (RC)'),
    '26490_surf_coast_(s)': u('Surf Coast (S)'),
    '26430_strathbogie_(s)': u('Strathbogie (S)'),
    '26350_stonnington_(c)': u('Stonnington (C)'),
    '26260_southern_grampians_(s)': u('Southern Grampians (S)'),
    '26170_south_gippsland_(s)': u('South Gippsland (S)'),
    '26080_queenscliffe_(b)': u('Queenscliffe (B)'),
    '25990_pyrenees_(s)': u('Pyrenees (S)'),
    '25900_port_phillip_(c)': u('Port Phillip (C)'),
    '25810_northern_grampians_(s)': u('Northern Grampians (S)'),
    '25710_nillumbik_(s)': u('Nillumbik (S)'),
    '25620_murrindindi_(s)': u('Murrindindi (S)'),
    '25490_moyne_(s)': u('Moyne (S)'),
    '25430_mount_alexander_(s)': u('Mount Alexander (S)'),
    '25340_mornington_peninsula_(s)': u('Mornington Peninsula (S)'),
    '25250_moreland_(c)': u('Moreland (C)'),
    '25150_moorabool_(s)': u('Moorabool (S)'),
    '25060_moonee_valley_(c)': u('Moonee Valley (C)'),
    '24970_monash_(c)': u('Monash (C)'),
    '24900_moira_(s)': u('Moira (S)'),
    '24850_mitchell_(s)': u('Mitchell (S)'),
    '24780_mildura_(rc)': u('Mildura (RC)'),
    '24650_melton_(c)': u('Melton (C)'),
    '24600_melbourne_(c)': u('Melbourne (C)'),
    '24410_maroondah_(c)': u('Maroondah (C)'),
    '24330_maribyrnong_(c)': u('Maribyrnong (C)'),
    '24250_mansfield_(s)': u('Mansfield (S)'),
    '24210_manningham_(c)': u('Manningham (C)'),
    '24130_macedon_ranges_(s)': u('Macedon Ranges (S)'),
    '23940_loddon_(s)': u('Loddon (S)'),
    '23810_latrobe_(c)_(vic.)': u('Latrobe (C) (Vic.)'),
    '23670_knox_(c)': u('Knox (C)'),
    '23430_kingston_(c)_(vic.)': u('Kingston (C) (Vic.)'),
    '23350_indigo_(s)': u('Indigo (S)'),
    '23270_hume_(c)': u('Hume (C)'),
    '23190_horsham_(rc)': u('Horsham (RC)'),
    '23110_hobsons_bay_(c)': u('Hobsons Bay (C)'),
    '22980_hindmarsh_(s)': u('Hindmarsh (S)'),
    '22910_hepburn_(s)': u('Hepburn (S)'),
    '22830_greater_shepparton_(c)': u('Greater Shepparton (C)'),
    '22750_greater_geelong_(c)': u('Greater Geelong (C)'),
    '22670_greater_dandenong_(c)': u('Greater Dandenong (C)'),
    '22620_greater_bendigo_(c)': u('Greater Bendigo (C)'),
    '22490_golden_plains_(s)': u('Golden Plains (S)'),
    '22410_glenelg_(s)': u('Glenelg (S)'),
    '22310_glen_eira_(c)': u('Glen Eira (C)'),
    '22250_gannawarra_(s)': u('Gannawarra (S)'),
    '22170_frankston_(c)': u('Frankston (C)'),
    '22110_east_gippsland_(s)': u('East Gippsland (S)'),
    '21890_darebin_(c)': u('Darebin (C)'),
    '21830_corangamite_(s)': u('Corangamite (S)'),
    '21750_colac-otway_(s)': u('Colac-Otway (S)'),
    '21670_central_goldfields_(s)': u('Central Goldfields (S)'),
    '21610_casey_(c)': u('Casey (C)'),
    '21450_cardinia_(s)': u('Cardinia (S)'),
    '21370_campaspe_(s)': u('Campaspe (S)'),
    '21270_buloke_(s)': u('Buloke (S)'),
    '21180_brimbank_(c)': u('Brimbank (C)'),
    '21110_boroondara_(c)': u('Boroondara (C)'),
    '21010_benalla_(rc)': u('Benalla (RC)'),
    '20910_bayside_(c)': u('Bayside (C)'),
    '20830_baw_baw_(s)': u('Baw Baw (S)'),
    '20740_bass_coast_(s)': u('Bass Coast (S)'),
    '20660_banyule_(c)': u('Banyule (C)'),
    '20570_ballarat_(c)': u('Ballarat (C)'),
    '20260_ararat_(rc)': u('Ararat (RC)'),
    '20110_alpine_(s)': u('Alpine (S)'),
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
