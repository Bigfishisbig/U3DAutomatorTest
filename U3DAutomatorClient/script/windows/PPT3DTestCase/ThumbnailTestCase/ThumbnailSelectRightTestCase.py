#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ThumbnailSelectRightTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/22 17:21
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ThumbnailSelectRightTestCase(Action, Operation, SystemDiaglog):
    '''右键幻灯片缩略图显示菜单'''

    def test_main(self):
        '''右键幻灯片缩略图显示菜单'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        
        self.ListClickR("PageItem", 0)
        # self.isElementsVisible("IsPageSelected", -1, "未选中新建的幻灯片")
        self.isElementExist("BtnStageRight", "右键缩略图菜单失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()