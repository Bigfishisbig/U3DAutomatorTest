#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ThumbnailSelectMuchTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/22 17:41
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath
import win32con, win32api

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ThumbnailSelectMuchTestCase(Action, Operation, SystemDiaglog):
    '''shift多选幻灯片缩略图'''

    def test_main(self):
        '''shift多选幻灯片缩略图'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.OneClick("BtnNewPage")
        self.OneClick("BtnNewPage")
        self.OneClick("BtnNewPage")
        win32api.keybd_event(16, 0, 0, 0)  # shift
        self.ListClickR("PageItem", 0)
        time.sleep(2)
        self.ListClickR("PageItem", -1)
        win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
        time.sleep(2)
        self.isElementsVisible("IsPageSelected", 0, "shift选中幻灯片0失败")
        self.isElementsVisible("IsPageSelected", 1, "shift选中幻灯片1失败")
        self.isElementsVisible("IsPageSelected", 2, "shift选中幻灯片2失败")
        self.isElementsVisible("IsPageSelected", 3, "shift选中幻灯片3失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()