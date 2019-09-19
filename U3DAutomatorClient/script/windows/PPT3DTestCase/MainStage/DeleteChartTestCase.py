#!/usr/bin/env python
# coding=utf-8
"""
文件名称：DeleteChartTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/26 15:16
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class DeleteChartTestCase(Action, Operation, SystemDiaglog):
    '''右键删除图表'''

    def test_main(self):
        '''右键删除图表'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("右键删除图表", time.time())

        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertChart")
        self.OneClick("BtnHistogram")
        self.ListClick("BtnChart", 1)

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.DelElement("ItemChart", "Histogram图表删除失败", chart_name="Histogram")
        time.sleep(2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()