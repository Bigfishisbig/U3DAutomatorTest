#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ImageBorderClearTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/18 13:54
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ImageBorderClearTestCase(Action, Operation, SystemDiaglog):
    '''清除图片边框'''

    def test_main(self):
        '''清除图片边框'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("清除边框", time.time())

        self.OneClick("BtnInsert")
        self.OpenImage(SourcePath.File_Image_bmp)

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.OneClick("BtnFormat")
        self.OneClick("BtnClearBorder")
        self.s_witForImg(SourcePath.File_Image_Border_Clear, 5, "清除图片边框失败", accurate=0.5)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()