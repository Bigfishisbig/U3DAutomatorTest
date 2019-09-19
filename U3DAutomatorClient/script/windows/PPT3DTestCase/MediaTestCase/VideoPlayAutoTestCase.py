#!/usr/bin/env python
# coding=utf-8
"""
文件名称：VideoPlayAutoTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/21 16:17
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class VideoPlayAutoTestCase(Action, Operation, SystemDiaglog):
    '''验证视频自动播放'''
    def test_main(self):
        '''验证视频自动播放'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("验证视频自动播放", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        path = SourcePath.File_Video_3gp
        self.OpenVideo(path)
        self.OneClick("VideoPlayModeDropdown")
        self.OneClick("VideoPlayAuto")
        self.OneClick("BtnPlaying")
        element = self.getElementPath("ItemVideo")
        self.mouse_moveToCore(element)
        time.sleep(2)
        x, y = self.WidthAndHeight("PlayedFillArea")  # 已播放进度
        self.WaitForElementText("VideoPlayCurrentTime", "00:15", 30, "视频自动播放失败")
        time.sleep(2)
        x1, y1 = self.WidthAndHeight("PlayedFillArea")
        if x == x1:
            assert False, "播放进度条未移动"
        else:
            pass

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
