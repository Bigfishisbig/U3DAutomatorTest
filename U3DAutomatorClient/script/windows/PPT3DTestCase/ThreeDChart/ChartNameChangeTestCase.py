#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ChartNameChangeTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/5/24 16:24
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ChartNameChangeTestCase(Action, Operation, SystemDiaglog):
    '''图表标题更改'''
    def test_main(self):
        '''图表标题更改'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        
        self.InsertChart("BtnHistogram")
        e = self.getChartContent()
        self.OneClick("ChartOptionToggleTitle")
        self.ThreeClick("ChartTitleInputField")
        self.InputStr(u"图例标题")
        self.OneClick("ChartConfirmAll")

        self.WaitForElementText("ChartTitleInputField", "图例标题", 5, "改变表名错误")


        self.endScene(tag)
        time.sleep(1)
        self.EndTag()