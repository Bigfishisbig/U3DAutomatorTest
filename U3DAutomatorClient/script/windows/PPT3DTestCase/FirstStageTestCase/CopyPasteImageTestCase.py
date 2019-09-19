#!/usr/bin/env python
# coding=utf-8
"""
文件名称：PlayingCopyPasteImageTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/9 15:25
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class CopyPasteImageTestCase(Action, Operation, SystemDiaglog):
    '''复制粘贴图片'''

    def test_main(self):
        '''复制粘贴图片'''
        self.OperationSetting()
        self.Init3DPPT()

        self.SetTag("复制图片", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        images = [SourcePath.File_Image_bmp, SourcePath.File_Image_gif, SourcePath.File_Image_jpeg,
                  SourcePath.File_Image_jpg, SourcePath.File_Image_png]
        for image in images:
            self.OneClick("BtnInsert")
            self.OpenImage(image)
            self.CopyPasteImage("ItemImageComp", "复制粘贴失败")
            # self.RevertAndRecover(SourcePath.File_Insert_JPEG)
            # self.OneClick("BtnStart")
            # self.OneClick("BtnRevert")
            # self.OneClick("BtnStart")
            # self.OneClick("BtnRevert")
            time.sleep(2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
