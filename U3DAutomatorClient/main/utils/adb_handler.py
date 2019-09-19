#! /usr/bin/env python
# coding=utf-8

import re
import os
import sys
import time
import functools
from collections import namedtuple

from main.object.enum import Environment
from main.utils import regex
from main.utils.process import Process
from main.log.logger import get_logger

__author__ = "Junpeng Chen"


def timeout_rerun(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        out, error = func(*args, **kwargs)
        return func(*args, **kwargs) if "timeout" in error else out, error

    return wrapper


class AdbHandler:
    """
        adb 命令集合
    """

    def __init__(self, device_id=None):
        self.runProcess = Process()
        self.__logCatProcess = None
        self.deviceId = device_id

        if device_id:
            self.adb = "adb -s %s " % device_id
            self.adbShell = "adb -s %s shell " % device_id
        else:
            self.adb = "adb "
            self.adbShell = "adb shell "

    def __cmd_timer(self, cmd, timer=10):
        """
            调用进程发送adb命令
        :param cmd: 命令
        :param timer: 超时时间
        :return:
        """
        get_logger().info(cmd)
        return self.runProcess.create_process_wait_timer(cmd, timer=timer)

    def forward(self, local_port, device_port):
        """
            pc与device端口衔接
            adb port forward. return 0 if success, else non-zero.
        :param local_port: pc端口
        :param device_port: device端口
        :return:
        """
        return self.__cmd_timer(self.adb + "forward tcp:%s tcp:%s" % (local_port, device_port))

    def forward_list(self):
        """端口链接列表"""
        version = get_version()
        if int(version[1]) <= 1 and int(version[2]) <= 0 and int(version[3]) < 31:
            raise EnvironmentError("Low adb get_version.")
        lines = self.__cmd_timer(self.adb + "forward --list")[0].strip().splitlines()
        return [line.strip().split() for line in lines]

    def pm_list_pkg(self, name=""):
        """
            查看package
        :param name: package name
        :return:
        """
        return self.__cmd_timer(self.adbShell + "pm list packages %s" % name)

    def install(self, name, args="-r", timeout=120):
        """
            安装app
        :param name: apk路径
        :param args: 安装参数
        :param timeout: 超时时间
        :return:
        """
        return self.__cmd_timer(self.adb + "install %s \"%s\"" % (args, name), timer=timeout)

    def start(self, package, activity, args="-W"):
        """
            启动app
        :param package: package name
        :param activity: launch activity name
        :param args: 启动参数
        :return:
        """
        return self.__cmd_timer(self.adbShell + "am start %s %s/%s" % (args, package, activity))

    def start_by_monkey(self, package):
        """
        启动app
        :param package: package name
        :return:
        """
        return self.__cmd_timer(self.adbShell + "monkey -p %s -c android.intent.category.LAUNCHER 1" % package)

    def uninstall(self, package):
        """
            卸载app
        :param package: package name
        :return:
        """
        return self.__cmd_timer(self.adb + "uninstall %s" % package)

    def ps_find_str(self, package):
        """
            查找进程信息
        :param package: package name
        :return:
        """
        return self.__cmd_timer(self.adbShell + " ps | findstr %s" % package)

    def pull(self, path1, path2, timeout=60):
        """
            从Android端拿文件放到pc上
        :param timeout:
        :param path1:
        :param path2:
        :return:
        """
        return self.__cmd_timer(self.adb + " pull \"%s\" \"%s\"" % (path1, path2), timer=timeout)

    def push(self, path1, path2):
        """
            从pc端拿文件放到Android上
        :param path1:
        :param path2:
        :return:
        """
        return self.__cmd_timer(self.adb + " push \"%s\" \"%s\"" % (path1, path2))

    def force_stop(self, package):
        """
            强关应用
        :param package:
        :return:
        """
        return self.__cmd_timer(self.adbShell + " am force-stop %s" % package)

    def remove(self, path):
        """
            删除文件
        :param path:
        :return:
        """
        return self.__cmd_timer(self.adbShell + " rm \"%s\"" % path)

    def start_log_cat(self, log, package=None):
        """
            启动LogCat
        :param log:
        :param package:
        :return:
        """
        self.__logCatProcess = Process()
        cmd = self.adb + "logcat %s >%s" % (
            package if "ActivityManager:D ANRManager:E AndroidRuntime:E %s:D *:S -v time" % package else "", log)
        self.__logCatProcess.create_process(cmd)

    def stop_log_cat(self):
        """
            关闭LogCat
        :return:
        """
        return self.__logCatProcess.stop_process()

    @timeout_rerun
    def click(self, x, y):
        """
            点击
        :param x:
        :param y:
        :return:
        """
        return self.__cmd_timer(self.adbShell + "input tap %s %s" % (x, y))

    @timeout_rerun
    def swipe(self, x, y, tox, toy):
        """
            滑动
        :param x:
        :param y:
        :param tox:
        :param toy:
        :return:
        """
        return self.__cmd_timer(self.adbShell + "input swipe %s %s %s %s" % (x, y, tox, toy))

    @timeout_rerun
    def text(self, text):
        """
            文本设置
        :param text:
        :return:
        """
        return self.__cmd_timer(self.adbShell + "input text %s" % text)

    @timeout_rerun
    def key_event(self, code):
        """
            操作key事件
        :param code:
        :return:
        """
        return self.__cmd_timer(self.adbShell + "input keyevent %s" % code)

    @timeout_rerun
    def screen_cap(self, path):
        """
            截图
        :param path:
        :return:
        """
        return self.__cmd_timer(self.adbShell + "screencap -p %s" % path)

    def screen_cap_pull(self, path):
        """
            截图并pull到pc端
        :param path:
        :return:
        """
        out, error = self.screen_cap("/sdcard/test.png")
        if error:
            sys.stderr.write("%s : %s\n" % (path, error))
            return out, error
        return self.pull("/sdcard/test.png", path)

    @timeout_rerun
    def date(self, localtime):
        return self.__cmd_timer(self.adbShell + "-s '%s'" % localtime)

    def date_sync(self):
        return self.date(time.strftime("%Y%m%d.%H%M%S", time.localtime()))

    def get_screen(self):
        out, error = self.__cmd_timer(self.adbShell + "dumpsys window displays|findstr init")
        pattern = "\s*init=(\S*)"
        if out == "" or error:
            out, error = self.__cmd_timer(self.adbShell + "dumpsys window|findstr init")
        if out == "" or error:
            out, error = self.__cmd_timer(self.adbShell + "dumpsys displays|findstr \"mPhys=PhysicalDisplayInfo\"")
            pattern = "mPhys=PhysicalDisplayInfo\\{(\S*),"
        if out and not error:
            screen = regex.search(pattern, out)
            if screen:
                return screen[0].replace(" ", "")
        return None

    def get_name(self):
        model, error = self.__cmd_timer(self.adbShell + "getprop ro.product.model")
        manufacturer, error2 = self.__cmd_timer(self.adbShell + "getprop ro.product.manufacturer")
        if model and manufacturer:
            return "%s-%s" % (manufacturer.replace("\r\r\n", ""), model.replace("\r\r\n", ""))
        return None

    def get_version(self):
        out, error = self.__cmd_timer(self.adbShell + "getprop ro.build.get_version.release")
        return out.split("\r\r\n")[0] if out else None

    def get_mac(self):
        out, error = self.__cmd_timer(self.adbShell + "cat /sys/class/net/wlan0/address")
        return out.split("\r\r\n")[0] if out else None

    ###########################################################################
    def list_files(self, dir):
        out, error = self.__cmd_timer(self.adbShell + "ls %s" % dir)
        return out.split("\r\r\n")[0] if out else None

    def get_device_model(self):
        out, error = self.__cmd_timer(self.adbShell + "getprop")
        strlist = out.split("\r\r\n")
        for strInfo in strlist:
            if strInfo.find("ro.product.model") != -1:
                strFrags = strInfo.split("[")
                strInfo = strFrags[2]
                strFrags = strInfo.split("]")
                return strFrags[0]
        return "UnkownDevice"

    def connect_device_via_tcp(self, deviceID):
        out, err = self.__cmd_timer("adb devices")
        deviceids = out.split("\r\r\n")
        for id in deviceids:
            if id.find("deviceID") != -1:
                #print "device : " + deviceID + " already connected!"
                return True
        out, err = self.__cmd_timer("adb connect " + deviceID)
        if out[0:9] == "connected":
            #print "device : " + deviceID + " connected!"
            return True
        else:
            #print "failed connect to " + deviceID
            return False

    def get_bettery_info(self):
        out, error = self.__cmd_timer(self.adbShell + "dumpsys battery")
        strlist = out.split()
        ret = namedtuple("BatterInfo", ["level", "temperature"])
        if "level:" in strlist:
            ret.level = int(strlist[strlist.index("level:") + 1])
        if "temperature:" in strlist:
            ret.temperature = int(strlist[strlist.index("temperature:") + 1])
        return ret

    def get_cpu_info(self):
        out, error = self.__cmd_timer(self.adbShell + "dumpsys cpuinfo")
        infoList = out.split("\r\r\n")
        loadInfo = infoList[0]
        loadInfoSplited = loadInfo.split()
        ret = namedtuple("CpuInfo", ["load", "usage"])
        # outInfo= {}
        ret.load = float(loadInfoSplited[1])
        for infoStr in infoList:
            if (infoStr.find(os.environ["PACKAGE"])) != -1:
                ret.usage = float(infoStr.split()[0].strip('%')) / 100
                break
        return ret

    def get_num_cpucore(self):
        out, error = self.__cmd_timer(self.adbShell + "cat /sys/devices/system/cpu/present")
        count = out.split("-")[1]
        return int(count) + 1

    def get_mem_info(self):
        out, error = self.__cmd_timer(self.adbShell + "dumpsys meminfo " + os.environ["PACKAGE"])
        ret = namedtuple("MemInfo", ["total", "heap", "heap_alloc", "heap_free"])
        memInfoList = out.split("\r\r\n")
        for infoStr in memInfoList:
            infoList = infoStr.split();
            if len(infoList) > 1 and infoList[0] == "TOTAL":
                ret.total = int(infoList[1])
                ret.heap = int(infoList[5])
                ret.heap_alloc = int(infoList[6])
                ret.heap_free = int(infoList[7])
                return ret
        return ret

    def get_mem_usage(self):
        out, error = self.__cmd_timer(self.adbShell + "dumpsys meminfo")
        memInfoList = out.split("\r\r\n")
        for infoStr in memInfoList:
            if (infoStr.find(os.environ["PACKAGE"])) != -1:
                infoList = infoStr.split();
                return int(infoList[0])
        return -1

    def get_files(self, dir):
        out, error = self.__cmd_timer(self.adbShell + "ls " + dir)
        fileList = out.split()
        return fileList

    def get_cur_freq(self, cpuIndex):
        out, error = self.__cmd_timer(
            self.adbShell + "cat /sys/devices/system/cpu/cpu%d/cpufreq/scaling_cur_freq" % cpuIndex)
        freq = 0
        try:
            freq = int(out)
        except ValueError:
            return 0
        return freq

    def get_pid(self, name):
        out, error = self.__cmd_timer(self.adbShell + "ps")
        infoList = out.split("\r\r\n")
        loadInfo = infoList[0]
        loadInfoSplited = loadInfo.split()
        for infoStr in infoList:
            splited = infoStr.split()
            if os.environ["PACKAGE"] in splited:
                pidAndPackageStr = splited[1]
                return int(pidAndPackageStr.split("/")[0])
        return 0

    def get_cputime_procss(self, pid):
        out, error = self.__cmd_timer(self.adbShell + "cat /proc/" + str(pid) + "/stat", )
        #print "process time " + out
        infoList = out.split()
        cpuTime = 0
        if (len(infoList) < 16):
            print("get cpu time failed")
            return -1;
        cpuTime += int(infoList[13])
        cpuTime += int(infoList[14])
        cpuTime += int(infoList[15])
        cpuTime += int(infoList[16])

        return cpuTime

    # cpuTimeMap = {}
    lastProcessTime = 0
    lastTotalTime = 0
    lastIdle = 0;
    lastIowait = 0;

    def cpu_usage_init(self, pid):
        self.lastProcessTime = get_adb_handler().get_cputime_procss(pid)
        self.lastTotalTime = self.get_total_time()

    def get_total_time(self):
        out, error = get_adb_handler().__cmd_timer(get_adb_handler().adbShell + "cat /proc/stat")
        infoList = out.split("\r\r\n")

        cpuInfo = infoList[0].split()
        totalTimeFirstCol = 0
        idle = int(cpuInfo[4])
        iowait = int(cpuInfo[5])
        if (idle < self.lastIdle):
            #print "idle reduce"
            idle = self.lastIdle
        if (iowait < self.lastIowait):
            print "iowait reduce"
            iowait = self.lastIowait
        self.lastIdle = idle
        self.lastIowait = iowait
        totalTimeFirstCol += int(cpuInfo[1])
        totalTimeFirstCol += int(cpuInfo[2])
        totalTimeFirstCol += int(cpuInfo[3])
        totalTimeFirstCol += idle
        totalTimeFirstCol += iowait
        totalTimeFirstCol += int(cpuInfo[6])
        totalTimeFirstCol += int(cpuInfo[7])
        totalTimeFirstCol += int(cpuInfo[8])
        totalTimeFirstCol += int(cpuInfo[9])
        print infoList[0]
        return totalTimeFirstCol
        '''
        infoList.pop(0)
        for infoStr in infoList:
            if infoStr[:3] == "cpu":
                cpuInfo = infoStr.split()
                totalTimeThisCore = 0
                totalTimeThisCore += int(cpuInfo[1])
                totalTimeThisCore += int(cpuInfo[2])
                totalTimeThisCore += int(cpuInfo[3])
                totalTimeThisCore += int(cpuInfo[4])
                totalTimeThisCore += int(cpuInfo[5])
                totalTimeThisCore += int(cpuInfo[6])
                totalTimeThisCore += int(cpuInfo[7])
                totalTimeThisCore += int(cpuInfo[8])
                totalTimeThisCore += int(cpuInfo[9])
                if cpuInfo[0] in self.cpuTimeMap:
                    self.cpuTimeMap[cpuInfo[0]] = totalTimeThisCore;
                else:
                    self.cpuTimeMap[cpuInfo[0]] = totalTimeThisCore;
        currTotalTimeCpu = 0
        for key,value in self.cpuTimeMap.iteritems():
            currTotalTimeCpu += value;
        #print "adb return total : " + str(totalTimeFirstCol) + " calculated : " + str(currTotalTimeCpu)
        if totalTimeFirstCol > currTotalTimeCpu:
            ##print "use first col"
            currTotalTimeCpu = totalTimeFirstCol
        return currTotalTimeCpu
            '''

    def get_cpu_usage(self, pid):
        processTimeCurr = get_adb_handler().get_cputime_procss(pid)
        currTotalTimeCpu = self.get_total_time()
        if currTotalTimeCpu <= self.lastTotalTime:
            print "Error total time reduced!"

        deltaProcessTime = processTimeCurr - self.lastProcessTime
        deltaTotalTime = currTotalTimeCpu - self.lastTotalTime
        self.lastProcessTime = processTimeCurr
        self.lastTotalTime = currTotalTimeCpu
        #print "cpu usage : " + str(deltaProcessTime / float(deltaTotalTime)) + " process : " + str(self.lastProcessTime) + "total : "+ str(self.lastTotalTime)
        usage = deltaProcessTime / float(deltaTotalTime)
        print "usage   total : " + str(deltaTotalTime) + " process: " + str(deltaProcessTime)
        if usage < 0:
            #print "usage < 0  total : " + str(deltaTotalTime) + " process: " + str(deltaProcessTime)
            usage = 0
        if usage > 1:
            #print "usage > 1  total : " + str(deltaTotalTime) + " process: " + str(deltaProcessTime)
            usage = 1
        return usage

    def get_cputime_total(self):
        out, error = self.__cmd_timer(self.adbShell + "cat /proc/stat")
        infoList = out.split("\r\r\n")
        cpuInfo = infoList[0].split()
        cpuTime = 0
        if (len(cpuInfo) < 10):
            return -1
        cpuTime += int(cpuInfo[1])
        cpuTime += int(cpuInfo[2])
        cpuTime += int(cpuInfo[3])
        cpuTime += int(cpuInfo[4])
        cpuTime += int(cpuInfo[5])
        cpuTime += int(cpuInfo[6])
        cpuTime += int(cpuInfo[7])
        cpuTime += int(cpuInfo[8])
        cpuTime += int(cpuInfo[9])

        return cpuTime


def start_adb():
    """启动adb"""
    return Process().create_process("adb start-server")


def kill_adb():
    """关闭adb"""
    return Process().create_process("adb kill-server")


def get_devices():
    """获取设备id"""
    out, error = Process().create_process_for_wait("adb devices")
    match = "List of devices attached"
    index = out.find(match)

    if index < 0:
        raise EnvironmentError("adb is not working.")
    devices = [tmp[0] for tmp in [line.strip().split("\t") for line in out[index + len(match):].strip().splitlines()] if
               len(tmp) == 2 and tmp[1] == "device"]

    if not devices:
        raise ValueError("not devices connect adb ")
    return devices


def get_version():
    """获取adb 版本"""
    out, error = Process().create_process_for_wait("adb version")
    match = re.search(r"(\d+)\.(\d+)\.(\d+)", out)
    return [match.group(i) for i in range(4)]


def get_adb_handler(device_id=None):
    """
        获取adb操作对象，单例模式
    :param device_id:
    :return:
    """
    if not get_adb_handler.instance:
        id = device_id or os.getenv(Environment.DEVICE_ID) or get_devices()[0]
        get_adb_handler.instance = AdbHandler(id)
    return get_adb_handler.instance


get_adb_handler.instance = None

# 弃用，采用多进程分发，不需要全局adb队列
# def get_adb_handler(device_id=None):
#     if device_id:
#         if device_id not in get_adb_handler.dictionary.keys() and device_id in get_devices():
#             get_adb_handler.dictionary[device_id] = AdbHandler(device_id)
#         return get_adb_handler.dictionary[device_id]
#     else:
#         first_device_id = get_devices()[0]
#         get_adb_handler.instance = AdbHandler(first_device_id)
#         get_adb_handler.dictionary[first_device_id] = get_adb_handler.instance
#     return get_adb_handler.instance
#
#
# get_adb_handler.instance = None
# get_adb_handler.dictionary = {}
