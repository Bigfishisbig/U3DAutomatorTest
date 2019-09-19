#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextParaSettingIndentSpeSymTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/26 19:56
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


class TextParaSettingIndentSpeSymTestCase(Action, Operation, SystemDiaglog):
    '''段落-带编号设置悬挂缩进3cm等于文本之前缩进3cm'''
    def test_main(self):
        '''段落-带编号设置悬挂缩进3cm等于文本之前缩进3cm'''
        # 段落-带编号设置悬挂缩进3cm等于文本之前缩进3cm
        self.OperationSetting()
        self.Init3DPPT()

        self.InputPara()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。\nabcdefghijklmnopqrstuvwxyz.\n123456789。")
        time.sleep(2)
        self.getText()
        self.OneClick("BtnMarks")
        self.OneClick("BtnRowSpacing")
        self.ListClick("BtnSpace")  #
        time.sleep(2)

        self.OneClick("InputFieldIndent")
        time.sleep(1)
        self.InputStr("3")
        # 设置缩进
        # self.WaitForElementText("LabelSpecialFormat", "（无）", 5, "特殊格式设置错误")
        self.OneClick("LabelSpecialFormat")
        time.sleep(3)
        self.OneClick("SpecialFormat_2")
        time.sleep(2)
        self.OneClick("InputFieldSpe")
        time.sleep(1)
        self.InputStr("3")
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.OneClick("BtnParaOK")
        self.s_witForImg(SourcePath.File_Img_Text_Para_Setting_Indent_Spe5, 5, "悬挂缩进小于等于文本之前缩进失败")
        self.endScene(tag)
