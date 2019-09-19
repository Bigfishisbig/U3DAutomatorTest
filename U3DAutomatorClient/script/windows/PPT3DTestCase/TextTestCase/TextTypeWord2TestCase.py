#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextTypeWord2TestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/13 10:41
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化为指定的编码格式

class TextTypeWord2TestCase(Action, Operation, SystemDiaglog):
    '''插入无背景文本框-文本框输入中文、英文'''
    def test_main(self):
        '''插入无背景文本框-文本框输入中文、英文'''
        #插入无背景文本框-文本框输入中文、英文
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.InputPara()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。\nabcdefghijklmnopqrstuvwxyz.\n123456789。")
        self.s_witForImg(SourcePath.File_Img_Text_typeWord, 5, "输入文字错误")
        self.s_witForImg(SourcePath.File_Img_Text_BGSetting, 5, "菜单显示文本设置菜单失败")
        self.endScene(tag)
