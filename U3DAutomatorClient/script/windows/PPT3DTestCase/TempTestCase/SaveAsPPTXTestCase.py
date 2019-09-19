#!/usr/bin/env python
# coding=utf-8
"""
文件名称：SaveAsPPTXTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/8/7 10:55
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath
from main.engine_handler import get_engine
from main.engine_handler import get_application
from main.utils.profile import monitor_unity_start, monitor_unity_stop
from TempOperate import TempOperation
from main.object.enum import *

import os, subprocess
from main.utils.windows_handler import get_windows_handler

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class SaveAsPPTXTestCase(Action, Operation, SystemDiaglog):

    def setUp(self):
        print "重写初始化"
        get_logger().info('-' * 30 + __package__ + "." + self.__class__.__name__ + ".setUp" + '-' * 30)
        self.engine = get_engine()
        get_application().open_application()
        time.sleep(5)

    def tearDown(self):
        print "结束保存"
        self.testImagPath = os.getcwd() + ur"\report\windows\screenshoot"
        # get_windows_handler().screen_cap(testImagPath + "\\" + self.__class__.__name__ + "_" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".png")
        if os.path.exists(self.testImagPath):
            pass
        else:
            os.mkdir(self.testImagPath)
        get_windows_handler().screen_cap(self.testImagPath + "\\" + self.__class__.__name__ + ".png")
        get_logger().info('-' * 30 + __package__ + "." + self.__class__.__name__ + ".tear_down" + '-' * 30)
        get_application().close_application()
        time.sleep(1)

    def test_main(self):
        self.OperationSetting()
        self.temp = TempOperation()
        self.Init3DPPT()
        # time.sleep(10)
        self.SetTag("另存为3dpx", time.time())

        time.sleep(1)
        self.OneClick("BtnNewPage")
        self.InputPara()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。")
        # time.sleep(2)
        self.OneClick("BtnNewPage")
        self.OpenImage(SourcePath.File_Image_gif)
        time.sleep(2)
        self.OneClick("BtnNewPage")
        self.OpenAudio(SourcePath.File_Audio_ape)
        time.sleep(2)
        self.OneClick("BtnNewPage")
        self.OpenVideo(SourcePath.File_Video_mp4)
        # time.sleep(3)
        self.OneClick("BtnNewPage")
        self.InsertShape("BtnShape_Process")
        # time.sleep(2)
        self.OneClick("BtnNewPage")
        self.Open3DModel(SourcePath.File_Insert_3DModel)
        # time.sleep(3)
        self.OneClick("BtnNewPage")
        self.InsertChart("BtnHistogram")
        # time.sleep(2)
        self.OneClick("BtnNewPage")
        self.InsertCustomTable()
        # time.sleep(2)
        self.OneClick("BtnNewPage")

        save_path = SourcePath.File_PPTOpenTestSave_pptx  # 保存
        if os.path.exists(save_path):
            os.remove(save_path)
        time.sleep(1)
        monitor_unity_start(self.__class__.__name__)

        self.SaveAs3DPPTFile(save_path)
        # self.WaitForElementText("TxtSaveStatus", "课件正在保存中...", 10, "10s内未开始保存课件")
        # self.LoadingWait("SliderFileSave")
        start_time = time.time()
        self.fileExist(save_path, "文件60s内另存为PPTX失败", 60)
        end_time = time.time()
        print "startTime:", start_time, "endTime:", end_time
        spend_time = end_time - start_time
        print "spendTime:", spend_time
        time.sleep(1)
        self.EndTag("", time.time())

        monitor_unity_stop(self.__class__.__name__)  # 停止性能监控
        self.create()
        self.xls_getOldXls(SourcePath.File_Source + "SavePPTX_" + os.environ[Environment.StartTime] + ".xls")
        self.xls_write(str(start_time), str(end_time), spend_time)
        self.xls_close(SourcePath.File_Source + "SavePPTX_" + os.environ[Environment.StartTime] + ".xls")

        # time.sleep(1)
        self.EndTag()

