#!/usr/bin/env python
# coding=utf-8
"""
文件名称：SavepptxAs3dpxTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/17 16:36
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class SavepptxAs3dpxTestCase(Action, Operation, SystemDiaglog):
    '''pptx文件保存为3dpx文件'''

    def test_main(self):
        '''pptx文件保存为3dpx文件'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("pptx文件保存成3dpx文件", time.time())

        self.OneClick("BtnCloseTab")
        file_path = SourcePath.File_PPTOpenTest_pptx
        self.Open3DPPTFile(file_path)
        # self.WaitForElementText("TxtSaveStatus", "课件正在打开中...", 10, "10s内未开始打开课件")
        # self.LoadingWait("SliderFileSave")
        time.sleep(10)
        # self.isNotElementsVisible("SliderFileSave", 0, "打开未结束", 15)
        # self.isElementVisible("SLiderFileOpen")
        # time.sleep(2)
        # self.WaitForElementText_list('FileName2', 'PPTOpenTest', 30, '30s内打开3DPPT失败')

        save_path = SourcePath.File_PPTOpenTestSave_3dpx  # 保存
        if os.path.exists(save_path):
            os.remove(save_path)

        tag = (self.__class__.__doc__ or "测试") + "_" + self.__class__.__name__
        tag = u"pptx文件保存成3dpx_testcase"
        self.startScene(tag)
        
        self.SaveAs3DPPTFile(save_path)
        # self.WaitForElementText("TxtSaveStatus", "课件正在保存中...", 10, "10s内未开始保存课件")
        # self.LoadingWait("SliderFileSave")
        # self.isNotElementsVisible("SLiderFileOpen2", 0, "打开未结束", 15)
        self.fileExist(save_path, "文件保存失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()

