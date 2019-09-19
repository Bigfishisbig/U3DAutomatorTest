#!/usr/bin/env python
# coding=utf-8
"""
文件名称：VideoPlayClickTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/21 16:04
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class VideoPlayClickTestCase(Action, Operation, SystemDiaglog):
    '''验证视频点击播放功能'''
    def test_main(self):
        '''验证视频点击播放功能'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("验证视频点击播放功能", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        path = SourcePath.File_Video_3gp
        self.OpenVideo(path)
        self.OneClick("VideoPlayModeDropdown")
        self.OneClick("VideoPlayClick")
        self.OneClick("BtnPlaying")
        self.s_witForImg(SourcePath.File_Video_Playing_Button_Pause, 10, "点击播放显示暂停按钮失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
