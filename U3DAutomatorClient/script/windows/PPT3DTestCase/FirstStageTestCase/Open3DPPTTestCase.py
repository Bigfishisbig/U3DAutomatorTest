# coding=utf-8
"""
Open3DPPT
作者: qa-wang
版本: 3DPPT Final.2017.1225.1314
创建日期：2017.12.26
修改日期：2017.12.26
"""

from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath
import datetime

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化为指定的编码格式


class Open3DPPTTestCase(Action, Operation, SystemDiaglog):
    '''打开3dpx文件'''

    # 打开3dpx文件
    def test_main(self):
        '''打开3dpx文件'''
        self.OperationSetting()
        self.Init3DPPT()
        file_path = SourcePath.File_3DPPTOpenTest_3dpx
        self.SetTag("打开3dpx文件", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        
        self.Open3DPPTFile(file_path)
        t = []
        t.append(datetime.datetime.now())
        t[0] = datetime.datetime.now()
        if self.LoadingWaitNot(0.5, "ImgLoading") == -999:
            # assert False, "3dpx打开失败"
            pass
        num = self.ElementNum("ImgLoading")
        #print "num:", num
        i = 1
        if num > 0:
            while True:
                # if self.engine.find_elements_path(self.PPT3DPath["ImgLoading"])[i-1]:
                flag = self.engine.find_elements_path(self.PPT3DPath["ImgLoading"])[num - 1].Visible
                if flag == False:
                    t.append(datetime.datetime.now())
                    k = (t[i] - t[0]).total_seconds()
                    #print "analysis file cost:%ss" % (k)
                    # 解析时间写入文件
                    file_handler = open(SourcePath.File_Log_Analysis_PPTX, mode='a')
                    file_handler.write('%s 3dpx文件解析时间 %s\n' % (datetime.datetime.now(), k))
                    file_handler.close()
                    break
                if (datetime.datetime.now() - t[0]).total_seconds() > 300:  # 解析时间超过5分钟
                    assert False, "3dpx解析时间超过5分钟"
        else:
            pass

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
        # begin = datetime.datetime.now()
        # while self.ElementTxt('FileName') != 'PPTOpenTest':
        #     pass
        # end = datetime.datetime.now()
        # k = end - begin
        # #print "open file cost:%ss" % k.total_seconds()

