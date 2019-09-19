#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ExitPlayingEscTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/16 19:25
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath
import win32api, win32con


reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ExitPlayingEscTestCase(Action, Operation, SystemDiaglog):
    '''ESC退出放映态'''

    def test_main(self):
        '''ESC退出放映态'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("快捷键退出", time.time())

        self.OneClick("BtnNewPage")
        self.OneClick("BtnNewPage")
        self.OneClick("BtnNewPage")
        self.OneClick("BtnPlaying")
        self.isElementExist("BtnNextPage", "放映失败")

        tag = self.test_main.__doc__ + "_" + self.__class__.__name__ or u"测试" + self.__class__.__name__
        self.startScene(tag)

        win32api.keybd_event(27, 0, 0, 0)  # ESC键位码是17
        win32api.keybd_event(27, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
        self.isNotElementExist("BtnNextPage", "退出失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
