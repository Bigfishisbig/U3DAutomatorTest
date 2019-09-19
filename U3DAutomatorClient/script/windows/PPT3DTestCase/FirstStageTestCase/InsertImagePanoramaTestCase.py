#!/usr/bin/env python
# coding=utf-8
"""
文件名称：InsertImagePanoramaTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/17 16:01
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class InsertImagePanoramaTestCase(Action, Operation, SystemDiaglog):
    '''插入全景图'''

    def test_main(self):
        '''插入全景图'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("插入全景资源", time.time())

        num1 = self.ElementNum("ImgLoading")
        self.OneClick("BtnInsert")
        path = SourcePath.File_Image_panorama

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.OpenImagePanorama(path)
        num2 = self.ElementNum("ImgLoading")
        if num1 + 3 == num2:
            pass
        else:
            assert False, "插入全景图失败"

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()