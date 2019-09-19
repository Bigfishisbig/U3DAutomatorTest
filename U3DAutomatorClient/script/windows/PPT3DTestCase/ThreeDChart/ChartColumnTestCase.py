#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ChartColumnTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/5/22 14:20
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ChartColumnTestCase(Action, Operation, SystemDiaglog):
    '''图表柱显示'''
    def test_main(self):
        '''图表柱显示'''

        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.InsertChart("BtnHistogram")
        # self.ListDoubleClick("ChartTableCell_5")
        e = self.getChartContent()
        self.ListClickV(str(e[0]))
        self.isElementExistPageID(str(e[1]))

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
