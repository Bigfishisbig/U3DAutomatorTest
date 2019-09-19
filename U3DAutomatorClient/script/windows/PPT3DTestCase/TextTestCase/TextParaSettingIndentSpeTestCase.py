#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextParaSettingIndentSpeTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/26 16:42
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

class TextParaSettingIndentSpeTestCase(Action, Operation, SystemDiaglog):
    '''段落-设置界面打开特殊格式下拉框'''
    def test_main(self):
        '''段落-设置界面打开特殊格式下拉框'''
        # 段落-设置界面打开特殊格式下拉框
        self.OperationSetting()
        self.Init3DPPT()
        self.OpenParaSetting() # 打开段落设置界面

        # 设置缩进
        # self.WaitForElementText("LabelSpecialFormat", "（无）", 5, "特殊格式设置错误")
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__
        self.startScene(tag)
        self.OneClick("LabelSpecialFormat")
        time.sleep(3)
        self.isElementExist("SpecialFormat_0", "特殊格式下拉框打开失败")
        self.isElementExist("SpecialFormat_1", "特殊格式下拉框打开失败")
        self.isElementExist("SpecialFormat_2", "特殊格式下拉框打开失败")

        self.endScene(tag)

