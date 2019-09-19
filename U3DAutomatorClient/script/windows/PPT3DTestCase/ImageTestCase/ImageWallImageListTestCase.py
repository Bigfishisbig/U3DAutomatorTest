#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ImageWallImageListTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/24 16:08
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ImageWallImageListTestCase(Action, Operation, SystemDiaglog):

    def test_main(self):
        '''图片墙图片列表'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("图片墙图片列表", time.time())

        full_path = SourcePath.File_Image + '"BMP.bmp""GIF.gif""JPEG.jpeg""JPG.jpg""PNG.png"'
        self.OneClick("BtnInsert")
        self.OpenImageWall(full_path)

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.s_witForImg(SourcePath.File_ImageWall_ImageList_Down, 5, "下拉按钮依旧置灰")
        self.OneClick("ImageListDown")
        self.s_witForImg(SourcePath.File_ImageWall_ImageList_Up, 5, "上拉按钮置灰")
        self.OneClick("ImageListUp")
        self.OneClick("ImageListMore")
        self.s_witForImg(SourcePath.File_ImageWall_ImageList_More, 5, "按钮未置灰")
        # self.OneClick("ImageListMore")
        # 图片拖拽
        self.Swipe2("ItemImageWall", -5, "ItemImageWall", -5, -100)
        self.s_witForImg(SourcePath.File_ImageWall_ImageList_Swipe, 5, "拖拽图片失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()