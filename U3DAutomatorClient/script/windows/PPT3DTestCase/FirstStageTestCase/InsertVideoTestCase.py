#!/usr/bin/env python
# coding=utf-8
"""
文件名称：InsertVideoTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2019/1/8 15:08
修改时间：
软件：PyCharm
"""

from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化为指定的编码格式

class InsertVideoTestCase(Action, Operation, SystemDiaglog):
    '''插入视频'''

    def test_main(self):
        #插入视频
        '''插入视频'''
        self.OperationSetting()
        self.Init3DPPT()

        self.SetTag("插入视频", time.time())

        paths = [SourcePath.File_Video_3gp, SourcePath.File_Video_asf, SourcePath.File_Video_avi,
                 SourcePath.File_Video_flv, SourcePath.File_Video_mov, SourcePath.File_Video_mp4,
                 SourcePath.File_Video_mpeg, SourcePath.File_Video_rm, SourcePath.File_Video_rmvb,
                 SourcePath.File_Video_wmv]
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        for path in paths:
            self.OneClick("BtnInsert")
            self.OpenVideo(path)
            self.RevertAndRecover2("ItemVideo")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
