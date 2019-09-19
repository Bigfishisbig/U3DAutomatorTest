#!/usr/bin/env python
# coding=utf-8
"""
文件名称：staf_handle.py
作者：ycy
版本：PPTPro
创建时间：2019/3/18 16:38
修改时间：
软件：PyCharm
"""
from PySTAF import STAFHandle
from PySTAF import STAFException
import sys, time, os, shutil, inspect
from main.object.enum import *

class Staf_Action:
    """
        用于staf操作，如返回数据给服务端
    """

    def __init__(self):
        pass

    def CopyFile(self, path, Machine2, targetPath):
        """
        从Machine1复制指定文件path到Machine2的指定的文件夹targetPath下
        :param path: 被复制的文件
        :param targetPath: 目标文件夹
        :return:
        """
        try:
            self.handle = STAFHandle("staf_handle")
        except STAFException, e:
            print "Error registering with STAF, RC: %d" % e.rc
            sys.exit(e.rc)
        result = self.handle.submit("local",
                                    "fs",
                                    "COPY FILE %s TODIRECTORY %s TOMACHINE %s" % (path, targetPath, Machine2))
        if result.rc is not 0:
            print "Error submitting COPY FILE, RC: %d, Result: %s" % (result.rc, result.result)
        self.CloseHandle()

    def CreateDIr(self):
        """
        创建文件夹
        :return:
        """
        os.system("")


    def CopyDir(self, Machine="172.18.62.138", path="D:\\YCY\\u3d\\U3DAutomatorClient\\report", targetPath="E:\\YCY\\u3d_report", name=""):
        """
        从Machine1复制文件夹path内的文件到Machine2的文件夹targetPath下
        :param path: 被复制的文件夹
        :param targetPath: 目标文件夹
        :return:
        """
        ip = os.environ[Environment.IP]
        if ip == "172.18.62.138":
            return
        # self.My_Copy(path, targetPath + "\\" + ip, "dir1")
        self.delete_dir(targetPath + "\\" + ip)
        self.My_Copy(path + "\\windows\\" + name, targetPath + "\\" + ip + "\\windows\\" + name, "dir1")
        self.My_Copy(path + "\\windows\\" + name + ".html", targetPath + "\\" + ip + "\\windows\\" + name + ".html",)

        # try:
        #     self.handle = STAFHandle("staf_handle")
        # except STAFException, e:
        #     #print "Error registering with STAF, RC: %d" % e.rc
        #     sys.exit(e.rc)
        # result = self.handle.submit(ip,
        #                             "fs",
        #                             "COPY Directory %s TODIRECTORY %s TOMACHINE %s RECURSE KEEPEMPTYDIRECTORIES" % (targetPath, targetPath, Machine))
        # if result.rc is not 0:
        #     #print "Error submitting COPY Dir, RC: %d, Result: %s" % (result.rc, result.result)
        # self.CloseHandle()
        try:
            os.system("staf %s fs COPY Directory %s TODIRECTORY %s TOMACHINE %s RECURSE KEEPEMPTYDIRECTORIES FAILIFNEW" % (ip, targetPath, targetPath, Machine))
            print "传输完毕"
        except:
            print "传输错误"
            pass


    def CloseHandle(self):
        """
        关闭句柄
        :return:
        """
        self.handle.unregister()

    def My_Copy(self, path1, path2, copytype='file'):
        if os.path.exists(path2):
            shutil.rmtree(path2)
        else:
            # os.makedirs(path2)
            pass
        if copytype == 'file':
            shutil.copyfile(path1, path2)  #
            print('文件复制成功')
        elif copytype == 'dir1':
            shutil.copytree(path1, path2) # 目录存在时无法复制
            print('目录复制成功')
        return

    def delete_dir(self, path):
        """
        删除文件夹
        :return:
        """
        if os.path.exists(path):
            shutil.rmtree(path)
        else:
            pass

    def current_directory(self):
        path = os.path.realpath(sys.path[0])
        if os.path.isfile(path):
            path = os.path.dirname(path)
            return os.path.abspath(path)
        else:
            caller_file = inspect.stack()[1][1]
            return os.path.abspath(os.path.dirname(caller_file))

if __name__ == '__main__':
    s = Staf_Action()
    s.CopyDir(path=os.path.dirname(os.path.dirname(s.current_directory())) + "\\report")