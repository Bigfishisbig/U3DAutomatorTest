#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ZoomOriginLeftVideoTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/27 11:57
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ZoomOriginLeftVideoTestCase(Action, Operation, SystemDiaglog):
    '''左原点缩放视频'''
    def test_main(self):
        '''左原点缩放视频'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("左原点缩放视频", time.time())

        self.OpenVideo(SourcePath.File_Video_3gp)
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.ZoomOrigin(SourcePath.File_Video_Playing_Show_Hide, x=-200)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()