#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextParaSettingIndentSpaceQian3TestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/26 20:46
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


class TextParaSettingIndentSpaceQian5TestCase(Action, Operation, SystemDiaglog):
    '''段落-段前设置增加最大'''
    def test_main(self):
        '''段落-段前设置增加最大'''
        # 段落-段前设置增加最大
        self.OperationSetting()
        self.Init3DPPT()
        self.OpenParaSetting()
        # 设置段前
        # self.WaitForElementText("LabelSpecialFormat", "（无）", 5, "特殊格式设置错误")
        self.OneClick("InputFieldPara1")
        time.sleep(1)
        self.InputStr("5")
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.OneClick("ParaQianSub")
        time.sleep(2)
        self.WaitForElementText("InputFieldPara1", "0磅", 5, "段前减少按钮失效")
        self.OneClick("ParaQianSub")
        time.sleep(2)
        self.WaitForElementText("InputFieldPara1", "0磅", 5, "段前减少按钮失效")
        self.endScene(tag)
