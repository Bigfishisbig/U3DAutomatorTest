#!/usr/bin/env python
# coding=utf-8
"""
文件名称：PlayingCopyPasteImagePNGTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/7 14:01
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class PlayingCopyPasteImagePNGTestCase(Action, Operation, SystemDiaglog):
    '''放映态复制黏贴图片PNG'''
    def test_main(self):
        '''放映态复制黏贴图片PNG'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        
        
        self.OneClick("BtnInsert")
        self.OpenImage(SourcePath.File_Image_png)
        self.startScene(tag)
        self.CopyPasteImagePlaying("ItemImageComp", "PNG复制删除失败")
        # self.RevertAndRecover(SourcePath.File_Insert_JPEG)
        time.sleep(2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()