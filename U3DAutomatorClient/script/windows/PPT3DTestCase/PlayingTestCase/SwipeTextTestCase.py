#!/usr/bin/env python
# coding=utf-8
"""
文件名称：SwipeTextTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/22 15:00
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class SwipeTextTestCase(Action, Operation, SystemDiaglog):
    '''放映态拖动文本框'''
    def test_main(self):
        '''放映态拖动文本框'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  

        self.InputPara()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。\nabcdefghijklmnopqrstuvwxyz.\n123456789。")
        self.OneClick("BtnPlaying")
        element = self.getText2()
        self.OneClickL(element, 30, 0)
        w, h = self.WidthAndHeight(element, "var")
        x, y = self.getCenter(element, "var")
        # self.Swipe(element, element, 1, 1, w/2+300, 0, w/2+30, 0,ElementType="var")
        self.startScene(tag)

        self.Swipe3(element, w/2+100, 0, w/2+30, 0, ElementType="var")
        time.sleep(2)
        x2, y2 = self.getCenter(element, "var")
        self.CompareValue(x, x2, "拖动失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()