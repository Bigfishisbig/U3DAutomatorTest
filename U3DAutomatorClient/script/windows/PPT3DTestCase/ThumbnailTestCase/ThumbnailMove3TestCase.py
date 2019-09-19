#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ThumbnailMove3TestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/22 18:45
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


class ThumbnailMove3TestCase(Action, Operation, SystemDiaglog):
    '''拖动多张幻灯片缩略图'''

    def test_main(self):
        '''拖动多张幻灯片缩略图'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        
        self.OneClick("BtnNewPage")
        self.OneClick("BtnNewPage")
        self.OpenImage(SourcePath.File_Image_bmp)
        self.ListClick("PageItem", -1)
        win32api.keybd_event(17, 0, 0, 0)  # num是键位码
        # self.ListClick("PageItem", -1)
        time.sleep(1)
        self.ListClick("PageItem", -2)
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
        self.Swipe2("PageItem", -1, "PageItem", 0, 0, 30, 0, 0)
        # self.Swipe_List()
        self.ListClick("PageItem", -1)  #
        self.s_witForImg(SourcePath.File_Insert_BMP, 10, "拖动多张幻灯片缩略图失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()