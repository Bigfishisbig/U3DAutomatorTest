#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextParaIndentSym2TestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/14 11:08
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

class TextParaIndentSym2TestCase(Action, Operation, SystemDiaglog):
    '''段落-减少缩进不带编号的光标所在的段落'''
    def test_main(self):
        '''段落-减少缩进不带编号的光标所在的段落'''
        # 段落-减少缩进不带编号的光标所在的段落
        self.OperationSetting()
        self.Init3DPPT()
        self.InputPara() # 在文本框内输入一段文字
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。\nabcdefghijklmnopqrstuvwxyz.\n123456789。")
        # win32api.keybd_event(13, 0, 0, 0)
        # win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
        # self.InputStr(u"哈哈哈哈哈哈哈哈哈哈哈")
        time.sleep(2)
        # 切换行间距
        self.getText()  # 选中文本框

        # 增加缩进
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.OneClick("BtnIncIndent")
        self.s_witForImg(SourcePath.File_Img_Text_Para_Indent_6, 5, "段落增加缩进失败")
        time.sleep(2)
        # 减少缩进
        self.s_clickImg(SourcePath.File_Img_Text_Para_Indent_6, 5, "输入文字错误")
        self.OneClick("BtnDecIndent")
        self.s_witForImg(SourcePath.File_Img_Text_Para_Indent_8, 5, "段落减少缩进失败")
        self.endScene(tag)
