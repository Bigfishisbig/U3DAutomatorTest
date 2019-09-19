#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ImageBorderPanelTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/18 14:13
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ImageBorderPanelTestCase(Action, Operation, SystemDiaglog):
    '''图片边框修改面板'''

    def test_main(self):
        '''图片边框修改面板'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("边框粗细调节面板", time.time())

        self.OneClick("BtnInsert")
        self.OpenImage(SourcePath.File_Image_bmp)
        self.OneClick("BtnFormat")

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.ListClick("BorderStyleItem", 1)
        self.OneClick("BtnBorderFactor")
        self.isElementExist("ThickPanel", "粗细调节面板未出现")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
