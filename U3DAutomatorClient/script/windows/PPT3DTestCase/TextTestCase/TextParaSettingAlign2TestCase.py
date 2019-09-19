#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextParaSettingAlign2TestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/14 14:59
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

class TextParaSettingAlign2TestCase(Action, Operation, SystemDiaglog):
    '''段落-设置界面-对齐方式'''
    def test_main(self):
        '''段落-设置界面-对齐方式'''
        # 段落-设置界面-对齐方式
        self.OperationSetting()
        self.Init3DPPT()
        self.OpenParaSetting()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.OneClick("AlignBar")
        self.OneClick("AlignRight")
        self.WaitForElementText("AlignLabel", "右对齐", 5, "设置对齐方式失败")
        self.OneClick("BtnParaOK")
        self.s_witForImg(SourcePath.File_Img_Text_Para_Setting_Align_Right, 5, "右对齐失败", 0.4)
        self.endScene(tag)



