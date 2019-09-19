# coding=utf-8
import datetime
import os
import unittest
import time
from main.log.logger import get_logger
from main.object.enum import *
from main.utils.adb_handler import get_devices
from main.utils.html_report2 import HTMLTestRunner
from main.utils.path import get_root_path
from main.utils.staf_handle import Staf_Action
from script.windows.PPT3DSetting import SourcePath

__author__ = "Junpeng Chen"


class UnittestHandler:
    """
        用于单元测试启动
    """

    def __init__(self):
        self.files = []
        self.start_time = None
        self.test_result = None
        self.start_time = datetime.datetime.now()
        self.timeReport = time.localtime()
        self.staf_action = Staf_Action()

    def run(self, module):
        self.set_up()
        self.unittest(module)
        self.tear_down()

    def set_up(self):
        ##print "第2个点"
        if os.getenv(Environment.PLATFORM) == Platform.Android and not os.getenv(Environment.DEVICE_ID):
            os.environ[Environment.DEVICE_ID] = get_devices()[0]

    def tear_down(self):
        if self.test_result:
            print "test_result:",self.test_result
        else:
            print "nothing to say"

    def unittest(self, modules):
        """
            运行用例
            :return:
        """
        module = modules.split(",")
        if module is not None and module != "":
            get_logger().info("unittest module %s" % module)
            suite = unittest.TestLoader().loadTestsFromNames(module)
        else:
            module = self._get_modules()
            get_logger().info("unittest modules %s" % module)
            suite = unittest.TestLoader().loadTestsFromNames(module)

        # insert_task(module)
        html_name = time.strftime("%Y-%m-%d_%H-%M-%S.html", self.timeReport)
        self._html_report(suite, html_name)

        dirname = html_name.split(".")[0]
        if os.environ[Environment.isTransSTAF] == "Y":
            for i in range(5):
                try:
                    self.staf_action.CopyDir(path=os.path.dirname(os.path.dirname(self.staf_action.current_directory())) + "\\report", name=dirname)
                    break
                except:
                    print "传递数据到服务端失败%d次"%(i+1)
            # Staf_Action.CloseHandle()
            print "********************************结束*****************************"

    def _html_report(self, suite, html_name):
        """
            html报告
        """

        print "报告名称：", html_name
        platform = os.getenv(Environment.PLATFORM)
        if platform == Platform.Windows:
            title = os.getenv(Environment.WINDOWS_TITLE)
            html_path = get_root_path("report", Platform.Windows, html_name)

        elif platform == Platform.Android:
            title = os.getenv(Environment.PACKAGE)
            device_id = os.getenv(Environment.DEVICE_ID)

            if device_id:
                html_path = get_root_path("report", Platform.Android, device_id, html_name)
            else:
                html_path = get_root_path("report", Platform.Android, html_name)

        elif platform == Platform.S3Windows:
            title = os.getenv(Environment.WINDOWS_TITLE)
            html_path = get_root_path("report", Platform.S3Windows, html_name)

        else:
            title = ""
            html_path = get_root_path("report", html_name)

        with file(html_path, 'wb') as html:
            runner = HTMLTestRunner(stream=html, verbosity=2, title="%s Test Report" % title)
            self.test_result = runner.run(suite)

    def _get_modules(self):
        """
            获取unittest模块
        :return:
        """
        self._walk_dir(get_root_path("script", os.getenv(Environment.PLATFORM)))
        return map(self._path_to_module, self.files)

    def _path_to_module(self, string):
        """
            路径转模块
        :param string:
        :return:
        """
        if not isinstance(string, str):
            raise TypeError(string + " isn't str type")
        split = os.path.splitext(string)[0]
        split = split.replace("/", os.sep)
        split = split.replace("\\", os.sep)
        split = split.split(os.path.abspath("."))
        return split[1].replace(os.sep, ".")[1:]

    def _walk_dir(self, dir_path):
        """
            遍历查找用例脚本
        :param dir_path:
        :return:
        """
        files = os.listdir(dir_path)
        for name in files:
            if not name.endswith(".py") or name.startswith("__init__"):
                continue
            new_file = os.path.join(dir_path, name)
            if os.path.isfile(new_file):
                self.files.append(new_file)
            if os.path.isdir(new_file):
                self._walk_dir(new_file)

