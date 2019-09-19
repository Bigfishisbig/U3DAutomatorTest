#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ShapeLineTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/22 19:16
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ShapeLineTestCase(Action, Operation, SystemDiaglog):
    '''线条不支持更改形状'''

    def test_main(self):
        '''线条不支持更改形状'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.InsertShape("BtnShape_Line")
        self.OneClick("BtnShapeChange")
        # self.isElementExist("ShapeChangeDlg", "更改形状窗口未出现")
        self.OneClick("BtnShape_Circle")
        self.s_witForImg(SourcePath.File_Insert_Shape_Line, 10, "线条形状不应支持更改形状")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
