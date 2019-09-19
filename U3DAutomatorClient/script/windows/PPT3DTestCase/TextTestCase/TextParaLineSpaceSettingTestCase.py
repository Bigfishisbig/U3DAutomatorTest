#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextParaLineSpaceSettingTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/14 11:56
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

class TextParaLineSpaceSettingTestCase(Action, Operation, SystemDiaglog):
    '''段落-设置界面'''
    def test_main(self):
        '''段落-设置界面'''
        # 段落-设置界面
        self.OperationSetting()
        self.Init3DPPT()
        self.InputPara()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。\nabcdefghijklmnopqrstuvwxyz.\n123456789。")
        # win32api.keybd_event(13, 0, 0, 0)
        # win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
        # self.InputStr(u"哈哈哈哈哈哈哈哈哈哈哈"))
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.OneClick("BtnRowSpacing")
        self.ListClick("BtnSpace")  #

        self.s_witForImg(SourcePath.File_Img_Text_Para_LineSpace_Setting, 5, "段落行距设置界面出错")
        self.OneClick("BtnPlaying")
        time.sleep(2)
        self.isElementExist("ParaContainer", "行距设置界面存在时依然可以操作其他功能")
        # self.OneClick("BtnStart")

        self.Swipe3("ParaContainerClose", 500, 0, -100, 0)

        self.s_witForImg(SourcePath.File_Img_Text_typeWord, 5, "行距设置界面拖动失败")
        self.endScene(tag)






