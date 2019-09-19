#!/usr/bin/env python
# coding=utf-8
"""
文件名称：SettingContractUsTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/17 15:13
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class SettingContractUsTestCase(Action, Operation, SystemDiaglog):
    '''联系我们'''
    def test_main(self):
        '''联系我们'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("联系我们", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.OneClick("BtnSetting")
        self.OneClick("BtnContractUs")
        self.WaitForElementText("ContractUsTitle", "联系我们", 5, "打开联系我们失败")
        self.OneClick("WeixinToggle")
        self.s_witForImg(SourcePath.File_ContractUs_Weixin, 5, "打开微信二维码失败")
        self.OneClick("QQToggle")
        self.s_witForImg(SourcePath.File_ContractUs_QQ1, 5, "打开QQ群列表失败")
        self.OneClick("AddQQ")
        self.s_witForImg(SourcePath.File_ContractUs_QQ2, 5, "打开QQ群二维码失败")

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
