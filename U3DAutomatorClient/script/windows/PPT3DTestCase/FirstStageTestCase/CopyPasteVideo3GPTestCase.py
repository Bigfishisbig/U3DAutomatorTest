#!/usr/bin/env python
# coding=utf-8
"""
文件名称：CopyPasteVideo3GPTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/7 16:55
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class CopyPasteVideo3GPTestCase(Action, Operation, SystemDiaglog):
    '''复制黏贴视频3GP'''

    def test_main(self):
        '''复制黏贴视频3GP'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("视频3GP复制粘贴", time.time())

        self.OneClick("BtnInsert")
        self.OpenVideo(SourcePath.File_Video_3gp)
        
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        
        self.CopyPaste2("ItemVideo", "视频3GP复制粘贴失败")
        time.sleep(2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()