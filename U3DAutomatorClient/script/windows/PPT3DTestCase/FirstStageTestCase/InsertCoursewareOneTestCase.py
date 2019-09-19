#!/usr/bin/env python
# coding=utf-8
"""
文件名称：InsertCoursewareOneTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/18 21:30
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class InsertCoursewareOneTestCase(Action, Operation, SystemDiaglog):
    '''插入单个课件'''

    def test_main(self):
        '''插入单个课件'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("插入单页课件", time.time())

        self.deleteDir()
        num1 = len(self.getPathValue("Page"))

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.InsertOneCourseware()
        time.sleep(5)
        num2 = len(self.getPathValue("Page"))

        if num1 == num2:
            assert False, "插入失败"
        else:
            pass
        time.sleep(5)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
