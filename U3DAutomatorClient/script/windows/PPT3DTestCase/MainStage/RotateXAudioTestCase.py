#!/usr/bin/env python
# coding=utf-8
"""
文件名称：RotateXAudioTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/26 14:25
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class RotateXAudioTestCase(Action, Operation, SystemDiaglog):
    '''音频绕X轴旋转'''

    def test_main(self):
        '''音频绕X轴旋转'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("音频绕X轴旋转", time.time())

        self.OpenAudio(SourcePath.File_Audio_ape)
        time.sleep(2)

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.RotateByX(SourcePath.File_Insert_AUDIO)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()