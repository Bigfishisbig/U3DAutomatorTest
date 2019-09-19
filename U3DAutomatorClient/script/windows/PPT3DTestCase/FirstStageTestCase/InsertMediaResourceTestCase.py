#!/usr/bin/env python
# coding=utf-8
"""
文件名称：InsertMediaResourceTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/19 11:09
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class InsertMediaResourceTestCase(Action, Operation, SystemDiaglog):
    '''插入多媒体'''

    def test_main(self):
        '''插入多媒体'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("插入多媒体", time.time())

        self.deleteDir()

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)


        self.InsertMedia()
        self.AudioR("人教部编版 小学 语文三年级 上册《大青树下的小学》.ogg")
        time.sleep(5)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
