#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ImageWallShowEditTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/23 11:23
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ImageWallShowEditTestCase(Action, Operation, SystemDiaglog):

    def test_main(self):
        '''进入图片墙设置'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("进入图片墙设置", time.time())

        full_path = SourcePath.File_Image + '"BMP.bmp""GIF.gif""JPEG.jpeg""JPG.jpg""PNG.png"'
        self.OneClick("BtnInsert")
        self.OpenImageWall(full_path)

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.OneClick("BtnStart")
        self.ClickRight_XY()
        self.ListClick("BtnStageRightImageWallSetting")
        self.s_witForImg(SourcePath.File_ImageWall_ShowEdit, 5, "显示图片墙设置界面失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()