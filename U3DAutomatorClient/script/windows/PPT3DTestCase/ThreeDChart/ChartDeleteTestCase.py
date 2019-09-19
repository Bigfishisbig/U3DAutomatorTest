#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ChartDeleteTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/5/24 17:00
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ChartDeleteTestCase(Action, Operation, SystemDiaglog):
    '''删除图表值'''
    def test_main(self):
        '''删除图表值'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        
        self.InsertChart("BtnHistogram")
        e = self.getChartContent()
        # self.OneClickV(e[1])
        self.ListClick("ChartTableCell_6")
        # self.key_event("del")
        win32api.keybd_event(46, 0, 0, 0)
        win32api.keybd_event(46, 0, win32con.KEYEVENTF_KEYUP, 0)
        self.WaitForElementText_list("ChartTableCell_6", "", 5, "删除后值错误")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
