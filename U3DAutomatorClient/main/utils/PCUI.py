#! /usr/bin/env python
#coding=utf-8

from main.utils.ImageRecognize import ImageRecognize
from main.utils.path import Path
from main.log.logger import get_logger
from main.utils.process import Process
from ctypes import *
# from pytesser import *
# import cv2.cv as cv
import sys,os,win32api,win32con,win32gui,time,win32clipboard
from PIL import ImageGrab, Image, ImageEnhance
import win32com.client,math,win32process,pyperclip


class UI:
    def __init__(self, scriptPath="TestCase"):
        self.scriptPath = scriptPath
        self.scriptName = scriptPath.split("\\")[-1].split(".")[0]
        self.pngNum = 0
        self.flag='notkey'
        self.VK_CODE = {
            'backspace':0x08,'tab':0x09,'clear':0x0C,'enter':0x0D,'shift':0x10,'esc':0x1B,' ':0x20,'spacebar':0x20,'page_up':0x21,'page_down':0x22,
            'end':0x23,'home':0x24,'left_arrow':0x25,'up_arrow':0x26, 'right_arrow':0x27,'down_arrow':0x28, 'select':0x29,'print':0x2A, 'execute':0x2B,
            'print_screen':0x2C, 'ins':0x2D,'del':0x2E, 'help':0x2F,
            '0':0x30, '1':0x31, '2':0x32, '3':0x33,'4':0x34,'5':0x35,'6':0x36, '7':0x37, '8':0x38,'9':0x39,
            ')':0x30, '!':0x31, '@':0x32, '#':0x33,'$':0x34,'%':0x35,'^':0x36, '&':0x37, '*':0x38,'(':0x39,
            'a':0x41,'b':0x42, 'c':0x43,'d':0x44,'e':0x45,'f':0x46, 'g':0x47, 'h':0x48,'i':0x49,'j':0x4A,'k':0x4B,'l':0x4C,'m':0x4D,'n':0x4E,'o':0x4F,'p':0x50, 'q':0x51, 'r':0x52, 's':0x53,'t':0x54,'u':0x55, 'v':0x56, 'w':0x57, 'x':0x58, 'y':0x59, 'z':0x5A,
            'A':0x41,'B':0x42, 'C':0x43,'D':0x44,'E':0x45,'F':0x46, 'G':0x47, 'H':0x48,'I':0x49,'J':0x4A,'K':0x4B,'L':0x4C,'M':0x4D,'N':0x4E,'O':0x4F,'P':0x50, 'Q':0x51, 'R':0x52, 'S':0x53,'T':0x54,'U':0x55, 'V':0x56, 'W':0x57, 'X':0x58, 'Y':0x59, 'Z':0x5A,
            'numpad_0':0x60,'numpad_1':0x61,'numpad_2':0x62,'numpad_3':0x63,'numpad_4':0x64,'numpad_5':0x65,'numpad_6':0x66,'numpad_7':0x67,'numpad_8':0x68, 'numpad_9':0x69,'multiply_key':0x6A, 'add_key':0x6B,'separator_key':0x6C, 'subtract_key':0x6D,'decimal_key':0x6E, 'divide_key':0x6F,
            'F1':0x70, 'F2':0x71, 'F3':0x72,'F4':0x73,'F5':0x74,'F6':0x75,'F7':0x76,'F8':0x77,'F9':0x78,'F10':0x79,'F11':0x7A,'F12':0x7B,'F13':0x7C, 'F14':0x7D, 'F15':0x7E, 'F16':0x7F,'F17':0x80,'F18':0x81, 'F19':0x82,'F20':0x83,'F21':0x84,'F22':0x85,'F23':0x86,'F24':0x87,
            'num_lock':0x90,'scroll_lock':0x91,'left_shift':0xA0,'right_shift ':0xA1,'left_control':0xA2,'right_control':0xA3,'left_menu':0xA4,'right_menu':0xA5,'browser_back':0xA6,'browser_forward':0xA7,'browser_refresh':0xA8,
            'browser_stop':0xA9,'browser_search':0xAA,'browser_favorelloites':0xAB,'browser_start_and_home':0xAC,'volume_mute':0xAD,'volume_Down':0xAE,'volume_up':0xAF,'next_track':0xB0,'previous_track':0xB1,'stop_media':0xB2,'play/pause_media':0xB3,'start_mail':0xB4,'select_media':0xB5,'start_application_1':0xB6,'start_application_2':0xB7,
            'attn_key':0xF6,'crsel_key':0xF7,'exsel_key':0xF8,'play_key':0xFA,'zoom_key':0xFB,'clear_key':0xFE,'left_win':0x5B,'right_win':0x5C,
            'caps':0x14,';':0xBA,':':0xBA,'+':0xBB,'=':0xBB,'-':0xBD,'_':0xBD,'/':0xBF,'?':0xBF,'`':0xC0,'~':0xC0,'[':0xDB,'{':0xDB,'\\':0xDC,'|':0xDC,"'":0xDE,'"':0xDE,']':0xDD,'}':0xDD,',':0xBC,'<':0xBC,'.':0xBE,'>':0xBE
            }

    def tempImagePath(self,file):#temp图片路径判断
        if "common" in self.scriptPath:
            return Path.commonTempPath(file)
        else:
            Path.create_file(Path.caseTempPath(self.scriptName))
            return Path.caseTempPath(self.scriptName+os.sep+file)
        
    def modelInagePath(self,file):#model图片路径判断
        if "common" in self.scriptPath:
            return Path.commonPath(file)
        else:
            return Path.windowsPath(file)
        
    def screenCap(self,file,resultPath=False,x = 1680, y = 1050):#截屏
        try:
            self.printScreen(file,resultPath,x, y)
        except Exception, e:
            get_logger().info("PC_UI.UI.screenCap:%s"%str(e))

    def serialmatch(self,pngModelnum,shunxv=False,alltime=30,spacetime=0,x = 1680, y = 1050,Accurate=0.5):#参数shunxv是为了匹配动作是否重复执行,为True时按顺序匹配所有图片，False匹配成功则返回
        self.pngNum += 1
        starttime=time.time()
        endtime=time.time()
        i=1
        self.image=[]
        while((endtime-starttime)<=alltime):
            name="%s_%s"%(pngModelnum,str(i))
            self.printScreen(name)
            self.image.append(name)
            time.sleep(spacetime)
            i+=1
            endtime=time.time()
        num=0
        for i in self.image:
            all=self.serialIamgeAll(pngModelnum,i,Accurate=Accurate)
            print all
            if all[0]:
                if shunxv:
                    num+=1
                    self.pngNum += 1
                else:
                    break
        return all[0],all[1],all[2],num,len(self.image)

    def serialIamgeAll(self,pngModelNum,nserialImage,x = 1680, y = 1050,Accurate=0.5):#传入模版图片和第n张图片
        dict = ImageRecognize.proxy(self.modelInagePath(self.scriptName + os.sep + "%s.png"%pngModelNum),self.tempImagePath("%s.png"%nserialImage),Path.resultImagePath(self.scriptName,"%s.png"%self.pngNum),srcX=x, srcY=y ,defaultAccurate=Accurate)
        return dict["match"],dict["maxLocX"],dict["maxLocY"]

    def imageIsExist(self,pngModelNum,x = 1680, y = 1050,Accurate=0.5):#判断图片是否存在，返回boolean，并复制图片
        try:
            return self.imageAll(pngModelNum,x,y,Accurate)[0]
        except Exception, e:
            get_logger().info("%s-PC_UI.UI.imageIsExist:%s"%(self.scriptName,str(e)))

    def imagePos(self,pngModelNum,x = 1680, y = 1050,Accurate=0.5):#获取图片中心坐标
        try:
            imagematch,imagex,imagey=self.imageAll(pngModelNum,x,y,Accurate)
            if imagematch==True:
                return imagex,imagey
            else:
                #print "%s %s.png not find element"%(self.scriptPath,self.pngNum)
                get_logger().info("%s %s.png not find element"%(self.scriptPath,self.pngNum))
                sys.exit()
        except Exception, e:
            get_logger().info("%s-PC_UI.UI.imageIsExist:%s"%(self.scriptName,str(e)))
        
    def imageAll(self,pngModelNum,x = 1680, y = 1050,Accurate=0.5):#输出图片的math，x,y
        try:
            self.pngNum += 1
            self.screenCap(self.pngNum)
            dict = ImageRecognize.proxy(self.modelInagePath(self.scriptName + os.sep + "%s.png"%pngModelNum),self.tempImagePath("%s.png"%self.pngNum),Path.resultImagePath(self.scriptName,"%s.png"%self.pngNum),srcX=x, srcY=y ,defaultAccurate=Accurate)
            return dict["match"],dict["maxLocX"],dict["maxLocY"]
        except Exception, e:
            get_logger().info("%s-PC_UI.UI.imageAll:%s-%s"%(self.scriptName,str(e),pngModelNum))

    def pressIfHas(self,pngModelNum,Accurate=0.5,t=0.5):
        match,x,y=self.imageAll(pngModelNum,Accurate=Accurate)
        if match:
            self.mouse_click(x,y,t)

    def get_mouse_point(self,t=0.5):#获取鼠标的坐标
        class POINT(Structure):
            _fields_ = [("x", c_ulong),("y", c_ulong)]
        po = POINT()
        windll.user32.GetCursorPos(byref(po))
        time.sleep(t)
        return int(po.x), int(po.y)

    def mouse_down(self,x=None,y=None,t=0.5):
        if not x is None and not y is None:
            self.mouse_move(x,y)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(t)

    def mouse_up(self,x=None,y=None):#有坐标的松开鼠标
        if not x is None and not y is None:
            self.mouse_move(x,y)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    def mouse_up_nopos(self,t=0.5):#无坐标的松开鼠标
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(t)
    
    def mouse_click(self, x=None, y=None, t=0.1):#单击
        try:
            if not x is None and not y is None:
                self.mouse_move(x, y)
            time.sleep(1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            time.sleep(t)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

        except Exception, e:
            # print str(e)
            raise Exception(str(e))


    def server_click(self,x=None,y=None,t=0.5):#该函数只用于服务器使用
        if not x is None and not y is None:
            self.mouse_move(x,y,t)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0) 
        time.sleep(t)

    def mouse_click_right(self,x=None,y=None,t=0.5):#右击
        if not x is None and not y is None:
            self.mouse_move(x,y)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0) 
        time.sleep(t)

    def mouse_dclick(self,x=None,y=None,t=0.5):#双击
        if not x is None and not y is None:
            self.mouse_move(x,y)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(t)

    def mouse_swip(self,x1,y1,x2,y2,t=0.5):#拖动
        if not x1 is None and not y1 is None and not x2 is None and not y2 is None:
            self.mouse_move(x1,y1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.5)
        self.mouse_move(x2,y2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(t)

    def mouse_move(self, x, y, t=1):#鼠标移动
        windll.user32.SetCursorPos(x, y)
        # win32api.SetCursorPos((int(x), int()))
        time.sleep(t)

    def key_input(self,str=''):#文本输入
        for c in str:
            self.key_event(c)
            time.sleep(0.1)

    def key_event(self,mykey,t=0.1):#键码输入
        if mykey in ["_","+","{","}",":",'"',"?",">","<","!","@","#","$","%",'^',"&","*","(",")"]:
            self.many_keyevent('shift',mykey)
        else:
            win32api.keybd_event(self.VK_CODE[mykey],0,0,0)
            win32api.keybd_event(self.VK_CODE[mykey],0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(t)

    def pressButtonRight(self,pngModelNum,Accurate=0.5,t=1.0):
        x,y=self.imagePos(pngModelNum,Accurate=Accurate)
        self.mouse_click_right(x,y,t)

    def pressButton(self,pngModelNum,Accurate=0.5,t=1):
        x,y=self.imagePos(pngModelNum,Accurate=Accurate)
        self.mouse_click(x,y,t)

    def pressButtonDown(self,pngModelNum,Accurate=0.5,t=1):#按下鼠标不放开
        x,y=self.imagePos(pngModelNum,Accurate=Accurate)
        self.mouse_down(x,y,t)

    def doublePressButton(self,pngModelNum,Accurate=0.5,t=1):
        x,y=self.imagePos(pngModelNum,Accurate=Accurate)
        self.mouse_dclick(x,y,t)

    def swipeOpe(self,pngModelNum1,pngModelNum2,t=1):#滑动操作 单击目标坐标放下
        x,y = self.imagePos(pngModelNum1)
        x1,y1 =self.imagePos(pngModelNum2)
        self.mouse_swip(x,y,x1,y1)
        self.mouse_click(x1,y1,t)

    def swipeOpedouble(self,pngModelNum1,pngModelNum2,t=1):#滑动操作 双击目标坐标放下
        x,y = self.imagePos(pngModelNum1)
        x1,y1 =self.imagePos(pngModelNum2)
        self.mouse_swip(x,y,x1,y1)
        self.mouse_dclick(x1,y1,t)

    def many_keyevent(self,mykey1,mykey2):#多按键按下
        win32api.keybd_event(self.VK_CODE[mykey1],0,0,0)
        win32api.keybd_event(self.VK_CODE[mykey2],0,0,0)
        win32api.keybd_event(self.VK_CODE[mykey1],0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(self.VK_CODE[mykey2],0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(0.05)

    def moveToImage(self,pngModelNum,Accurate=0.5,t=1):
        x,y=self.imagePos(pngModelNum,Accurate=Accurate)
        self.mouse_move(x,y,t)

    def down_keyevent(self,mykey,t=0.5):#按下键
        win32api.keybd_event(self.VK_CODE[mykey],0,0,0)
        time.sleep(t)

    def up_keyevent(self,mykey,t=0.5):#放开键
        win32api.keybd_event(self.VK_CODE[mykey],0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(t)

    def click_keyevent(self,x,y,mykey,t=0.5):#键码加鼠标左击（鼠标不会松开）
        self.down_keyevent(mykey)
        self.mouse_click(x,y,t)

    def click_keyevent_right(self,x,y,mykey,t=0.5):#键码加鼠标右击（鼠标不会松开）
        self.down_keyevent(mykey)
        self.mouse_click_right(x,y,t)

    def keyMouse(self,pngModelNum,mykey,Accurate=0.5,t=1):#键码加鼠标左击
        x,y=self.imagePos(pngModelNum,Accurate=Accurate)
        self.click_keyevent(x,y,mykey,t)
        self.up_keyevent(mykey)

    def keyMouseRight(self,pngModelNum,mykey,Accurate=0.5,t=1):#键码加鼠标右击
        x,y=self.imagePos(pngModelNum,Accurate=Accurate)
        self.click_keyevent_right(x,y,mykey,t)
        self.up_keyevent(mykey)

    def getText(self):  
        win32clipboard.OpenClipboard()  
        d = win32clipboard.GetClipboardData(win32con.CF_TEXT)  
        win32clipboard.CloseClipboard()  
        return d 

    def setText(self,aString):  
        win32clipboard.OpenClipboard()  
        win32clipboard.EmptyClipboard()  
        win32clipboard.SetClipboardData(win32con.CF_TEXT, aString)  
        win32clipboard.CloseClipboard() 

    def text(self,str):#可以以剪贴板的形式避免中英文输入法的切换   ui.text("texttext")  ui.text("你好".decode('UTF-8').encode('GBK'))
        pyperclip.copy(str)
        self.many_keyevent("left_control","v")

    def passkey_event(self,mykey,t=1):#键码输入
        win32api.keybd_event(self.VK_CODE[mykey],win32api.MapVirtualKey(self.VK_CODE[mykey], 0),0,0)
        time.sleep(0.1)
        win32api.keybd_event(self.VK_CODE[mykey],win32api.MapVirtualKey(self.VK_CODE[mykey], 0),win32con.KEYEVENTF_KEYUP,0)

    def passkey_input(self,str=''):#文本输入
        for i,c in enumerate(str):
            if i!=0 and c==str[i-1]:#避免前后键码一致导致后一个键码无法输出
                time.sleep(1)
            self.passkey_event(c)

    def pressNPC(self,pngModelNum,Accurate=0.5,t=1.0):
        self.doublePressButton(pngModelNum,Accurate,t)
        self.mouse_move(0,0)

    def printScreen(self,file,resultPath=False,x = 1680, y = 1050):
        try:
            if resultPath==True:#在image下的脚本文件夹
                path = Path.resultImagePath(self.scriptName,"%s.png"%file)
            elif resultPath==False:#默认在case下的temp
                path = self.tempImagePath("%s.png"%file)
            else:
                path = resultPath
            self.key_event('print_screen')
            im = ImageGrab.grabclipboard()
            n=15
            while(n>=0):
                if im!=None:
                    break
                else:
                    self.key_event('print_screen')
                    im = ImageGrab.grabclipboard()
                    n=n-1
                    time.sleep(1)
            region=im.crop((0,0,x,y))#裁剪图片
            region.save(path)
        except Exception, e:
            get_logger().info("PC_UI.UI.printScreen:%s"%str(e))

    def PMcmd(self,thetext,t=0.5):
        self.mouse_click(152,909)
        #self.key_event('enter')
        self.text(thetext)
        self.key_event('enter')
        self.key_event('enter')
        time.sleep(t)

    def getImage(self,imagepath,savepath,startx=610,starty=470,endx=755,endy=505):
        im=Image.open(imagepath)
        region=im.crop((startx,starty,endx,endy))#裁剪图片
        region.save(savepath)

    def callback(self,hwnd,nothing):
        #去掉下面这句就所有都输出了，但是我不需要那么多
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            self.titles.append(win32gui.GetWindowText(hwnd))
            self.handle.append(hwnd)

    def getHandle(self,name):
        try:
            self.titles = []
            self.handle=[]
            myhwnd=[]
            win32gui.EnumWindows(self.callback,None)
            for i,v in enumerate(self.titles):
                if name.decode("utf-8").encode("gbk") in v:
                    myhwnd.append(self.handle[i])
            return myhwnd
        except Exception, e:
            get_logger().info("PC_UI.UI.getHandle:%s"%str(e))

    def showMyWindow(self,hWnd,t=1):
        try:
            win32gui.ShowWindow(hWnd,win32con.SW_NORMAL) 
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('%')
            win32gui.SetForegroundWindow(hWnd)
            time.sleep(t)
        except Exception, e:
            get_logger().info("%s-PC_UI.UI.showMyWindow:%s"%(self.scriptName,str(e)))

    def findClient(self,pngModelNum,myAccurate=0.5,t=1.0,processname='魔域'):
        try:
            hand=[]
            hand=self.getHandle(processname)
            for i in hand:
                self.showMyWindow(i)
                time.sleep(1.0)
                match,x,y=self.imageAll(pngModelNum,Accurate=myAccurate)
                if match:
                    self.mouse_click(x,y)
                    break
            time.sleep(t)
        except Exception, e:
            get_logger().info("%s-PC_UI.UI.findClient:%s"%(self.scriptName,str(e)))

    def getMyhwndByName(self,processname='【魔域】'):#获取所有应用名字对应的获取窗口句柄列表，该句柄列表是通过时间排序的
        try:
            hwnd=self.getHandle(processname)
            ph={}
            hw=[]
            for h in hwnd:
                hreadID,pid=win32process.GetWindowThreadProcessId(h)
                ph[Process().getProCreatTime(pid)]=h
            for v in sorted(ph.keys()):#字典按进城时间排序  返回对应的值列表
                hw.append(ph[v])
            return hw
        except Exception as e:
            get_logger().info("PC_UI.UI.GetMyhwndByName:%s"%str(e))



if __name__=='__main__':
    ui=UI(r"F:\autotestU3D\U3DAutomatorClient\script\windows\actionhavior.py")
    #ui.serialmatch("nongming",alltime=30,spacetime=0,Accurate=0.8)
    print ui.serialmatch("yulan3miao",shunxv=True,alltime=17,spacetime=0,Accurate=0.89)
