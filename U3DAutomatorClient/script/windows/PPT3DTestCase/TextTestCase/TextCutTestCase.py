#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextCutTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/13 11:37
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

class TextCutTestCase(Action, Operation, SystemDiaglog):
    '''插入文本框-剪切文本框'''
    def test_main(self):
        '''插入文本框-剪切文本框'''
        # 插入文本框-剪切文本框
        self.OperationSetting()
        self.Init3DPPT()
        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertTextBar")
        self.OneClick("BtnInsertTextX")
        self.Click_XY()
        self.InputStr("1234567890")
        PageID = self.getPathValue("Page")  # 获取可变路径
        itemTextID = self.getPathValue("ItemText")
        Xpath = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page" + PageID[0] + "/ItemText/ItemText" + itemTextID[
            1] + "/TextRoot/CharRoot/Text 1"
        print Xpath
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        # 右键
        self.OneClickL(Xpath, 0, 30)
        self.Right()
        time.sleep(1)
        self.isElementExist("BtnStageRight", "右键失效")  # 右键是否成功
        self.ListClick("BtnStageRightCut") #剪切
        time.sleep(2)
        self.isNotElementExistPageID(Xpath, "剪切后该元素依旧存在")
        self.endScene(tag)
