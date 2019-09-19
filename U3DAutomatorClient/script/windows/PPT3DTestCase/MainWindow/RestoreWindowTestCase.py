#!/usr/bin/env python
# coding=utf-8
"""
文件名称：RestoreWindowTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/14 11:50
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class RestoreWindowTestCase(Action, Operation, SystemDiaglog):
    '''恢复窗口'''
    def test_main(self):
        '''恢复窗口'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("恢复窗口", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.OneClick("BtnMinimize")
        self.s_waitForImgVanish(SourcePath.File_Img_FullScreen)
        # self.isNotElementExist("FileName", "最小化失败")
        self.s_clickImg(SourcePath.File_Minimize,5, "任务栏无该程序")
        self.s_witForImg(SourcePath.File_Img_FullScreen, 5, "恢复窗口失败", SourcePath.File_Img_FullScreen3)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
