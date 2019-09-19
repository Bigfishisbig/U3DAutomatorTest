#! /usr/bin/env python
#  coding=utf-8

import threading
import time

__author__ = "Junpeng Chen"


class EasyTimer(threading.Thread):
    """
        定时器，达到预设时间，self.timeout="timeout"
    """

    def __init__(self, fun, sleep):
        threading.Thread.__init__(self)
        self.__flag = True
        self.__sleep = sleep
        self.__fun = fun
        self.timeout = None

    def run(self):
        flag_time = 0
        while self.__flag:
            time.sleep(1)
            flag_time += 1
            if flag_time >= self.__sleep:
                self.timeout = "timeout"
                self.__fun()

    def stop(self):
        self.__flag = False
