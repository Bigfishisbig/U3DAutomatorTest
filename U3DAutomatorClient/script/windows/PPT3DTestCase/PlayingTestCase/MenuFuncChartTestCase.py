#!/usr/bin/env python
# coding=utf-8
"""
文件名称：MenuFuncChartTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/2/26 16:39
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class MenuFuncChartTestCase(Action, Operation, SystemDiaglog):
    '''放映态菜单图表'''

    def test_main(self):
        '''放映态菜单图表'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        
        path = ["BtnHistogram"]
        names = ["Histogram"]
        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertChart")
        self.OneClick(path[0])
        # self.OneClick("BtnHistogram")
        self.ListClick("BtnChart", 1)
        # self.OneClick("BtnExitChart")

        self.MenuPlaying2("ItemChart", "图表菜单按钮失效", chart_name=names[0])

        time.sleep(2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()