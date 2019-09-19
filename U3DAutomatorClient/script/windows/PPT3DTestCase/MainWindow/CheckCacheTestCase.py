#!/usr/bin/env python
# coding=utf-8
"""
文件名称：CheckCacheTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/5/21 15:36
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class CheckCacheTestCase(Action, Operation, SystemDiaglog):
    '''验证清除缓存'''
    def test_main(self):
        '''验证清除缓存'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("验证清除缓存", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.TimesClick(
            ["BtnSetting", "BtnPublicSetup", "DownloadSetup", "BtnClearCache"], 1)
        self.WaitForElementText("ClearCacheTip", "清除成功", 10, "清除缓存失败")


        self.endScene(tag)
        time.sleep(1)
        self.EndTag()