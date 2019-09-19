#!/usr/bin/env python
# coding=utf-8
"""
文件名称：MenuFunc3DModelTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/2/26 16:07
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class MenuFunc3DModelTestCase(Action, Operation, SystemDiaglog):
    '''放映态菜单3D模型'''

    def test_main(self):
        '''放映态菜单3D模型'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__ 
        self.startScene(tag)

        path = SourcePath.File_Insert_3DModel
        self.OneClick("BtnInsert")
        self.Open3DModel(path)
        self.MenuPlaying2("ItemModel", "3D模型复制粘贴失败")
        # self.RevertAndRecover(SourcePath.File_Insert_JPEG)
        time.sleep(2)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()