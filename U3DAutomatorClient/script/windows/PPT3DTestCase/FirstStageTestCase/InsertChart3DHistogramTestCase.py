#!/usr/bin/env python
# coding=utf-8
"""
文件名称：InsertChart3DHistogramTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/7 17:27
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class InsertChart3DHistogramTestCase(Action, Operation, SystemDiaglog):
    '''插入3D图表柱形'''

    def test_main(self):
        '''插入3D图表柱形'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("插入撤销还原柱状图", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.InsertChart("BtnHistogram")
        element = self.getChart("Histogram")
        self.isElementExistPageID(element, "插入图表失败")
        self.OneClick("BtnStart")
        self.OneClick("BtnRevert")
        # element = self.getChart(names[i])
        self.isNotElementExistPageID(element, "撤销失败")
        self.OneClick("BtnStart")
        self.OneClick("BtnRecover")
        element = self.getChart("Histogram")
        self.isElementExistPageID(element, "还原失败")
        # self.OneClick("BtnStart")
        # self.OneClick("BtnRevert")
        time.sleep(2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()