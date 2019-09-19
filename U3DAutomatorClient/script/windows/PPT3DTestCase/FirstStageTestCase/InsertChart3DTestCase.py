#!/usr/bin/env python
# coding=utf-8
"""
文件名称：InsertChart3DTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2019/1/7 20:43
修改时间：
软件：PyCharm
"""

from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath
import win32api, win32con

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化为指定的编码格式


class InsertChart3DTestCase(Action, Operation, SystemDiaglog):
    '''插入图表'''

    def test_main(self):
        '''插入图表'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("插入撤销还原图表", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        paths = ["BtnHistogram", "BtnLine", "BtnPie"]
        names = ["Histogram", "LineChart", "PieChart"]
        i=0
        for path in paths:
            self.OneClick("BtnInsert")
            self.OneClick("BtnInsertChart")
            self.OneClick(path)
            self.ListClick("BtnChart", 1)
            # self.OneClick("BtnExitChart")
            element = self.getChart(names[i])
            self.isElementExistPageID(element, "插入图表失败")
            self.OneClick("BtnStart")
            self.OneClick("BtnRevert")
            # element = self.getChart(names[i])
            self.isNotElementExistPageID(element, "撤销失败")
            self.OneClick("BtnStart")
            self.OneClick("BtnRecover")
            element = self.getChart(names[i])
            self.isElementExistPageID(element, "还原失败")
            self.OneClick("BtnStart")
            self.OneClick("BtnRevert")
            time.sleep(2)
            i = i + 1

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()