#!/usr/bin/env python
# coding=utf-8
"""
文件名称：InsertAudioTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2019/1/7 17:59
修改时间：
软件：PyCharm
"""

from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath
import win32api, win32con

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化为指定的编码格式


class InsertAudioTestCase(Action, Operation, SystemDiaglog):
    '''插入音频'''

    def test_main(self):
        '''插入音频'''
        self.OperationSetting()
        self.Init3DPPT()

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        paths = [SourcePath.File_Audio_ape, SourcePath.File_Audio_m4a, SourcePath.File_Audio_m4r,
                 SourcePath.File_Audio_mp3, SourcePath.File_Audio_wav, SourcePath.File_Audio_wma]
        titles = ["APE.ape", "M4A.m4a", "M4R.m4r", "MP3.mp3", "WAV.wav", "WMA.wma"]
        i=0
        for path in paths:
            self.OneClick("BtnInsert")
            self.OpenAudio(path)
            self.AudioR(titles[i])
            i = i + 1
            time.sleep(5)


        # begin = datetime.datetime.now()
        # while self.ElementTxt('FileName') != 'PPTOpenTest':
        #     pass
        # end = datetime.datetime.now()
        # k = end - begin
        # #print "open file cost:%ss" % k.total_seconds()