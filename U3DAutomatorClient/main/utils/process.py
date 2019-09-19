#! /usr/bin/env python
# coding=utf-8

import subprocess
from main.utils.easy_timer import EasyTimer

__author__ = "Junpeng Chen"


class Process:
    """
        进程
    """

    def __init__(self):
        self.__pro = None

    def create_process(self, cmd):
        """
            创建非阻塞进程
        :param cmd: c命令
        :return: None
        """
        self.__pro = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                      shell=True)

    def create_process_for_wait(self, cmd, message=None):
        """
            创建阻塞进程
        :param cmd: 命令
        :param message: 写入信息
        :return:
        """
        self.create_process(cmd)
        return self.__pro.communicate(message)

    def stop_process(self):
        """
            终止阻塞进程的调用
        :return:
        """
        if self.__pro.poll() != 0:
            value, error = self.create_process_for_wait("TASKKILL /T /F /PID %s" % self.__pro.pid)
            return value, error

    def create_process_wait_timer(self, cmd, message=None, timer=60):
        """
            调用阻塞进程，超时关闭
        :param cmd: 命令
        :param message: 写入stdin信息
        :param timer:
        :return:
        """
        easy_timer = EasyTimer(self.stop_process, timer)
        easy_timer.start()
        self.create_process(cmd)
        value, error = self.__pro.communicate(message)
        easy_timer.stop()
        if easy_timer.timeout == "timeout":
            error = easy_timer.timeout
        return value, error
