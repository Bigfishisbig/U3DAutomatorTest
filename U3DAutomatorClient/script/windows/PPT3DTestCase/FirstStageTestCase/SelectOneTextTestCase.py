#!/usr/bin/env python
# coding=utf-8
"""
文件名称：SelectOneTextTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/20 13:57
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class SelectOneTextTestCase(Action, Operation, SystemDiaglog):
    '''选中文本框'''

    def test_main(self):
        '''选中文本框'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("单选文本框", time.time())

        self.InputPara()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。")

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.getText()
        PageID = self.getPathValue("Page")  # 获取可变路径
        itemTextID = self.getPathValue("ItemText")
        IsTextSelected = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page"+PageID[0]+"/ItemText/ItemText"+itemTextID[1]+"/TextAdjustGizmo"
        self.isElementExistPageID(IsTextSelected)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
