#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextDefWordTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/12 17:22
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化为指定的编码格式

class TextDefWordTestCase(Action, Operation, SystemDiaglog):
    '''插入文本框-文本框默认文字'''
    def test_main(self):
        '''插入文本框-文本框默认文字'''
        #插入文本框-文本框默认文字
        self.OperationSetting()
        self.Init3DPPT()
        # self.cmdCommand(SourcePath.File_PCPA + " --STARTSCENE('插入文本框-文字默认文字')")


        self.OneClick("BtnInsert")
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.OneClick("BtnInsertTextBar")
        self.OneClick("BtnInsertTextBG")
        self.OneClick("BG_Text_1")
        # self.s_clickImg(SourcePath.File_Img_Text_BGEditor, 5, "文字背景创建失败", 0.8, 100, 300)
        # self.s_witForImg(SourcePath.File_Img_Text_DefWord, 5, "文本框默认文字失败")
        self.isElementExist("TextFormatShow")

        # self.cmdCommand(SourcePath.File_PCPA + " --ENDSCENE('插入文本框-文字背景')")

        self.endScene(tag)

