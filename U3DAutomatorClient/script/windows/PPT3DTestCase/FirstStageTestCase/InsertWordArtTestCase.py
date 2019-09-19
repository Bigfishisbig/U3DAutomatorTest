#!/usr/bin/env python
# coding=utf-8
"""
文件名称：InsertWordArtTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/18 15:51
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class InsertWordArtTestCase(Action, Operation, SystemDiaglog):
    '''插入艺术字'''

    def test_main(self):
        '''插入艺术字'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("插入艺术字", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.InputPara()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。")

        wordart = [SourcePath.File_Img_WordArt_Text_1, SourcePath.File_Img_WordArt_Text_2, SourcePath.File_Img_WordArt_Text_3]
        for i in range(3):
            self.OneClick("BtnFormat")
            path = self.getText()
            # self.OneClickL(path, 50)
            self.ListClick("RotateByZAxisNor")
            self.ListClick("WordArtStyle", i)
            self.s_witForImg(wordart[i], 10, "艺术字插入失败", None, 0.4)
            self.OneClick("BtnStart")
            self.OneClick("BtnRevert")
            self.s_waitForImgVanish(wordart[i], 10, "撤销艺术字失败", 0.4)
            self.OneClick("BtnStart")
            self.OneClick("BtnRecover")
            self.s_witForImg(wordart[i], 10, "艺术字插入失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
