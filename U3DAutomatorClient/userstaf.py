#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
文件名称：userstaf.py
作者：ycy
版本：PPTPro
创建时间：2019/2/28 16:56
修改时间：
软件：PyCharm
"""
from PySTAF import STAFHandle
from PySTAF import STAFException
from PySTAF import STAFWrapData
from PySTAFMon import *
from PySTAFLog import *
import shutil, os, inspect
import sys


try:
    handle = STAFHandle("MyTest")
except STAFException, e:
    #print "Error1 registering with STAF, RC: %d" % e.rc
    sys.exit(e.rc)


# ----------------- Monitor start -----------------
# # STAX任务监控工具
# monitor = STAFMonitor(handle)
# result = monitor.log("Beginning section ABC of test")
# #print "monitor data: RC: %d, Result: %s" % (result.rc, result.result)
# ----------------- Monitor end -----------------



# ----------------- STAFWrapData start -----------------
# semName = "My Synch Sem"
# result = handle.submit("local", "sem", "EVENT %s post" % STAFWrapData(semName))
# #print "STAFWrapData data: RC: %d, Result: %s" % (result.rc, result.result)
# ----------------- STAFWrapData end -----------------



# ----------------- STAFLog start -----------------
# # The variable "handle" is an instance of the STAFHandle class that was
# # previously instantiated
#
# # Let's create a machine based log file that also sends fatal, error, and
# # warning messages to the Monitor service
#
# log = STAFLog(handle, STAFLog.Machine, "MyLog",
#               [STAFLog.Fatal, STAFLog.Error, STAFLog.Warning])
#
# # This message will only go to the log service, since we didn't specify
# # that start message get sent to the Monitor service
#
# result = log.log(STAFLog.Start, "Beginning ABC test")
# #print "Log1 data: RC: %d, Result: %s" % (result.rc, result.result)
#
# # This message will be sent to the Log and Monitor services
#
# result = log.log(STAFLog.Warning, "Got some ambiguous result")
# #print "Log2 data: RC: %d, Result: %s" % (result.rc, result.result)
# ----------------- STAFLog end -----------------


# ----------------- STAFHandle start -----------------
#判断本地staf服务是否正常，结果是PONG代表服务正常
# result = handle.submit("172.18.60.170", "ping", "ping")
# #print "result1:", result.result
# if (result.rc != 0):
#     #print "Error2 submitting request, RC: %d, Result: %s" % (result.rc, result.result)

# result = handle.submit("172.18.60.170", "var", "resolve string {STAF/Config/OS/Name}")
# #print "result2:", result.result
# if (result.rc != 0):
#     #print "Error3 submitting request, RC: %d, Result: %s" % (result.rc, result.result)
# else:
#     #print "OS Name: %s" % result.result

# #执行命令，要执行远程，把local替换远程ip，如打开notepad
# result = handle.submit("local", "PROCESS", "start command notepad")
# #print "Error4 submitting request, RC: %d, Result: %s" % (result.rc, result.result)

# result = handle.submit("local", "var", "resolve string {STAF/Config/OS/Name}")
# #print "Error submitting request, RC: %d, Result: %s" % (result.rc, result.result)

# result = handle.submit("local", "fs", "COPY DIRECTORY D:\\YCY\\new_UITest\\U3DAutomatorClient\\main\\utils TODIRECTORY d:\\desk TOMACHINE 172.18.60.170 RECURSE KEEPEMPTYDIRECTORIES")
# #print "Error5 submitting request, RC: %d, Result: %s" % (result.rc, result.result)
# ----------------- STAFHandel end -----------------

# print os.path.join(__file__.split(__package__.replace(".", os.sep))[0] if __package__ else ".", "log\windows\2018123")

print os.path.exists(".\log\windows\\2019-03-20.log")

def runStaf():

    pc_list = [#"172.18.62.138",
               "172.18.60.170",
               # "192.168.241.194",
        "192.168.244.61",
        "192.168.244.63",
        "192.168.244.64",
        "192.168.244.70",
               ]
    local_dir = "D:\YCY\u3d"
    target_dir = "E:\YCY\u3d"

    for pc in pc_list:
        result = handle.submit("local", "fs",
                               "COPY DIRECTORY %s TODIRECTORY %s TOMACHINE %s RECURSE KEEPEMPTYDIRECTORIES" % (
                               local_dir, target_dir, pc))
        if result.rc != 0:
            result = handle.submit("local", "fs",
                                   "COPY DIRECTORY %s TODIRECTORY %s TOMACHINE %s RECURSE KEEPEMPTYDIRECTORIES" % (
                                   local_dir, target_dir, pc))
            print pc, "执行任务1，RC: %d, Result: %s" (result.rc, result.result)
        else:
            print pc, "执行任务1，RC: %d, Result: %s"(result.rc, result.result)
            pass

        result = handle.submit(pc,
                               "Process",
                               "start command %s" % target_dir+"\install.bat")
        print pc, "执行任务2，RC: %d, Result: %s"(result.rc, result.result)

    print "传输完毕"

    #执行完记得注销handle
    rc = handle.unregister()
    print "unregister: RC: %d" % rc



# runStaf() # 运行staf传输文件及运行

# result = handle.submit("172.18.60.170",
#                                "Process",
#                                "start command notepad")


#
# pc_list = [#"172.18.62.138",
#                "172.18.60.170",
#                # "192.168.241.194",
#         "192.168.244.61",
#         "192.168.244.63",
#         "192.168.244.64",
#         "192.168.244.70",
#            ]
# for pc in pc_list:
#     result = handle.submit(pc,
#                                    "Process",
#                                    "start command notepad")

#print "这是一个测试123"
