#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ScaleNormalQuitPlayingTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/5/21 16:41
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ScaleNormalQuitPlayingTestCase(Action, Operation, SystemDiaglog):
    '''退出放映还原比例'''
    def test_main(self):
        '''退出放映还原比例'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("退出放映还原比例", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.OneClick("BtnDecScale")
        self.OneClick("BtnPlaying")
        time.sleep(1)
        win32api.keybd_event(27, 0, 0, 0)  # ESC键位码是17
        win32api.keybd_event(27, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
        self.WaitForElementText("TextScaleValue", "99%", 5, "缩小比例失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()