#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ImageWallDistanceTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/22 17:35
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ImageWallDistanceTestCase(Action, Operation, SystemDiaglog):

    def test_main(self):
        '''图片墙远近调整'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("圖片墻遠近調整", time.time())

        full_path = SourcePath.File_Image + '"BMP.bmp""GIF.gif""JPEG.jpeg""JPG.jpg""PNG.png"'
        self.OneClick("BtnInsert")
        self.OpenImageWall(full_path)
        time.sleep(2)
        # 遠近調整
        self.Swipe2(ElementOne="BtnMoveStep", ElementTwo="BtnMoveStep", x2=0, y2=50, sleeptime=1)
        time.sleep(2)
        self.Swipe2(ElementOne="BtnMoveStep", ElementTwo="BtnMoveStep", x2=0, y2=-50, sleeptime=1)
        self.s_witForImg(SourcePath.File_Insert_IMAGEWALL, 30, "遠近調整失敗")
        # 繞x軸調整
        self.Swipe2(ElementOne="BtnRotateByXAxis", ElementTwo="BtnRotateByXAxis", x2=0, y2=300, sleeptime=1)
        time.sleep(2)
        self.Swipe2(ElementOne="BtnRotateByXAxis", ElementTwo="BtnRotateByXAxis", x2=0, y2=-300, sleeptime=1)
        self.s_witForImg(SourcePath.File_Insert_IMAGEWALL, 30, "绕X轴調整失敗")
        # 繞y軸調整
        self.Swipe2(ElementOne="BtnRotateByYAxis", ElementTwo="BtnRotateByYAxis", x2=500, y2=0, sleeptime=1)
        time.sleep(2)
        self.Swipe2(ElementOne="BtnRotateByYAxis", ElementTwo="BtnRotateByYAxis", x2=-500, y2=0, sleeptime=1)
        self.s_witForImg(SourcePath.File_Insert_IMAGEWALL, 30, "绕Y轴調整失敗")
        # 繞z軸調整
        self.Swipe2(ElementOne="BtnRotateByZAxis", ElementTwo="BtnRotateByZAxis", x2=0, y2=300, sleeptime=1)
        time.sleep(2)
        self.Swipe2(ElementOne="BtnRotateByZAxis", ElementTwo="BtnRotateByZAxis", x2=0, y2=-300, sleeptime=1)
        self.s_witForImg(SourcePath.File_Insert_IMAGEWALL, 30, "绕Z轴調整失敗")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
