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
from main.utils.profile import monitor_unity_start
from script.windows.PPT3DSetting.SourcePath import SourcePath
from main.object.enum import *
from script_handler import ScriptHandler
from main.utils.xml_reader import get_config

reload(sys)
sys.setdefaultencoding('UTF-8') #将脚本编码格式转化为指定的编码格式

# os.environ[Environment.VERSION] = Version.Debug
# os.environ[Environment.PLATFORM] = Platform.Windows
# # os.environ[Environment.MODULE] = ""
#
# # Windows设置项
# os.environ[Environment.TEST_PATH] = get_config().exe_path
# os.environ[Environment.WINDOWS_TITLE] = "3DPPT"
class Start3DPPTTestCase(Action, Operation, SystemDiaglog):
    '''启动3DPPT'''

    # 启动3dPPT
    def setUp(self):
        self.SetTag("Start3DPPT", time.time())

        monitor_unity_start(self.__class__.__name__)
        print time.time()
        try:
            self.engine = get_engine()
            print time.time()
            # previousTime = time.time()
            get_application().open_application()
            print time.time()
            # currentTime = time.time()
            # #print "启动耗时：", int(currentTime) - int(previousTime), "秒"
        except Exception:
            print "Error:3DPPT启动失败"
        time.sleep(10)

        monitor_unity_start(self.__class__.__name__)

    def test_main(self):
        '''启动3DPPT'''
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.OperationSetting()
        self.Init3DPPT()
        self.WaitForElementText('FileName', '演示文稿', 20, "3DPPT在30s内未启动")
        self.s_witForImg(SourcePath.File_Img_FullScreen, 10, "3DPPT在60s内未启动", accurate=0.5)

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
