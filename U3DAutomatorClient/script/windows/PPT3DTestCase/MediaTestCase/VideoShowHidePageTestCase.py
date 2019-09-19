#!/usr/bin/env python
# coding=utf-8
"""
文件名称：VideoShowHidePageTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/21 16:30
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class VideoShowHidePageTestCase(Action, Operation, SystemDiaglog):
    '''视频设置隐藏画面展示'''
    def test_main(self):
        '''视频设置隐藏画面展示'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("视频设置隐藏画面展示", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        path = SourcePath.File_Video_3gp
        self.OpenVideo(path)
        self.OneClick("VideoShowTypeLabel")
        self.OneClick("VideoShowTypeHide")
        self.s_witForImg(SourcePath.File_Video_Playing_Show_Hide, 10, "隐藏画面展示失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
