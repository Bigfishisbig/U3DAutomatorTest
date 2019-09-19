#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ExitPlayingRightTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/16 19:11
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ExitPlayingRightTestCase(Action, Operation, SystemDiaglog):
    '''右键退出放映态'''

    def test_main(self):
        '''右键退出放映态'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("右键退出放映", time.time())

        self.OneClick("BtnNewPage")
        self.OneClick("BtnNewPage")
        self.OneClick("BtnNewPage")
        self.OneClick("BtnPlaying")
        self.isElementExist("BtnNextPage", "放映失败")

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.ClickRight_XY()
        self.ListClick("BtnPlayingRight", 2)
        self.isNotElementExist("BtnNextPage", "退出失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
