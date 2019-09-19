#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ChartDeleteMuchTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/5/24 18:11
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ChartDeleteMuchTestCase(Action, Operation, SystemDiaglog):
    '''删除图表多个值'''
    def test_main(self):
        '''删除图表多个值'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.InsertChart("BtnHistogram")
        e = self.getChartContent()
        self.ListClick("ChartTableCell_6")
        self.down_keyevent("left_control")
        self.ListClick("ChartTableCell_4")
        self.up_keyevent("left_control")
        self.key_event("del")
        self.WaitForElementText("ChartTableCell_6", "", 5, "删除后值错误")
        self.WaitForElementText("ChartTableCell_4", "", 5, "删除后值错误")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()