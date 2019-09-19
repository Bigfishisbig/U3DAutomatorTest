#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextParaSettingIndentTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/14 15:07
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

class TextParaSettingIndentTestCase(Action, Operation, SystemDiaglog):
    '''段落-设置界面-填写缩进'''
    def test_main(self):
        '''段落-设置界面-填写缩进'''
        # 段落-设置界面-填写缩进
        self.OperationSetting()
        self.Init3DPPT()
        # self.OpenParaSetting() # 打开段落设置界面
        self.InputPara()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。\nabcdefghijklmnopqrstuvwxyz.\n123456789。")
        time.sleep(2)
        self.OneClick("BtnRowSpacing")
        self.ListClick("BtnSpace")  #
        # 设置缩进
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.WaitForElementText("LabelSpecialFormat", "（无）", 5, "特殊格式设置错误")
        self.OneClick("InputFieldIndent")
        self.InputStr("14")
        self.OneClick("BtnParaOK")
        self.s_witForImg(SourcePath.File_Img_Text_Para_Setting_Indent_14cm, 5, "文本缩进设置失败")
        self.endScene(tag)
