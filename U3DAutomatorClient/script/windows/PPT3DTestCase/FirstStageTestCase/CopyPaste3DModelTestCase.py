#!/usr/bin/env python
# coding=utf-8
"""
文件名称：CopyPaste3DModelTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/2/26 15:48
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class CopyPaste3DModelTestCase(Action, Operation, SystemDiaglog):
    '''复制粘贴3D模型'''

    def test_main(self):
        '''复制粘贴3D模型'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("复制粘贴3D模型", time.time())

        path = SourcePath.File_Insert_3DModel
        self.OneClick("BtnInsert")
        self.Open3DModel(path)

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.CopyPaste2("ItemModel", "3D模型复制粘贴失败")
        # self.RevertAndRecover(SourcePath.File_Insert_JPEG)
        # self.OneClick("BtnStart")
        # self.OneClick("BtnRevert")
        # self.OneClick("BtnStart")
        # self.OneClick("BtnRevert")
        time.sleep(2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()