#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ThumbnailSelectMoreTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/22 17:30
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


class ThumbnailSelectMoreTestCase(Action, Operation, SystemDiaglog):
    '''ctrl多选幻灯片缩略图'''

    def test_main(self):
        '''ctrl多选幻灯片缩略图'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        
        self.OneClick("BtnNewPage")
        self.OneClick("BtnNewPage")
        self.OneClick("BtnNewPage")
        win32api.keybd_event(17, 0, 0, 0)  # num是键位码
        self.ListClickR("PageItem", -1)
        time.sleep(2)
        self.ListClickR("PageItem", -2)
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
        time.sleep(2)
        self.isElementsVisible("IsPageSelected", 0, "选中幻灯片0失败")
        self.isElementsVisible("IsPageSelected", 1, "选中幻灯片1失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()