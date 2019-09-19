#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ChartTableAddColumnTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/5/24 18:30
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ChartTableAddColumnTestCase(Action, Operation, SystemDiaglog):
    '''图表添加列'''
    def test_main(self):
        '''图表添加列'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        
        self.InsertChart("BtnHistogram")
        self.OneClick("AddTypeDropdown")
        self.OneClick("AddTypeColumn")
        self.OneClick("AddBtn")
        self.isElementNum("ChartColumn", 5)


        self.endScene(tag)
        time.sleep(1)
        self.EndTag()