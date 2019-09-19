# coding=utf-8
"""
Open3DPPT
作者: qa-ycy
版本: 3DPPT Final.2017.1225.1314
创建日期：2017.12.26
修改日期：2017.12.26
"""

from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from main.engine_handler import get_application
from main.engine_handler import get_engine
from main.utils.profile import monitor_unity_start, monitor_unity_stop
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8') #将脚本编码格式转化为指定的编码格式


class Start3DPPTTestCase2(Action, Operation, SystemDiaglog):
    # 启动3dPPT及关闭是否正常
    def setUp(self):
        # self.sikuli_Init()
        get_logger().info('-' * 30 + __package__ + "." + self.__class__.__name__ + ".setUp" + '-' * 30)
        self.SetTag("DoubleClickStart3DPPT", time.time())
        self.s_doubleClickImg(SourcePath.File_Image_Icon_3DPPT, 5, "未找到3DPPT快捷方式")
        time.sleep(10)
        monitor_unity_start(self.__class__.__name__)

    def tearDown(self):
        testImagPath = os.getcwd() + ur"\\script\\windows\\PPT3DSetting\\Source\\ScreenShoot"
        # get_windows_handler().screen_cap(testImagPath + "\\" + self.__class__.__name__ + "_" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".png")
        # self.engine.screen_cap(testImagPath + "\\" + self.__class__.__name__ + "_" + str(time.time()) + + ".png")
        time.sleep(10)
        get_logger().info('-' * 30 + __package__ + "." + self.__class__.__name__ + ".tear_down" + '-' * 30)
        monitor_unity_stop(self.__class__.__name__)
        # self.getScreenShot(SourcePath.File_ScreenShoot_Path, self.timeImageName())
        time.sleep(5)

        # get_application().close_application()
        # set_tag("")
        time.sleep(5)

    def test_main(self):
        self.OperationSetting()
        # self.sikuli_Init()
        # self.WaitForElementText('FileName', '演示文稿', 30, "3DPPT在30s内未启动")
        # self.s_witForImg(SourcePath.File_Img_FullScreen, 60, "3DPPT在60s内未启动")
        imgPath = SourcePath.File_Img_FullScreen
        WaitTime = 5
        ErrMsg = "3DPPT在60s内未启动"
        i = 0
        while self.s_isExists(imgPath, 0) == False and i < WaitTime:
            #print self.s_isExists(imgPath)
            i += 1
            time.sleep(1)
        #print "------------60s结束------------"
        if self.s_isExists(imgPath, 0) == "True":
            pass
        else:
            # self.getScreenShot(SourcePath.File_ScreenShoot_Path, self.timeImageName())
            os.system("taskkill /f /im 3DPPT.exe")
            assert False, ErrMsg
        self.s_clickImg(SourcePath.File_Image_Icon_Close_3DPPT, 5, "未找到3DPPT关闭按钮")
        self.endScene(tag)
        time.sleep(1)
        self.EndTag()