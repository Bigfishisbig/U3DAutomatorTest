#!/usr/bin/env python
# coding=utf-8
"""
文件名称：PlayingCopyPasteChartPieTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/7 11:59
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class PlayingCopyPasteChartPieTestCase(Action, Operation, SystemDiaglog):
    '''放映态复制黏贴饼图'''
    def test_main(self):
        '''放映态复制黏贴饼图'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  


        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertChart")
        self.OneClick("BtnPie")
        # self.OneClick("BtnHistogram")
        self.ListClick("BtnChart", 1)
        # self.OneClick("BtnExitChart")
        self.startScene(tag)
        self.CopyPastePlaying2("ItemChart", "Pie图表复制删除失败", chart_name="PieChart")
        time.sleep(2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
