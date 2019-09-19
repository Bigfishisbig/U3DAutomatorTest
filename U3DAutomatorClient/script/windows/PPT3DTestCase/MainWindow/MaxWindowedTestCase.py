#!/usr/bin/env python
# coding=utf-8
"""
文件名称：MaxWindowedTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/14 14:26
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class MaxWindowedTestCase(Action, Operation, SystemDiaglog):
    '''窗口最大化与恢复'''
    def test_main(self):
        '''窗口最大化与恢复'''
        self.OperationSetting()
        # self.Init3DPPT()
        self.SetTag("窗口最大化与恢复", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        if self.isVisible("BtnMaxmize") == False:
            # self.DoubleClick("FileName")
            self.OneClick("BtnWindowmize")
            self.isElementVisible("BtnMaxmize", "窗口化失败")
        else:
            # self.DoubleClick("FileName")
            self.OneClick("BtnMaxmize")
            self.isNotElementVisible("BtnMaxmize", "最大化失败")


        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
