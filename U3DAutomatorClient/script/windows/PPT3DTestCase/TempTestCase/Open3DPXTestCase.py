 #!/usr/bin/env python
# coding=utf-8
"""
文件名称：Open3DPXTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/8/8 11:04
修改时间：
软件：PyCharm
"""
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
from main.utils.windows_handler import get_windows_handler

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class Open3DPXTestCase(Action, Operation, SystemDiaglog, TempOperation):

    def setUp(self):

        print "重写初始化"
        get_logger().info('-' * 30 + __package__ + "." + self.__class__.__name__ + ".setUp" + '-' * 30)
        self.engine = get_engine()
        get_application().open_application()
        time.sleep(3)

    def tearDown(self):
        print "结束保存"
        self.testImagPath = os.getcwd() + ur"\report\windows\screenshoot"
        # get_windows_handler().screen_cap(testImagPath + "\\" + self.__class__.__name__ + "_" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".png")
        if os.path.exists(self.testImagPath):
            pass
        else:
            os.mkdir(self.testImagPath)
        get_windows_handler().screen_cap(self.testImagPath + "\\" + self.__class__.__name__ + ".png")
        time.sleep(2)
        get_logger().info('-' * 30 + __package__ + "." + self.__class__.__name__ + ".tear_down" + '-' * 30)
        get_application().close_application()
        os.system(SourcePath.File_Source + "\kill3dppt.bat")
        time.sleep(1)

    def test_main(self):
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__
        self.startScene(tag)

        # exe_path = os.environ[Environment.TEST_PATH]
        # error_path = os.path.dirname(exe_path) + "/LO/PPTEditor/temp/error.txt"
        # report_name = "report_open3dpx_%s.xls" % time.strftime('%Y%m%d_%H%M%S', time.localtime())
        #
        # pptx_page = 0
        # break_time = 0
        # run_time = 0
        #
        # rendering_spend_time = 0
        # start_spend_time = 0
        # isBreak = 'Y'
        rendering_break_time = 0

        try:
            rendering_path = u"C:/Users/Administrator/AppData/Roaming/3DPPT/Log/" + time.strftime('%Y%m%d', time.localtime()) + ".log"
            self.deleteFile(rendering_path)
        except Exception, e:
            print u"删除文件失败"
            print str(e)
        monitor_unity_start(self.__class__.__name__)
        file_path = SourcePath.File_PPTOpenTestSave_3dpx
        self.Open3DPPTFile(file_path)  # 打开文件
        start_time = time.time()
        # 获取解析渲染时间
        for i in range(100):
            print i
            try:
                flag = self.isExist(rendering_path, "SyncInfo")
                print "flag:", flag
                if flag:
                    rendering_break_time = rendering_break_time - 1
                    isBreak = 'N'
                    break
            except Exception, e:
                print str(e)
                break
            time.sleep(0.5)
        else:
            try:
                # self.copy2Path(error_path, report_path+"error\\error_%s.txt"%start_time)
                self.Screen_cap("error_%s_png" % start_time)
            except Exception, e:
                print str(e)
        end_time = time.time()
        time.sleep(2)
        monitor_unity_stop(self.__class__.__name__)  # 停止性能监控
        openTime = 0
        try:
            value1 = "Log Info (.*?):Open start load"
            value2 = "Log Info (.*?):SyncInfo当前页数"
            print u"渲染日志路径：", rendering_path
            startFile_time = self.getPathValue1(rendering_path, value1)
            endFile_time = self.getPathValue1(rendering_path, value2)
            print startFile_time, startFile_time
            d1 = datetime.datetime.strptime(startFile_time, '%Y:%m:%d %H:%M:%S')
            d2 = datetime.datetime.strptime(endFile_time, '%Y:%m:%d %H:%M:%S')
            openTime = (d2 - d1).seconds

        except Exception, e:
            print str(e)
            # self.copy2Path(rendering_path, report_path+"error\\error_rendering_%s.txt"%start_time)
            pass

        # input(u"结束")
        # end_time = time.time()
        spend_time = end_time - start_time
        self.create()
        self.xls_getOldXls(SourcePath.File_Source + "Open3DPX_" + os.environ[Environment.StartTime] + ".xls")
        self.xls_write(str(start_time), str(end_time), spend_time)
        self.xls_close(SourcePath.File_Source + "Open3DPX_" + os.environ[Environment.StartTime] + ".xls")
        # self.getSaveTimeXLS(str(start_time), str(end_time), spend_time)
        # self.getSaveTimeXLSClose(SourcePath.File_Source + "Open3DPX_" + os.environ[Environment.StartTime] + ".xls")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
