#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ThumbnailZoomTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/5/21 18:13
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ThumbnailZoomTestCase(Action, Operation, SystemDiaglog):
    '''幻灯片缩略图缩放'''

    def test_main(self):
        '''幻灯片缩略图缩放'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        x, y = self.WidthAndHeight("PageItem")
        self.OneClick("PageItem")
        win32api.keybd_event(17, 0, 0, 0)  # num是键位码
        for i in range(1500):
            self.mouse_wheel(-1)  # 向下滚动
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
        x2, y2 = self.WidthAndHeight("PageItem")
        self.CompareValue(x, x2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()