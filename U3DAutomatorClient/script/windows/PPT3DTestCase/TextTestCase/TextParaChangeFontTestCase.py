#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextParaChangeFontTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/14 11:46
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

class TextParaChangeFontTestCase(Action, Operation, SystemDiaglog):
    '''段落-更改字体不改变行距'''
    def test_main(self):
        '''段落-更改字体不改变行距'''
        # 段落-更改字体不改变行距
        self.OperationSetting()
        self.Init3DPPT()
        self.InputPara()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。\nabcdefghijklmnopqrstuvwxyz.\n123456789。")
        # win32api.keybd_event(13, 0, 0, 0)
        # win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
        # self.InputStr(u"哈哈哈哈哈哈哈哈哈哈哈")
        time.sleep(2)
        # 切换行间距
        self.getText()
        # PageID = self.getPathValue("Page")  # 获取可变路径
        # itemTextID = self.getPathValue("ItemText")
        # Xpath = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page" + PageID[0] + "/ItemText/ItemText" + itemTextID[
        #     1] + "/TextRoot/CharRoot/Text 1"
        # self.OneClickL(Xpath, 2, 0)
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.OneClick("BtnRowSpacing")
        self.ListClick("BtnSpace2")
        # self.s_witForImg(SourcePath.File_Img_Text_Para_LineSpace_Change_30, 5, "更改行间距为3.0失败")
        self.OneClick("BtnFontBar")
        self.OneClick("BtnFontSong")
        self.s_witForImg(SourcePath.File_Img_Text_Para_Font, 5, "段落更改字体失败", 0.4)
        self.endScene(tag)

