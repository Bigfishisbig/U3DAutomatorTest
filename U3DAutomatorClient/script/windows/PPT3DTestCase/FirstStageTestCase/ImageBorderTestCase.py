#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ImageBorderTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/18 11:49
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ImageBorderTestCase(Action, Operation, SystemDiaglog):
    '''图片边框设置'''

    def test_main(self):
        '''图片边框设置'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("图片边框设置", time.time())

        self.OneClick("BtnInsert")
        self.OpenImage(SourcePath.File_Image_bmp)
        self.OneClick("BtnFormat")

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        border_path = [SourcePath.File_Image_Border_1, SourcePath.File_Image_Border_2, SourcePath.File_Image_Border_3]
        for i in range(3):
            self.ListClick("BorderStyleItem", 0-1-i)
            self.s_witForImg(border_path[0-1-i], 5, "边框设置失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
