#!/usr/bin/env python
# coding=utf-8
"""
文件名称：OpenDlgTransitionsTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/2/27 16:27
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class OpenDlgTransitionsTestCase(Action, Operation, SystemDiaglog):
    '''打开转场动效弹窗'''

    def test_main(self):
        '''打开转场动效弹窗'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.OneClick("BtnTransition")
        self.isElementExist("DlgTransition", "打开转场动效弹窗失败", 10)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()