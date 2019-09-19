#!/usr/bin/env python
# coding=utf-8
"""
文件名称：SettingFloatTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/17 11:10
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class SettingFloatTestCase(Action, Operation, SystemDiaglog):
    '''设置模块浮动'''
    def test_main(self):
        '''设置模块浮动'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("设置模块浮动", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.InputPara()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。")
        path = self.getText2()
        self.DoubleClickL(path, -20, 0)
        self.isElementExist("FloatTool", "浮动工具栏显示失败1")
        self.OneClickL(path, -20)
        self.OneClickRightV(path)  # 定位在文字处
        self.isElementExist("FloatTool", "浮动工具栏显示失败2")

        self.TimesClick(["BtnSetting", "BtnPublicSetup", "CommonSetup", "STEnableBySelect", "STEnableByRightMenu", "BtnSettingOK"],1)

        self.DoubleClickL(path, -20, 0)
        self.isNotElementExist("FloatTool", "无浮动工具栏显示失败1")
        self.OneClickL(path, -20)
        self.OneClickRightV(path)  # 定位在文字处
        self.isNotElementExist("FloatTool", "无浮动工具栏显示失败2")

        self.TimesClick(["BtnSetting", "BtnPublicSetup", "CommonSetup", "STEnableBySelect", "STEnableByRightMenu", "BtnSettingOK"])

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
