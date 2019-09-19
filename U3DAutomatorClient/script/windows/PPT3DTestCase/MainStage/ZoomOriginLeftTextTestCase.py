#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ZoomOriginLeftTextTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/27 12:05
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath
from script_handler import ScriptHandler

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式

# a = ScriptHandler()
# a.settingScripts(0, None, None, None)

class ZoomOriginLeftTextTestCase(Action, Operation, SystemDiaglog):
    '''左原点缩放文本框'''
    def test_main(self):
        '''左原点缩放文本框'''

        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("左原点缩放文本框", time.time())

        self.InputPara()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。\nabcdefghijklmnopqrstuvwxyz.\n123456789。")
        time.sleep(1)
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.ZoomOrigin(SourcePath.File_Img_Text_typeWord, -200)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()