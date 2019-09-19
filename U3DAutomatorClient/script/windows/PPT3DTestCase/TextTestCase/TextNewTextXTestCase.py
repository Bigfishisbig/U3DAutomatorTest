#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextNewTextXTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/7 11:51
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化为指定的编码格式

class TextNewTextXTestCase(Action, Operation, SystemDiaglog):
    '''插入文本框_横排'''
    def test_main(self):
        '''插入文本框_横排'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__
        self.startScene(tag)
        self.InputPara()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。")
        self.s_witForImg(SourcePath.File_Img_TextX, 5, "文本不在编辑态")
        self.s_witForImg(SourcePath.File_Img_Text_BGSetting, 5, "菜单显示文本设置菜单失败")
        self.endScene(tag)
        # PageID = self.getPathValue("Page")  # 获取可变路径
        # itemTextID = self.getPathValue("ItemText")
        # Xpath = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page" + PageID[0] + "/ItemText/ItemText" + itemTextID[
        #     1] + "/TextRoot/CharRoot/Text 1"
        # print Xpath
        # self.OneClick("BtnStart")
        # self.s_clickImg(SourcePath.File_Img_Text_newX, 5, "无此文本",0.8, 0, 100)
        # self.s_witForImg(SourcePath.File_Img_Text_newX, 5, "创建文本失败")
        # 关闭java虚拟机
        # self.closeJVM()
