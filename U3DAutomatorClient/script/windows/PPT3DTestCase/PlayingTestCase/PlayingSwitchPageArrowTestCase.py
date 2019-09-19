#!/usr/bin/env python
# coding=utf-8
"""
文件名称：PlayingSwitchPageArrowTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/2/25 16:59
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath
import win32api, win32con

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class PlayingSwitchPageArrowTestCase(Action, Operation, SystemDiaglog):
    '''放映态切页_方向键'''

    def test_main(self):
        '''放映态切页_方向键'''

        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__

        self.OneClick("BtnNewPage")
        self.OneClick("BtnNewPage")
        self.ListClick("PageItem1")
        self.OneClick("BtnPlaying")
        self.startScene(tag)
        self.type_keyboard(39)  # right arrow键位码是39
        s = self.getPathValue("Page")
        #print "s[1]:", s[1]
        path = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page%s" % s[1]
        if self.isVisibleV(path):
            pass
        else:
            assert False, "右方向键切页失败"
        time.sleep(1)
        self.type_keyboard(37)  # left arrow键位码是37
        path = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page%s" % s[0]
        if self.isVisibleV(path):
            pass
        else:
            assert False, "左方向键切页失败"
        self.type_keyboard(40)  # down arrow键位码是40
        path = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page%s" % s[1]
        if self.isVisibleV(path):
            pass
        else:
            assert False, "下方向键切页失败"
        time.sleep(1)
        self.type_keyboard(38)  # up arrow键位码是38
        path = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page%s" % s[0]
        if self.isVisibleV(path):
            pass
        else:
            assert False, "上方向键切页失败"

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()