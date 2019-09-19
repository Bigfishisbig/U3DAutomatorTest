#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ImageWallsEditTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/23 11:02
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


class ImageWallsEditTestCase(Action, Operation, SystemDiaglog):

    def test_main(self):
        '''多选图片墙不能编辑'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("多选图片墙不编辑", time.time())

        full_path = SourcePath.File_Image + '"BMP.bmp""GIF.gif""JPEG.jpeg""JPG.jpg""PNG.png"'
        self.OneClick("BtnInsert")
        self.OpenImageWall(full_path)
        time.sleep(5)
        self.OneClick("BtnInsert")
        self.OpenImageWall(full_path)

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        
        win32api.keybd_event(17, 0, 0, 0)  # ctrl
        win32api.keybd_event(65, 0, 0, 0)  # A
        win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
        self.s_witForImg(SourcePath.File_ImageWall_WallShow, 5, "多选图片墙编辑界面异常")


        self.endScene(tag)
        time.sleep(1)
        self.EndTag()