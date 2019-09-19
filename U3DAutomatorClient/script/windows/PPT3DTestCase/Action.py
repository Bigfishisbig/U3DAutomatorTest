# coding=utf-8
"""
Action
作者: qa-wang
版本: 3DPPT Final.2017.1225.1314
创建日期：2017.12.27
修改日期：2017.12.27
"""

from __future__ import division
from script.windows.Operation import *
from script.windows.PPT3DSetting.SourcePath import SourcePath
import time, sys, os
import win32con, win32api
from win32api import GetSystemMetrics
from script.windows.SystemDialog import *
from jpype import *
from main.utils.profile import set_tag, end_tag
from main.utils.PCUI import UI
#from main.utils.pc_mouseandkey import mouse_absolute
# from pymouse import PyMouse

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化为指定的编码格式

startTime = 0
endTime = 0
class Action(Operation, SystemDiaglog, UI):
    # 3DPPT初始页面还原
    """黑夜给了你黑色的眼睛，你却用它来寻找光明。\nabcdefghijklmnopqrstuvwxyz.\n123456789。"""


    global screen_x, screen_y  # 显示器分辨率
    screen_x = GetSystemMetrics(0)
    screen_y = GetSystemMetrics(1)
    # print "分辨率为：", screen_x, "*", screen_y
    global x_compare, y_compare
    x_compare = screen_x / 1440
    y_compare = screen_y / 900

    jvmPath = SourcePath.File_Jvm_18
    if isJVMStarted():
        print "JVM is already started"
        pass
    else:
        print "Start java JVM"
        startJVM(jvmPath, '-ea', "-Djava.class.path=%s" % (SourcePath.File_Jar_sikuli), "-Xms1g", "-Xmx1g")

        # app = JClass('org.sikuli.script.App')
        Screen = JClass('org.sikuli.script.Screen')
        Location = JClass('org.sikuli.script.Location')
        Pattern = JClass('org.sikuli.script.Pattern')
        global screen
        screen = Screen()
        location = Location(0, 0)
        pattern = Pattern()

    pageNotFind = -999

    def Init3DPPT(self):
        # self.sikuli_Init()
        # self.s_witForImg(SourcePath.File_Img_FullScreen, 60, "60秒内启动3DPPT失败")

        i = 0
        while self.s_isExists(SourcePath.File_Img_FullScreen, 0, 0.1, accurate=0.6, isDel=True) == False and i < 10:
            # print self.s_isExists(imgPath)
            if self.s_isExists(SourcePath.File_Img_FullScreen2, 0, 0.1, accurate=0.6, isDel=True):
                break
            i += 1
            time.sleep(1)
        print "------------60s结束------------"
        # if self.s_isExists(SourcePath.File_Img_FullScreen, 0, 0.1, accurate=0.6) == False:
        #     pass
        # else:
        #     pass

        if self.isVisible("BtnMaxmize") == False:
            pass
        else:
            self.OneClick("BtnMaxmize")
        # time.sleep(120)

        # self.Move_Pos("MaxSizeBtn")
        # if self.engine.find_element(self.PPT3DPath["MaxSizeTip"]).Txt == "最大化":
        #     # self.DoubleClick_Pos("MinimizeBtn", -60, 0)
        #     self.OneClick("MaxSizeBtn")
        # else:
        #     pass
        # time.sleep(2)
        # if self.engine.find_element("BtnBottomClose"):  # 关闭文件备份恢复
        #     self.OneClick("BtnBottomClose")
        #

        # time.sleep(5)

    # 打开指定目录的3DPPT文件
    def Open3DPPTFile(self, file_path):
        self.OneClick('BtnOpenFile')
        # time.sleep(2)
        self.inputDlgClick("#32770", u"选择文件", [("ComboBoxEx32", 0), ("ComboBox", 0), ("Edit", 0)], file_path,
                           "Button")  # 输入路径点击打开
        # time.sleep(3)

    # 另存到3DPPT文件
    def SaveAs3DPPTFile(self, save_path):
        # self.OneClick("BtnSave")
        self.OneClick("BtnSaveMenu")
        self.OneClick("BtnSaveAs")
        # time.sleep(1)
        self.inputDlgClick("#32770", u"保存文件",
                           [("DUIViewWndClassName", 0), ("DirectUIHWND", 0), ("FloatNotifySink", 0), ("ComboBox", 0),
                            ("Edit", 0)], save_path, "Button")  # 输入路径点击保存
        # time.sleep(1)
        # self.overrideFile(True)

    # 保存文件操作
    def SavePPTFile(self, save_path):
        self.OneClick('BtnSave')
        time.sleep(1)
        self.inputDlgClick("#32770", u"保存",
                           [("DUIViewWndClassName", 0), ("DirectUIHWND", 0), ("FloatNotifySink", 0), ("ComboBox", 0),
                            ("Edit", 0)], save_path, "Button")  # 输入路径点击保存
        time.sleep(1)
        self.overrideFile(True)

    # 判断新增幻灯片次数且是否一次一页
    def NewPage(self, Number, ElementBtn, ErrMsg):  # 页数，按钮，元素，错误提示
        num1 = self.ElementNum("PageNum")
        for i in range(Number - 1):
            self.OneClick(ElementBtn)
            time.sleep(3)
            num2 = self.ElementNum("PageNum")
            if num1 + i + 1 == num2:
                pass
            else:
                assert False, ErrMsg

    # 多次点击
    def TimesClick(self, Element_list=[], intervalTime=1):
        for Element in Element_list:
            self.OneClick(Element)
            time.sleep(intervalTime)

    # 打开指定目录的文件
    def OpenFile(self, path):
        time.sleep(1)
        self.inputDlgClick("#32770", u"选择文件", [("ComboBoxEx32", 0), ("ComboBox", 0), ("Edit", 0)], path,
                           "Button")  # 输入路径点击打开

    # 打开指定目录的图片
    def OpenImage(self, image_path):
        # self.TimesClick(["ImageBtn", "Image"])
        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertImage")
        # self.OneClick("BtnInsertImageBar")
        # self.OneClick("BtnInsertImageListImage")  # 新版
        time.sleep(1)
        # print "输入文件路径"
        self.inputDlgClick("#32770", u"选择文件", [("ComboBoxEx32", 0), ("ComboBox", 0), ("Edit", 0)], image_path,
                           "Button")  # 输入路径点击打开
        time.sleep(1)
        # self.OneClick("BtnImageBack")

    # 打开指定目录的图片
    def OpenImagePanorama(self, image_path):
        # self.TimesClick(["ImageBtn", "Image"])
        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertImageBar")
        self.OneClick("BtnInsertPanoram")  # 新版
        time.sleep(1)
        self.inputDlgClick("#32770", u"选择文件", [("ComboBoxEx32", 0), ("ComboBox", 0), ("Edit", 0)], image_path,
                           "Button")  # 输入路径点击打开
        time.sleep(1)
        # self.OneClick("BtnImageBack")

    # 打开指定目录的图片墙
    def OpenImageWall(self, image_path):
        # self.TimesClick(["ImageBtn", "ImageWall"])
        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertImageBar")
        self.OneClick("BtnInsertImageListImageWall")
        self.OneClick("BtnImageWallConfirm")
        time.sleep(1)
        self.inputDlgClick("#32770", u"选择文件", [("ComboBoxEx32", 0), ("ComboBox", 0), ("Edit", 0)], image_path,
                           "Button")  # 输入路径点击打开
        time.sleep(1)
        # self.OneClick("BtnImageWallBack")

    # 打开指定目录的视频
    def OpenVideo(self, video_path):
        # self.OneClick("VideoBtn")
        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertVideo")
        time.sleep(1)
        self.inputDlgClick("#32770", u"选择文件", [("ComboBoxEx32", 0), ("ComboBox", 0), ("Edit", 0)], video_path,
                           "Button")  # 输入路径点击打开
        time.sleep(1)
        # self.OneClick("BtnVideoBack")

    # 打开指定目录的音频
    def OpenAudio(self, audio_path):
        # self.OneClick("AudioBtn")
        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertAudio")
        time.sleep(1)
        self.inputDlgClick("#32770", u"选择文件", [("ComboBoxEx32", 0), ("ComboBox", 0), ("Edit", 0)], audio_path,
                           "Button")  # 输入路径点击打开
        time.sleep(1)
        # self.OneClick("BtnAudioBack")

    # 打开指定目录的3D模型
    def Open3DModel(self, module_path):
        # self.OneClick("AudioBtn")
        self.OneClick("BtnInsert")
        self.OneClick("BtnInsert3DModel")
        time.sleep(1)
        self.inputDlgClick("#32770", u"选择文件", [("ComboBoxEx32", 0), ("ComboBox", 0), ("Edit", 0)], module_path,
                           "Button")  # 输入路径点击打开
        time.sleep(1)
        # self.OneClick("BtnAudioBack")

    # 插入图表
    def InsertChart(self, Toggle):
        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertChart")
        self.OneClick(Toggle)
        self.ListClick("BtnChart", 1)
        # self.OneClick("InsertChart")

    # 插入形状
    def InsertShape(self, Shape):
        # self.OneClick("ShapeBtn")
        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertShape")
        self.OneClick(Shape)
        time.sleep(1)
        # self.Click_XY(dx=0, dy=-200)
        self.Click_XY(dx=0, dy=0)

        # self.OneClickL("Canvas/DlgMenuBar(Clone)001/Menubar/PanelOperate/PanelInsertOperate/BtnShape(Clone)/dis_Img")
        # self.OneClick(Shape)
        # self.engine.swipe_press(start_x=600*x_compare, start_y=350*y_compare, end_x=840*x_compare, end_y=550*y_compare, steps=1, duration=1)

    def InsertWholeCourseware(self):
        """
        插入整个课件
        :return:
        """
        self.OneClick("ToggleCourse")
        self.ListClick("ItemCourse", -1)  # 选择课件选项
        self.OneClick("AllResource")
        self.OneClick("InsertWholeResource")

    def InsertOneCourseware(self):
        """
        插入课件单页
        :return:
        """
        self.OneClick("ToggleCourse")
        self.ListClick("ItemCourse", -1)
        self.OneClick("AllResource")
        self.OneClick("CoursePageShow")
        self.ListClick("InsertOneCourse", 0)

    def Insert3DResource(self):
        """
        插入3D资源
        :return:
        """
        self.OneClick("Toggle3DResource")
        self.OneClick("AllResource")
        self.ListClick("InsertWholeResource", 0)

    def InsertCefWordCard(self):
        """
        插入生字卡
        :return:
        """
        self.OneClick("ToggleSubjectTool")
        self.OneClick("CefWordShow")
        self.ListClick("BtnInsertCefWord", 0)

    def InsertMedia(self):
        """
        插入多媒体
        :return:
        """
        self.OneClick("ToggleMedia")
        self.ListClick("ItemCourse", 0)
        self.OneClick("AllResource")
        self.OneClick("InsertAudioResource")

    def InsertExercise(self):
        """
        插入习题
        :return:
        """
        self.OneClick("ToggleExercise")
        self.s_clickImg(SourcePath.File_Insert_Exercise, 10, "插入习题失败")

    def InsertInteractExercise(self):
        """
        插入趣味习题
        :return:
        """
        self.OneClick("ToggleInteractExercise")

    def InsertCustomTable(self):
        """
        插入传统表格
        :return:
        """
        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertTable")
        self.OneClick("BtnTableCustom")
        self.OneClick("SureInsertTable")

    def IsInsertPageID(self, key, ErrMsg="插入失败"):
        """
        判断控件的插入
        :return:
        """
        PageID = self.getPathValue("Page")[0]  # 获取可变路径
        itemTextID = self.getPathValue(key)
        path = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page" + PageID + "/" + key + "/" + key + itemTextID[1]
        self.isElementExistPageID(path, "插入元素失败")
        # if len(itemTextID) != 2:
        #     assert False, ErrMsg
        # else:
        #     return path
        return path

    def URPageID(self, key, ErrMsg="撤销还原失败"):
        """
        判断无法定位的控件的撤销还原
        :return:
        """
        time.sleep(5)
        path = self.IsInsertPageID(key)
        # path = self.getElementPath(key)
        # self.isElementExistPageID(path, "插入失败", 10)
        num1 = len(self.getPathValue(key))
        # num1 = len(itemTextID)
        self.OneClick("BtnStart")
        self.OneClick("BtnRevert")
        self.isNotElementExistPageID(path, "撤销失败", 10)
        self.OneClick("BtnStart")
        self.OneClick("BtnRecover")
        time.sleep(5)
        num2 = len(self.getPathValue(key))
        # self.isElementExistPageID(path, "还原3D模型失败")
        if num2 == num1:
            pass
        else:
            assert False, "还原失败"
        self.OneClick("BtnStart")
        # self.OneClick("BtnRevert")

    # 复制黏贴(不可变路径)
    def CopyPaste(self, key, Element_path, ErrMsg, num=1):  # num为插入一个元素所产生key个数
        """
        useless
        :param key:
        :param Element_path:
        :param ErrMsg:
        :param num:
        :return:
        """
        strNum = self.getPathValue(key)
        # print "strNum:", len(strNum)
        self.Click(Element_path)  # 选中控件
        # self.TimesClick(["CopyBtn", "PasteBtn"], 2) # 停顿2s

        self.OneClickRight(Element_path)
        self.isElementExist("BtnStageRight", "右键失效")  # 右键是否成功
        self.ListClick("BtnStageRightCopy")  # 复制
        self.OneClickRight(Element_path)
        self.ListClick("BtnStageRightPaste")  # 粘贴

        new_num = len(self.getPathValue(key))
        # print "len:", new_num
        if new_num - num == len(strNum):
            return
        else:
            assert False, ErrMsg

    # 拖动列表元素位移
    def Swipe2(self, ElementOne=None, One=0, ElementTwo=None, Two=0, x2=0, y2=0, x1=0, y1=0,
               sleeptime=0.5):
        x3 = 0
        y3 = 0
        temp_x = 0
        temp_y = 0
        Element1 = self.engine.find_elements_path(self.PPT3DPath[ElementOne])[One]
        x = Element1.Bounds.centre_x
        y = Element1.Bounds.centre_y
        if ElementTwo is not None:
            Element2 = self.engine.find_elements_path(self.PPT3DPath[ElementTwo])[Two]
            x3 = Element2.Bounds.centre_x
            y3 = Element2.Bounds.centre_y
            temp_x = x3 - x
            temp_y = y3 - y
        win32api.SetCursorPos((int(x + x1), int(y + y1)))  # 鼠标移动到
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 左键按下
        time.sleep(1)
        screen.mouseMove(int(x2 + temp_x), int(y2 + temp_y))
        time.sleep(1)
        # self.engine.move_pos2(Element1.Bounds.centre_x + x1, Element1.Bounds.centre_y + y1, Element2.Bounds.centre_x + x2, Element2.Bounds.centre_y + y2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # 左键放开

    # 拖动元素位移
    def Swipe3(self, ElementOne=None, x2=0, y2=0, x1=0, y1=0, ElementType="0"):
        """
        根据元素位置拖动元素位移
        :return:
        """
        if ElementType == "var":
            Element1 = self.engine.find_element(ElementOne)
        else:
            Element1 = self.engine.find_element(self.PPT3DPath[ElementOne])
        x = Element1.Bounds.centre_x
        y = Element1.Bounds.centre_y
        win32api.SetCursorPos((int(x + x1), int(y + y1)))  # 鼠标移动到
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 左键按下
        time.sleep(1)
        screen.mouseMove(int(x2), int(y2))
        time.sleep(1)
        # self.engine.move_pos2(Element1.Bounds.centre_x + x1, Element1.Bounds.centre_y + y1, Element2.Bounds.centre_x + x2, Element2.Bounds.centre_y + y2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # 左键放开

    # 实现文本类超链接
    def Hyperlink(self, disk):
        # 选中元素之后
        # win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        # win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
        self.Right()
        self.isElementExist("BtnStageRight", "右键失效")  # 右键是否成功
        time.sleep(1)
        self.ListClick("BtnStageRightHyperLink")  # 超链接
        self.OneClick("BtnOpenDisk")
        time.sleep(1)
        if disk == 0:
            self.ListClick("BtnDisk", 2)
        elif disk == 2:
            self.ListClick("BtnDisk", 0)
        else:
            self.ListClick("BtnDisk", 1)
        time.sleep(1)
        self.OneClick("BtnLinkSubmit")
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    # 实现幻灯片超链接
    def HyperlinkPage(self, locate, Msg=None):
        # 选中元素之后
        time.sleep(1)
        if locate == 2:  # 形状的超链接
            self.ClickRight_XY(dx=30, dy=30)
            self.isElementExist("BtnStageRight", "右键失效")  # 右键是否成功
            self.ListClick("BtnStageRightHyperLink")  # 超链接
            self.OneClick("BtnPPTToggle")
            self.OneClickL("TglPreviousPPT")
            self.OneClick("ScreenShowTextBtn")
            time.sleep(1)
            self.OneClick("TipInputField")
            time.sleep(1)
            self.InputStr(Msg)
            self.OneClick("BtnTipSubmit")
            self.OneClick("BtnLinkSubmit")
        else:
            self.ListClick("TextLocation", 0)
            time.sleep(1)
            self.ListClick("PageLocation", locate)
            time.sleep(1)
            self.OneClick("LinkSubmit")

        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        global msg
        msg = Msg

    # 编辑状态时判断文本类超链接
    def isHyperlinkEditing(self, Element_path, disk, ErrMsg):  # disk:超链接位置
        win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
        if disk == 0:
            self.OneClickL(Element_path, 5, 0)  # 选中控件
        else:
            self.OneClickL(Element_path, -2, 0)  # 选中控件
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(1)
        self.isDisk(disk, ErrMsg)

    # 判断放映状态时
    def isHyperlinkPlaying(self, Element_path=None, disk=0, ErrMsg=None, page_path_true=None):

        if Element_path == None:
            pass
        else:
            self.OneClickL(Element_path, 20, 0)
        # self.OneClick("BtnPlayCurrent")
        self.OneClick("BtnPlaying")
        time.sleep(2)
        self.OneClick("BtnNextPage")
        time.sleep(5)
        # self.Click_XY(dx=300)
        if disk == 0:
            self.OneClickL(Element_path, 5, 0)  # 选中控件
        elif disk == 1 or disk == 2:
            self.OneClickL(Element_path, -2, 0)  # 选中控件
        elif disk == 5:
            if msg != None:  # 含提示信息则为形状超链接
                self.engine.move_pos(screen_x / 2, screen_y / 2)  # 全屏放映时鼠标悬停超链接
                time.sleep(1)
                for i in range(20):
                    if self.engine.find_element(self.PPT3DPath["Tip"]):
                        self.WaitForElementText("Tip", msg, 5, "提示信息失败")
                    else:
                        time.sleep(1)
                if self.engine.find_element(self.PPT3DPath["Tip"]):
                    self.WaitForElementText("Tip", msg, 5, "提示信息失败")
                else:
                    time.sleep(1)
            time.sleep(5)
            self.engine.click(screen_x / 2, screen_y / 2)  # 全屏放映时点击超链接
            time.sleep(5)
        elif disk == 4:
            self.engine.click(screen_x / 2, screen_y / 2)  # 全屏放映时点击超链接
            time.sleep(3)

        if disk == 5 or disk == 4:  # 幻灯片"1 <color=#a0a0a0>/3</color>"
            self.WaitForElementText("PlayingPage", "1 <color=#a0a0a0>/2</color>", 10, "超链接上一页失败")
            self.OneClick("BtnNextPage")
            self.WaitForElementText("PlayingPage", "2 <color=#a0a0a0>/2</color>", 10, "超链接上一页失败")
            # self.s_witForImg(SourcePath.File_Img_FullScreen, 10, "超链接上一页失败")
            # self.s_waitForImgVanish(SourcePath.File_Img_FullScreen, 10, "超链接上一页失败")
        else:
            self.isDisk(disk, ErrMsg)

    # 是否打开硬盘
    def isDisk(self, disk, ErrMsg):
        Mhandle = win32gui.FindWindow("CabinetWClass", None)
        buffer = ''
        if Mhandle > 0:
            toolbar_handle = self.find_subHandle(Mhandle,
                                                 [("WorkerW", 0), ("ReBarWindow32", 0), ("Address Band Root", 0),
                                                  ("msctls_progress32", 0), ("Breadcrumb Parent", 0),
                                                  ("ToolbarWindow32", 0)])  # 获取Mhandle下ToolbarWindow32的句柄
            # print "toolbar_handle:",toolbar_handle
            length = win32api.SendMessage(toolbar_handle, win32con.WM_GETTEXTLENGTH) + 1  # 获取控件文本长度
            buffer = '0' * length
            win32gui.SendMessage(toolbar_handle, win32con.WM_GETTEXT, length, buffer)  # 读取文本
            time.sleep(5)
            win32gui.SendMessage(Mhandle, win32con.WM_CLOSE)

        if disk == 0:
            addr = "C:\\"
        elif disk == 1:
            addr = "D:\\"
        else:
            addr = "E:\\"
        # print "buffer:", (buffer and addr)
        if (buffer and addr) == addr:
            return
        else:
            assert False, ErrMsg

    # 实现网页超链接
    def HyperlinkWeb(self, url):
        # 选中元素之后
        self.ClickRight_XY(dx=30, dy=30)
        self.isElementExist("BtnStageRight", "右键失效")  # 右键是否成功
        self.ListClick("BtnStageRightHyperLink")  # 超链接
        self.OneClick("WebPathInputField")
        self.InputStr(url)
        self.OneClick("BtnLinkSubmit")
        self.Click_XY(dx=300)
        # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    # 实现网页超链接判断
    def isHyperlinkWeb(self, url_web):
        # 编辑状态时是否显示tip
        self.engine.move_pos(screen_x / 2, screen_y / 2)
        time.sleep(2)
        self.WaitForElementText("Tip", "http://www.baidu.com\n按住Crtl并单击可访问链接", 10, "提示信息失败")
        self.Click_XY(dx=300)  # 点击空白处
        win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
        self.Click_XY()  # 选中控件
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(3)
        process_name = self.getProcess_name()
        self.isProcessExist(process_name, "编辑状态网址未打开")
        time.sleep(1)
        os.system("taskkill /F /IM %s" % process_name)
        time.sleep(2)

        self.OneClick("BtnPlaying")
        time.sleep(1)
        # 放映状态时
        # self.Click_XY(dx=300)  # 点击空白处
        self.engine.move_pos(screen_x / 2, screen_y / 2)
        self.isElementExist("Tip", "提示信息不存在")
        self.WaitForElementText("Tip", url_web, 2, "提示信息失败")
        self.engine.click(screen_x / 2, screen_y / 2)
        time.sleep(3)
        self.isProcessExist(process_name, "放映状态网址未打开")
        time.sleep(1)
        os.system("taskkill /F /IM %s" % process_name)

    # 检查更新关闭窗口
    def checkUpdate(self):
        self.engine.click(screen_x / 2, screen_y / 3 * 2)

    # 选中文本框
    def getText(self, x=20, y=20):
        PageID = self.getPathValue("Page")  # 获取可变路径
        itemTextID = self.getPathValue("ItemText")
        Xpath = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page" + PageID[0] + "/ItemText/ItemText" + itemTextID[
            1] + "/TextRoot/CharRoot/Text 1"
        return self.OneClickL(Xpath, x, y)
        # return Xpath

    # 选中文本框，返回文本框文字路径
    def getText2(self):
        PageID = self.getPathValue("Page")  # 获取可变路径
        itemTextID = self.getPathValue("ItemText")
        Xpath = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page" + PageID[0] + "/ItemText/ItemText" + itemTextID[
            1] + "/TextRoot/CharRoot/Text 1"
        return Xpath
        # return Xpath

    # 在文本框内输入一段文字
    def InputPara(self):
        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertTextBar")
        self.OneClick("BtnInsertTextX")
        # time.sleep(1)
        # self.engine.swipe_press(start_x=500, start_y=330, end_x=650, end_y=430, steps=1, duration=1)
        self.Click_XY(screen_x / 2, screen_y / 2)
        time.sleep(1)

    # 打开段落设置
    def OpenParaSetting(self):
        self.InputPara()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。\nabcdefghijklmnopqrstuvwxyz.\n123456789。")
        # time.sleep(1)
        self.getText()
        self.OneClick("BtnRowSpacing")
        self.ListClick("BtnSpace")  #

    # 打开段落设置
    def OpenParaSetting2(self):
        self.InputPara()
        self.InputStr(u"黑夜给了你黑色的眼睛，你却用它来寻找光明。\nabcdefghijklmnopqrstuvwxyz.\n123456789。")
        time.sleep(1)
        self.OneClick("BtnRowSpacing")
        self.ListClick("BtnSpace")  #

    # 设置性能数据标记
    def SetTag(self, tag, timestamp=""):
        set_tag(tag, timestamp)

    # 取消性能数据标记
    def EndTag(self, tag="", timestamp=""):

        end_tag(timestamp, tag)
        # time.sleep(1)

    # cmd中文乱码解决
    def Ucode(self, x):
        if sys.version_info.major == 2:
            # return x.decode('utf-8').encode("gbk") if type(x) is str else x
            return x.decode('utf-8') if type(x) is str else x
        elif sys.version_info.major == 3:
            return x

    # 指定时间内是否出现图片
    def s_witForImg(self, imgPath, WaitTime, ErrMsg, imgPath2=None, accurate=0.5):
        """
        :rtype: object
        """
        i = 0
        while self.s_isExists(imgPath, 0, 0.1, accurate, True) == False and i < WaitTime:
            # if self.s_isExists(imgPath2, 0, 0.1, accurate) == True:
            #     return
            # print self.s_isExists(imgPath)
            i += 1
            time.sleep(1)
        # print "------------60s结束------------"
        if self.s_isExists(imgPath, 0, 0.1, accurate) == False:
            assert False, ErrMsg
        else:
            return

    # 指定时间内图片是否消失
    def s_waitForImgVanish(self, imgPath, WaitTime=5, ErrMsg="图片未消失", accurate=0.6):
        # if screen.waitVanish(imgPath, WaitTime) == "false":
        #     assert False, "ErrMsg"
        # else:
        #     return
        result = self.imgPair(imgPath, screen_x, screen_y, accurate)
        if result[0] == True:
            assert False, ErrMsg
        else:
            pass

    # 是否存在
    def s_isExists(self, target, timeout=2.0, similar=0.8, accurate=0.5, isDel=False):
        # global screen
        try:
            # print "识别结果：", screen.exists(target).isValid()
            # if screen.exists(target).isValid() is True:
            #     return True
            # else:
            #     return False
            # print "分辨率为：", screen_x, screen_y
            result = self.imgPair(target, screen_x, screen_y, accurate, isDel)
            return result[0]  # 匹配结果TRUE/FALSE

        except Exception, e:
            print str(e)
            return False

    # def s_isExists_2(self, target, timeout=2.0, similar=0.8):
    #     try:
    #         screen.exists(self.pattern(target).similar(float(similar)).targetOffset(100, 0), timeout).toString()
    #         return "true"
    #     except Exception:
    #         return "false"

    # 单击目标图片(精确度及相对位置)
    def s_clickImg(self, imgPath, WaitTime, ErrMsg, similar=0.8, dx=0, dy=0, accurate=0.5):
        i = 0
        while self.s_isExists(imgPath, accurate=accurate) == False and i < WaitTime:
            i += 1
            time.sleep(1)
        if self.s_isExists(imgPath, accurate=accurate) == False:
            assert False, ErrMsg
        else:
            # if self.s_click(imgPath, similar, dx, dy) == self.pageNotFind:
            #     assert False, ErrMsg
            # else:
            #     pass
            match, x, y = self.imgPair(imgPath, screen_x, screen_y, accurate)
            print match, x, y
            if match:
                # self.engine.click(x + dx, y + dy)
                self.mouse_click(x + dx, y + dy)

    # 右击目标图片(精确度及相对位置)
    def s_rightclickImg(self, imgPath, WaitTime, ErrMsg, similar=0.8, dx=0, dy=0, accurate=0.5):
        i = 0
        while self.s_isExists(imgPath, accurate=accurate) == False and i < WaitTime:
            i += 1
            time.sleep(1)
        if self.s_isExists(imgPath, accurate=accurate) == False:
            assert False, ErrMsg
        else:
            # if self.s_click(imgPath, similar, dx, dy) == self.pageNotFind:
            #     assert False, ErrMsg
            # else:
            #     pass
            match, x, y = self.imgPair(imgPath, screen_x, screen_y, accurate)
            if match:
                # self.engine.click_right(x + dx, y + dy)
                self.mouse_click_right(x + dx, y + dy)

    # 双击目标图片
    def s_doubleClickImg(self, imgPath, WaitTime, ErrMsg, dx=0, dy=0, accurate=0.6):
        i = 0
        while self.s_isExists(imgPath, accurate=accurate) == False and i < WaitTime:
            i += 1
            time.sleep(1)
        if self.s_isExists(imgPath, accurate=accurate) == True:
            match, x, y = self.imgPair(imgPath, screen_x, screen_y, accurate)
            if match:
                self.mouse_dclick(x + dx, y + dy)
        else:
            # self.getScreenShot(SourcePath.File_ScreenShoot_Path, self.timeImageName())
            assert False, ErrMsg

    # 拖动图片
    # def Move_Img(self, arg0, arg1):
    #     tmp = screen.dragDrop(arg0, arg1)
    #     if tmp == -999:
    #         # self.getScreenShot(SourcePath.File_ScreenShoot_Path, self.timeImageName())
    #         assert False, "拖动失败"
    #     else:
    #         return

    # 关闭虚拟机
    def closeJVM(self):
        shutdownJVM(self)



    # 点击
    # def s_click(self, target, similar=0.8, dx=0, dy=0):
    #     try:
    #         screen.click(target)
    #         return time.time()
    #
    #     except Exception:
    #         return self.pageNotFind

    # 双击
    # def s_doubleclick(self, target, similar=0.8, dx=0, dy=0):
    #     try:
    #         screen.doubleClick(target)
    #         return time.time()
    #     except Exception:
    #         return self.pageNotFind

    # 点击坐标点
    # def s_clickLocation(self, x, y):
    #     try:
    #         self.location.setLocation(x, y)
    #         self.location.click()
    #         return time.time()
    #     except:
    #         return self.pageNotFind

    # 插入图片、图片墙、视频撤销还原
    def RevertAndRecover(self, path, key):
        # self.OneClick("BtnImageBack")
        # self.s_witForImg(path, 10, "10s内未插入")
        fileroot = self.getPathValue("File")  # 获取可变路径
        PageID = self.getPathValue("Page")  # 获取可变路径
        itemTextID = self.getPathValue(key)
        Xpath = "3DP Root/File" + fileroot[0] + "/3DP Root/Page" + PageID[0] + "/"+key+"/"+key+itemTextID[1]
        self.isElementExistPageID(Xpath, "插入元素失败", 10)

        self.OneClick("BtnStart")
        self.OneClick("BtnRevert")
        # self.s_witForImg(SourcePath.File_Img_FullScreen, 10, "撤销失败")
        self.s_waitForImgVanish(path, 5, "撤销失败")
        self.OneClick("BtnStart")
        self.OneClick("BtnRecover")
        # self.s_witForImg(path, 10, "还原失败")
        Xpath = self.getElementPath(key)
        self.isElementExistPageID(Xpath, "还原元素失败", 10)

    #
    def RevertAndRecover2(self, key):
        # self.OneClick("BtnImageBack")
        time.sleep(2)
        element = self.IsInsertPageID(key)
        # element = self.getElementPath(key)
        # self.isElementExistPageID(element, "插入元素失败")
        num1 = len(self.getPathValue(key))
        self.OneClick("BtnStart")
        self.OneClick("BtnRevert")
        time.sleep(1)
        self.isNotElementExistPageID(element, "撤销元素失败")
        self.OneClick("BtnStart")
        self.OneClick("BtnRecover")
        # time.sleep(1)
        # element = self.getElementPath(key)
        time.sleep(2)
        num2 = len(self.getPathValue(key))
        if num2 == num1:
            pass
        else:
            assert False, "还原元素失败"
        # self.isElementExistPageID(element, "还原元素失败")
        self.OneClick("BtnStart")
        # self.OneClick("BtnRevert")

    # 获取不同元素路径
    def getElementPath(self, key):
        time.sleep(1)
        PageID = self.getPathValue("Page")[0]  # 获取可变路径
        itemTextID = self.getPathValue(key)[1]
        element = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page" + PageID + "/" + key + "/" + key + itemTextID
        return element

    def Move_XY(self, x=0, y=0):
        """
        移动到坐标点
        :return:
        """
        time.sleep(1)
        if x == 0 and y == 0:
            x = screen_x
            y = screen_y
        self.engine.move_pos(x, y)
        time.sleep(1)

    def Click_XY(self, x=0, y=0, dx=0, dy=0):  # 点击屏幕中心
        """
        点击坐标点
        :return:
        """
        time.sleep(1)
        if x == 0 and y == 0:
            x = screen_x / 2
            y = screen_y / 2
        self.engine.click(x + dx, y + dy)
        time.sleep(1)

    def ClickRight_XY(self, x=0, y=0, dx=0, dy=0):
        """
        右键点击坐标点
        :return:
        """
        time.sleep(1)
        if x == 0 and y == 0:
            x = screen_x / 2
            y = screen_y / 2
        self.engine.click_right(x + dx, y + dy)
        time.sleep(1)

    def AudioR(self, Title):
        time.sleep(1)
        # self(SourcePath.File_Insert_AUDIO, 5, "点击失败")
        self.Move_XY(screen_x / 2, screen_y / 2)

        time.sleep(1)
        # self.isElementExist("AudioTitle", "插入失败")
        self.WaitForElementText("AudioTitle", Title, 5, "插入失败")
        self.OneClick("BtnStart")
        self.OneClick("BtnRevert")
        # self.OneClick("BtnRevert")
        time.sleep(3)
        self.isNotElementExist("AudioTitle", "撤销失败")
        self.OneClick("BtnStart")
        self.OneClick("BtnRecover")
        time.sleep(1)
        # print self.s_clickImg(SourcePath.File_Insert_AUDIO, 5, "点击失败")
        self.isElementExist("AudioTitle", "还原失败")
        self.OneClick("BtnStart")
        # self.OneClick("BtnRevert")

    # 图表
    def getChart(self, chart_name="Histogram"):
        path = ""
        PageID = ""
        itemTextID = ""
        try:
            PageID = self.getPathValue("Page")  # 获取可变路径
            itemTextID = self.getPathValue("ItemChart")
            path = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page" + PageID[0] + "/ItemChart/ItemChart" + itemTextID[
                1] + "/" + chart_name + "/Title/3DText/TextRoot/CharRoot/Text 1"
        except:
            pass
        # return self.OneClickL(Xpath, 20, 0)
        return path

    def getChart2(self, chart_name="Histogram"):
        path = ""
        PageID = ""
        itemTextID = ""
        try:
            PageID = self.getPathValue("Page")  # 获取可变路径
            itemTextID = self.getPathValue("ItemChart")
            path = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page" + PageID[0] + "/Chart/"+ chart_name + "/Title/3DText/TextRoot/CharRoot/Text 1"
        except:
            pass
        # return self.OneClickL(Xpath, 20, 0)
        return path

    def getChartPreview(self, chart_name="Histogram"):
        path = ""
        PageID = ""
        itemTextID = ""
        try:
            PageID = self.getPathValue("Page")  # 获取可变路径
            itemTextID = self.getPathValue("ItemChart")
            path = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page" + PageID[0] + "/Chart/" + chart_name + "/Title/3DText/TextRoot/CharRoot/Text 1"
        except:
            pass
        # return self.OneClickL(Xpath, 20, 0)
        return path

    def getTable(self):
        """
        选中表格
        :return:
        """
        path = ""
        try:
            PageID = self.getPathValue("Page")  # 获取可变路径
            itemTextID = self.getPathValue("ItemChart")
            path = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page" + PageID[0] + "/ItemFormComp/ItemFormComp" + itemTextID[
                1] + "/Table(Clone)/ItemGrid/FormItemPrefab(Clone)/ItemGrid/TabeleCell/3DText"

        except:
            pass
        # return self.OneClickL(Xpath, 20, 0)
        return path

    def getChartContent(self):
        """
        获取图表的控件路径
        :return:
        """
        pageId = 0
        itemId = 0
        pageId = self.getPathValue("Page")
        itemId = self.getPathValue("ItemChart")
        element_path = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page" + pageId[0] + "/ItemChart/ItemChart" + itemId[1] + "/Histogram/DrawArea/HistogramModel/Cylinder[5]"  # 选中 柱
        element_path_2 = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page" + pageId[0] + "/ItemChart/ItemChart" + itemId[1] + "/Histogram/DrawArea/控件-资源(Clone)"
        element_path_3 = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page" + pageId[0] + "/ItemChart/ItemChart" + itemId[1] + "/Histogram/DrawArea/控件-资源(Clone)/角锥"
        element_path_4 = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page" + pageId[0] + "/ItemChart/ItemChart" + itemId[1] + "/Histogram/DrawArea/控件-资源(Clone)/角锥_1"
        element_path_5 = "3DP Root/File"+self.getPathValue("File")[0]+"/3DP Root/Page" + pageId[0] + "/ItemChart/ItemChart" + itemId[1] + "/Histogram/DrawArea/DrawAreaTextNode/3DText[5]"
        return element_path, element_path_2, element_path_3, element_path_4, element_path_5


    def CopyPaste2(self, key, ErrMsg, num=2, chart_name="Histogram"):
        """
        复制粘贴（可定位到的控件）
        :param key:
        :param ErrMsg:
        :param num:
        :param chart_name:
        :return:
        """
        time.sleep(1)
        strNum = self.getPathValue(key)
        print key, "1:", len(strNum)
        if key == "ItemChart":
            element = self.getChart(chart_name)
            self.OneClickRightV(element)
        elif key == "ItemText":
            element = self.getText()
            self.OneClickL(element, 50, 0)
            self.Right()
        elif key == "ItemFormComp":
            element = str(self.getTable())
            # x, y = self.WidthAndHeight(element, "var")
            self.OneClickR("RotateByZAxisNor")
        elif key == "ItemAudio":
            self.OneClickR("RotateByZAxisNor")
        else:
            element = self.getElementPath(key)
            self.OneClickRightV(element)
        self.isElementExist("BtnStageRight", "右键1失效")  # 右键是否成功
        time.sleep(1)
        self.ListClick("BtnStageRightCopy")  # 复制
        time.sleep(1)
        self.OneClickR("RotateByZAxisNor")
        self.isElementExist("BtnStageRight", "右键2失效")  # 右键是否成功
        time.sleep(1)
        self.ListClick("BtnStageRightPaste")  # 粘贴
        new_num = len(self.getPathValue(key))
        print key, "2:", new_num
        if new_num - num == len(strNum):
            # self.OneClick("BtnStart")
            # self.OneClick("BtnRevert")
            # self.OneClick("BtnStart")
            # self.OneClick("BtnRevert")
            return
        else:
            assert False, ErrMsg

    def MenuPlaying2(self, key, ErrMsg, num=2, chart_name="Histogram"):
        self.OneClick("BtnPlaying")
        time.sleep(1)
        strNum = self.getPathValue(key)
        print key, "1:", len(strNum)
        if key == "ItemChart":
            element = self.getChart(chart_name)
            self.OneClickL(element)
            # self.OneClickRightV(element)
            if self.isVisible("BtnElementOptionOpen"):
                self.OneClick("BtnElementOption")
        elif key == "ItemText":
            element = self.getText()
            self.OneClickL(element, 30, 0)
            if self.isVisible("BtnElementOptionOpen"):
                self.OneClick("BtnElementOption")
        else:
            element = self.getElementPath(key)
            self.OneClickV(element)
            if self.isVisible("BtnElementOptionOpen"):
                self.OneClick("BtnElementOption")
        self.isElementExist("BtnStageRight", "菜单按钮功能显示失效")  # 右键是否成功
        self.MenuFunc()

    def CopyPastePlaying2(self, key, ErrMsg="菜单删除失败", num=2, chart_name="Histogram"):
        """
        放映态下复制粘贴（可定位的控件）
        :param key:
        :param ErrMsg:
        :param num:
        :param chart_name:
        :return:
        """
        self.OneClick("BtnPlaying")
        time.sleep(1)
        strNum = self.getPathValue(key)
        print key, "1:", len(strNum)
        if key == "ItemChart":
            element = self.getChart(chart_name)
            self.OneClickL(element, z=-20)
            # self.OneClickRightV(element)
        elif key == "ItemText":
            element = self.getText()
            self.OneClickL(element, 30, 0)
        else:
            element = self.getElementPath(key)
            self.OneClickV(element)
        if self.isVisible("BtnElementOptionOpen"):
            self.OneClick("BtnElementOption")
        self.isElementExist("BtnStageRight", "菜单按钮功能显示失效")  # 右键是否成功
        time.sleep(1)
        self.ListClick("BtnStageRightCopy")  # 复制立刻粘贴
        time.sleep(2)

        new_num = len(self.getPathValue(key))
        print key, "2:", new_num
        if new_num - num == len(strNum):
            pass
        else:
            assert False, ErrMsg
        if self.isVisible("BtnElementOptionOpen"):
            self.OneClick("BtnElementOption")
        self.ListClick("BtnStageRightDel")  # 删除
        time.sleep(1)
        # self.OneClick("BtnExitPlaying")
        self.type_keyboardsss(17, 90)  # 组合键
        time.sleep(2)
        self.type_keyboardsss(17, 90)
        time.sleep(2)
        new_num = len(self.getPathValue(key))
        # print "len2:", new_num
        if new_num == len(strNum):
            pass
        else:
            assert False, "撤销删除失败"
        # time.sleep(1)
        # self.type_keyboardsss(17, 90)
        # self.isNotElementExistPageID(element, "撤销删除失败", 10)
        # print "element:", element
        # self.isNotElementExistPageID(element, "删除失败", 5)

        self.OneClick("BtnExitPlaying")

    def CopyPasteImage(self, key, ErrMsg, num=2, dx=0, dy=0):
        """
        复制粘贴（无法定位到的控件）
        :param key:
        :param ErrMsg:
        :param num:
        :param dx:
        :param dy:
        :return:
        """
        strNum = self.getPathValue(key)
        # print "strNum:", len(strNum)
        # self.ClickRight_XY(screen_x/2, screen_y/2, dx, dy)
        self.OneClickR("RotateByZAxisNor")

        self.isElementExist("BtnStageRight", "右键1失效")  # 右键是否成功
        time.sleep(1)
        self.ListClick("BtnStageRightCopy")  # 复制
        time.sleep(2)
        self.OneClickR("RotateByZAxisNor")
        # self.ClickRight_XY(screen_x / 2, screen_y / 2, dx, dy)
        self.isElementExist("BtnStageRight", "右键2失效")  # 右键是否成功
        time.sleep(1)
        self.ListClick("BtnStageRightPaste")  # 粘贴
        new_num = len(self.getPathValue(key))
        # print "len:", new_num
        if new_num - num == len(strNum):
            # self.OneClick("BtnStart")
            # self.OneClick("BtnRevert")
            # self.OneClick("BtnStart")
            # self.OneClick("BtnRevert")
            return
        else:
            assert False, ErrMsg

    def MenuPlaying(self, key, ErrMsg, num=2, dx=0, dy=0):
        self.OneClick("BtnPlaying")
        time.sleep(1)
        strNum = self.getPathValue(key)
        # print "strNum:", len(strNum)
        self.ClickRight_XY(screen_x / 2, screen_y / 2, dx, dy)
        if self.isVisible("BtnElementOptionOpen"):
            self.OneClick("BtnElementOption")
        self.isElementExist("BtnStageRight", "菜单按钮功能显示失效")  # 右键是否成功
        self.MenuFunc()

    def CopyPasteImagePlaying(self, key, ErrMsg, num=2, dx=20, dy=20):
        """
        放映态下的复制粘贴（无法定位的控件）
        :param key:
        :param ErrMsg:
        :param num:
        :param dx:
        :param dy:
        :return:
        """
        self.OneClick("BtnPlaying")
        time.sleep(1)
        strNum = self.getPathValue(key)
        # print "strNum:", len(strNum)
        # self.ClickRight_XY(screen_x / 2, screen_y / 2, dx, dy)
        self.ClickRight_XY(screen_x / 2, screen_y / 2, dx, dy)
        if self.isVisible("BtnElementOptionOpen"):
            self.OneClick("BtnElementOption")
        self.isElementExist("BtnStageRight", "菜单按钮功能显示失效")  # 右键是否成功
        time.sleep(1)
        self.ListClick("BtnStageRightCopy")  # 复制
        time.sleep(2)
        new_num = len(self.getPathValue(key))
        # print "len:", new_num
        if new_num - num == len(strNum):
            pass
        else:
            assert False, ErrMsg
        if self.isVisible("BtnElementOptionOpen"):
            self.OneClick("BtnElementOption")
        self.ListClick("BtnStageRightDel")  # 菜单删除
        time.sleep(1)
        new_num = len(self.getPathValue(key))
        # print "len2:", new_num
        if new_num == len(strNum):
            pass
        else:
            assert False, "菜单功能删除失败"
        time.sleep(3)
        self.type_keyboardsss(17, 90)
        time.sleep(3)
        self.type_keyboardsss(17, 90)
        time.sleep(3)
        # self.type_keyboardsss(17, 90)
        new_num = len(self.getPathValue(key))
        # print "len2:", new_num
        if new_num == len(strNum):
            pass
        else:
            assert False, "撤销删除失败"
        # self.s_witForImg(SourcePath.File_Img_FullScreen, 10, "撤销删除失败")
        self.OneClick("BtnExitPlaying")

    # 放映态复制黏贴(不可变路径)
    def CopyPastePlaying(self, key, Element_path, ErrMsg, num=1):  # num为插入一个元素所产生key个数
        strNum = self.getPathValue(key)
        # print "strNum:", len(strNum)
        self.Click(Element_path)  # 选中控件
        # self.TimesClick(["CopyBtn", "PasteBtn"], 2) # 停顿2s
        self.OneClickRight(Element_path)
        self.isElementExist("BtnStageRight", "菜单按钮功能显示失效")  # 右键是否成功
        self.ListClick("BtnStageRightCopy")  # 复制

        new_num = len(self.getPathValue(key))
        # print "len:", new_num
        if new_num - num == len(strNum):
            return
        else:
            assert False, ErrMsg

    def MenuFunc(self):
        self.WaitForElementText_list("BtnStageRightCopy", "复制", 10, "菜单按钮无支持复制功能")
        self.WaitForElementText_list("BtnStageRightDel", "删除", 10, "菜单按钮无支持删除功能")

    def CutElement(self, key, ErrMsg, num=2, chart_name="Histogram"):
        """
        剪切元素（可定位到的控件）
        :param key:
        :param ErrMsg:
        :param num:
        :param chart_name:
        :return:
        """
        time.sleep(1)
        strNum = self.getPathValue(key)
        print key, "1:", len(strNum)
        if key == "ItemChart":
            element = self.getChart(chart_name)
            self.OneClickRightV(element)
        elif key == "ItemText":
            element = self.getText()
            self.OneClickL(element, 30, 0)
            self.Right()
        elif key == "ItemFormComp":
            element = str(self.getTable())
            # x, y = self.WidthAndHeight(element, "var")
            self.OneClickR("RotateByZAxisNor")
        else:
            element = self.getElementPath(key)
            self.OneClickRightV(element)
        self.isElementExist("BtnStageRight", "右键1失效")  # 右键是否成功
        time.sleep(1)
        self.ListClick("BtnStageRightCut")  # 剪切
        time.sleep(2)
        new_num = len(self.getPathValue(key))
        if new_num + num == len(strNum):
            pass
        else:
            assert False, ErrMsg

    def CutElement2(self, key, ErrMsg, num=2, dx=0, dy=0):
        """
        剪切元素（无法定位到的控件）
        :param key:
        :param ErrMsg:
        :param num:
        :param dx:
        :param dy:
        :return:
        """
        strNum = self.getPathValue(key)
        # print "strNum:", len(strNum)
        self.ClickRight_XY(screen_x / 2, screen_y / 2, dx, dy)
        self.isElementExist("BtnStageRight", "右键1失效")  # 右键是否成功
        time.sleep(1)
        self.ListClick("BtnStageRightCut")  # 剪切
        time.sleep(2)
        # self.ClickRight_XY(screen_x / 2, screen_y / 2, dx, dy)
        new_num = len(self.getPathValue(key))
        if new_num + num == len(strNum):
            return
        else:
            assert False, ErrMsg

    def DelElement(self, key, ErrMsg, num=2, chart_name="Histogram"):
        """
        右键删除元素（可定位到的控件）
        :param key:
        :param ErrMsg:
        :param num:
        :param chart_name:
        :return:
        """
        time.sleep(1)
        strNum = self.getPathValue(key)
        print key, "1:", len(strNum)
        if key == "ItemChart":
            element = self.getChart(chart_name)
            self.OneClickRightV(element)
        elif key == "ItemText":
            element = self.getText()
            self.OneClickL(element, 30, 0)
            self.Right()
        else:
            element = self.getElementPath(key)
            self.OneClickRightV(element)
        self.isElementExist("BtnStageRight", "右键1失效")  # 右键是否成功
        time.sleep(1)
        self.ListClick("BtnStageRightDel")  # 删除
        time.sleep(2)
        new_num = len(self.getPathValue(key))
        if new_num + num == len(strNum):
            pass
        else:
            assert False, ErrMsg

    def DelElement2(self, key, ErrMsg, num=2, dx=0, dy=0):
        """
        右键删除元素（无法定位到的控件）
        :param key:
        :param ErrMsg:
        :param num:
        :param dx:
        :param dy:
        :return:
        """
        strNum = self.getPathValue(key)
        # print "strNum:", len(strNum)
        self.ClickRight_XY(screen_x / 2, screen_y / 2, dx, dy)
        self.isElementExist("BtnStageRight", "右键1失效")  # 右键是否成功
        time.sleep(1)
        if key == "ItemFormComp":
            self.ListClick("BtnStageRightDelTable")  # 删除
        else:
            self.ListClick("BtnStageRightDel")  # 删除
        time.sleep(2)
        # self.ClickRight_XY(screen_x / 2, screen_y / 2, dx, dy)
        new_num = len(self.getPathValue(key))
        if new_num + num == len(strNum):
            return
        else:
            assert False, ErrMsg

    def Swipe4(self, start_x, start_y, x2=0, y2=0, x1=0, y1=0,
               sleeptime=0.5):
        """
        根据坐标拖动元素位移
        :return:
        """
        # p = PyMouse()
        # mouse_absolute(start_x + x1, start_y + y1, start_x + x2, start_y + y2)
        win32api.SetCursorPos((int(start_x + x1), int(start_y + y1)))  # 鼠标移动到
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 左键按下
        time.sleep(1)
        screen.mouseMove(int(x2), int(y2))
        # win32api.SetCursorPos((int(start_x + x1 + x2), int(start_y + y1 + y2)))
        # p.move(int(start_x + x1 + x2), int(start_y + y1 + y2))
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # 左键放开

    def CompareValue(self, one, two, ErrMsg="两个值相等"):
        if one == two:
            assert False, ErrMsg
        else:
            pass

    def RotateByX(self, image, angle=100, ErrMsg="绕X轴調整失敗", sleep=1):
        """
        元素绕X轴旋转
        :return:
        """
        self.Swipe2(ElementOne="BtnRotateByXAxis", ElementTwo="BtnRotateByXAxis", x2=0, y2=angle, sleeptime=sleep)
        time.sleep(1)
        # self.Swipe2(ElementOne="BtnRotateByXAxis", ElementTwo="BtnRotateByXAxis", x2=0, y2=-angle, sleeptOime=sleep)
        self.s_witForImg(image, 10, ErrMsg)

    def RotateByY(self, image, angle=100, ErrMsg="绕Y轴調整失敗", sleep=1):
        """
        元素绕Y轴旋转
        :return:
        """
        self.Swipe2(ElementOne="BtnRotateByYAxis", ElementTwo="BtnRotateByYAxis", x2=angle, y2=0, sleeptime=sleep)
        time.sleep(2)
        # self.Swipe2(ElementOne="BtnRotateByYAxis", ElementTwo="BtnRotateByYAxis", x2=-angle, y2=0, sleeptime=sleep)
        self.s_witForImg(image, 10, ErrMsg)

    def RotateByZ(self, image, angle=500, ErrMsg="绕Z轴调整失败", sleep=1):
        """
        元素绕Z轴旋转
        :return:
        """
        self.Swipe2(ElementOne="BtnRotateByZAxis", ElementTwo="BtnRotateByZAxis", x2=0, y2=angle, sleeptime=sleep)
        time.sleep(1)
        # self.Swipe2(ElementOne="BtnRotateByZAxis", ElementTwo="BtnRotateByZAxis", x2=0, y2=angle, sleeptime=sleep)
        self.s_witForImg(image, 10, ErrMsg)

    def FarAndNear(self, image, angle=30, ErrMsg="远近调整失败", sleep=1):
        """
        元素远近调整
        :return:
        """
        self.Swipe2(ElementOne="BtnMoveStep", ElementTwo="BtnMoveStep", x2=0, y2=angle, sleeptime=sleep)
        time.sleep(1)
        # self.Swipe2(ElementOne="BtnMoveStep", ElementTwo="BtnMoveStep", x2=0, y2=-angle, sleeptime=sleep)
        self.s_witForImg(image, 10, ErrMsg)

    def ZoomOrigin(self, image, x=0, y=0, ErrMsg="原点缩放失败"):
        """
        原点缩放（左原点）
        :return:
        """
        self.Swipe3(ElementOne="BtnDragball5", x2=x, y2=y)
        time.sleep(1)
        # self.Swipe3(ElementOne="BtnDragball5", x2=-x, y2=-y)
        self.s_witForImg(image, 10, ErrMsg)

    def startScene(self, tag):
        '''
        开始场景性能监控
        :param tag: 场景名
        :return: 
        '''
        # tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        # print "tag:", tag
        self.cmdSubprocess('"%s" --STARTSCENE("%s")' % (SourcePath.File_PCPA, tag))

    def endScene(self, tag):
        '''
        结束场景性能监控
        :param tag: 场景名
        :return: 
        '''
        self.cmdSubprocess('"%s" --ENDSCENE("%s")' % (SourcePath.File_PCPA, tag))
