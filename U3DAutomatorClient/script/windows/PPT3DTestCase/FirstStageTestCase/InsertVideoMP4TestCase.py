#!/usr/bin/env python
# coding=utf-8
"""
文件名称：InsertVideoASFTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2019/1/7 17:21
修改时间：
软件：PyCharm
"""

from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化为指定的编码格式

class InsertVideoMP4TestCase(Action, Operation, SystemDiaglog):
    '''插入视频MP4'''

    def test_main(self):
        #插入视频MP4
        '''插入视频MP4'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("插入视频MP4", time.time())

        self.OneClick("BtnInsert")

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.OpenVideo(SourcePath.File_Video_mp4)
        self.RevertAndRecover2("ItemVideo")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
