#!/usr/bin/env python
# coding=utf-8
"""
文件名称：VideoPlayCycleTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/21 17:04
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class VideoPlayCycleTestCase(Action, Operation, SystemDiaglog):
    '''验证视频循环播放功能'''
    def test_main(self):
        '''验证视频循环播放功能'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("验证视频循环播放功能", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        path = SourcePath.File_Video_3gp
        self.OpenVideo(path)
        self.OneClick("LoopToggle")
        self.OneClick("BtnPlaying")
        element = self.getElementPath("ItemVideo") # 选中视频
        self.OneClickV(element)
        time.sleep(5)
        self.Swipe_Media("PlayHandle", "PlayFillArea", 1, 1, -5, 0)
        self.WaitForElementText("VideoPlayCurrentTime", "00:05", 120, "视频循环播放失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
