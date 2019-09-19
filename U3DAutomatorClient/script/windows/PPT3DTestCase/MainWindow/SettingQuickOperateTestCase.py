#!/usr/bin/env python
# coding=utf-8
"""
文件名称：SettingQuickOperateTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/5/13 17:33
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class SettingQuickOperateTestCase(Action, Operation, SystemDiaglog):
    '''快捷操作验证'''
    def test_main(self):
        '''快捷操作验证'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("快捷操作验证", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.TimesClick(
            ["BtnSetting", "BtnPublicSetup", "CommonSetup", "BasicOperationOption", "BtnSettingOK"],
            1)
        self.InsertShape("BtnShape_Rectangle")
        i = 0
        while self.engine.find_element(self.PPT3DPath["BtnRotateByXAxisDown"]) is None and i < 5:
            i += 1
            time.sleep(1)
            # print "this is :",self.engine.find_element(self.PPT3DPath[Element])
        if self.engine.find_element(self.PPT3DPath["BtnRotateByXAxisDown"]):
            pass
            self.TimesClick(
                ["BtnSetting", "BtnPublicSetup", "CommonSetup", "BasicOperationOption", "BtnSettingOK"],
                1)
        else:
            self.TimesClick(
                ["BtnSetting", "BtnPublicSetup", "CommonSetup", "BasicOperationOption", "BtnSettingOK"],
                1)
            assert False, "快捷键出现失败"



        self.endScene(tag)
        time.sleep(1)
        self.EndTag()