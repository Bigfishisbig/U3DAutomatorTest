#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ImageWallNumWarnTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/22 15:59
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ImageWallNumWarnTestCase(Action, Operation, SystemDiaglog):

    def test_main(self):
        '''照片墻提示圖片數'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("照片墻提示圖片數", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.OneClick("BtnInsert")
        self.OpenImageWall(SourcePath.File_Image_bmp)
        self.WaitForElementText("ImageWallWarn", "插入图片墙时,选择的图片数量小于2,无法插入", 5, "圖片墻提示數量小於2失敗")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
