#!/usr/bin/env python
# coding=utf-8
"""
文件名称：MenuFuncShapeTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/2/26 16:35
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class MenuFuncShapeTestCase(Action, Operation, SystemDiaglog):
    '''放映态复制黏贴形状'''

    def test_main(self):
        '''放映态复制黏贴形状'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        
        path = "BtnShape_Rectangle"
        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertShape")
        self.OneClick(path)
        time.sleep(1)
        self.Click_XY()
        self.MenuPlaying("ItemShape2D", "复制形状失败", num=2, dx=50, dy=50)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()