#!/usr/bin/env python
# coding=utf-8
"""
文件名称：InsertImageTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/12/18 15:54
修改时间：
软件：PyCharm
"""

from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化为指定的编码格式

class InsertImageGIFTestCase(Action, Operation, SystemDiaglog):
    '''插入图片GIF'''

    def test_main(self):
        '''插入图片GIF'''
        self.OperationSetting()
        self.Init3DPPT()
        self.OneClick("BtnInsert")

        self.SetTag("插入图片2", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.OpenImage(SourcePath.File_Image_gif)

        self.RevertAndRecover(SourcePath.File_Insert_GIF, "ItemImageComp")
        self.endScene(tag)
        time.sleep(1)
        self.EndTag()

