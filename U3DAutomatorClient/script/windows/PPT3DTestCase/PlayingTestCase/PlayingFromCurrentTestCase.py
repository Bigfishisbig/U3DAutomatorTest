#!/usr/bin/env python
# coding=utf-8
"""
文件名称：PlayingFromCurrentTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/2/25 15:45
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class PlayingFromCurrentTestCase(Action, Operation, SystemDiaglog):
    '''从当前页开始放映'''

    def test_main(self):
        '''从当前页开始放映'''

        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        
        self.OneClick("BtnNewPage")
        self.OneClick("BtnNewPage")
        # self.ListClick("PageItem3")
        # self.ListClick("PageNum", 2)
        self.OneClick("BtnPlayFirst")
        s = self.getPathValue("Page")
        path = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page%s" % s[2]
        time.sleep(5)
        if self.isVisibleV(path):
            pass
        else:
            assert False, "当前页播放失败"

        self.endScene(tag)
        time.sleep(5)
        self.EndTag()
