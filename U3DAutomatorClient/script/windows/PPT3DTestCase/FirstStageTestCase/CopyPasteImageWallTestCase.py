#!/usr/bin/env python
# coding=utf-8
"""
文件名称：PlayingCopyPasteImageWallTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/9 16:08
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class CopyPasteImageWallTestCase(Action, Operation, SystemDiaglog):
    '''复制粘贴图片墙'''

    def test_main(self):
        '''复制粘贴图片墙'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("复制图片墙", time.time())

        images = SourcePath.File_Image + '"BMP.bmp""GIF.gif""JPEG.jpeg""JPG.jpg""PNG.png"'

        self.OneClick("BtnInsert")
        self.OpenImageWall(images)

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)


        self.CopyPasteImage("PhotoWallComp", "复制粘贴失败", 2)
        # self.RevertAndRecover(SourcePath.File_Insert_JPEG)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()