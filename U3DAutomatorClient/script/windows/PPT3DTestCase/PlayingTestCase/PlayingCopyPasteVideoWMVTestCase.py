#!/usr/bin/env python
# coding=utf-8
"""
文件名称：PlayingCopyPasteVideoWMVTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/7 14:56
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class PlayingCopyPasteVideoWMVTestCase(Action, Operation, SystemDiaglog):
    '''放映态复制黏贴视频WMVT'''
    def test_main(self):
        '''放映态复制黏贴视频WMVT'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  

        self.OneClick("BtnInsert")
        self.OpenVideo(SourcePath.File_Video_wmv)
        self.startScene(tag)
        self.CopyPastePlaying2("ItemVideo", "视频WMV复制删除失败")
        # self.RevertAndRecover(SourcePath.File_Insert_JPEG)
        time.sleep(2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()