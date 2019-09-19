#!/usr/bin/env python
# coding=utf-8
"""
文件名称：CutImageTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/20 16:58
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class CutImageTestCase(Action, Operation, SystemDiaglog):
    '''剪切图片'''

    def test_main(self):
        '''剪切图片'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("剪切元素", time.time())

        path = SourcePath.File_Image_bmp
        self.OpenImage(path)

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.CutElement2("ItemImageComp", "剪切图片失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
