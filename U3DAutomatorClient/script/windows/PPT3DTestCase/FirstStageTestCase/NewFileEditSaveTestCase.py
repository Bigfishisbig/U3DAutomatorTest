#!/usr/bin/env python
# coding=utf-8
"""
文件名称：NewFileEditSaveTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/17 17:35
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class NewFileEditSaveTestCase(Action, Operation, SystemDiaglog):
    '''编辑保存新建'''

    def test_main(self):
        '''编辑保存新建'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("编辑保存新建", time.time())

        target_path = SourcePath.File_3DPPTCopy_3dpx
        self.deleteFile(target_path)
        file_path = SourcePath.File_3DPPTOpenTest_3dpx
        self.CopyFileTo(file_path, target_path, "未找到原文件")  # 拷贝一份文件
        time.sleep(5)

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__ 
        self.startScene(tag)
        
        self.Open3DPPTFile(target_path)
        # self.WaitForElementText("TxtSaveStatus", "课件正在打开中...", 10, "10s内未开始打开课件")
        # self.LoadingWait("SliderFileSave")
        time.sleep(10)
        # self.isNotElementsVisible("SLiderFileOpen2", 0, "打开未结束", 15)
        self.WaitForElementText_list('FileName2', '3DPPTCopy', 30, "3DPPT文件30秒内未打开")
        self.OneClick("BtnNewPage")
        self.OneClick("BtnNewTab")
        # self.OneClick("TxtRightButton")  # 取消
        # self.OneClick("BtnCreateNewFile")
        # self.OneClick("TxtLeftButton")  # 是
        # self.WaitForElementText("FileName", "演示文稿", 10, "10s内新建文件失败")
        time.sleep(2)
        try:
            self.deleteFile(target_path)
        except Exception, e:
            print str(e)
        # os.remove(target_path)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()