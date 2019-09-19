#!/usr/bin/env python
# coding=utf-8
"""
文件名称：CloseFileRemindTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/20 10:51
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class CloseFileRemindTestCase(Action, Operation, SystemDiaglog):
    '''关闭文件保存提醒'''
    def test_main(self):
        '''关闭文件保存提醒'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("关闭文件保存提醒", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__ 
        self.startScene(tag)
        self.OneClick("BtnNewPage")
        self.OneClick("BtnCloseApp")
        self.WaitForElementText("DlgConfirmTxt", "是否保存对演示文稿的更改？", 10, "文件关闭未提醒保存")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
