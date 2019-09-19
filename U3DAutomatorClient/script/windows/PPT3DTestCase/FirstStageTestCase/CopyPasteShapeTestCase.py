#!/usr/bin/env python
# coding=utf-8
"""
文件名称：PlayingCopyPasteShapeTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/9 17:24
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class CopyPasteShapeTestCase(Action, Operation, SystemDiaglog):
    '''复制粘贴形状'''

    def test_main(self):
        '''复制粘贴形状'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("复制形状", time.time())

        paths = ["BtnShape_Line", "BtnShape_Rectangle", "BtnShape_Circle", "BtnShape_Arrow", "BtnShape_Add",
                 "BtnShape_Process", "BtnShape_Start"]
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        for path in paths:
            self.OneClick("BtnInsert")
            self.OneClick("BtnInsertShape")
            self.OneClick(path)
            time.sleep(1)
            self.Click_XY()
            self.CopyPasteImage("ItemShape2D", "复制形状失败", num=2, dx=30, dy=30)
            # self.OneClick("BtnStart")
            # self.OneClick("BtnRevert")
            # self.OneClick("BtnStart")
            # self.OneClick("BtnRevert")
            time.sleep(2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
