#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ImageWallPlayingTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/23 15:35
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ImageWallPlayingTestCase(Action, Operation, SystemDiaglog):

    def test_main(self):
        '''图片墙放映'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("图片墙放映", time.time())


        full_path = SourcePath.File_Image + '"BMP.bmp""GIF.gif""JPEG.jpeg""JPG.jpg""PNG.png"'
        self.OneClick("BtnInsert")
        self.OpenImageWall(full_path)
        # self.s_witForImg(SourcePath.File_Insert_IMAGEWALL, 5, "插入图片墙失败")
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        time.sleep(2)
        self.OneClick("BtnPlaying")
        time.sleep(5)
        self.s_clickImg(SourcePath.File_ImageWall_SelectImage, 5, "图片墙中无此图片")
        self.s_witForImg(SourcePath.File_Insert_JPEG, 5, "图片墙主视图播放失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
