#!/usr/bin/env python
# coding=utf-8
"""
文件名称：CutPasteElementTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/11 13:47
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath
import win32api, win32con

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class CutPasteElementTestCase(Action, Operation, SystemDiaglog):
    '''剪切元素'''

    def test_main(self):
        '''剪切元素'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("元素剪切粘贴", time.time())

        btns = [["BtnInsertTextBar", "BtnInsertTextX" ], ["BtnInsertImageBar", "BtnInsertImage"], ["BtnInsertVideo"],
                ["BtnInsertAudio"], ["BtnInsertChart", "BtnHistogram"], ["BtnInsertShape", "BtnShape_Rectangle"]]  # 插入元素
        # 查询关键字的字典
        dict1 = {"BtnInsertTextBar": "ItemText",
                 "BtnInsertImageBar": "ItemImageComp",
                 "BtnInsertVideo": "ItemVideo",
                 "BtnInsertAudio": "ItemAudio",
                 "BtnInsertChart": "ItemChart",
                 "BtnInsertShape": "ItemShape2D",
                 }
        # 查询关键字的结果的字典
        dict2 = {}
        for btn in btns:
            self.OneClick("BtnInsert")
            self.TimesClick(btn)
            if btn[0] == "BtnInsertTextBar":  # 文本
                # self.InputPara()
                self.Click_XY()
                self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。\nabcdefghijklmnopqrstuvwxyz.\n123456789。")
            if btn[0] == "BtnInsertImageBar":  # 图片
                self.inputDlgClick("#32770", u"选择文件", [("ComboBoxEx32", 0), ("ComboBox", 0), ("Edit", 0)],
                                   SourcePath.File_Image_bmp, "Button")  # 输入路径点击打开
            if btn[0] == "BtnInsertVideo":  #  视频
                self.inputDlgClick("#32770", u"选择文件",[("ComboBoxEx32", 0), ("ComboBox", 0), ("Edit", 0)],
                                   SourcePath.File_Video_3gp, "Button")  # 输入路径点击打开
            if btn[0] == "BtnInsertAudio":  # 音频
                self.inputDlgClick("#32770", u"选择文件",[("ComboBoxEx32", 0), ("ComboBox", 0), ("Edit", 0)],
                                   SourcePath.File_Audio_ape, "Button")  # 输入路径点击打开
            if btn[0] == "BtnInsertChart":  # 图表
                self.ListClick("BtnChart", 1)
                # self.OneClick("BtnExitChart")
            if btn[0] == "BtnInsertShape":
                self.Click_XY()
                # self.OneClick("BtnInsert")
                # self.OneClick("BtnInsertShape")
                # self.OneClick("BtnShape_Rectangle")
                # self.engine.swipe_press(start_x=830, start_y=530, end_x=900, end_y=600, steps=1, duration=1)
            time.sleep(2)
            # 将查询的结果的最后一个输入字典
            numbers = len(self.getPathValue(dict1[btn[0]]))
            print btn[0], "=", numbers
            dict2[btn[0]] = numbers

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        # 全选元素
        time.sleep(2)
        # self.engine.click(720, 450)
        # time.sleep(1)
        win32api.keybd_event(17, 0, 0, 0)  # ctrl
        win32api.keybd_event(65, 0, 0, 0)  # A
        win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(3)
        # 剪切
        win32api.keybd_event(17, 0, 0, 0)  # ctrl
        win32api.keybd_event(88, 0, 0, 0)  # X
        win32api.keybd_event(88, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(5)
        # PageID2 = self.getPathValue("Page")
        # PageID = PageID2[0]
        # #print "PageID:", PageID
        for key in dict1.keys():
            # #print "value:", value
            # path = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page%s/%s" % (PageID, value)
            # self.isNotElementExistPageID(path, "剪切元素剪切失败")
            num = len(self.getPathValue(dict1[key]))
            print num, ":", dict2[key]
            if num == dict2[key]:
                assert False, "剪切元素%s失败"%key
            else:
                pass
        time.sleep(2)
        # 粘贴
        win32api.keybd_event(17, 0, 0, 0)  # ctrl
        win32api.keybd_event(86, 0, 0, 0)  # V
        win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(5)
        # PageID = self.getPathValue("Page")[0]
        # PageID2 = self.getPathValue("Page")
        # PageID = PageID2[0]
        # #print "PageID:", PageID
        for key in dict1.keys():
            # path = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page%s/%s" % (PageID, value)
            # path = path.encode('unicode-escape').decode('string_escape')
            self.Click_XY()
            num = len(self.getPathValue(dict1[key]))
            if num == dict2[key]:
                pass
            else:
                assert False, "粘贴元素失败"
            # self.isElementExistPageID(path, "粘贴元素失败")
            # self.OneClickL(path)


        self.endScene(tag)
        time.sleep(1)
        self.EndTag()

