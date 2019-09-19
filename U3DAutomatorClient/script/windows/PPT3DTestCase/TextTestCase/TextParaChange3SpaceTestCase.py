#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextParaChange3SpaceTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/14 11:19
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

class TextParaChange3SpaceTestCase(Action, Operation, SystemDiaglog):
    '''段落-改变光标所在行间距为3.0'''
    def test_main(self):
        '''段落-改变光标所在行间距为3.0'''
        # 段落-改变光标所在行间距为3.0
        self.OperationSetting()
        self.Init3DPPT()
        self.InputPara()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。\nabcdefghijklmnopqrstuvwxyz.\n123456789。")
        time.sleep(2)
        # 切换行间距
        # self.getText() # 选中文本框
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__
        self.startScene(tag)
        self.OneClick("BtnRowSpacing")
        self.ListClick("BtnSpace3.0")
        self.s_witForImg(SourcePath.File_Img_Text_Para_LineSpace_Change_30, 5, "更改行间距为3.0失败", 0.4)
        self.endScene(tag)
