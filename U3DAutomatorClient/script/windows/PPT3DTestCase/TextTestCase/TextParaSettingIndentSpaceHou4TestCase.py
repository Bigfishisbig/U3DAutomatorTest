#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextParaSettingIndentSpaceQianTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/26 20:31
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


class TextParaSettingIndentSpaceHou4TestCase(Action, Operation, SystemDiaglog):
    '''段落-段后设置减少'''
    def test_main(self):
        '''段落-段后设置减少'''
        # 段落-段后设置减少
        self.OperationSetting()
        self.Init3DPPT()
        self.InputPara()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。\nabcdefghijklmnopqrstuvwxyz.\n123456789。")
        # win32api.keybd_event(13, 0, 0, 0)
        # win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
        # self.InputStr(u"哈哈哈哈哈哈哈哈哈哈哈")
        time.sleep(2)
        self.s_clickImg(SourcePath.File_Img_Text_Para_Setting_Indent_Para3, 5, "无此文本")
        time.sleep(2)
        self.OneClick("BtnRowSpacing")
        self.ListClick("BtnSpace")
        # 设置段前
        # self.WaitForElementText("LabelSpecialFormat", "（无）", 5, "特殊格式设置错误")
        self.OneClick("InputFieldPara2")
        time.sleep(1)
        self.InputStr("100")
        time.sleep(2)
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.OneClick("ParaHouSub")
        time.sleep(2)
        self.WaitForElementText("InputFieldPara2", "94磅", 5, "段后减少按钮失效")
        self.endScene(tag)
