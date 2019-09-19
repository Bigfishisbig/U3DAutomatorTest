#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextTypeWordTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/12 17:32
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化为指定的编码格式

class TextTypeWordTestCase(Action, Operation, SystemDiaglog):
    '''插入文本框-文本框输入文字'''
    def test_main(self):
        '''插入文本框-文本框输入文字'''
        #插入文本框-文本框输入文字
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertTextBar")
        self.OneClick("BtnInsertTextBG")
        self.OneClick("BG_Text_1")
        self.Click_XY(dx=-200)
        # self.s_clickImg(SourcePath.File_Img_Text_BGEditor, 5, "文字背景创建失败", 0.8, 100, 200)
        self.isElementExist("TextFormatShow")
        # self.s_witForImg(SourcePath.File_Img_Text_DefWord, 5, "文本框默认文字失败")
        path = self.getText2()
        # self.WaitForElementTextV(path, "单击以编辑文本框内容", 5, "文本里默认文字失败")
        time.sleep(2)
        self.OneClickV(path)
        time.sleep(1)
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。\nabcdefghijklmnopqrstuvwxyz.\n123456789。")

        # self.WaitForElementTextV(path, "黑夜给了你黑色的眼睛，你却用它来寻找光明。\nabcdefghijklmnopqrstuvwxyz.\n123456789。", 5, "文本里输入文字失败")
        element = self.getText2()
        self.isElementExistPageID(element, "输入文字失败")
        # self.s_witForImg(SourcePath.File_Img_Text_typeWord, 5, "输入文字失败")
        self.endScene(tag)
