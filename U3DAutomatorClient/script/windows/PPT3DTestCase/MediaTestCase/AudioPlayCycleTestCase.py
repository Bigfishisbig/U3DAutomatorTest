#!/usr/bin/env python
# coding=utf-8
"""
文件名称：AudioPlayCycleTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/21 20:18
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class AudioPlayCycleTestCase(Action, Operation, SystemDiaglog):
    '''验证音频循环播放'''
    def test_main(self):
        '''验证音频循环播放'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("验证音频循环播放", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__ 
        self.startScene(tag)
        path = SourcePath.File_Audio_ape
        self.OpenAudio(path)
        self.OneClick("AudioLoopToggle")
        self.OneClick("BtnPlaying")
        self.Click_XY(0,0,0,-20)
        self.OneClick("BtnAudioPlay")
        self.Swipe_Media("AudioPlayHandle", "AudioPlayFillArea", 1, 1, -5, 0)
        time.sleep(2)
        # self.ClickL("AudioPlayedFillArea", -5)
        self.WaitForElementText("AudioPlayCurrentTime", "00:10", 120, "音频循环播放失败")
        x, y = self.WidthAndHeight("AudioPlayedFillArea")  # 已播放进度
        time.sleep(2)
        x1, y1 = self.WidthAndHeight("AudioPlayedFillArea")
        if x == x1:
            assert False, "播放进度条未移动"
        else:
            pass

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
