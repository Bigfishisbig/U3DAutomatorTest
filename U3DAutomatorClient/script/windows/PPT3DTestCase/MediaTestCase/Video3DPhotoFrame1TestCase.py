#!/usr/bin/env python
# coding=utf-8
"""
文件名称：Video3DPhotoFrame1TestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/21 18:05
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class Video3DPhotoFrame1TestCase(Action, Operation, SystemDiaglog):

    def test_main(self):
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("验证视频3D化相框1", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__ 
        self.startScene(tag)
        path = SourcePath.File_Video_3gp
        self.OpenVideo(path)
        self.OneClick("BtnVideoStyleMore")
        self.ListClick("EntityItem", 3) # 相框1
        self.s_witForImg(SourcePath.File_Video_3D_PhotoFrame1, 10, "相框1的3D化失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
