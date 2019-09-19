#!/usr/bin/env python
# coding=utf-8
"""
文件名称：PlayingCopyPasteVideoTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/9 16:22
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class CopyPasteVideoTestCase(Action, Operation, SystemDiaglog):
    '''复制黏贴视频'''

    def test_main(self):
        '''复制黏贴视频'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("视频复制粘贴", time.time())
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        videos = [SourcePath.File_Video_3gp, SourcePath.File_Video_mpeg, SourcePath.File_Video_rm,
                  SourcePath.File_Video_mp4, SourcePath.File_Video_rmvb, SourcePath.File_Video_mov,
                  SourcePath.File_Video_flv, SourcePath.File_Video_avi, SourcePath.File_Video_asf,
                  SourcePath.File_Video_wmv]
        i=0
        for video in videos:
            self.OneClick("BtnInsert")
            self.OpenVideo(video)
            self.CopyPaste2("ItemVideo", "%d复制粘贴失败"%i)
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