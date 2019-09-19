#!/usr/bin/env python
# coding=utf-8
"""
文件名称：CopyPasteTableCustomTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/20 16:47
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class CopyPasteTableCustomTestCase(Action, Operation, SystemDiaglog):
    '''复制黏贴表格（传统）'''

    def test_main(self):
        '''复制黏贴表格（传统）'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("复制粘贴表格", time.time())

        self.InsertCustomTable()
        # self.Click_XY()

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.CopyPaste2("ItemFormComp", "复制表格失败", num=2)
        time.sleep(2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()