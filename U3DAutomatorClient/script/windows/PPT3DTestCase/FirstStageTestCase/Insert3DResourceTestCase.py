#!/usr/bin/env python
# coding=utf-8
"""
文件名称：Insert3DResourceTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/18 21:44
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class Insert3DResourceTestCase(Action, Operation, SystemDiaglog):
    '''插入3D资源'''

    def test_main(self):
        '''插入3D资源'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("插入3D资源", time.time())

        self.deleteDir()

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)


        self.Insert3DResource()
        self.URPageID("ItemModel")
        # path = self.getElementPath("ItemModel")
        # self.isElementExistPageID(path, "插入3D资源失败", 10)
        # num1 = len(self.getPathValue("ItemModel"))
        # self.OneClick("BtnStart")
        # self.OneClick("BtnRevert")
        # self.isNotElementExistPageID(path, "撤销3D模型失败")
        # self.OneClick("BtnStart")
        # self.OneClick("BtnRecover")
        # num2 = len(self.getPathValue("ItemModel"))
        # # self.isElementExistPageID(path, "还原3D模型失败")
        # if num2 == num1:
        #     pass
        # else:
        #     assert False, "还原3D资源失败"
        # self.OneClick("BtnStart")
        # self.OneClick("BtnRevert")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()