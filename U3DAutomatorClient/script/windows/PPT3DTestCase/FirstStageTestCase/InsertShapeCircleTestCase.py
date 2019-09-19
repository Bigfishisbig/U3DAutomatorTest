#!/usr/bin/env python
# coding=utf-8
"""
文件名称：InsertShapeCircleTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/7 18:06
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class InsertShapeCircleTestCase(Action, Operation, SystemDiaglog):
    '''插入形状Circle'''

    def test_main(self):
        '''插入形状Circle'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("插入撤销还原形状Circle", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.InsertShape("BtnShape_Circle")
        self.RevertAndRecover(SourcePath.File_Insert_Shape_Circle, "ItemShape2D")
        # self.OneClick("BtnStart")
        # self.OneClick("BtnRevert")
        # self.Move_XY()
        time.sleep(2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()