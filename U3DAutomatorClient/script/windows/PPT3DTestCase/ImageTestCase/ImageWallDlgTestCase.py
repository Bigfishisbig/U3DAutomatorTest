#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ImageWallDlgTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/24 15:16
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ImageWallDlgTestCase(Action, Operation, SystemDiaglog):

    def test_main(self):
        '''打开图片墙选择窗口'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("打开图片墙选择窗口", time.time())

        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertImageBar")

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__ 
        self.startScene(tag)

        self.OneClick("BtnInsertImageListImageWall")
        self.WaitForElementText("ImageWallSelectTitle", "选择图片墙", 5, "打开图片墙失败")
        self.s_witForImg(SourcePath.File_ImageWall_Dlg, 5, "打开图片墙失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()