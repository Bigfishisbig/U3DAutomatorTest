#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ImageWallAddTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/22 16:34
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ImageWallAddTestCase(Action, Operation, SystemDiaglog):

    def test_main(self):
        '''图片墙添加图片'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("圖片墻添加圖片", time.time())

        full_path = SourcePath.File_Image + '"BMP.bmp""GIF.gif""JPEG.jpeg""JPG.jpg""PNG.png"'
        full_path2 = SourcePath.File_Image + '"BMP1.bmp""GIF1.gif""JPEG1.jpeg""JPG1.jpg""PNG1.png"' \
                                             '"BMP2.bmp""GIF2.gif""JPEG2.jpeg""JPG2.jpg""PNG2.png"' \
                                             '"BMP3.bmp""GIF3.gif""JPEG3.jpeg""JPG3.jpg""PNG3.png"'
        self.OneClick("BtnInsert")

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.OpenImageWall(full_path)
        # 圖片墻添加圖片
        self.OneClick("BtnImageWallMore")
        self.OneClick("BtnAddImage")
        self.inputDlgClick("#32770", u"选择文件", [("ComboBoxEx32", 0), ("ComboBox", 0), ("Edit", 0)], full_path, "Button")  # 输入路径点击打开

        if self.engine.find_elements_path(self.PPT3DPath["ItemImageWall"])[10].Visible == True and self.engine.find_elements_path(self.PPT3DPath["ItemImageWall"])[9].Visible == False:
            pass
        else:
            assert False, "图片墙添加失败"
        self.OneClick("BtnImageWallMore")
        self.OneClick("BtnAddImage")
        self.inputDlgClick("#32770", u"选择文件", [("ComboBoxEx32", 0), ("ComboBox", 0), ("Edit", 0)], full_path2, "Button")  # 输入路径点击打开
        self.WaitForElementText("ImageWallWarn", "图片总数大于20,插入失败", 5, "圖片數量超過20")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
