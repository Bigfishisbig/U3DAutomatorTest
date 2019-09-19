#!/usr/bin/env python
# coding=utf-8
"""
文件名称：HyperLinkImageTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/14 16:01
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class HyperLinkImageTestCase(Action, Operation, SystemDiaglog):
    '''图片超链接'''

    def test_main(self):
        '''图片超链接'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("图片超链接", time.time())

        self.OneClick("BtnNewPage")
        self.OneClick("BtnInsert")
        self.OpenImage(SourcePath.File_Image_bmp)
        # self.OneClick("BtnImageBack")
        self.ClickRight_XY()
        self.isElementExist("BtnStageRight", "右键失效")  # 右键是否成功
        self.ListClick("BtnStageRightHyperLink")  # 超链接
        self.OneClick("BtnPPTToggle")
        self.OneClickL("TglPreviousPPT")
        self.OneClick("BtnLinkSubmit")
        PageIDs = self.getPathValue("Page")

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.isHyperlinkPlaying(disk=4, ErrMsg="超链接失败", page_path_true=PageIDs[1])  # 4:图片连接幻灯片

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
