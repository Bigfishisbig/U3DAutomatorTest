#!/usr/bin/env python
# coding=utf-8
"""
文件名称：InsertTextXTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/12/18 15:41
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


class InsertTextXTestCase(Action, Operation, SystemDiaglog):
    '''插入横排文本'''

    # 插入横排文本元素的操作
    def test_main(self):
        '''插入横排文本'''
        self.OperationSetting()
        self.Init3DPPT()

        self.SetTag("文本框横排文字")

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.InputPara()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。")
        self.s_witForImg(SourcePath.File_Img_TextX, 5, "文本不在编辑态")
        self.s_witForImg(SourcePath.File_Img_Text_BGSetting, 5, "菜单显示文本设置菜单失败")
        self.OneClick("BtnStart")
        if self.getText() != -999:
            pass
        else:
            assert False, "输入文本失败"
        self.OneClick("BtnStart")
        self.OneClick("BtnRevert")
        if self.getText() == -999:
            pass
        else:
            assert False, "撤销失败"
        self.OneClick("BtnStart")
        self.OneClick("BtnRecover")
        if self.getText() != -999:
            pass
        else:
            assert False, "还原失败"

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
