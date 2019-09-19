# coding=utf-8
import sys, win32gui, win32con, time

reload(sys)
sys.setdefaultencoding('UTF-8') #将脚本编码格式转化为指定的编码格式


#  系统弹窗操作处理类
class SystemDiaglog(object):

    def find_idxSubHandle(self, pHandle, winClass, index=0):
        """
        已知子窗口的窗体类名
        寻找第index号个同类型的兄弟窗口
        """
        assert type(index) == int and index >= 0
        handle = win32gui.FindWindowEx(pHandle, 0, winClass, None)
        while index > 0:
            handle = win32gui.FindWindowEx(pHandle, handle, winClass, None)
            index -= 1
        return handle

    def find_subHandle(self, pHandle, winClassList):
        """
        递归寻找子窗口的句柄
        pHandle是祖父窗口的句柄
        winClassList是各个子窗口的class列表，父辈的list-index小于子辈
        """
        assert type(winClassList) == list
        if len(winClassList) == 1:
            return self.find_idxSubHandle(pHandle, winClassList[0][0], winClassList[0][1])
        else:
            pHandle = self.find_idxSubHandle(pHandle, winClassList[0][0], winClassList[0][1])
            return self.find_subHandle(pHandle, winClassList[1:])

    def inputDlgClick(self, class_name, win_name, win_class_list, edit_text, btn_class):
        """
        查找弹窗句柄并输入路径点击按钮
        class_name是弹窗的类名
        win_class_list是各个子窗口的class列表，父辈的list-index小于子辈
        edit_text是输入的路径文本
        btn_class是输入文本后点击的按钮
        """
        Mhandle = win32gui.FindWindow(class_name, win_name)
        #print "Mhandle:%x" % (Mhandle)
        edit_handle = self.find_subHandle(Mhandle, win_class_list)
        #print "edit_handle:%x" % (edit_handle)
        win32gui.SendMessage(edit_handle, win32con.WM_SETTEXT, None, edit_text)
        time.sleep(1)
        btn_handle = win32gui.FindWindowEx(Mhandle, None, btn_class, None)
        #print "btn_handle:%x" % (btn_handle)
        win32gui.PostMessage(btn_handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        # time.sleep(0.1)
        # win32gui.PostMessage(btn_handle, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

    def overrideFile(self, confirm):
        """
        另存覆盖文件操作
        confirm为是否覆盖bool值
        """
        hwnd = win32gui.FindWindow(None, u"确认另存为")
        if hwnd:
            if confirm:
                btn_index = 6
            else:
                btn_index = 7
            btn_handle = self.find_subHandle(hwnd, [("DirectUIHWND", 0), ("CtrlNotifySink", btn_index), ("Button", 0)])
            win32gui.PostMessage(btn_handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
            time.sleep(0.1)
            win32gui.PostMessage(btn_handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)