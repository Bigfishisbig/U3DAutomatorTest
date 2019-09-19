#!/usr/bin/env python
# coding=utf-8
"""
文件名称：InsertShapeLabelTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/7 18:57
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class InsertShapeLabelTestCase(Action, Operation, SystemDiaglog):
    '''插入形状Label'''

    def test_main(self):
        '''插入形状Label'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("插入撤销还原形状Label", time.time())


        # self.OneClick("BtnInsert")
        # self.OneClick("BtnInsertShape")
        # self.OneClick("BtnShape_Label")
        # time.sleep(1)
        # self.Click_XY(dx=0, dy=-200)

        # self.s_witForImg(SourcePath.File_Insert_Shape_Label, 5, "插入形状Label失败")
        # self.OneClick("BtnStart")
        # self.OneClick("BtnRevert")
        # self.Move_XY()
        # self.s_witForImg(SourcePath.File_Img_FullScreen, 5, "撤销形状失败")
        # self.OneClick("BtnStart")
        # self.OneClick("BtnRecover")
        # self.Move_XY()
        # self.s_witForImg(SourcePath.File_Insert_Shape_Label, 5, "还原形状Label失败")
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.InsertShape("BtnShape_Label")
        self.RevertAndRecover(SourcePath.File_Insert_Shape_Label, "ItemShape2D")
        # self.OneClick("BtnStart")
        # self.OneClick("BtnRevert")
        # self.Move_XY()
        time.sleep(2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()