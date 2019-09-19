#!/usr/bin/env python
# coding=utf-8
"""
文件名称：HyperLinkShapeTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/14 16:29
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class HyperLinkShapeTestCase(Action, Operation, SystemDiaglog):
    '''形状超链接'''

    def test_main(self):
        '''形状超链接'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("形状超链接", time.time())
        self.OneClick("BtnNewPage")
        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertShape")
        self.OneClick("BtnShape_Rectangle")
        time.sleep(1)
        self.Click_XY(dx=-50, dy=-50)
        Msg = "hahahahaha"
        self.HyperlinkPage(2, Msg)  # 2:下一张
        PageIDs = self.getPathValue("Page")
        page_path_0 = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page%s" % PageIDs[1]

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.isHyperlinkPlaying(disk=5, ErrMsg="超链接失败", page_path_true=PageIDs[1])  # 5:链接幻灯片

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
