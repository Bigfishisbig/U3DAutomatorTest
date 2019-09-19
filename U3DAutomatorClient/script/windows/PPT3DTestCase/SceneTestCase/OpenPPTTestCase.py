# coding=utf-8
"""
Open3DPPT
作者: qa-ycy
版本: 3DPPT Final.2017.1225.1314
创建日期：2018.01.05
修改日期：2018.01.05
"""

from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath
import datetime


reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化为指定的编码格式


class OpenPPTTestCase(Action, Operation, SystemDiaglog):
    # 打开pptx文件
    def test_main(self):
        self.OperationSetting()
        self.Init3DPPT()
        file_path = SourcePath.File_PPTOpenTest_pptx
        self.Open3DPPTFile(file_path)
        self.WaitForElementText('FileName', 'PPTOpenTest', 10, "PPT文件10秒内未打开完成")
        #print "解析开始："
        t = []
        t.append(datetime.datetime.now())
        # t[0] = datetime.datetime.now()
        # self.LoadingWait("Slider", 0.5)
        i=1
        num = self.ElementNum("ImgLoading")
        #print "num:", num
        while True:
            # if self.engine.find_elements_path(self.PPT3DPath["ImgLoading"])[i-1]:
            if i<=num :
                if self.engine.find_elements_path(self.PPT3DPath["ImgLoading"])[i-1].Visible == False:
                    t.append(datetime.datetime.now())
                    k = t[i] - t[i-1]
                    #print "analysis file %d cost:%ss" %(i, k.total_seconds())
                    #print "analysis file cost:%ss" % ((t[i]-t[0]).total_seconds())
                    i = i + 1
            else:
                break
            # else:
            #     k = t[i-1] - t[0]
            #     #print "analysis file cost:%ss" % k.total_seconds()
            #     break
        # begin = datetime.datetime.now()
        # while self.ElementTxt('FileName') != 'PPTOpenTest':
        #     pass
        # end = datetime.datetime.now()
        # k = end - begin
        # #print "open file cost:%ss" % k.total_seconds()










