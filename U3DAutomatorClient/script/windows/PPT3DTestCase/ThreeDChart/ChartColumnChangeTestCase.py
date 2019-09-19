#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ChartColumnChangeTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/5/22 15:24
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ChartColumnChangeTestCase(Action, Operation, SystemDiaglog):
    '''改变图表柱'''
    def test_main(self):
        '''改变图表柱'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.InsertChart("BtnHistogram")
        e = self.getChartContent()
        self.ListClickV(str(e[0]))
        self.WaitForElementText_list("ChartTableCell_6", "1", 5, "初始值不为1")
        self.Swipe(ElementOne=str(e[1]), ElementTwo=str(e[1]), y2=-100, ElementType="var")
        self.WaitForElementNotText_list("ChartTableCell_6", "1", 5, "改变后值为1")


        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
