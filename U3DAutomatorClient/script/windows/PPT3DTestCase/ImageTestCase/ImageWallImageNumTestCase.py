#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ImageWallImageNumTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/23 11:32
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ImageWallImageNumTestCase(Action, Operation, SystemDiaglog):

    def test_main(self):
        '''图片墙默认图片数量'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("图片墙默认图片数量", time.time())

        full_path = SourcePath.File_Image + '"BMP.bmp""GIF.gif""JPEG.jpeg""JPG.jpg""PNG.png"'
        self.OneClick("BtnInsert")
        self.OpenImageWall(full_path)

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.WaitForElementText("TextImageCount", "5/20", 10, "图片墙图片数量异常")
        self.ListClick("ItemImageWallClose")
        self.WaitForElementText("TextImageCount", "4/20", 10, "图片墙图片数量异常")
        self.OneClick("BtnImageWallMore")
        self.OneClick("BtnAddImage")
        self.inputDlgClick("#32770", u"选择文件", [("ComboBoxEx32", 0), ("ComboBox", 0), ("Edit", 0)], full_path,
                           "Button")  # 输入路径点击打开
        self.WaitForElementText("TextImageCount", "9/20", 10, "图片墙图片数量异常")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()