#!/usr/bin/env python
# coding=utf-8
"""
文件名称：CutTableTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/20 17:51
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class CutTableTestCase(Action, Operation, SystemDiaglog):
    '''剪切表格'''

    def test_main(self):
        '''剪切表格'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("剪切表格", time.time())

        self.InsertCustomTable()
        # self.Click_XY()

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.CutElement("ItemFormComp", "剪切表格失败", num=2)
        time.sleep(2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()