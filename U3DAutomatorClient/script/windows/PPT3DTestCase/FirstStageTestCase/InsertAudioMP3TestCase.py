#!/usr/bin/env python
# coding=utf-8
"""
文件名称：InsertAudioMP3TestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/7 17:23
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class InsertAudioMP3TestCase(Action, Operation, SystemDiaglog):
    '''插入音频MP3'''

    def test_main(self):
        '''插入音频MP3'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("插入撤销还原音频MP3", time.time())

        self.OneClick("BtnInsert")

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.OpenAudio(SourcePath.File_Audio_mp3)
        self.AudioR("MP3.mp3")
        time.sleep(5)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()