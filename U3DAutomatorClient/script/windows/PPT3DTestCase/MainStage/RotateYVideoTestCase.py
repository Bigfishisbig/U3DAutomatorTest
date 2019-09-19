#!/usr/bin/env python
# coding=utf-8
"""
文件名称：RotateYVideoTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/26 14:24
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class RotateYVideoTestCase(Action, Operation, SystemDiaglog):
    '''视频绕Y轴旋转'''
    def test_main(self):
        '''视频绕Y轴旋转'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("视频绕Y轴旋转", time.time())

        self.OpenVideo(SourcePath.File_Video_avi)
        time.sleep(2)
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.RotateByY(SourcePath.File_Insert_VIDEO)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()