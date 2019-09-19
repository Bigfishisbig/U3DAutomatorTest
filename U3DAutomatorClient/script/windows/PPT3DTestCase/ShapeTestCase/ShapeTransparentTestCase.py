#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ShapeTransparentTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/22 19:37
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ShapeTransparentTestCase(Action, Operation, SystemDiaglog):
    '''更改形状透明度'''

    def test_main(self):
        '''更改形状透明度'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        
        self.InsertShape("BtnShape_Rectangle")
        self.OneClick("BtnShapeFillMore")
        self.OneClick("TransparentText")
        self.InputStr("50")
        self.Click_XY()
        self.s_witForImg(SourcePath.File_Shape_Transparent, 10, "更改透明度失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()