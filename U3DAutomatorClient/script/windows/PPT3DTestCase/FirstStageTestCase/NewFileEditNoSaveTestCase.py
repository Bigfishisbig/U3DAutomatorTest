#!/usr/bin/env python
# coding=utf-8
"""
文件名称：NewFileEditNoSaveTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/17 17:24
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class NewFileEditNoSaveTestCase(Action, Operation, SystemDiaglog):
    '''未保存新建文件'''

    def test_main(self):
        '''未保存新建文件'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("未保存新建文件", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        file_path = SourcePath.File_3DPPTOpenTest_3dpx
        self.Open3DPPTFile(file_path)
        # self.WaitForElementText("TxtSaveStatus", "课件正在打开中...", 10, "10s内未开始打开课件")
        # self.LoadingWait("SliderFileSave")
        self.WaitForElementText('FileName', '3DPPTOpenTest', 30, "3DPPT文件30秒内未打开")
        time.sleep(5)
        # self.OneClick("BtnPageDelete")
        self.OneClick("BtnNewPage")
        self.OneClick("BtnCreateNewFile")
        self.OneClick("TxtRightButton") # 取消
        self.OneClick("BtnCreateNewFile")
        self.OneClick("TxtCenterButton") # 否
        self.WaitForElementText("FileName", "演示文稿", 10, "10s内新建文件失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()