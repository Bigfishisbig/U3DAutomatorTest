#!/usr/bin/env python
# coding=utf-8
"""
文件名称：CopyPasteChartPieTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/7 16:05
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class CopyPasteChartPieTestCase(Action, Operation, SystemDiaglog):
    '''复制粘贴3D图表Pie'''

    def test_main(self):
        '''复制粘贴3D图表Pie'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("复制粘贴3D图表Pie", time.time())

        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertChart")
        self.OneClick("BtnPie")
        # self.OneClick("BtnHistogram")
        self.ListClick("BtnChart", 1)
        # self.OneClick("BtnExitChart")
        
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        
        self.CopyPaste2("ItemChart", "Pie图表复制粘贴失败", chart_name="PieChart")
        time.sleep(2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()