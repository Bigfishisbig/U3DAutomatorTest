#!/usr/bin/env python
# coding=utf-8
"""
文件名称：InsertExerciseTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/19 11:25
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class InsertExerciseTestCase(Action, Operation, SystemDiaglog):
    '''插入习题'''

    # 小学三年级-》人民教育出版社（人教版部编版）-》上册-》第一单元-》大青树下的小学
    def test_main(self):
        '''插入习题'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("插入基础习题", time.time())

        self.deleteDir()

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.InsertExercise()
        self.URPageID("ItemCefWeb")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()