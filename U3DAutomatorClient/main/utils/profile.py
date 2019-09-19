#! /usr/bin/env python
# coding=utf-8
import heapq
import os
import time
import sched
import threading
import socket
from functools import wraps

from main.object.enum import Platform, Environment
from main.utils.path import get_root_path
from main.engine_handler import get_engine
from main.utils.xlsx_writer import XlsxWriter

from script.windows.PPT3DSetting.SourcePath import SourcePath
from script.windows.PPT3DSetting import DataBaseSet
import traceback
import datetime

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
        #print "Total time running %s: %s seconds" % (func.func_name, str(t1 - t0))
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
        #print "关闭性能监控"
        self.__flag = False


__monitor_tag = ""
__monitor_timestamp = ""
__Name_id = 0
__IP_id = 0
__Result_id = 0

def set_tag(tag, timestamp=""):
    global __monitor_tag
    __monitor_tag = tag

    global __monitor_timestamp
    __monitor_timestamp = timestamp


def end_tag(timestamp="", tag=""):
    global __monitor_tag
    __monitor_tag = tag

    global __monitor_timestamp
    __monitor_timestamp = timestamp

def nameAndIp(filename):
    global __Name_id
    global __IP_id
    global __Result_id
    # 数据库操作
    try:
        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        except Exception, e:
            print str(e)
        finally:
            s.close()
        d = DataBaseSet.DataBase()
        sql_ip = "select IP_id from t_IPs where ip='" + ip + "'"
        __IP_id = d.getData(sql_ip)
        #print "IP:", type(__IP_id[0])
        sql_1 = "select Name_id from t_CaseName where TestCaseName='" + filename + "'"
        __Name_id = d.getData(sql_1)
        #print "Name:", type(__Name_id[0])
        # 获取任务ID
        # sql_lastId = "SHOW TABLE STATUS where Name = 't_Result'"
        # __Result_id = d.getData(sql_lastId)
        # #print "__Result_id:", int(__Result_id[10])-1
        __Result_id = os.getenv(Environment.Result_id)

    except Exception:
        traceback.print_exc()

def __monitor(writer,filename):
    performance,fpsdata,cpudata,Memorydata= get_engine().get_performance()

    platform = os.getenv(Environment.PLATFORM)
    app = os.getenv(Environment.PACKAGE) if platform == Platform.Android else os.getenv(
        Environment.WINDOWS_TITLE)

    # for key in performance:
    #     print (key+":"+performance[key])

    # #print "GPU:", performance
    # 数据库操作
    try:
        d = DataBaseSet.DataBase()
        sql_2 = "INSERT INTO t_Performance(Name_id, Platform, App, Time, Fps, Cpu, TotalAllocatedMemory, TotalReservedMemory, MonoUsedSize, MonoHeapSize, Result_id, Tag, IP_id, Stamp)" \
              +"VALUES('%d','%s','%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%d', '%s', '%d', '%s')" %(__Name_id[0], platform, app,
               str(datetime.datetime.now()), str(performance.Fps), str(performance.CpuUsage),
               str(performance.Memory.TotalAllocatedMemory),str(performance.Memory.TotalReservedMemory),
               str(performance.Memory.MonoUsedSize), str(performance.Memory.MonoHeapSize), int(__Result_id)-1, __monitor_tag, __IP_id[0], __monitor_timestamp)
        d.databaseOperate(sql_2)
    except Exception, e:
        print  str(e)
        traceback.print_exc()

    if performance:
        writer.write_line(time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()), performance.Fps,
                          performance.Memory.MonoUsedSize, performance.Memory.MonoHeapSize,
                          performance.Memory.TotalAllocatedMemory, performance.Memory.TotalReservedMemory,
                          performance.CpuUsage, __monitor_tag, __monitor_timestamp)
    print fpsdata,cpudata,Memorydata
    # ExecNonQuery(fpsdata,cpudata,Memorydata)
    if fpsdata:
        fpsfile=open('fpsdata.txt','a')
        fpsfile.write(str(fpsdata)+'\n')
        fpsfile.close()
    if cpudata:
        fpsfile=open('cpudata.txt','a')
        fpsfile.write(str(cpudata)+'\n')
        fpsfile.close()
    if Memorydata:
        fpsfile=open('Memorydata.txt','a')
        fpsfile.write(str(Memorydata)+'\n')
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


def monitor_unity_start(filename):
    """
        unity 性能监控
    :return:
    """
    nameAndIp(filename)
    platform = os.getenv(Environment.PLATFORM)
    __get_writer().write_line("Platform", platform)
    __get_writer().write_line("App", os.getenv(Environment.PACKAGE) if platform == Platform.Android else os.getenv(
        Environment.WINDOWS_TITLE))

    __get_writer().set_line(5)
    __get_writer().write_line("Time", "Fps", "MonoUsedSize(b)", "MonoHeapSize(b)", "TotalAllocatedMemory(b)",
                              "TotalReservedMemory(b)", "Cpu(%)", "Tag", "Stamp")
    __get_scheduler().enter(1, 0, __monitor, (__get_writer(),filename))
    __get_scheduler().run()


def monitor_unity_stop(file_name="performance"):
    """
        unity 性能监控
    :return:
    """
    # nameAndIp(file_name)
    if __get_scheduler():
        __get_scheduler().close()
        __get_scheduler.instance = None
    if __get_writer():
        __get_writer().close(get_root_path(SourcePath.File_Performance_xls + file_name+".xls")) # 性能数据文件位置
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
