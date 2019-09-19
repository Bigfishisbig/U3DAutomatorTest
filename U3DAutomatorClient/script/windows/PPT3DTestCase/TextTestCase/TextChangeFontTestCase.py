#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextChangeFontTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/13 11:47
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

class TextChangeFontTestCase(Action, Operation, SystemDiaglog):
    '''插入文本框-更换字体'''
    def test_main(self):
        '''插入文本框-更换字体'''
        # 插入文本框-更换字体
        self.OperationSetting()
        self.Init3DPPT()
        self.InputPara()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。\nabcdefghijklmnopqrstuvwxyz.\n123456789。")
        # 切换字体
        PageID = self.getPathValue("Page")  # 获取可变路径
        itemTextID = self.getPathValue("ItemText")
        Xpath = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page" + PageID[0] + "/ItemText/ItemText" + itemTextID[
            1] + "/TextRoot/CharRoot/Text 1"
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.OneClickL(Xpath, 30, 0)
        self.OneClick("BtnFontBar")
        self.OneClick("BtnFontSong")
        self.s_witForImg(SourcePath.File_Img_TextX_Song, 5, "更换宋体失败", accurate=0.4)
        self.endScene(tag)


