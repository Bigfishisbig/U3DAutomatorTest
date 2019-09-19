#!/usr/bin/env python
# coding=utf-8
"""
文件名称：MenuFuncVideoTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/2/26 15:36
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class MenuFuncVideoTestCase(Action, Operation, SystemDiaglog):
    '''放映态菜单_视频'''

    def test_main(self):
        '''放映态菜单_视频'''
        self.OperationSetting()
        self.Init3DPPT()
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        
        videos = [SourcePath.File_Video_3gp]
        i = 0
        for video in videos:
            self.OneClick("BtnInsert")
            self.OpenVideo(video)
            self.MenuPlaying("ItemVideo", "%d复制粘贴失败" % i)
            # self.RevertAndRecover(SourcePath.File_Insert_JPEG)

            time.sleep(2)
            i = i + 1

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
