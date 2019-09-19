#!/usr/bin/env python
# coding=utf-8
"""
文件名称：test.py
作者：ycy
版本：PPTPro
创建时间：2019/3/18 19:55
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath
import os

from script.windows.PPT3DSetting import SourcePath
# print os.path.dirname(SourcePath.SourcePath.current_file_directory()+"\\report")

print SourcePath.SourcePath.current_file_directory()
