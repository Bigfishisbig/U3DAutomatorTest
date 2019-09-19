#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ImageWallShowTypeListTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/24 15:48
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ImageWallShowTypeListTestCase(Action, Operation, SystemDiaglog):

    def test_main(self):
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("菜单栏图片墙展示方式列表验证", time.time())

        full_path = SourcePath.File_Image + '"BMP.bmp""GIF.gif""JPEG.jpeg""JPG.jpg""PNG.png"'
        self.OneClick("BtnInsert")
        self.OpenImageWall(full_path)

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.s_witForImg(SourcePath.File_ImageWall_ShowType1, 5, "展示类型第1行显示失败")
        self.OneClick("ShowTypeListDown")
        self.s_witForImg(SourcePath.File_ImageWall_ShowType2, 5, "展示类型第2行显示失败")
        self.OneClick("ShowTypeListMore")
        self.s_witForImg(SourcePath.File_ImageWall_ShowType3, 5, "展示类型全部显示失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()