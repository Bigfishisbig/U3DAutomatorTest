#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextParaChangeFontTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/14 11:46
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

class TextChangeSize2TestCase(Action, Operation, SystemDiaglog):
    '''段落-更改字体不改变行距A+/A-'''
    def test_main(self):
        '''段落-更改字体不改变行距A+/A-'''
        # 段落-更改字体不改变行距A+/A-
        self.OperationSetting()
        self.Init3DPPT()
        self.InputPara()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。\nabcdefghijklmnopqrstuvwxyz.\n123456789。")
        # 切换字体

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.getText()

        self.TimesClick(["BtnIncreaseFontSize", "BtnIncreaseFontSize", "BtnIncreaseFontSize"], 2)
        self.s_witForImg(SourcePath.File_Img_TextX_Add3, 5, "更换字体大小失败")
        time.sleep(2)
        self.TimesClick(["BtnDecreaseFontSize", "BtnDecreaseFontSize", "BtnDecreaseFontSize",
                         "BtnDecreaseFontSize", "BtnDecreaseFontSize", "BtnDecreaseFontSize", ], 2)
        self.s_witForImg(SourcePath.File_Img_TextX_Sub3, 5, "更换字体大小失败")
        self.endScene(tag)
