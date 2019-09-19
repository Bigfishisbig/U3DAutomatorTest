#!/usr/bin/env python
# coding=utf-8
"""
文件名称：PlayingSwitchPageMouseWheelTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/2/25 17:28
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class PlayingSwitchPageMouseWheelTestCase(Action, Operation, SystemDiaglog):
    '''放映态切页_鼠标滚轮'''

    def test_main(self):
        '''放映态切页_鼠标滚轮'''

        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__
        
        self.OneClick("BtnNewPage")
        self.OneClick("BtnNewPage")
        self.ListClick("PageItem1")
        self.OneClick("BtnPlaying")
        time.sleep(2)
        self.Click_XY()
        time.sleep(1)
        #self.type_keyboard(34)  # PgDown键位码是34
        self.startScene(tag)
        for i in range(1500):
            self.mouse_wheel(-1)  # 向下滚动
        s = self.getPathValue("Page")
        path = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page%s" % s[1]
        if self.isVisibleV(path):
            pass
        else:
            assert False, "向下滚动切页失败"
        time.sleep(1)
        for i in range(1500):
            self.mouse_wheel(1)  # 向下滚动
        path = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page%s" % s[0]
        if self.isVisibleV(path):
            pass
        else:
            assert False, "向上滚动切页失败"

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
