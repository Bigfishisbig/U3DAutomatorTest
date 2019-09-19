#!/usr/bin/env python
# coding=utf-8

from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath
from TempOperate import TempOperation
import datetime
from main.utils.profile import monitor_unity_start, monitor_unity_stop
from main.engine_handler import get_application, get_engine, get_image_engine
from main.object.enum import *
import os

import sys
import time
import subprocess


reload(sys)
sys.setdefaultencoding("utf-8")

# x = xlwtWriter.XlsxWriter()
# x.write_line("start_time", "end_time", "run_times", "break_times", "isBreak")



class Start10000TimesTestCase(Action, Operation, SystemDiaglog, TempOperation):

    def setUp(self):

        pwd = os.getcwd()
        exe_path = os.environ[Environment.TEST_PATH]
        self.img_fullscreen = pwd + ur"\image\img_fullscreen.png"
        self.img_fullscreen_2 = pwd + ur"\image\img_fullscreen_2.png"
        report_path = pwd

        # self.run_time = 0
        self.pptx_page = 0
        self.break_time = 0
        self.run_time = 0
        self.spend_time = 0
        self.isBreak = "Y"

        try:
            # 杀进程
            # subprocess.Popen(report_path + "\kill3dppt.bat")
            # time.sleep(3)
            # print u"第", (i + 1), u"次运行启动"

            # self.run_time = self.run_time + 1  # 运行次数
            cmd = '"%s"' % exe_path
            self.write_file(report_path + r'\test.bat', cmd)
            self.convertUTF8ToANSI(report_path + ur'\test.bat', report_path + ur'\test.bat')
            # monitor_unity_start(self.__class__.__name__)
            self.start_time = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
            subprocess.Popen(report_path + r"\test.bat")
        except Exception, e:
            print str(e)

    def tearDown(self):
        # self.run_time
        print u"结束保存"
        # monitor_unity_stop(self.__class__.__name__)  # 停止性能监控\
        try:
            self.create()
            self.xls_getOldXls(SourcePath.File_Source + "Open3DPX_" + os.environ[Environment.StartTime] + ".xls")
            self.xls_write(str(self.start_time), str(self.end_time), self.spend_time, self.isBreak)
            self.xls_close(SourcePath.File_Source + "Open3DPX_" + os.environ[Environment.StartTime] + ".xls")
            os.system(SourcePath.File_Source + "\kill3dppt.bat")
        except Exception, e:
            print str(e)

    def test_main(self):
        # self.OperationSetting()
        # self.Init3DPPT()
        # tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__
        # self.startScene(tag)
        # for i in range(30):
        #
        #     try:
        #         if self.s_isExists(SourcePath.File_Img_FullScreen, 0, 0.1, accurate=0.6, isDel=True) == False and i < 10: == True:
        #             break_time = break_time - 1
        #             isBreak = 'N'
        #             break
        #         elif self.imgPair(self.img_fullscreen_2, 1920, 1080, 0.6)[0] == True:
        #             break_time = break_time - 1
        #             isBreak = 'N'
        #             break
        #         else:
        #             pass
        #     except:
        #         pass
        #     time.sleep(1)
        i=0
        while self.s_isExists(self.img_fullscreen, 0, 0.1, accurate=0.6, isDel=True) == False and i < 10:
            # print self.s_isExists(imgPath)
            if self.s_isExists(self.img_fullscreen_2, 0, 0.1, accurate=0.6, isDel=True):
                # break_time = break_time - 1
                self.isBreak = 'N'
                break
            i += 1
            time.sleep(1)
        else:
            self.Screen_cap("Error_Start_%s" % self.start_time)

        self.end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.spend_time = self.end_time - self.start_time
        print "spendTime:", self.spend_time

        # self.getSaveTimeXLS(str(start_time), str(end_time), spend_time)
        # self.getSaveTimeXLSClose(SourcePath.File_Source + "Open3DPX_" + os.environ[Environment.StartTime] + ".xls")

        # self.endScene(tag)
        # time.sleep(1)
        # self.EndTag()
