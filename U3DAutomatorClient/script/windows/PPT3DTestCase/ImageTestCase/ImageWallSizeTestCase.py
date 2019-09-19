#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ImageWallSizeTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/22 19:32
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ImageWallSizeTestCase(Action, Operation, SystemDiaglog):

    def test_main(self):
        '''等比缩放'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("等比縮放", time.time())

        full_path = SourcePath.File_Image + '"BMP.bmp""GIF.gif""JPEG.jpeg""JPG.jpg""PNG.png"'
        self.OneClick("BtnInsert")
        self.OpenImageWall(full_path)

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        time.sleep(1)
        # 等比縮放
        self.Swipe2(ElementOne="BtnDragball0", ElementTwo="BtnDragball0", x2=100, y2=100, sleeptime=1)
        time.sleep(2)
        self.Swipe2(ElementOne="BtnDragball0", ElementTwo="BtnDragball0", x2=-100, y2=-100, sleeptime=1)
        self.s_witForImg(SourcePath.File_Insert_IMAGEWALL, 30, "等比缩放失敗")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()