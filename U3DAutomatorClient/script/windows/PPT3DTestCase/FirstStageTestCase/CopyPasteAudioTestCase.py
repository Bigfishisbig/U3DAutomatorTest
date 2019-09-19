#!/usr/bin/env python
# coding=utf-8
"""
文件名称：PlayingCopyPasteAudioTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/9 16:32
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class CopyPasteAudioTestCase(Action, Operation, SystemDiaglog):
    '''复制粘贴音频'''

    def test_main(self):
        '''复制粘贴音频'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("复制音频", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        audios = [SourcePath.File_Audio_wma, SourcePath.File_Audio_wav, SourcePath.File_Audio_mp3,
                  SourcePath.File_Audio_m4r, SourcePath.File_Audio_m4a, SourcePath.File_Audio_ape
                  ]
        i=0
        for audio in audios:
            self.OneClick("BtnInsert")
            self.OpenAudio(audio)
            self.CopyPasteImage("ItemAudio", "%d复制粘贴失败"%i)
            # self.RevertAndRecover(SourcePath.File_Insert_JPEG)
            # self.OneClick("BtnStart")
            # self.OneClick("BtnRevert")
            # self.OneClick("BtnStart")
            # self.OneClick("BtnRevert")
            time.sleep(2)
            i = i + 1

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()