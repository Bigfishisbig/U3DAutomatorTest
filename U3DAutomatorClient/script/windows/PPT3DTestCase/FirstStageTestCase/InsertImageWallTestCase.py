#!/usr/bin/env python
# coding=utf-8
"""
文件名称：InsertImageWallTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2019/1/7 15:32
修改时间：
软件：PyCharm
"""


from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化为指定的编码格式

class InsertImageWallTestCase(Action, Operation, SystemDiaglog):
    '''插入图片墙'''

    def test_main(self):
        '''插入图片墙'''
        self.OperationSetting()
        self.Init3DPPT()
        full_path = SourcePath.File_Image + '"BMP.bmp""GIF.gif""JPEG.jpeg""JPG.jpg""PNG.png"'
        self.OneClick("BtnInsert")
        self.SetTag("插入图片墙", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.OpenImageWall(full_path)

        self.RevertAndRecover(SourcePath.File_Insert_IMAGEWALL, "ItemImageComp")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()

