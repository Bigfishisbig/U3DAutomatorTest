#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ImageWallPlayModeTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/23 14:59
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ImageWallPlayModeTestCase(Action, Operation, SystemDiaglog):

    def test_main(self):
        '''图片墙播放方式'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("图片墙播放方式", time.time())

        full_path = SourcePath.File_Image + '"BMP.bmp""GIF.gif""JPEG.jpeg""JPG.jpg""PNG.png"'
        self.OneClick("BtnInsert")
        self.OpenImageWall(full_path)

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.WaitForElementText("CurrentPlayMode", "手动播放", 5, "默认播放类型不是手动播放")
        self.OneClick("ItemActionPlayMode")
        self.WaitForElementText("ManualMode", "手动播放", 5, "播放方式列表错误")
        self.WaitForElementText("AutoMode", "自动播放", 5, "播放方式列表错误")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
