#!/usr/bin/env python
# coding=utf-8
"""
文件名称：InsertCoursewareWholeTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/3/18 21:02
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath
import datetime

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class InsertCoursewareWholeTestCase(Action, Operation, SystemDiaglog):
    '''插入整个课件'''

    def test_main(self):
        '''插入整个课件'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("插入课件", time.time())

        self.deleteDir()

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.InsertWholeCourseware()
        t = []
        t.append(datetime.datetime.now())
        t[0] = datetime.datetime.now()
        if self.LoadingWaitNot(0.1, "ImgLoading") == -999:
            assert False, "插入课件打开失败"
        num = self.ElementNum("ImgLoading")
        #print "num:", num
        i = 1
        while True:
            # if self.engine.find_elements_path(self.PPT3DPath["ImgLoading"])[i-1]:
            flag = self.engine.find_elements_path(self.PPT3DPath["ImgLoading"])[num - 1].Visible
            if flag == False:
                t.append(datetime.datetime.now())
                k = (t[i] - t[0]).total_seconds()
                #print "analysis file cost:%ss" % (k)
                # 解析时间写入文件
                file_handler = open(SourcePath.File_Log_Analysis_PPTX, mode='a')
                file_handler.write('%s 插入课件文件解析时间 %s\n' % (datetime.datetime.now(), k))
                file_handler.close()
                break
            if (datetime.datetime.now() - t[0]).total_seconds() > 300:  # 解析时间超过5分钟
                assert False, "插入课件解析时间超过5分钟"
        time.sleep(5)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
