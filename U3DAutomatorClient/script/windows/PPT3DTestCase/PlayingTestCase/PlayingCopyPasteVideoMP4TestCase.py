#!/usr/bin/env python
# coding=utf-8
"""
文件名称：PlayingCopyPasteVideoMP4TestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/7 14:32
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class PlayingCopyPasteVideoMP4TestCase(Action, Operation, SystemDiaglog):
    '''放映态复制黏贴视频MP4'''
    def test_main(self):
        '''放映态复制黏贴视频MP4'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  

        self.OneClick("BtnInsert")
        self.OpenVideo(SourcePath.File_Video_mp4)
        self.startScene(tag)
        self.CopyPastePlaying2("ItemVideo", "视频MP4复制删除失败")
        # self.RevertAndRecover(SourcePath.File_Insert_JPEG)
        time.sleep(2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()