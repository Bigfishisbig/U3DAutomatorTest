#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextParaSettingCloseTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/28 10:55
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


class TextParaSettingCloseTestCase(Action, Operation, SystemDiaglog):
    '''段落-关闭设置'''
    def test_main(self):
        '''段落-关闭设置'''
        # 段落-关闭设置
        self.OperationSetting()
        self.Init3DPPT()
        self.OpenParaSetting()
        # 设置行距
        # self.WaitForElementText("LabelSpecialFormat", "（无）", 5, "特殊格式设置错误")
        time.sleep(5)
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.OneClick("ParaContainerClose")
        self.isNotElementExist("ParaContainer", "关闭段落设置界面失败")
        self.endScene(tag)
