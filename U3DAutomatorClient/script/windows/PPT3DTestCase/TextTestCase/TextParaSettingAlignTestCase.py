#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextParaSettingAlignTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/14 14:47
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath
import win32api, win32con

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化为指定的编码格式

class TextParaSettingAlignTestCase(Action, Operation, SystemDiaglog):
    '''段落-设置界面'''
    def test_main(self):
        '''段落-设置界面'''
        # 段落-设置界面
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.OpenParaSetting()

        self.OneClick("AlignLabel")
        self.isElementExist("AlignLeft", "段落设置界面错误")
        self.isElementExist("AlignRight", "段落设置界面错误")
        self.isElementExist("AlignDouble", "段落设置界面错误")
        self.isElementExist("AlignMiddle", "段落设置界面错误")
        self.isElementExist("AlignSep", "段落设置界面错误")
        self.endScene(tag)
