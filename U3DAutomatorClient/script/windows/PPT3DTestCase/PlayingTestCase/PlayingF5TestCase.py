#!/usr/bin/env python
# coding=utf-8
"""
文件名称：PlayingF5TestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/2/25 16:52
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


class PlayingF5TestCase(Action, Operation, SystemDiaglog):
    '''放映态退出_F5'''

    def test_main(self):
        '''放映态退出_F5'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  

        self.OneClick("BtnNewPage")
        self.OneClick("BtnNewPage")
        self.OneClick("BtnNewPage")
        self.startScene(tag)
        self.ListClick("PageItem1")
        # self.OneClick("BtnPlaying")
        win32api.keybd_event(116, 0, 0, 0)  # F5键位码是116
        win32api.keybd_event(116, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
        s = self.getPathValue("Page")
        path = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page%s" % s[0]
        time.sleep(5)
        if self.isVisibleV(path):
            pass
        else:
            assert False, "F5快捷播放失败"

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
