#!/usr/bin/env python
# coding=utf-8
"""
文件名称：SettingAboutUsTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/17 13:44
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class SettingAboutUsTestCase(Action, Operation, SystemDiaglog):
    '''关于我们'''
    def test_main(self):
        '''关于我们'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("关于我们", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.TimesClick(["BtnSetting", "BtnAboutUs"], 1)
        self.WaitForElementText("AboutUsTitle", "关于我们", 5, "打开关于我们失败")
        self.OneClick("AboutUsClose")
        self.isNotElementExist("AboutUsTitle", "关闭关于我们失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()