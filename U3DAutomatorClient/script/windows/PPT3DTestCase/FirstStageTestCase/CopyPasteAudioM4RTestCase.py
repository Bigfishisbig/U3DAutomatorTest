#!/usr/bin/env python
# coding=utf-8
"""
文件名称：CopyPasteAudioM4RTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/7 15:39
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class CopyPasteAudioM4RTestCase(Action, Operation, SystemDiaglog):
    '''复制粘贴音频M4R'''
    def test_main(self):
        '''复制粘贴音频M4R'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("复制粘贴音频M4R", time.time())

        self.OneClick("BtnInsert")
        self.OpenAudio(SourcePath.File_Audio_m4r)

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.CopyPaste2("ItemAudio", "音频M4R复制粘贴失败")
        # self.RevertAndRecover(SourcePath.File_Insert_JPEG)
        time.sleep(2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()