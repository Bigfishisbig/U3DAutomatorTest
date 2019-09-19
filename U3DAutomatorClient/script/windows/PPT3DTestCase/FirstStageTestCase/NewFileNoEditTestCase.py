#!/usr/bin/env python
# coding=utf-8
"""
文件名称：NewFileNoEditTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/17 17:16
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class NewFileNoEditTestCase(Action, Operation, SystemDiaglog):
    '''未编辑新建文件'''

    def test_main(self):
        '''未编辑新建文件'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("未编辑新建文件", time.time())

        file_path = SourcePath.File_3DPPTOpenTest_3dpx

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.Open3DPPTFile(file_path)
        # self.WaitForElementText("TxtSaveStatus", "课件正在打开中...", 10, "10s内未开始打开课件")
        # self.LoadingWait("SliderFileSave")
        time.sleep(10)
        # self.isNotElementsVisible("SLiderFileOpen2", 0, "打开未结束", 15)
        # self.isVisible("SLiderFileOpen")
        # self.LoadingWait("SLiderFileOpen")
        self.WaitForElementText_list('FileName2', '3DPPTOpenTest', 5, "3DPPT文件30秒内未打开")
        time.sleep(5)
        self.OneClick("BtnNewTab")
        self.WaitForElementText_list("FileName2", "演示文稿（1）", 10, "10s内新建文件失败")



        self.endScene(tag)
        time.sleep(1)
        self.EndTag()