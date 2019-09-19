#!/usr/bin/env python
# coding=utf-8
"""
文件名称：SelectOneChartTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/20 15:48
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class SelectOneChartTestCase(Action, Operation, SystemDiaglog):
    '''选中3D图表'''

    def test_main(self):
        '''选中3D图表'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("单选图表", time.time())

        self.InsertChart("BtnLine")

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        
        element = self.getChart("LineChart")
        self.OneClickL(element, 2, 0)
        self.OneClickRightV(element)
        # self.Click_XY()
        self.isElementVisible("BtnDragball0", "选中元素失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()