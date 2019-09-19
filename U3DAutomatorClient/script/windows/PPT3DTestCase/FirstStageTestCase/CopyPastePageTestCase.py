#!/usr/bin/env python
# coding=utf-8
"""
文件名称：PlayingCopyPastePageTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/9 19:15
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class CopyPastePageTestCase(Action, Operation, SystemDiaglog):
    '''复制粘贴幻灯片'''

    def test_main(self):
        '''复制粘贴幻灯片'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("复制幻灯片", time.time())

        # self.OneClick("PageNum")
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.CopyPaste("Number", "PageNum", "幻灯片复制粘贴失败", 1)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()