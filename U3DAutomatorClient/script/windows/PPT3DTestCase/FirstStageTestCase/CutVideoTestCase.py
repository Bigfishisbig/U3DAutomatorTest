#!/usr/bin/env python
# coding=utf-8
"""
文件名称：CutVideoTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/20 17:45
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class CutVideoTestCase(Action, Operation, SystemDiaglog):
    '''剪切视频'''

    def test_main(self):
        '''剪切视频'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("剪切视频", time.time())

        self.OneClick("BtnInsert")
        self.OpenVideo(SourcePath.File_Video_rmvb)

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__ 
        self.startScene(tag)

        self.CutElement("ItemVideo", "视频RMVB剪切失败")
        time.sleep(2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()