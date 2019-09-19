#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ClickOneHourTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/9/12 17:13
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ClickOneHourTestCase(Action, Operation, SystemDiaglog):

    def setUp(self):
        print "Start %s", time.time()


    def tearDown(self):
        print "End %s", time.time()

    def test_main(self):
        self.OperationSetting()

        for i in range(80):
            print "hahaha"
            self.s_clickImg(SourcePath.File_Phone_Click, 10, "点击截屏失败")
            time.sleep(3600)
