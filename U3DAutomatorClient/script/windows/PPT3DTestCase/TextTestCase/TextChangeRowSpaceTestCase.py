#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextChangeRowSpaceTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/13 15:34
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

class TextChangeRowSpaceTestCase(Action, Operation, SystemDiaglog):
    '''插入文本框-倾斜'''
    def test_main(self):
        '''插入文本框-倾斜'''
        # 插入文本框-改变行间距
        self.OperationSetting()
        self.Init3DPPT()
        self.InputPara()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。\nabcdefghijklmnopqrstuvwxyz.\n123456789。")
        # 切换行间距

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__ 
        self.startScene(tag)
        self.getText()
        self.OneClick("BtnRowSpacing")
        self.ListClick("BtnSpace2")
        self.s_witForImg(SourcePath.File_Img_TextX_RowSpacing, 5, "行间距2.0失败")
        self.endScene(tag)
