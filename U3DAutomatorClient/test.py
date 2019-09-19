# -*- coding: utf-8 -*-
import sys
#print "这是个python实例123"
#print "abcdefghijklmnopqrstuvwxyz"
from artsdk import uimonitor as uim
from selenium import webdriver

# defaultencoding = 'utf-8'
# if sys.getdefaultencoding() != defaultencoding:
#     reload(sys)
#     sys.setdefaultencoding(defaultencoding)
#
# scene_name = "test_CEF"
# uim.Init()
# uim.CaseStart({'type': 1,
#                'scene_name':scene_name,
#                'scene_id': 23,
#                'work_mode':'art-cap',
#                'params':{"window":{"location_only":0},
#                          'similarity':0.85,
#                          'steady_time': 10,
#                          'time_out': 30,
#                          'rect_info': 'monitor: 0-0-500-500'
#                          }
#                })
# print(uim.SetCurrentlyAsStartTime())
# # uim.ReadCaseResult()
# #uim.CaseStart({'scene_name':scene_name, 'work_mode':'art-cap', 'params':{'similarity':0.85, 'steady_time': 5, 'time_out': 20}})
# print(uim.ReadCaseResult())


browser = webdriver.Chrome()
