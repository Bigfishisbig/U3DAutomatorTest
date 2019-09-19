#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ChartPreviewTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/5/22 11:37
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ChartPreviewTestCase(Action, Operation, SystemDiaglog):
    '''图表预览'''
    def test_main(self):
        '''图表预览'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertChart")
        self.OneClick("BtnHistogram")
        self.Move_Pos("BtnChart")
        element = self.getChart2("Histogram")

        self.isElementExistPageID(element, "预览图表失败")
        #取消预览
        self.Move_XY()
        self.isNotElementExistPageID(element, "取消预览失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()