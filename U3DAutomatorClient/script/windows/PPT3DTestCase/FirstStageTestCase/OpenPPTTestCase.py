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
    '''打开pptx文件'''

    # 打开pptx文件
    def test_main(self):
        '''打开pptx文件'''
        self.OperationSetting()
        self.Init3DPPT()
        file_path = SourcePath.File_PPTOpenTest_pptx
        self.SetTag("打开pptx文件", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.Open3DPPTFile(file_path)
        t = []
        t.append(datetime.datetime.now())
        t[0] = datetime.datetime.now()
        # self.WaitForElementText("TxtSaveStatus", "课件正在打开中...", 10, "10s内未开始打开课件")
        # # self.LoadingWait("SliderFileSave")
        # self.WaitForElementText('FileName', 'PPTOpenTest', 30, "PPT文件30秒内未打开")
        # #print "解析开始："
        # self.LoadingWait("SliderTip", 0.1)
        # #print "进度条消失"
        if self.LoadingWaitNot(0.1, "ImgLoading") == -999:
            # assert False, "打开pptx文件失败"
            pass
        i = 1
        num = self.ElementNum("ImgLoading")
        print "num:", num

        while True:
            if num < 1:
                break
            # if self.engine.find_elements_path(self.PPT3DPath["ImgLoading"])[i-1]:
            flag = self.engine.find_elements_path(self.PPT3DPath["ImgLoading"])[num-1].Visible
            if flag == False:
                t.append(datetime.datetime.now())
                k = (t[i] - t[0]).total_seconds()
                #print "analysis file cost:%ss" % (k)
                # 解析时间写入文件
                file_handler = open(SourcePath.File_Log_Analysis_PPTX, mode='a')
                file_handler.write('%s pptx文件解析时间 %s\n' %(datetime.datetime.now(), k))
                file_handler.close()
                break

            if (datetime.datetime.now() - t[0]).total_seconds() > 300: # 解析时间超过5分钟
                assert False, "pptx解析时间超过5分钟"

            # if i <= num :
            #     flag = self.engine.find_elements_path(self.PPT3DPath["ImgLoading"])[i-1].Visible
            #     if flag == False:
            #         i = i + 1
            # else:
            #     t.append(datetime.datetime.now())
            #     # k = t[i] - t[i - 1]
            #     # #print "analysis file %d cost:%ss" % (i, k.total_seconds())
            #     #print "analysis file cost:%ss" % ((t[i] - t[0]).total_seconds())
            #     break
            # if (datetime.datetime.now() - t[0]).total_seconds() > 300: # 解析时间超过5分钟
            #     assert False, "解析时间超过5分钟"
        #
        # self.endScene(tag)


        time.sleep(10)
        self.EndTag()
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










