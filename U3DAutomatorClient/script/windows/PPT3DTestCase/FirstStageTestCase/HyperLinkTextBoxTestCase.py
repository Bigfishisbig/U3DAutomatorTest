#!/usr/bin/env python
# coding=utf-8
"""
文件名称：HyperLinkTextBoxTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/14 14:40
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class HyperLinkTextBoxTestCase(Action, Operation, SystemDiaglog):
    '''文本框超链接'''

    def test_main(self):
        '''文本框超链接'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("文本框超链接", time.time())

        self.InputPara()
        self.InputStr("cdisk")
        text_path = self.getText2()

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.OneClickL(text_path, 2, 0)  # 选中控件（编辑状态）
        self.Hyperlink(2)  # 实现超链接,0:c盘
        self.isHyperlinkEditing(text_path, 0, "超链接失败")
        time.sleep(1)
        self.isHyperlinkPlaying(text_path, 0, "超链接失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
