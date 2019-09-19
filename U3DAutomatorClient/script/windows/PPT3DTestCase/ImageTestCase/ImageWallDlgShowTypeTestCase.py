#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ImageWallDlgShowTypeTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/24 15:23
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ImageWallDlgShowTypeTestCase(Action, Operation, SystemDiaglog):

    def test_main(self):
        '''图片墙弹窗中展示方式'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("图片墙弹窗中图片墙展示方式", time.time())

        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertImageBar")
        self.OneClick("BtnInsertImageListImageWall")

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.OneClick("ShowTypeAll")
        self.s_witForImg(SourcePath.File_ImageWall_Dlg_ShowTypes_All, 5, "全部展示类型显示异常")
        self.OneClick("ShowTypeOrder")
        self.s_witForImg(SourcePath.File_ImageWall_Dlg_ShowTypes_Order, 5, "顺序展示类型显示异常")
        self.OneClick("ShowTypeCompared")
        # self.s_witForImg(SourcePath.File_ImageWall_Dlg_ShowTypes_Order, 5, "顺序展示类型显示异常")
        self.WaitForElementText("NoModeTips", "暂无样式",5 ,"对比展示类型显示异常")
        self.OneClick("ShowTypeMain")
        self.s_witForImg(SourcePath.File_ImageWall_Dlg_ShowTypes_Main, 5, "顺序展示类型显示异常")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()