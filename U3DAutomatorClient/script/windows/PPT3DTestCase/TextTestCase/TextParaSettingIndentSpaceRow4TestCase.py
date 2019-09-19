#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextParaSettingIndentSpaceRow2TestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/28 10:29
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


class TextParaSettingIndentSpaceRow4TestCase(Action, Operation, SystemDiaglog):
    '''段落-行距-固定值行距'''
    def test_main(self):
        '''段落-行距-固定值行距'''
        # 段落-行距-固定值行距
        self.OperationSetting()
        self.Init3DPPT()
        self.OpenParaSetting()
        # 设置行距
        # self.WaitForElementText("LabelSpecialFormat", "（无）", 5, "特殊格式设置错误")
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.OneClick("InputFieldParaSpace")
        time.sleep(1)
        self.OneClick("RowSpace4")
        self.WaitForElementText("InputFieldParaSpace2", "19.2磅", 5, "固定值行距设置失败")
        self.endScene(tag)