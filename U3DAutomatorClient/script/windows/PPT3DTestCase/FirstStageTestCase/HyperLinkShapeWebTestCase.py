#!/usr/bin/env python
# coding=utf-8
"""
文件名称：HyperLinkShapeWebTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/14 17:24
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class HyperLinkShapeWebTestCase(Action, Operation, SystemDiaglog):
    '''形状网页超链接'''

    def test_main(self):
        '''形状网页超链接'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("形状网页超链接", time.time())
        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertShape")
        self.OneClick("BtnShape_Rectangle")
        time.sleep(1)
        self.Click_XY(dx=-50, dy=-50)
        url = "www.baidu.com"
        url_web = "http://www.baidu.com"
        self.HyperlinkWeb(url)

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.isHyperlinkWeb(url_web)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()