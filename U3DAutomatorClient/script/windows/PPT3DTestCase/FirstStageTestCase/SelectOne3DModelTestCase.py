#!/usr/bin/env python
# coding=utf-8
"""
文件名称：SelectOne3DModelTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/20 15:47
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class SelectOne3DModelTestCase(Action, Operation, SystemDiaglog):
    '''选中3D模型'''

    def test_main(self):
        '''选中3D模型'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("单选3D模型", time.time())

        path = SourcePath.File_Insert_3DModel
        self.Open3DModel(path)
        time.sleep(5)
        # self.Click_XY()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        path = self.getElementPath("ItemModel")
        self.OneClickV(path)
        self.isElementVisible("BtnDragball0", "选中元素失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()