#!/usr/bin/env python
# coding=utf-8
"""
文件名称：InsertTextBGTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/12/18 15:53
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化为指定的编码格式

class InsertTextBGTestCase(Action, Operation, SystemDiaglog):
    '''插入文字背景'''

    def test_main(self):
        '''插入文字背景'''
        #插入文本框-文字背景
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("文字背景", time.time())

        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertTextBar")
        self.SetTag("文字背景", str(time.time()))

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.OneClick("BtnInsertTextBG")
        self.OneClick("BG_Text_1")
        self.s_witForImg(SourcePath.File_Img_Text_BGEditor, 5, "文字背景创建失败")

        self.EndTag("", str(time.time()))
        time.sleep(2)
        self.EndTag("")
        self.s_witForImg(SourcePath.File_Img_Text_BGSetting, 5, "文字背景创建失败")
