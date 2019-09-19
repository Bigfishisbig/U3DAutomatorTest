#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ThumbnailRightStageTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/22 18:50
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ThumbnailRightStageTestCase(Action, Operation, SystemDiaglog):
    '''右键幻灯片缩略图菜单选项'''

    def test_main(self):
        '''右键幻灯片缩略图菜单选项'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        
        self.ListClickR("PageItem", 0)
        self.WaitForElementText_list("BtnStageRightCopy", "复制", 10, "右键菜单无复制", 0)
        self.WaitForElementText_list("BtnStageRightCut", "剪切", 10, "右键菜单无剪切", 0)
        # self.WaitForElementText_list("BtnStageRightPaste2", "<color=#BEBEBEFF>粘贴</color>", 10, "右键菜单无粘贴")
        self.isElementPathExist("BtnStageRightPaste", "右键菜单无粘贴", 10)
        self.WaitForElementText_list("BtnStageRightNewPage", "新建幻灯片", 10, "右键菜单无新建幻灯片")
        self.WaitForElementText_list("BtnStageRightDel", "删除", 10, "右键菜单无删除")
        # self.WaitForElementText_list("BtnStageRightEditTrans2", "<color=#BEBEBEFF>修改转场特效</color>", 10, "右键菜单无修改转场效果")
        self.isElementPathExist("BtnStageRightEditTrans2", "右键菜单无修改转场效果", 10)
        self.WaitForElementText_list("BtnStageRightChangeBK", "背景更换", 10, "右键菜单无更换背景")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
