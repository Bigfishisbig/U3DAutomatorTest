#!/usr/bin/env python
# coding=utf-8
"""
文件名称：StartRightTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/9/16 21:34
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath
from main.engine_handler import get_engine
from main.object.enum import *
from main.utils.profile import monitor_unity_start, monitor_unity_stop
from TempOperate import TempOperation
from main.utils.windows_handler import get_windows_handler

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class StartRightTestCase(Action, Operation, SystemDiaglog, TempOperation):
    '''右键启动3DPPT程序'''

    def setUp(self):
        get_logger().info('-' * 30 + __package__ + "." + self.__class__.__name__ + ".setUp" + '-' * 30)
        self.engine = get_engine()

        pass

    def tearDown(self):
        self.testImagPath = os.getcwd() + ur"\report\windows\screenshoot"
        # get_windows_handler().screen_cap(testImagPath + "\\" + self.__class__.__name__ + "_" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".png")
        if os.path.exists(self.testImagPath):
            pass
        else:
            os.mkdir(self.testImagPath)
        get_windows_handler().screen_cap(self.testImagPath + "\\" + self.__class__.__name__ + ".png")
        os.system(SourcePath.File_3DPPT_Kill)
        pass

    def test_main(self):
        '''右键启动3DPPT程序'''

        self.OperationSetting()

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__
        self.startScene(tag)

        print "开始启动"
        exe_path = os.environ[Environment.TEST_PATH]
        error_path = os.path.dirname(exe_path) + "/LO/PPTEditor/temp/error.txt"
        analyse_spend_time = 0
        rendering_break_time = 0
        rendering_spend_time = 0
        rendering_path = u"C:/Users/Administrator/AppData/Roaming/3DPPT/Log/" + time.strftime('%Y%m%d',
                                                                                              time.localtime()) + ".log"
        try:

            self.deleteFile(error_path)
            self.deleteFile(rendering_path)
        except Exception, e:
            print u"删除文件失败"
            print str(e)

        # self.s_clickImg(SourcePath.File_Img_PPTXThumbnail, 5, "未找到pptx图标", accurate=0.7)
        self.s_rightclickImg(SourcePath.File_Img_PPTXThumbnail, 5, "未找到pptx图标右键")
        self.s_clickImg(SourcePath.File_Img_RightStart, 5, "未找到打开3DPPT程序右键菜单")
        # time.sleep(5)

        monitor_unity_start(self.__class__.__name__)
        start_time = time.time()
        # 获取解析渲染时间
        for i in range(200):
            print i
            try:
                flag = self.isExist(error_path, "end!!!!!")
                print "flag:", flag
                if flag:
                    rendering_break_time = rendering_break_time - 1
                    isBreak = 'N'
                    break
            except Exception, e:
                print str(e)
                break
            time.sleep(0.5)
        else:
            try:
                flag = False
                # self.copy2Path(error_path, report_path+"error\\error_%s.txt"%start_time)
                self.Screen_cap("error_%s_png" % start_time)
            except Exception, e:
                print str(e)

        analyse_s = '"actual":"([\d.]+)"'
        rendering_s = '"解析器返回:页FODP文件消息/s","TimeSpan":"([\d.]+)"'
        print u"渲染日志路径：", rendering_path
        try:

            analyse_spend_time = self.getPathValue1(rendering_path, rendering_s)
            # analyse_spend_time = op.getPathValue1(error_path)
            rendering_spend_time = self.getPathValue2(rendering_path, "解析渲染", '"TimeSpan":"([\d.]+)"')
        except Exception, e:
            print str(e)
            self.copy2Path(rendering_path, SourcePath.File_Source + "error/error_rendering_%s.txt" % start_time)
            pass
        print "actual:", analyse_spend_time
        print "rendering:", rendering_spend_time
        end_time = time.time()
        time.sleep(1)
        # subprocess.Popen(u'"D:\Program Files (x86)\PCPA ASSISTENT\AutoImport\ProAutoImport.exe" --ENDSCENE("打开多表格文件")')
        monitor_unity_stop(self.__class__.__name__)  # 停止性能监控
        # input(u"结束")
        self.s_clickImg(SourcePath.File_Image_Icon_Close_3DPPT, 5, "未完成关闭3DPPT")
        # end_time = time.time()
        spend_time = end_time - start_time
        if flag == False:
            analyse_spend_time = -1
            rendering_spend_time = -1
        self.create()
        self.xls_getOldXls(SourcePath.File_Source + "StartRight_" + os.environ[Environment.StartTime] + ".xls")
        self.xls_write(str(start_time), str(end_time), analyse_spend_time, rendering_spend_time)
        self.xls_close(SourcePath.File_Source + "StartRight_" + os.environ[Environment.StartTime] + ".xls")


        self.endScene(tag)

        # self.s_clickImg(SourcePath.File_Img_RightStart, 5, "未找到打开3DPPT程序右键菜单")
