#!/usr/bin/env python
# coding=utf-8
"""
文件名称：Swipe3DModelTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/22 16:48
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath
from win32api import GetSystemMetrics

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class Swipe3DModelTestCase(Action, Operation, SystemDiaglog):
    '''放映态拖动3D模型'''
    def test_main(self):
        '''放映态拖动3D模型'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  

        path = SourcePath.File_Insert_3DModel
        self.Open3DModel(path)
        self.OneClick("BtnPlaying")
        screen_x = GetSystemMetrics(0)
        screen_y = GetSystemMetrics(1)
        self.Click_XY()
        element = self.getElementPath("ItemModel")
        x, y = self.getCenter(element, "var")
        self.startScene(tag)

        self.Swipe4(screen_x/2, screen_y/2, 100, 100, 0, 0)
        time.sleep(2)
        x2, y2 = self.getCenter(element, "var")
        self.CompareValue(x, x2, "拖动3D模型失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
