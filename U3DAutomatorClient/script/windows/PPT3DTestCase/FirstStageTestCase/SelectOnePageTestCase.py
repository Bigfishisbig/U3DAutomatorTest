#!/usr/bin/env python
# coding=utf-8
"""
文件名称：SelectOnePageTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/20 11:31
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class SelectOnePageTestCase(Action, Operation, SystemDiaglog):
    '''选中一张幻灯片'''

    def test_main(self):
        '''选中一张幻灯片'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("单选幻灯片", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.OneClick("BtnNewPage")
        self.ListClick("PageItem2", 0)
        self.isElementsVisible("IsPageSelected2", 0, "单选幻灯片失败")
        # if
        self.isNotElementsVisible("IsPageSelected1", 0, "不止选中一张幻灯片")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
