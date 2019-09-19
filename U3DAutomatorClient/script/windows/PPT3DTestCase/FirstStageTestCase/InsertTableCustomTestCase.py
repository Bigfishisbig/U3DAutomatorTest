#!/usr/bin/env python
# coding=utf-8
"""
文件名称：InsertTableCustomTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/26 16:10
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class InsertTableCustomTestCase(Action, Operation, SystemDiaglog):
    '''插入传统表格'''

    def test_main(self):
        '''插入传统表格'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("传统方式插入表格", time.time())

        self.OneClick("BtnInsert")

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.OneClick("BtnInsertTable")
        self.OneClick("BtnTableCustom")
        self.OneClick("TableRowInput")
        self.InputStr("5")
        self.OneClick("TableColumnInput")
        self.InputStr("5")
        self.OneClick("SureInsertTable")
        path = self.getElementPath("ItemFormComp") + "/Table(Clone)/ItemGrid/FormItemPrefab(Clone)/ItemGrid/TabeleCell/3DText"
        path = str(path)
        self.isElementNumV(path, 25)  # 插入25个单元格
        #print "插入表格完毕"
        self.OneClick("BtnStart")
        self.OneClick("BtnRevert")
        time.sleep(2)
        if len(self.getPathValue("ItemFormComp")) is not 0:
            assert False, "撤销失败"
        else:
            pass
        # self.isElementNumV(path, 0)  # 插入0个单元格
        self.OneClick("BtnStart")
        self.OneClick("BtnRecover")
        path = self.getElementPath(
            "ItemFormComp") + "/Table(Clone)/ItemGrid/FormItemPrefab(Clone)/ItemGrid/TabeleCell/3DText"
        path = str(path)
        self.isElementNumV(path, 25)  # 插入25个单元格

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()