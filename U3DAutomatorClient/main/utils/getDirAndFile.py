#!/usr/bin/env python
# coding=utf-8
"""
文件名称：getDirAndFile.py
作者：ycy
版本：PPTPro
创建时间：2019/8/16 18:16
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class getDirAndFile(Action, Operation, SystemDiaglog):

    def test_main(self):
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("sdasdasdasd", time.time())

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()