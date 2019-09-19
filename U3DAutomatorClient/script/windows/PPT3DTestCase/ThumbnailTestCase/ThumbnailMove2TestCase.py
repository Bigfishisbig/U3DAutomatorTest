#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ThumbnailMove2TestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/22 18:18
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ThumbnailMove2TestCase(Action, Operation, SystemDiaglog):
    '''拖动幻灯片缩略图到栏外'''

    def test_main(self):
        '''拖动幻灯片缩略图到栏外'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__
        self.startScene(tag)
        
        self.OneClick("BtnNewPage")
        self.OneClick("BtnNewPage")
        self.OpenImage(SourcePath.File_Image_bmp)
        self.Swipe2("PageItem3", 0, "PageItem1", 0, 0, -200, 0, 0)
        # self.Swipe_List()
        self.ListClick("PageItem1")  #
        self.s_witForImg(SourcePath.File_Insert_BMP, 10, "拖动幻灯片到栏外效果失效")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
