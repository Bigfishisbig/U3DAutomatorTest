#!/usr/bin/env python
# coding=utf-8
"""
文件名称：CopyPasteShapeArrowTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/7 16:47
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class CopyPasteShapeArrowTestCase(Action, Operation, SystemDiaglog):
    '''复制粘贴形状Arrow'''

    def test_main(self):
        '''复制粘贴形状Arrow'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("形状Arrow复制粘贴", time.time())

        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertShape")
        self.OneClick("BtnShape_Arrow")
        time.sleep(1)
        self.Click_XY()
        
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        
        self.CopyPasteImage("ItemShape2D", "Arrow复制形状失败", num=2, dx=30, dy=30)
        time.sleep(2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()