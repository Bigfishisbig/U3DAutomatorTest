# coding=utf-8
import unittest
from main.engine_handler import get_engine
from main.log.logger import get_logger
from main.engine_handler import get_application
from main.utils.profile import monitor_unity_start, monitor_unity_stop, set_tag, end_tag
import time, os, subprocess
from main.utils.windows_handler import get_windows_handler
from script.windows.PPT3DSetting.SourcePath import SourcePath

class Sample(unittest.TestCase):

    def setUp(self):
        #print "disna"
        get_logger().info('-' * 30 + __package__ + "." + self.__class__.__name__ + ".setUp" + '-' * 30)
        self.engine = get_engine()
        get_application().open_application()
        time.sleep(5)
        monitor_unity_start(self.__class__.__name__)

    def tearDown(self):
        # 结束场景设计
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__
        self.endScene(tag)

        monitor_unity_stop(self.__class__.__name__)  # 停止性能监控
        self.testImagPath = os.getcwd() + ur"\report\windows\screenshoot"
        # get_windows_handler().screen_cap(testImagPath + "\\" + self.__class__.__name__ + "_" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".png")
        if os.path.exists(self.testImagPath):
            pass
        else:
            os.mkdir(self.testImagPath)
        get_windows_handler().screen_cap(self.testImagPath + "\\" + self.__class__.__name__ + ".png")
        time.sleep(1)
        get_logger().info('-' * 30 + __package__ + "." + self.__class__.__name__ + ".tear_down" + '-' * 30)
        get_application().close_application()
        set_tag("")
        time.sleep(1)

    def endScene(self, tag):
        '''
        结束场景性能监控
        :param tag: 场景名
        :return:
        '''

        subprocess.Popen('"%s" --ENDSCENE("%s")' % (SourcePath.File_PCPA, tag))