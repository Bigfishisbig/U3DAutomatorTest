#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextParaSettingIndentSpe2TestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/26 17:03
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

class TextParaSettingIndentSpe2TestCase(Action, Operation, SystemDiaglog):
    '''段落-设置界面打开特殊格式下拉框选中首行缩进'''
    def test_main(self):
        '''段落-设置界面打开特殊格式下拉框选中首行缩进'''
        # 段落-设置界面打开特殊格式下拉框选中首行缩进
        self.OperationSetting()
        self.Init3DPPT()
        self.OpenParaSetting() # 打开段落设置界面

        # 设置缩进
        # self.WaitForElementText("LabelSpecialFormat", "（无）", 5, "特殊格式设置错误")
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__ 
        self.startScene(tag)
        self.OneClick("LabelSpecialFormat")
        time.sleep(3)
        self.OneClick("SpecialFormat_1")
        self.WaitForElementText("LabelSpecialFormat", "首行缩进", 5, "首行缩进失败")

        self.endScene(tag)
        # self.OneClick("BtnParaOK")
        # self.s_witForImg(SourcePath.File_Img_Text_Para_Setting_Indent_14cm, 5, "文本缩进设置失败")
        #
        #
