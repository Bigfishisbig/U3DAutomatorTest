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

class TextNewTextYTestCase(Action, Operation, SystemDiaglog):
    '''插入文本框-竖排'''
    def test_main(self):
        '''插入文本框-竖排'''
        # 插入文本框-竖排
        self.OperationSetting()
        self.Init3DPPT()
        self.OneClick("BtnInsert")
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.OneClick("BtnInsertTextBar")
        self.OneClick("BtnInsertTextY")
        self.Click_XY()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。")
        self.s_witForImg(SourcePath.File_Img_TextY, 5, "文本不是编辑态" ,accurate=0.4)
        self.s_witForImg(SourcePath.File_Img_Text_BGSetting, 5, "菜单显示文本设置菜单失败")
        self.endScene(tag)
        # PageID = self.getPathValue("Page")  # 获取可变路径
        # itemTextID = self.getPathValue("ItemText")
        # Xpath = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page" + PageID[0] + "/ItemText/ItemText" + itemTextID[
        #     1] + "/TextRoot/CharRoot/Text 1"
        # print Xpath
        # self.OneClick("BtnStart")
        # self.s_clickImg(SourcePath.File_Img_Text_newY, 5, "无此文本", 0.8, 50, 0)
        # self.s_witForImg(SourcePath.File_Img_Text_newY, 5, "创建文本失败")



