#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ImageWallMaxNumTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/22 16:10
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


class ImageWallMaxNumTestCase(Action, Operation, SystemDiaglog):

    def test_main(self):
        '''图片前最大数量图片'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("圖片墻最大數量圖片", time.time())

        self.OneClick("BtnInsert")
        full_path = SourcePath.File_Image
        full_path2 = '"BMP1.bmp""GIF1.gif""JPEG1.jpeg""JPG1.jpg""PNG1.png"' \
                                             '"BMP2.bmp""GIF2.gif""JPEG2.jpeg""JPG2.jpg""PNG2.png"' \
                                             '"BMP3.bmp""GIF3.gif""JPEG3.jpeg""JPG3.jpg""PNG3.png"' \
                     '"BMP.bmp""GIF.gif""JPEG.jpeg""JPG.jpg""PNG.png"' \
                     '"Panorama.jpg"'
        self.OneClick("BtnInsert")
        self.SetTag("插入图片墙", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        # self.OpenImageWall(full_path)
        self.OneClick("BtnInsertImageBar")
        self.OneClick("BtnInsertImageListImageWall")
        self.OneClick("BtnImageWallConfirm")
        time.sleep(1)
        self.inputDlgClick("#32770", u"选择文件", [("ComboBoxEx32", 0), ("ComboBox", 0), ("Edit", 0)], full_path,
                           "Button")  # 输入路径点击打开
        self.inputDlgClick("#32770", u"选择文件", [("ComboBoxEx32", 0), ("ComboBox", 0), ("Edit", 0)], full_path2,
                           "Button")  # 输入路径点击打开
        time.sleep(1)
        # win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
        # win32api.keybd_event(65, 0, 0, 0)  # v键位码是86
        # win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
        # win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
        # time.sleep(1)
        # win32api.keybd_event(13, 0, 0, 0)  # v键位码是86
        # win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
        self.WaitForElementText("ImageWallWarn", "图片总数大于20,无法插入", 10, "圖片墻提示最大數量失敗")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
