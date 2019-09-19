#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextParaSymPreviewTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/13 19:04
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

class TextParaSymPreviewTestCase(Action, Operation, SystemDiaglog):
    '''段落-预览符号'''
    def test_main(self):
        '''段落-预览符号'''
        # 段落-预览符号
        self.OperationSetting()
        self.Init3DPPT()
        self.InputPara()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。\nabcdefghijklmnopqrstuvwxyz.\n123456789。")
        self.getText()
        # self.s_witForImg(SourcePath.File_Img_Text_Para_Setting, 5, "文本段落打开失败")
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        # 标志符号
        self.OneClick("BtnMarksBar")
        self.isElementVisible("BtnMarksNull", "标志段落符号不为空")
        time.sleep(1)
        self.Move_Pos("BtnMarks1")
        self.s_witForImg(SourcePath.File_Img_Text_Para_Sym_Marks, 5, "标志符号预览失败", accurate=0.4)
        self.Move_Pos("BtnMarks1", 0, -100)
        self.s_witForImg(SourcePath.File_Img_Text_Para_Sym_NoSym, 5, "还原为原有符号失败", accurate=0.4)
        # 数字符号
        self.OneClick("BtnIdentifierBar")
        self.isElementVisible("BtnIdentifierNull", "数字段落符号不为空")
        time.sleep(1)
        self.Move_Pos("BtnIdentifier1")
        self.s_witForImg(SourcePath.File_Img_Text_Para_Sym_Identifier, 5, "数字符号预览失败", accurate=0.4)
        self.Move_Pos("BtnIdentifier1", 0, -100)
        self.s_witForImg(SourcePath.File_Img_Text_Para_Sym_NoSym, 5, "还原为原有符号失败", accurate=0.4)
        self.endScene(tag)


