#!/usr/bin/env python
# coding=utf-8
"""
文件名称：CopyPasteVideoRMTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/7 17:02
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class CopyPasteVideoRMTestCase(Action, Operation, SystemDiaglog):
    '''复制黏贴RMT'''

    def test_main(self):
        '''复制黏贴RMT'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("视频RM复制粘贴", time.time())

        self.OneClick("BtnInsert")
        self.OpenVideo(SourcePath.File_Video_rm)
        
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        
        self.CopyPaste2("ItemVideo", "视频RM复制粘贴失败")
        time.sleep(2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()