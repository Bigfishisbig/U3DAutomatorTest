#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ShapeLineTypeCircleTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/22 20:01
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ShapeLineTypeCircleTestCase(Action, Operation, SystemDiaglog):
    '''更改轮廓线为圆点'''

    def test_main(self):
        '''更改轮廓线为圆点'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        
        self.InsertShape("BtnShape_Rectangle")
        self.OneClick("BtnShapeOutlineMore")
        self.ListClick("OutlineWidth")
        self.ListClick("LineWidthItem6")  # 更改宽度
        self.OneClick("BtnShapeOutlineMore")
        self.ListClick("OutlineType")
        self.ListClick("LineTypeItem2")  # 更改类型
        self.Click_XY(dy=200)
        self.s_witForImg(SourcePath.File_Shape_LineType_Circle, 10, "更改圆点类型失败", 0.4)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()