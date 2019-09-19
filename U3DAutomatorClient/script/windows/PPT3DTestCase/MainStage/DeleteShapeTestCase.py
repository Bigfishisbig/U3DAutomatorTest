#!/usr/bin/env python
# coding=utf-8
"""
文件名称：DeleteShapeTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/26 15:14
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class DeleteShapeTestCase(Action, Operation, SystemDiaglog):
    '''右键删除形状'''

    def test_main(self):
        '''右键删除形状'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__


        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertShape")
        self.OneClick("BtnShape_Line")
        time.sleep(1)
        self.Click_XY()
        self.startScene(tag)
        self.DelElement2("ItemShape2D", "Line删除失败", num=2, dx=30, dy=30)
        time.sleep(2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()