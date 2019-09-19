#!/usr/bin/env python
# coding=utf-8
"""
文件名称：InsertInteractExerciseTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/19 14:43
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class InsertInteractExerciseTestCase(Action, Operation, SystemDiaglog):
    '''插入趣味习题'''

    def test_main(self):
        '''插入趣味习题'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("插入趣味习题", time.time())

        self.deleteDir()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)


        self.InsertInteractExercise()
        assert False, "无习题"

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
