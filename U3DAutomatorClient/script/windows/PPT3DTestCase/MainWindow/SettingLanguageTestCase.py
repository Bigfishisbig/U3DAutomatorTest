#!/usr/bin/env python
# coding=utf-8
"""
文件名称：SettingLanguageTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/17 11:36
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class SettingLanguageTestCase(Action, Operation, SystemDiaglog):
    '''设置语言'''
    def test_main(self):
        '''设置语言'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("设置语言", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.TimesClick(["BtnSetting", "BtnPublicSetup", "LanguageSetup", "LanguageDropDown", "English", "BtnSettingOK"], 1)
        self.WaitForElementText_Language("LanguageText", "Start", 5, "英语语言切换失败")
        time.sleep(1)
        self.TimesClick(
            ["BtnSetting", "BtnPublicSetup", "LanguageSetup", "LanguageDropDown", "HardChinese", "BtnSettingOK"], 1)
        self.WaitForElementText_Language("LanguageText", "開始", 5, "繁体语言切换失败")
        time.sleep(1)
        self.TimesClick(
            ["BtnSetting", "BtnPublicSetup", "LanguageSetup", "LanguageDropDown", "SimpleChinese", "BtnSettingOK"], 1)
        self.WaitForElementText_Language("LanguageText", "开始", 5, "简体语言切换失败")
        time.sleep(1)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()