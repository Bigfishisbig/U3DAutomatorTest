#!/usr/bin/env python
# coding=utf-8
"""
文件名称：FarAndNearTextTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/26 13:58
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class FarAndNearTextTestCase(Action, Operation, SystemDiaglog):
    '''文本远近调整'''

    def test_main(self):
        '''文本远近调整'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("文本远近调整", time.time())

        self.InputPara()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。\nabcdefghijklmnopqrstuvwxyz.\n123456789。")
        time.sleep(2)

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.FarAndNear(SourcePath.File_Img_Text_typeWord)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()