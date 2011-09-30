# -*- coding: utf-8 -*-
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Library General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# model_data.py
# Copyright (C) 2011 Simon Newton
# Data for the device models.

DEVICE_MODEL_DATA = {
  161: [{'device_model': 258,
         'model_description': 'SLAMMO',
         'product_category': 1289,
         'software_versions': {16909060: {'label': 'SLAMMO XC1 v0.01',
                                          'personalities': [{'description': '8-bit dimming only',
                                                             'index': 1,
                                                             'slot_count': 1},
                                                            {'description': '8-bit and vector',
                                                             'index': 2,
                                                             'slot_count': 2},
                                                            {'description': '16-bit dim and vector',
                                                             'index': 3,
                                                             'slot_count': 3},
                                                            {'description': '16-bit dim, vector and strobe',
                                                             'index': 4,
                                                             'slot_count': 4}],
                                          'sensor_count': 0,
                                          'supported_parameters': []}}}],
  2056: [{'device_model': 307,
          'model_description': 'Betapack3',
          'product_category': 1281,
          'software_versions': {1395798066: {'label': 'S202',
                                             'personalities': [],
                                             'sensor_count': 1,
                                             'supported_parameters': []}}}],
  9258: [{'device_model': 3,
          'model_description': 'EURODMX STROBE',
          'product_category': 257,
          'software_versions': {1: {'label': 'E00000001',
                                    'personalities': [{'description': 'd',
                                                       'index': 1,
                                                       'slot_count': 2},
                                                      {'description': 'dE2',
                                                       'index': 2,
                                                       'slot_count': 2},
                                                      {'description': 'dE4',
                                                       'index': 3,
                                                       'slot_count': 4},
                                                      {'description': 'H',
                                                       'index': 4,
                                                       'slot_count': 2},
                                                      {'description': 'A',
                                                       'index': 5,
                                                       'slot_count': 0},
                                                      {'description': 'AE2',
                                                       'index': 6,
                                                       'slot_count': 0},
                                                      {'description': 'AC1',
                                                       'index': 7,
                                                       'slot_count': 1},
                                                      {'description': 'AC3',
                                                       'index': 8,
                                                       'slot_count': 3},
                                                      {'description': 'AC4',
                                                       'index': 9,
                                                       'slot_count': 4},
                                                      {'description': 'SLF',
                                                       'index': 10,
                                                       'slot_count': 0}],
                                    'sensor_count': 4,
                                    'supported_parameters': []}}}],
  19541: [{'device_model': 257,
           'model_description': 'CRMX Nova TX2 RDM',
           'personality_count': 5,
           'product_category': 2049,
           'software_version': 131328},
          {'device_model': 4661,
           'model_description': 'DALI/DSI Interface',
           'personality_count': 3,
           'product_category': 2050,
           'software_version': 4}],
  18501: [{'device_model': 258,
           'model_description': 'StarLED Dimmer (rev C)',
           'product_category': 1289,
           'software_versions': {131081: {'label': 'v2.9r 03-Nov-08 22:51:03 c3.249',
                                          'personalities': [{'description': '4cct White Led',
                                                             'index': 1,
                                                             'slot_count': 4},
                                                            {'description': '3cct RBG Led',
                                                             'index': 2,
                                                             'slot_count': 9},
                                                            {'description': '3cct RGBMaster',
                                                             'index': 3,
                                                             'slot_count': 12},
                                                            {'description': '3cct RGB/Preset',
                                                             'index': 4,
                                                             'slot_count': 9}],
                                          'sensor_count': 6,
                                          'supported_parameters': []}}},
          {'device_model': 388,
           'model_description': 'Vari-DC Dimmer',
           'product_category': 1287,
           'software_versions': {65540: {'label': 'v1.4r 05-Jun-09 14:03:15 c4.093',
                                         'personalities': [{'description': 'CandlePSU',
                                                            'index': 1,
                                                            'slot_count': 2},
                                                           {'description': 'ELDriver',
                                                            'index': 2,
                                                            'slot_count': 2}],
                                         'sensor_count': 0,
                                         'supported_parameters': []}}},
          {'device_model': 777,
           'model_description': 'LEDController/4 24V',
           'product_category': 1289,
           'software_versions': {131074: {'label': 'v2.2r 13-May-08 17:54:32 c3.249',
                                          'personalities': [{'description': '4cct RGBW',
                                                             'index': 1,
                                                             'slot_count': 4},
                                                            {'description': '4cct RGBW Mstr',
                                                             'index': 2,
                                                             'slot_count': 5},
                                                            {'description': '3cct RGB',
                                                             'index': 3,
                                                             'slot_count': 3},
                                                            {'description': '3cct RGB Mstr',
                                                             'index': 4,
                                                             'slot_count': 4},
                                                            {'description': '6cct RGB',
                                                             'index': 5,
                                                             'slot_count': 6},
                                                            {'description': '6cct RGB Mstr',
                                                             'index': 6,
                                                             'slot_count': 8},
                                                            {'description': '1cct LED',
                                                             'index': 7,
                                                             'slot_count': 1}],
                                          'sensor_count': 2,
                                          'supported_parameters': []}}}],
  18771: [{'device_model': 64516,
           'model_description': 'Quad120W',
           'product_category': 1289,
           'software_versions': {19267923: {'label': 'Quad120W V1.53',
                                            'personalities': [{'description': '4 DMX Channels',
                                                               'index': 1,
                                                               'slot_count': 4},
                                                              {'description': 'All output chans have same',
                                                               'index': 2,
                                                               'slot_count': 1},
                                                              {'description': 'Custom',
                                                               'index': 3,
                                                               'slot_count': 4}],
                                            'sensor_count': 3,
                                            'supported_parameters': []}}}],
  19792: [{'device_model': 2,
           'model_description': 'MAC 101 CT',
           'product_category': 258,
           'software_versions': {932: {'label': 'MAC 101 CT 1.0.0',
                                       'personalities': [{'description': 'CT',
                                                          'index': 1,
                                                          'slot_count': 10}],
                                       'sensor_count': 0,
                                       'supported_parameters': []}}},
          {'device_model': 1300,
           'model_description': 'MAC 350 Entour',
           'product_category': 258,
           'software_versions': {85196800: {'label': 'MAC 350E 1.1.0',
                                            'personalities': [{'description': '8 Bit Mode',
                                                               'index': 1,
                                                               'slot_count': 14},
                                                              {'description': '16 Bit Mode',
                                                               'index': 2,
                                                               'slot_count': 17}],
                                            'sensor_count': 0,
                                            'supported_parameters': []}}}],
  20813: [{'device_model': 592,
           'model_description': 'QS250S',
           'product_category': 258,
           'software_versions': {1069314: {'label': 'QMxxx 3.16',
                                           'personalities': [{'description': 'Normal',
                                                              'index': 1,
                                                              'slot_count': 16},
                                                             {'description': 'Simple',
                                                              'index': 2,
                                                              'slot_count': 16}],
                                           'sensor_count': 2,
                                           'supported_parameters': []}}}],
  21075: [{'device_model': 78,
           'model_description': 'Robin 600 LEDWash SmartWhite',
           'product_category': 256,
           'software_versions': {10: {'label': 'Sw.ver. 1.0',
                                      'personalities': [{'description': 'Mode 1',
                                                         'index': 1,
                                                         'slot_count': 24},
                                                        {'description': 'Mode 2',
                                                         'index': 2,
                                                         'slot_count': 16},
                                                        {'description': 'Mode 3',
                                                         'index': 3,
                                                         'slot_count': 12},
                                                        {'description': 'Mode 4',
                                                         'index': 4,
                                                         'slot_count': 10},
                                                        {'description': 'Mode 5',
                                                         'index': 5,
                                                         'slot_count': 0}],
                                      'sensor_count': 2,
                                      'supported_parameters': []}}},
          {'device_model': 118,
           'model_description': 'Robin 600 LEDWash',
           'product_category': 256,
           'software_versions': {22: {'label': 'Sw.ver. 2.2',
                                      'personalities': [{'description': 'Mode 1',
                                                         'index': 1,
                                                         'slot_count': 37},
                                                        {'description': 'Mode 2',
                                                         'index': 2,
                                                         'slot_count': 21},
                                                        {'description': 'Mode 3',
                                                         'index': 3,
                                                         'slot_count': 15},
                                                        {'description': 'Mode 4',
                                                         'index': 4,
                                                         'slot_count': 10},
                                                        {'description': 'Mode 5',
                                                         'index': 5,
                                                         'slot_count': 0}],
                                      'sensor_count': 2,
                                      'supported_parameters': []}}}],
  21324: [{'device_model': 13828,
           'model_description': '3604PWM CV DRIVER Interface',
           'personality_count': 4,
           'product_category': 1289,
           'software_versions': {33816835: {'label': '',
                                            'personalities': [{'description': '',
                                                               'index': 1,
                                                               'slot_count': 0},
                                                              {'description': '',
                                                               'index': 2,
                                                               'slot_count': 1},
                                                              {'description': '',
                                                               'index': 3,
                                                               'slot_count': 1},
                                                              {'description': '',
                                                               'index': 4,
                                                               'slot_count': 3}],
                                            'sensor_count': 4,
                                            'supported_parameters': []}}}],
  21580: [{'device_model': 1,
           'model_description': 'DEC3 Enclosure Control',
           'product_category': 1536,
           'software_versions': {33: {'label': 'Main2.1 and UI2.1',
                                      'personalities': [{'description': 'RDM Monitoring',
                                                         'index': 1,
                                                         'slot_count': 0},
                                                        {'description': 'DMX Lamp Relay Enable',
                                                         'index': 2,
                                                         'slot_count': 1},
                                                        {'description': 'DMX Lamp Fan Heater Rly Enable',
                                                         'index': 3,
                                                         'slot_count': 3}],
                                      'sensor_count': 3,
                                      'supported_parameters': []}}},
          {'device_model': 3,
           'model_description': 'DEC3-MK2 Controller',
           'product_category': 1536,
           'software_versions': {85: {'label': '00.13',
                                      'personalities': [{'description': 'Monitor Mode',
                                                         'index': 1,
                                                         'slot_count': 0},
                                                        {'description': 'Control Mode',
                                                         'index': 2,
                                                         'slot_count': 1},
                                                        {'description': 'Service Mode',
                                                         'index': 3,
                                                         'slot_count': 3}],
                                      'sensor_count': 4,
                                      'supported_parameters': []}}}],
  22355: [{'device_model': 1,
           'model_description': 'W-RDM transmitter',
           'product_category': 257,
           'software_versions': {5505282: {'label': 'Micro RDM T1.6.7',
                                           'personalities': [],
                                           'sensor_count': 0,
                                           'supported_parameters': []}}}],
#          {'device_model': 1,
#           'product_category': 258,
#           'software_versions': {'5570818': {'label': 'Pico RDM U1.6.5',
#                                             'personalities': [],
#                                             'sensor_count': 0,
#                                             'supported_parameters': []}}}],
  25444: [{'device_model': 7882,
           'model_description': '788-LD+ Quad Dimmer Pack v2',
           'product_category': 1281,
           'software_versions': {1296: {'label': '788-LD+ v5.10',
                                        'personalities': [{'description': '8-bit',
                                                           'index': 1,
                                                           'slot_count': 8},
                                                          {'description': '16-bit',
                                                           'index': 2,
                                                           'slot_count': 8}],
                                        'sensor_count': 1,
                                        'supported_parameters': []}}}],
  25972: [{'device_model': 265,
           'model_description': 'Desire Vivid 40',
           'product_category': 257,
           'software_versions': {16908292: {'label': '1.2.0.0.0.04',
                                            'personalities': [{'description': 'Direct',
                                                               'index': 1,
                                                               'slot_count': 9},
                                                              {'description': 'HSI',
                                                               'index': 2,
                                                               'slot_count': 5},
                                                              {'description': 'HSI Plus 7',
                                                               'index': 3,
                                                               'slot_count': 14},
                                                              {'description': 'HSIC',
                                                               'index': 4,
                                                               'slot_count': 6},
                                                              {'description': 'HSIC Plus 7',
                                                               'index': 5,
                                                               'slot_count': 14},
                                                              {'description': 'RGB',
                                                               'index': 6,
                                                               'slot_count': 5},
                                                              {'description': 'RGB Plus 7',
                                                               'index': 7,
                                                               'slot_count': 14},
                                                              {'description': 'Studio',
                                                               'index': 8,
                                                               'slot_count': 5},
                                                              {'description': 'Studio Plus 7',
                                                               'index': 9,
                                                               'slot_count': 14}],
                                            'sensor_count': 9,
                                            'supported_parameters': []}}}],
  31344: [{'device_model': 1,
           'model_description': 'Dummy Model',
           'product_category': 0,
           'software_versions': {1: {'label': 'Dummy Software Version',
                                     'personalities': [{'description': 'Personality 1',
                                                        'index': 1,
                                                        'slot_count': 5},
                                                       {'description': 'Personality 2',
                                                        'index': 2,
                                                        'slot_count': 10},
                                                       {'description': 'Personality 3',
                                                        'index': 3,
                                                        'slot_count': 20}],
                                     'sensor_count': 0,
                                     'supported_parameters': []}}},
          {'device_model': 2,
           'model_description': 'Arduino RGB Mixer',
           'personality_count': 3,
           'product_category': 1288,
           'software_versions': {1: {'label': '1.0',
                                     'personalities': [],
                                     'sensors': [],
                                     'supported_parameters': [112,
                                                              128,
                                                              129,
                                                              130,
                                                              160,
                                                              176,
                                                              224,
                                                              225,
                                                              512,
                                                              513,
                                                              514,
                                                              1029,
                                                              32768]}}}],
}