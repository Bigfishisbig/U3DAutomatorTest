#!/usr/bin/env python
# coding=utf-8
"""
文件名称：HyperLinkTextWordTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/14 15:37
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class HyperLinkTextWordTestCase(Action, Operation, SystemDiaglog):
    '''文本框文字超链接'''

    def test_main(self):
        '''文本框文字超链接'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("文本文字超链接", time.time())

        self.InputPara()
        self.InputStr("ddisk")
        text_path = self.getText2()

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.DoubleClickL(text_path, -10, 0)
        self.Hyperlink(1)  # 实现超链接,1:d盘
        self.isHyperlinkEditing(text_path, 1, "超链接失败")
        time.sleep(1)
        self.isHyperlinkPlaying(text_path, 1, "超链接失败")


        self.endScene(tag)
        time.sleep(1)
        self.EndTag()