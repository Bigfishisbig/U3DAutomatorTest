#! /usr/bin/env python
# coding=utf-8
import heapq
import os
import time
import sched
import threading
from functools import wraps

from main.object.enum import Platform, Environment
from main.utils.path import get_root_path
from main.engine_handler import get_engine
from main.utils.xlsx_writer import XlsxWriter

__author__ = "Junpeng Chen"
__version__ = "0.0.2"


def func_timer(func):
    """
        检测python性能
    :param func: 
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        t1 = time.time()
        print "Total time running %s: %s seconds" % (func.func_name, str(t1 - t0))
        return result

    return wrapper


class Scheduler(sched.scheduler):
    """
        周期执行
    """

    def __init__(self):
        sched.scheduler.__init__(self, time.time, time.sleep)
        self.__flag = True

    def enter(self, delay, priority, action, argument):
        sched.scheduler.enter(self, delay, priority, self.__method, (delay, priority, action, argument))

    def run(self):
        threading.Thread(target=self.__loop, name='SchedulerThread').start()

    def __loop(self):
        q = self._queue
        delay_func = self.delayfunc
        time_func = self.timefunc
        pop = heapq.heappop
        while q and self.__flag:
            times, priority, action, argument = checked_event = q[0]
            now = time_func()
            if now < times:
                delay_func(times - now)
            else:
                event = pop(q)
                # Verify that the event was not removed or altered
                # by another thread after we last looked at q[0].
                if event is checked_event:
                    action(*argument)
                    delay_func(0)  # Let other threads run
                else:
                    heapq.heappush(q, event)

    def __method(self, delay, priority, action, argument):
        sched.scheduler.enter(self, delay, priority, self.__method, (delay, priority, action, argument))
        action(*argument)

    def close(self):
        self.__flag = False


__monitor_tag = ""


def set_tag(tag):
    global __monitor_tag
    __monitor_tag = tag


def end_tag():
    global __monitor_tag
    __monitor_tag = ""


def __monitor(writer):
    performance,fpsdata= get_engine().get_performance()
    if performance:
        writer.write_line(time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()), performance.Fps,
                          performance.Memory.MonoUsedSize, performance.Memory.MonoHeapSize,
                          performance.Memory.TotalAllocatedMemory, performance.Memory.TotalReservedMemory,
                          performance.CpuUsage, __monitor_tag)
    if fpsdata:
        fpsfile=open('fpsdata.txt','a')
        fpsfile.write(str(fpsdata)+'\n')
        fpsfile.close()


def __get_writer():
    if not __get_writer.instance:
        __get_writer.instance = XlsxWriter()
    return __get_writer.instance


__get_writer.instance = None


def __get_scheduler():
    if not __get_scheduler.instance:
        __get_scheduler.instance = Scheduler()
    return __get_scheduler.instance


__get_scheduler.instance = None


def monitor_unity_start():
    """
        unity 性能监控
    :return:
    """
    platform = os.getenv(Environment.PLATFORM)
    __get_writer().write_line("Platform", platform)
    __get_writer().write_line("App", os.getenv(Environment.PACKAGE) if platform == Platform.Android else os.getenv(
        Environment.WINDOWS_TITLE))

    __get_writer().set_line(5)
    __get_writer().write_line("Time", "Fps", "MonoUsedSize(b)", "MonoHeapSize(b)", "TotalAllocatedMemory(b)",
                              "TotalReservedMemory(b)", "Cpu(%)", "Tag")
    __get_scheduler().enter(60, 0, __monitor, (__get_writer(),))
    __get_scheduler().run()


def monitor_unity_stop(file_name="performance"):
    """
        unity 性能监控
    :return:
    """
    if __get_scheduler():
        __get_scheduler().close()
        __get_scheduler.instance = None
    if __get_writer():
        __get_writer().close(get_root_path(file_name+".xls"))
        __get_writer.instance = None


if __name__ == '__main__':
    monitor_unity_start()
    # time.sleep(10)
    # set_tag("login")
    # time.sleep(5)
    # end_tag()
    # time.sleep(5)
    # set_tag("")
    # time.sleep(5)
    # end_tag()
    # time.sleep(10)
    monitor_unity_stop()
    pass
