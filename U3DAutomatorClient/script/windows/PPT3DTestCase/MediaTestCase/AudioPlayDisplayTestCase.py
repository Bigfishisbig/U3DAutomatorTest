#!/usr/bin/env python
# coding=utf-8
"""
文件名称：AudioPlayDisplayTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/2/27 17:14
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class AudioPlayDisplayTestCase(Action, Operation, SystemDiaglog):
    '''音频不隐藏播放'''
    def test_main(self):
        '''音频不隐藏播放'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("音频不隐藏播放", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        audios = [SourcePath.File_Audio_wma
                  ]
        i = 0
        for audio in audios:
            self.OneClick("BtnInsert")
            self.OpenAudio(audio)
            time.sleep(2)
            self.OneClick("BtnFormat")
            self.OneClick("NoTypeLabel")
            time.sleep(2)
            self.OneClick("BtnPlaying")
            time.sleep(5)
            element = self.getElementPath("ItemAudio")
            if self.isVisibleV(element):
                pass
            else:
                assert False, "设置不隐藏播放窗口失败"
            i = i + 1

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()