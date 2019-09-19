#!/usr/bin/env python
# coding=utf-8
"""
文件名称：VideoWindowNoTransTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/21 16:58
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class VideoWindowNoTransTestCase(Action, Operation, SystemDiaglog):
    '''验证窗口播放功能'''
    def test_main(self):
        '''验证窗口播放功能'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("验证窗口播放功能", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__
        self.startScene(tag)
        path = SourcePath.File_Video_3gp
        self.OpenVideo(path)
        self.OneClick("SwitchEffectToggle") # 取消转场效果
        self.OneClick("BtnPlaying")
        element = self.getElementPath("ItemVideo")
        self.OneClickV(element)
        self.isElementVisible("BtnVideoPlayFullScreen", "窗口播放失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
