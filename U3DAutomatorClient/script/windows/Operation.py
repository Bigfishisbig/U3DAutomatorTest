# coding=utf-8
from script.windows.PPT3DSetting.Settings import PPT3DPath
from script.windows.sample import Sample
import time, os, sys
from main.log.logger import get_logger
from main.utils.ImageRecognize import ImageRecognize
import win32api, win32com, win32con
import socket, pyperclip, _winreg, re, shutil
from win32com.client import GetObject
import subprocess
from main.utils.xlsx_writer import XlsxWriter

reload(sys)
sys.setdefaultencoding('UTF-8') #将脚本编码格式转化为指定的编码格式


class Operation(Sample):

    # ============OperationSetting=======每次调用的时候要先启动OperationSetting=================
    def OperationSetting(self):
        self.PPT3DPath = PPT3DPath().PPT3DPath
        self.CapPath = os.getcwd()


    '''单元素---鼠标左键点击'''
    def OneClick(self, Element=None, sleeptime=1):
        for i in range(20):
            if self.engine.find_element(self.PPT3DPath[Element]):
                self.engine.find_element(self.PPT3DPath[Element]).click(sleeptime)
                break
            else:
                time.sleep(1)

    '''列表元素---鼠标左键点击'''
    def ListClick(self, Element=None, x=0, sleeptime=1):
        time.sleep(1)
        for i in range(20):
            if self.engine.find_elements_path(self.PPT3DPath[Element])[x]:
                self.engine.find_elements_path(self.PPT3DPath[Element])[x].click(sleeptime)
                break
            else:
                time.sleep(2)

    '''列表元素---鼠标左键点击'''

    def ListDoubleClick(self, Element=None, x=0, sleeptime=1):
        time.sleep(1)
        for i in range(20):
            if self.engine.find_elements_path(self.PPT3DPath[Element])[x]:
                self.engine.find_elements_path(self.PPT3DPath[Element])[x].click_double(sleeptime)
                break
            else:
                time.sleep(2)

    '''列表元素偏差---鼠标左键点击'''
    def ListClickL(self, Element=None, x=0, z=0, o=0, sleeptime=1):
        for i in range(20):
            if self.engine.find_elements_path(self.PPT3DPath[Element])[x]:
                Element0 = self.engine.find_elements_path(self.PPT3DPath[Element])[x]
                self.engine.click(Element0.Bounds.centre_x + z, Element0.Bounds.centre_y + o)
                time.sleep(sleeptime)
                break
            else:
                time.sleep(2)

    def ListClickV(self, Element=None, x=0, z=0, o=0, sleeptime=1):
        """
        列表元素可变路径单击
        :return:
        """
        for i in range(20):

            if self.engine.find_elements_path(Element)[x]:
                Element0 = self.engine.find_elements_path(Element)[x]
                self.engine.click(Element0.Bounds.centre_x + z, Element0.Bounds.centre_y + o)
                time.sleep(sleeptime)
                break
            else:
                time.sleep(2)

    def ListDoubleClickV(self, Element=None, x=0, z=0, o=0, sleeptime=1):
        """
        列表元素可变路径双击
        :return:
        """
        for i in range(20):

            if self.engine.find_elements_path(Element)[x]:
                Element0 = self.engine.find_elements_path(Element)[x]
                self.engine.click_double(Element0.Bounds.centre_x + z, Element0.Bounds.centre_y + o)
                time.sleep(sleeptime)
                break
            else:
                time.sleep(2)


    '''单元素偏差---鼠标右键点击'''
    def OneClickR(self, Element=None, z=0, o=0, sleeptime=1):
        for i in range(20):
            if self.engine.find_element(self.PPT3DPath[Element]):
                x = self.engine.find_element(self.PPT3DPath[Element]).Bounds.centre_x
                y = self.engine.find_element(self.PPT3DPath[Element]).Bounds.centre_y
                self.engine.click_right(x + z, y + o)
                time.sleep(sleeptime)
                break
            else:
                time.sleep(2)


    '''列表元素偏差---鼠标右键点击'''
    def ListClickR(self, Element=None, x=0, z=0, o=0, sleeptime=1):
        Element0 = self.engine.find_elements_path(self.PPT3DPath[Element])[x]
        self.engine.click_right(Element0.Bounds.centre_x + z, Element0.Bounds.centre_y + o)
        time.sleep(sleeptime)

    '''列表元素---鼠标右键点击'''
    def ListClickRight(self, Element=None, x=0, sleeptime=1):
        self.engine.find_elements_path(self.PPT3DPath[Element])[x].click_right(sleeptime)

    '''单元素---鼠标右键点击'''
    def OneClickRight(self, Element=None,  sleeptime=1):
        self.engine.find_element(self.PPT3DPath[Element]).click_right(sleeptime)

    '''键盘按键'''
    def KeyPress(self, key, sleep_time):
        self.engine.key_press(key, sleep_time)

    '''获取元素中心点X坐标'''
    def PositionX(self, Element):
        x = self.engine.find_element(self.PPT3DPath[Element]).Bounds.centre_x
        return x

    '''获取元素中心点Y坐标'''
    def PositionY(self, Element):
        y = self.engine.find_element(self.PPT3DPath[Element]).Bounds.centre_x
        return y

    '''移动到元素中心点或中心点偏移位置'''
    def Move_Pos(self, Element=None,x0=0,y0=0, sleeptime=1):
        x = self.engine.find_element(self.PPT3DPath[Element]).Bounds.centre_x
        y = self.engine.find_element(self.PPT3DPath[Element]).Bounds.centre_y
        self.engine.move_pos(x+x0, y+y0)
        time.sleep(sleeptime)

    '''错误截图'''
    def ErrorScreen_cap(self, CapName="Error"):
        ErrorCapPath = self.CapPath + ur"\image\ErrorCap"
        if not os.path.isdir(ErrorCapPath):
            os.mkdir(ErrorCapPath)
        self.engine.screen_cap(ErrorCapPath + "\\" + CapName + ".png")

    '''测试截图'''
    def TestScreen_cap(self, CapName="Test"):
        TestCapPath = self.CapPath + ur"\image\TestCap"
        if not os.path.isdir(TestCapPath):
            os.mkdir(TestCapPath)
        self.engine.screen_cap(TestCapPath + "\\" + CapName + ".png")

    '''拖动操作'''
    def Swipe_List(self, ElementOne=None, One=0, ElementTwo=None, Two=0, steps=1, duration=1, x2=0, y2=0, x1=0, y1=0,
              sleeptime=0.5):
        Element1 = self.engine.find_elements_path(self.PPT3DPath[ElementOne])[One]
        Element2 = self.engine.find_elements_path(self.PPT3DPath[ElementTwo])[Two]
        self.engine.swipe_press(Element1.Bounds.centre_x + x1, Element1.Bounds.centre_y + y1, Element2.Bounds.centre_x + x2,
                                Element2.Bounds.centre_y + y2, steps, duration, sleeptime)

    '''拖动操作'''

    def Swipe(self, ElementOne=None, ElementTwo=None, steps=1, duration=1, x2=0, y2=0, x1=0, y1=0,
                   sleeptime=0.5, ElementType="0"):
        if ElementType=="var":
            Element1 = self.engine.find_element(ElementOne)
            Element2 = self.engine.find_element(ElementTwo)
        else:
            Element1 = self.engine.find_element(self.PPT3DPath[ElementOne])
            Element2 = self.engine.find_element(self.PPT3DPath[ElementTwo])
        self.engine.swipe_press(Element1.Bounds.centre_x + x1, Element1.Bounds.centre_y + y1,
                                Element2.Bounds.centre_x + x2,
                                Element2.Bounds.centre_y + y2, steps, duration, sleeptime)

    def Swipe_Media(self, ElementOne=None, ElementTwo=None, steps=1, duration=1, x2=0, y2=0, x1=0, y1=0,
              sleeptime=0.5):
        """
        音视频滑动条拖动
        :return:
        """
        Element1 = self.engine.find_element(self.PPT3DPath[ElementOne])
        Element2 = self.engine.find_element(self.PPT3DPath[ElementTwo])
        self.engine.swipe_press(Element1.Bounds.centre_x + x1, Element1.Bounds.centre_y + y1, Element2.Bounds.centre_x + Element2.Bounds.Width / 2 + x2,
                                Element2.Bounds.centre_y + Element2.Bounds.Height / 2 + y2, steps, duration, sleeptime)


    '''滚轴Y滑动设置'''
    def Sliding(self,Elements="Sliding", z=20, steps=1, duration=1):
        Element = self.engine.find_element(self.PPT3DPath[Elements])
        self.engine.swipe_press(Element.Bounds.centre_x, Element.Bounds.centre_y, Element.Bounds.centre_x,Element.Bounds.centre_y + z, steps, duration)

    '''滚轴X滑动设置'''

    def SlidingLevel(self, Elements="Sliding", z=20, steps=1, duration=1):
        Element = self.engine.find_element(self.PPT3DPath[Elements])
        self.engine.swipe_press(Element.Bounds.centre_x, Element.Bounds.centre_y, Element.Bounds.centre_x + z,
                                Element.Bounds.centre_y, steps, duration)

    '''载入判断'''
    '''有当前元素等待'''
    def LoadingWait(self, Element="LoadingWait",loading=1):
        for i in range(100):
            if self.engine.find_element(self.PPT3DPath[Element]):
                time.sleep(loading)
            else:
                # break
                return 0
        return -999

    '''没有当前元素等待'''
    def LoadingWaitNot(self, loading=3,Element="LoadingWait"):
        for i in range(100):
            if not self.engine.find_element(self.PPT3DPath[Element]):
                time.sleep(loading)
            else:
                # break
                return 0
        return -999

    '''载入等待'''
    def Loading(self, Element="BtnLogin",WaitTime=3):
        for i in range(100):
            if self.engine.find_element(self.PPT3DPath[Element]):
                break
            else:
                time.sleep(WaitTime)

    '''等待元素的值匹配'''
    def WaitForElementText(self, Element, Value, WaitTime, ErrMsg, loadTime=1):
        i = 0
        while self.engine.find_element(self.PPT3DPath[Element]).Txt != Value and i < WaitTime:
            i += 1
            time.sleep(loadTime)
        if i == WaitTime:
            if self.engine.find_element(self.PPT3DPath[Element]).Txt == Value:
                return
            else:
                assert False, ErrMsg
        else:
            return

    '''等待元素的值匹配'''
    def WaitForElementText_Language(self, Element, Value, WaitTime, ErrMsg):
        i = 0
        while self.engine.find_element(self.PPT3DPath[Element]).Txt != Value and i < WaitTime:
            i += 1
            time.sleep(1)
        if self.engine.find_element(self.PPT3DPath[Element]).Txt == Value:
            return
        else:
            self.OneClick("BtnSetting")
            self.OneClick("BtnPublicSetup")
            self.OneClick("LanguageSetup")
            self.OneClick("LanguageDropDown")
            self.OneClick("SimpleChinese")
            self.OneClick("BtnSettingOK")
            assert False, ErrMsg

    '''找到指定Txt元素'''
    def TxtFindElement(self,Element,Value):
        for i in range(int(self.engine.find_element(self.PPT3DPath["totalPage"]).Txt)-1):
            if not self.engine.find_element(self.PPT3DPath[Element]).Txt == Value:
                self.ListClick("SceneRightShowBtn")
            else:
                break

    '''获取元素Txt值'''
    def ElementTxt(self,Element,x=None, var=None):
        if not var:
            if not x:
                if self.engine.find_element(self.PPT3DPath[Element]):
                    ElementTxt = self.engine.find_element(self.PPT3DPath[Element]).Txt
                else:
                    ElementTxt = None

            else:
                ElementTxt = self.engine.find_elements_path(self.PPT3DPath[Element])[x].Txt
        else:
            if not x:
                if self.engine.find_element(Element):
                    ElementTxt = self.engine.find_element(Element).Txt
                else:
                    ElementTxt = None

            else:
                ElementTxt = self.engine.find_elements_path(Element)[x].Txt
        return ElementTxt


    '''获取元素个数'''
    def ElementNum(self, Elemnet):
        ElementNum=len(self.engine.find_elements_path(self.PPT3DPath[Elemnet]))
        return ElementNum


    '''获取最大页面'''
    def ElementPageMax(self, Elemnet):
        Page=self.engine.find_element(self.PPT3DPath[Elemnet]).Txt
        PageList=Page.split('/')
        return PageList[-1]

    '''找到对应的资源列表'''
    def ResourceTitle(self,Elmennt,Value,Elmennt2,Elmennt3,Value2,Elmennt4):
        ResourceMax=self.ElementNum(Elmennt)
        for r in range(0,ResourceMax-1,1):
            if r>=16:
                self.Sliding('Sliding', 155, 2, 2)
            if self.engine.find_elements_path(self.PPT3DPath[Elmennt])[r].Txt==Value:
                self.ListClick(Elmennt2,ResourceMax-r-1)
                break
            else:
                continue
        PageMax = int(self.ElementPageMax("ResourcePageInfo"))
        for p in range(PageMax):
            ResourceNum = self.ElementNum(Elmennt3)
            for t in range(ResourceNum):
                if self.ElementTxt(Elmennt3,t)==Value2:
                    self.ListClick(Elmennt4,ResourceNum-t-1)
                    return
                else:
                    continue
            self.OneClick("ResourcePagePageDown")

    '''输入文本'''
    def InputText(self, content):
        self.engine.input_text(content)

    '''图片匹配'''
    def imgPair(self,pngModelName,x=1920,y=1080,Accurate=0.6, isDel=True):
        '''
        isDel为true则删掉当次匹配的图片
        :param pngModelName:
        :param x:
        :param y:
        :param Accurate:
        :param isDel:
        :return:
        '''
        try:
            self.imgTimename=self.timeImageName()
            self.imgName = self.__class__.__name__+"_"+self.imgTimename
            self.Screen_cap(self.imgName)
            imgdict = ImageRecognize.proxy(#self.CapPath + ur"\image\tmp\windows\sample\%s.png"% pngModelName ,
                                            pngModelName,
                                           self.CapPath + ur"\image\source\windows\sample\%s.png" % (self.imgName) ,
                                           self.CapPath + ur"\image\target\windows\sample\%s.png" % (self.imgName),
                                           srcX=x, srcY=y,defaultAccurate=Accurate, isDel=isDel)
            # print ("imgPairSuccess")
            print "Image Match:", imgdict["match"], imgdict["maxVal"], imgdict["maxLocX"], imgdict["maxLocY"]
            get_logger().info("%s-imgPair:%s-%s------%s" % (self.imgTimename, imgdict["match"], imgdict["maxVal"], pngModelName))
            return imgdict["match"], imgdict["maxLocX"], imgdict["maxLocY"]
        except Exception, e:
            print "IMAGE MATCH FAILE：", str(e)
            get_logger().info("%s-imgPair:%s-%s" % (self.imgTimename, str(e), pngModelName))

    def Screen_cap(self, CapName="Test"):
        TestCapPath = self.CapPath + r"\image\source\windows\sample"
        # print TestCapPath
        if not os.path.isdir(TestCapPath):
            os.mkdir(TestCapPath)
        self.engine.screen_cap(TestCapPath + "\\" + CapName + ".png")

    def timeImageName(self):
        return time.strftime("%Y%m%d%H%M%S", time.localtime())

    '''图片匹配单击'''
    def imgPairClick(self,pngModelName,x=1920,y=1080,Accurate=0.8,t=1):
        match,x,y=self.imgPair(pngModelName,x,y,Accurate)
        if match:
            self.engine.click(x,y)
            time.sleep(t)

    def imgPairClickR(self, pngModelName, x=1920, y=1080, Accurate=0.8, t=1):
        match, x, y = self.imgPair(pngModelName, x, y, Accurate)
        if match:
            self.engine.click_right(x, y)
            time.sleep(t)

    # ------------------------------ 新增 ----------------------------------

    def ElementNumV(self, Element):
        """
        可变路径下的元素数量
        :return:
        """
        ElementNum = len(self.engine.find_elements_path(Element))
        return ElementNum

    def getCenter(self, Element, element_type="0"):
        """
        获取控件的中心位置
        :param Element:
        :param element_type:
        :return:
        """
        x = 0
        y = 0
        if element_type=="var":
            x = self.engine.find_element(Element).Bounds.centre_x
            y = self.engine.find_element(Element).Bounds.centre_y
        else:
            x = self.engine.find_element(self.PPT3DPath[Element]).Bounds.centre_x
            y = self.engine.find_element(self.PPT3DPath[Element]).Bounds.centre_y
        get_logger().info("%s-getCenter:%s-%s" % (Element, x, y))
        return x, y

    def WidthAndHeight(self, Element, element_type="0"):
        """
        获取控件的宽高
        :param Element:
        :return:
        """
        x = 0
        y = 0
        if element_type=="var":
            x = self.engine.find_element(Element).Bounds.Width
            y = self.engine.find_element(Element).Bounds.Height
        else:
            x = self.engine.find_element(self.PPT3DPath[Element]).Bounds.Width
            y = self.engine.find_element(self.PPT3DPath[Element]).Bounds.Height
        print "x-y:", x, y
        get_logger().info("%s-getWidthAndHeight:%s-%s" % (Element, x, y))
        return x, y

    def type_keyboardsss(self, num1=17, num2=86):
        """
        模拟键盘混合按键
        :param num1:
        :param num2:
        :return:
        """
        win32api.keybd_event(num1, 0, 0, 0)
        time.sleep(0.05)
        win32api.keybd_event(num2, 0, 0, 0)
        time.sleep(0.05)
        win32api.keybd_event(num2, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.05)
        win32api.keybd_event(num1, 0, win32con.KEYEVENTF_KEYUP, 0)

    def type_keyboard(self, num):  # 模拟键盘按键
        win32api.keybd_event(num, 0, 0, 0)  # num是键位码
        win32api.keybd_event(num, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键

    def Right(self):
        """
        原地右键
        :return:
        """
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

    def cmdCommand(self, command):
        """
        实现cmd命令
        :param command:
        :return:
        """
        os.system(command)

    def cmdSubprocess(self, command):
        """
        实现cmd命令
        :param command:
        :return:
        """
        subprocess.Popen(command)

    # 获取本机IP地址
    def get_host_ip(self):
        """
        查询本机ip地址
        :return: ip
        """
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip

    def InputStr(self, msg):
        """
        复制黏贴字符串
        :param msg:
        :return:
        """
        pyperclip.copy(msg)
        time.sleep(1)
        # pyperclip.paste()
        win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
        win32api.keybd_event(86, 0, 0, 0)  # v键位码是86
        win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(1)

    def isElementNum(self, Element, num, ErrMsg="元素数量异常"):
        """
        元素个数判断
        :param Element:
        :param num:
        :param ErrMsg:
        :return:
        """
        Enum = len(self.engine.find_elements_path(self.PPT3DPath[Element]))
        if Enum == num:
            pass
        else:
            assert False, ErrMsg  # 如果不是该数量则出错

    def isElementNumV(self, Element, num, ErrMsg="元素数量异常"):
        """
        可变路径元素个数判断
        :param Element:
        :param num:
        :param ErrMsg:
        :return:
        """
        Enum = len(self.engine.find_elements_path(Element))
        if Enum == num:
            pass
        else:
            assert False, ErrMsg  # 如果不是该数量则出错

    def isElementNumV_list(self, Element, num, ErrMsg="元素数量异常"):
        """
        列表元素个数判断
        :param Element:
        :param num:
        :param ErrMsg:
        :return:
        """
        Enum = len(self.engine.find_elements_path(self.PPT3DPath[Element]))
        if Enum == num:
            pass
        else:
            assert False, ErrMsg  # 如果不是该数量则出错

    def LoadingWaitV(self, Element="LoadingWait", loading=3):
        """
        有当前元素等待--可变元素路径
        :param Element:
        :param loading:
        :return:
        """
        for i in range(100):
            if self.engine.find_element(Element):
                time.sleep(loading)
            else:
                break

    def WaitForElementText_list(self, Element, Value, WaitTime, ErrMsg, x=0):
        """
        等待列表元素出现 --
        :param Element:
        :param Value:
        :param WaitTime:
        :param ErrMsg:
        :param x:
        :return:
        """
        # print "txt:", self.engine.find_elements_path(self.PPT3DPath[Element])[x].Txt
        i = 0
        while self.engine.find_elements_path(self.PPT3DPath[Element])[x].Txt != Value and i < WaitTime:
            i += 1
            time.sleep(1)
        if self.engine.find_elements_path(self.PPT3DPath[Element])[x].Txt == Value:
            return
        else:
            assert False, ErrMsg

    def WaitForElementNotText(self, Element, Value, WaitTime, ErrMsg,):
        """
        等待元素出现非对应文本 --
        :param Element:
        :param Value:
        :param WaitTime:
        :param ErrMsg:
        :param x:
        :return:
        """
        i = 0
        while self.engine.find_element(self.PPT3DPath[Element]).Txt == Value and i < WaitTime:
            i += 1
            time.sleep(1)
        if self.engine.find_element(self.PPT3DPath[Element]).Txt != Value:
            return
        else:
            assert False, ErrMsg

    def WaitForElementNotText_list(self, Element, Value, WaitTime, ErrMsg, x=0):
        """
        等待列表元素出现非对应文本 --
        :param Element:
        :param Value:
        :param WaitTime:
        :param ErrMsg:
        :param x:
        :return:
        """
        i = 0
        while self.engine.find_elements_path(self.PPT3DPath[Element])[x].Txt == Value and i < WaitTime:
            i += 1
            time.sleep(1)
        if self.engine.find_elements_path(self.PPT3DPath[Element])[x].Txt != Value:
            return
        else:
            assert False, ErrMsg

    def WaitForElementTextV(self, Element, Value, WaitTime, ErrMsg):
        """
        等待元素的值匹配 -- 可变路径
        :param Element:
        :param Value:
        :param WaitTime:
        :param ErrMsg:
        :return:
        """
        i = 0
        while self.engine.find_element(Element).Txt != Value and i < WaitTime:
            i += 1
            time.sleep(1)
        if self.engine.find_element(Element).Txt == Value:
            return
        else:
            assert False, ErrMsg

    def isProcessExist(self, process_name, ErrMsg):
        """
        判断进程是否存在
        :param process_name:
        :param ErrMsg:
        :return:
        """
        WMI = GetObject('winmgmts:')
        processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
        if len(processCodeCov) > 0:
            return
        else:
            assert False, ErrMsg

    def getProcess_name(self):
        """
        打开注册表,获取默认浏览器进程名
        :return:
        """
        key = _winreg.OpenKey(_winreg.HKEY_CLASSES_ROOT, 'http\shell\open\command', 0, _winreg.KEY_READ)
        result = _winreg.QueryValueEx(key, '')  # 读取默认浏览器位置
        _winreg.CloseKey(key)
        info = re.findall(r'(.+)\\(.+).exe', result[0])  # 获取程序名
        if info == []:
            info = re.findall(r'(.+)\\(.+).EXE', result[0])  # 获取程序名
        process_name = info[0][1] + '.exe'
        return process_name


    def mouse_wheel(self, num):
        """
        鼠标滚轮操作
        :param num:
        :return:
        """
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, num) # -1向下，1向上

    def list_mouse_move(self, Element, num=0):
        """
        鼠标移动到列表元素中心
        :param Element:
        :param num:
        :return:
        """
        x = self.engine.find_elements_path(self.PPT3DPath[Element])[num].Bounds.centre_x
        y = self.engine.find_elements_path(self.PPT3DPath[Element])[num].Bounds.centre_y
        self.engine.move_pos(x, y)
        time.sleep(1)

    def DoubleClick_Pos(self, Element=None,x0=0,y0=0, sleeptime=1):
        """
        双击元素偏移位置
        :param Element:
        :param x0:
        :param y0:
        :param sleeptime:
        :return:
        """
        for i in range(20):
            if self.engine.find_element(self.PPT3DPath[Element]):
                x = self.engine.find_element(self.PPT3DPath[Element]).Bounds.centre_x
                y = self.engine.find_element(self.PPT3DPath[Element]).Bounds.centre_y
                self.engine.click_double(x + x0, y + y0)
                time.sleep(sleeptime)
                break
            else:
                time.sleep(1)

    def DoubleClick_Pos_V(self, Element=None, x0=0, y0=0, sleeptime=1):
        """
        双击元素偏移位置(路径可变)
        :param Element:
        :param x0:
        :param y0:
        :param sleeptime:
        :return:
        """
        for i in range(20):
            if self.engine.find_element(Element):
                x = self.engine.find_element(Element).Bounds.centre_x
                y = self.engine.find_element(Element).Bounds.centre_y
                self.engine.click_double(x + x0, y + y0)
                time.sleep(sleeptime)
                break
            else:
                time.sleep(1)

    def mouse_moveToCore(self, Element):
        """
        鼠标移动到元素中心
        :param Element:
        :return:
        """
        x = self.engine.find_element(Element).Bounds.centre_x
        y = self.engine.find_element(Element).Bounds.centre_y
        self.engine.move_pos(x, y)

    #
    def OneClickRightV(self, Element=None, sleeptime=1):
        """
        单元素---鼠标右键点击（路径可变）
        :param Element:
        :param sleeptime:
        :return:
        """
        # print "第5个点"
        for i in range(20):
            if self.engine.find_element(Element):
                self.engine.find_element(Element).click_right(sleeptime)
                break
            else:
                time.sleep(1)

    def DoubleClickL(self, Element=None, z=0, o=0, sleeptime=1):
        """
        单元素偏差---鼠标左键双击
        :param Element:
        :param z:
        :param o:
        :param sleeptime:
        :return:
        """
        for i in range(20):
            if self.engine.find_element(Element):
                x = self.engine.find_element(Element).Bounds.centre_x
                y = self.engine.find_element(Element).Bounds.centre_y
                width = self.engine.find_element(Element).Bounds.Width
                self.engine.click_double(x + width/2 + z, y)
                time.sleep(sleeptime)
                break
            else:
                time.sleep(2)

    def Click(self, Element=None, sleeptime=1):
        """
        单元素---鼠标左键点击(路径可变)
        :param Element:
        :param sleeptime:
        :return:
        """
        for i in range(20):
            if self.engine.find_element(Element):
                self.engine.find_element(Element).click(sleeptime)
                break
            else:
                time.sleep(2)

    #
    def OneClickL(self, Element=None, z=0, o=0, sleeptime=1):
        """
        单元素偏差---鼠标左键点击(路径可变)
        :param Element:
        :param z:
        :param o:
        :param sleeptime:
        :return:
        """
        for i in range(10):
            if self.engine.find_element(Element):
                x = self.engine.find_element(Element).Bounds.centre_x
                y = self.engine.find_element(Element).Bounds.centre_y
                width = self.engine.find_element(Element).Bounds.Width
                self.engine.click(x + width/2 + z, y+o)
                time.sleep(sleeptime)
                return Element   # break
            else:
                time.sleep(2)
        return -999

    '''单元素---鼠标左键点击--可变路径'''
    def OneClickV(self, Element=None, sleeptime=1):
        for i in range(20):
            if self.engine.find_element(Element):
                self.engine.find_element(Element).click(sleeptime)
                return Element
            else:
                time.sleep(2)
        return -999

    # 单元素偏差---鼠标左键点击
    def ClickL(self, Element=None, z=0, o=0, sleeptime=1):
        for i in range(20):
            if self.engine.find_element(self.PPT3DPath[Element]):
                x = self.engine.find_element(self.PPT3DPath[Element]).Bounds.centre_x
                y = self.engine.find_element(self.PPT3DPath[Element]).Bounds.centre_y
                width = self.engine.find_element(self.PPT3DPath[Element]).Bounds.Width
                self.engine.click(x + width / 2 + z, y+o)
                time.sleep(sleeptime)
                break
            else:
                time.sleep(2)

    '''单元素---鼠标左键双击'''
    def DoubleClick(self, Element=None, sleeptime=0.05):
        for i in range(20):
            if self.engine.find_element(self.PPT3DPath[Element]):
                px = self.engine.find_element(self.PPT3DPath[Element]).Bounds.centre_x
                py = self.engine.find_element(self.PPT3DPath[Element]).Bounds.centre_y
                self.engine.click_double(px, py)
                break
            else:
                time.sleep(2)

    '''单元素---鼠标左键三击'''
    def ThreeClick(self, Element=None, sleeptime=0.05):
        for i in range(20):
            if self.engine.find_element(self.PPT3DPath[Element]):
                px = self.engine.find_element(self.PPT3DPath[Element]).Bounds.centre_x
                py = self.engine.find_element(self.PPT3DPath[Element]).Bounds.centre_y
                self.engine.click_three(px, py)
                break
            else:
                time.sleep(2)

    def isVisible(self, Element, WaitTime=10):
        """
        元素是否可见
        :param Element:
        :param WaitTime:
        :return:
        """
        i = 0
        while self.engine.find_element(self.PPT3DPath[Element]).Visible is not True and i < WaitTime:
            time.sleep(1)
            i = i + 1
        if self.engine.find_element(self.PPT3DPath[Element]).Visible:
            return True
        else:
            return False

    def isVisibleV(self, Element, WaitTime=20):
        """
        可变元素是否可见
        :param Element:
        :param WaitTime:
        :return:
        """

        i = 0
        while self.engine.find_element(Element) is None and i < WaitTime:
            i = i + 1
            time.sleep(1)
        if self.engine.find_element(Element) is None:
            return False
        else:
            while self.engine.find_element(Element).Visible is not True and i <WaitTime:
                time.sleep(1)
                i = i + 1
            if self.engine.find_element(Element).Visible:
                return True
            else:
                return False

    def isNotElementVisible(self, Element, ErrMsg, loadTime=300):
        """
        判断元素是否不可视化
        :param Element:
        :param ErrMsg:
        :return:
        """
        time.sleep(1)
        for i in range(loadTime):
            if self.engine.find_element(self.PPT3DPath[Element]):
                if self.engine.find_element(self.PPT3DPath[Element]).Visible == False:
                    return
                else:
                    pass
            else:
                time.sleep(1)
        if self.engine.find_element(self.PPT3DPath[Element]):
            if self.engine.find_element(self.PPT3DPath[Element]).Visible == False:
                return
            else:
                assert False, ErrMsg
        else:
            assert False, ErrMsg

    def isNotElementsVisible(self, Element=None, x=0, ErrMsg=None, sleeptime=1):
        """
        判断列表元素是否不可视化
        :return:
        """
        time.sleep(1)
        for i in range(10):
            if self.engine.find_elements_path(self.PPT3DPath[Element])[x]:
                if self.engine.find_elements_path(self.PPT3DPath[Element])[x].Visible == False:
                    return
                else:
                    pass
            else:
                time.sleep(sleeptime)
        if self.engine.find_elements_path(self.PPT3DPath[Element])[x]:
            if self.engine.find_elements_path(self.PPT3DPath[Element])[x].Visible == False:
                return
            else:
                assert False, ErrMsg
        else:
            assert False, ErrMsg

    def isElementVisible(self, Element, ErrMsg="该元素不可见", sleeptime=1):
        """
        判断元素是否可视化
        :return:
        """
        time.sleep(1)
        for i in range(10):
            if self.engine.find_element(self.PPT3DPath[Element]):
                if self.engine.find_element(self.PPT3DPath[Element]).Visible == True:
                    return
                else:
                    pass
            else:
                time.sleep(sleeptime)
        if self.engine.find_element(self.PPT3DPath[Element]):
            if self.engine.find_element(self.PPT3DPath[Element]).Visible == True:
                return
            else:
                assert False, ErrMsg
        else:
            assert False, ErrMsg

    def isElementsVisible(self, Element=None, x=0, ErrMsg=None, sleeptime=1):
        """
        判断列表元素是否可视化
        :return:
        """
        time.sleep(1)
        for i in range(10):
            if self.engine.find_elements_path(self.PPT3DPath[Element])[x]:
                # print "visible:", self.engine.find_elements_path(self.PPT3DPath[Element])[x].Visible
                if self.engine.find_elements_path(self.PPT3DPath[Element])[x].Visible == True:
                    return
                else:
                    pass
            else:
                time.sleep(sleeptime)
        if self.engine.find_elements_path(self.PPT3DPath[Element])[x]:
            # print "visible:", self.engine.find_elements_path(self.PPT3DPath[Element])[x].Visible
            if self.engine.find_elements_path(self.PPT3DPath[Element])[x].Visible == True:
                return
            else:
                assert False, ErrMsg
        else:
            assert False, ErrMsg

    def isElementPathExist(self, Element, ErrMsg=None, WaitTime=5, x=0):
        """
        判断列表元素是否存在
        :param Element:
        :param ErrMsg:
        :param WaitTime:
        :param x:
        :return:
        """
        i = 0
        while self.engine.find_elements_path(self.PPT3DPath[Element])[x] is None and i < WaitTime:
            i += 1
            time.sleep(1)
            #print "this is :", self.engine.find_element(self.PPT3DPath[Element])
        if self.engine.find_elements_path(self.PPT3DPath[Element])[x]:
            return
        else:
            assert False, ErrMsg

    def isNotElementExist(self, Element, ErrMsg, WaitTime=5):
        """
        判断元素是否不存在
        :param Element:
        :param ErrMsg:
        :param WaitTime:
        :return:
        """
        i = 0
        while self.engine.find_element(self.PPT3DPath[Element]) and i < WaitTime:
            i += 1
            time.sleep(1)
        if self.engine.find_element(self.PPT3DPath[Element]):
            assert False, ErrMsg
        else:
            return

    def isElementExist(self, Element, ErrMsg=None, WaitTime=5):
        """
        判断元素是否存在
        :param Element:
        :param ErrMsg:
        :param WaitTime:
        :return:
        """
        i = 0
        while self.engine.find_element(self.PPT3DPath[Element]) is None and i < WaitTime:
            i += 1
            time.sleep(1)
            #print "this is :",self.engine.find_element(self.PPT3DPath[Element])
        if self.engine.find_element(self.PPT3DPath[Element]):
            return
        else:
            assert False, ErrMsg

    def isNotElementExistPageID(self, Element, ErrMsg=None, WaitTime=5):
        """
        判断元素是否不存在（路径可变）
        :param Element:
        :param ErrMsg:
        :param WaitTime:
        :return:
        """
        i = 0
        while self.engine.find_element(Element) and i < WaitTime:
            i += 1
            time.sleep(1)
            # print "this is :", self.engine.find_element(Element)
        if self.engine.find_element(Element):
            assert False, ErrMsg
        else:
            return

    def isElementExistPageID(self, Element, ErrMsg=None, WaitTime=5):
        """
        判断元素是否存在（路径可变）
        :param Element:
        :param ErrMsg:
        :param WaitTime:
        :return:
        """
        i = 0
        while self.engine.find_element(Element) is None and i < WaitTime:
            i += 1
            time.sleep(1)
            # print "this is :", self.engine.find_element(Element)
        if self.engine.find_element(Element):
            return
        else:
            assert False, ErrMsg

    # 全词匹配
    def getWholeMatch(self, str, flags=0):
        xml = self.engine.dumpTree()
        for k in xml:
            txt = xml[k]
        # s = re.findall(r'Page=(\w+)*', txt)
        # s = re.fullmatch(str, txt)
        s = re.findall("(?:" + str + r")\Z", txt)
        return s[0]

    #
    def getPathValue(self, str):
        """
        获取所插入元素路径中的特定值
        :param str:
        :return:
        """
        xml = self.engine.dumpTree()
        for k in xml:
            txt = xml[k]
        # s = re.findall(r'%s(\w+)*'%str, txt)
        s = re.findall('%s(.+?)"' % str, txt)
        if s is None:
            s[0] = 0
        return s

    def getPageID(self):
        """
        获取PageID
        :return:
        """
        xml = self.engine.dumpTree()
        for k in xml:
            txt = xml[k]
        # s = re.findall(r'Page=(\w+)*', txt)
        s = re.findall(r'Page(\w+)*', txt)
        return s[0]

    def DateJuge(self, modifyTime, currentTime, ErrMsg):
        """
        判断文件修改日期是否为当前日期
        :param modifyTime:
        :param currentTime:
        :param ErrMsg:
        :return:
        """
        if int(currentTime) - int(modifyTime) < 20:
            return
        else:
            assert False, ErrMsg

    def fileExist(self, path, ErrMsg, WaitTime=60):
        """
        判断路径下是否存在文件
        :param path:
        :param ErrMsg:
        :param WaitTime:
        :return:
        """
        i = 0
        while os.path.exists(path) is False and i < WaitTime:
            i += 1
            time.sleep(0.1)
        if os.path.exists(path):
            pass
        else:
            assert False, ErrMsg

    def CopyFileTo(self, file_path, target_path, ErrMsg):
        """
        复制文件到指定目录
        :param file_path:
        :param target_path:
        :param ErrMsg:
        :return:
        """
        if os.path.exists(file_path):
            shutil.copyfile(file_path, target_path)
        else:
            assert False, ErrMsg

    def deleteFile(self, path):
        """
        删除指定文件
        :param path:
        :return:
        """
        if os.path.exists(path):
            os.remove(path)

    def deleteDir(self, dir="C:\\Users\\Administrator\\AppData\\Roaming\\3DPPT\\ResourcesCenter20"):
        '''
        @Description:   删除文件
        @param:     path
        @return:    None
        '''
        if os.path.exists(dir):
            print 1
            shutil.rmtree(dir)

    '''解析渲染表格'''
    def create(self):
        self.xlsW = XlsxWriter()

    def xls_getOldXls(self, name):
        self.create()
        self.xlsW.getOldData(name)

    def xls_write(self, *args):
        self.xlsW.write_line(*args)

    def xls_close(self, name):
        self.xlsW.close(name)

