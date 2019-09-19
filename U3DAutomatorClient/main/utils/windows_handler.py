# coding=utf-8
import ctypes
import win32api
import win32con
import win32process
import win32gui
import os, subprocess
import time
from PIL import ImageGrab
from main.log.logger import get_logger
from main.object.enum import Environment
from script.windows.PPT3DSetting.SourcePath import SourcePath
__author__ = "Junpeng Chen"
__all__ = ["get_windows_handler"]


class WindowsHandler:
    def __init__(self, path, title):
        self.path = path.decode("utf8").encode("gbk")
        self.title = title.decode("utf8").encode("gbk")
        self.hwnd = None
        self.process = None

    def get_mouse_point(self):
        """
            获取鼠标坐标
        :return:
        """
        x, y = win32gui.GetCursorPos()
        return int(x), int(y)

    def get_client_centre(self):
        """
            获取客户端中心点
        :return:
        """
        rect = win32gui.GetClientRect(self.__get_hwnd)
        return (rect[2] - rect[0]) / 2, (rect[3] - rect[1]) / 2

    def client_to_screen(self, x, y):
        """
            客户端坐标转屏幕坐标
        :param x:
        :param y:
        :return:
        """
        return win32gui.ClientToScreen(self.__get_hwnd, (int(x), int(y)))

    def mouse_move(self, px, py):
        """
            鼠标移动
        :param px:
        :param py:
        :return:
        """
        if px and py:
            win32api.SetCursorPos((int(px), int(py)))
            time.sleep(0.1)

    def mouse_absolute(self, x, y, x2, y2):
        """
            鼠标移动
        :param px:
        :param py:
        :return:
        """
        # SW = 1377
        # SH = 768
        # win32api.SetCursorPos((x, y))  # 鼠标移动到
        # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 左键按下
        # time.sleep(0.2)
        # mw = int(x2 * 65535 / SW)
        # mh = int(y2 * 65535 / SH)
        # win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, mw, mh, 0, 0)
        # time.sleep(0.2)
        # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        win32api.SetCursorPos((int(x), int(y)))  # 鼠标移动到
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 左键按下
        time.sleep(1)
        win32api.SetCursorPos((int(x2), int(y2)))  # 鼠标移动到
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    def mouse_click(self, px=None, py=None):
        """
            鼠标左键点击
        :param px:
        :param py:
        :return:
        """
        self.mouse_press(px, py)

    def mouse_click_double(self, px=None, py=None):
        """
            鼠标左键双击
        :param px:
        :param py:
        :return:
        """
        self.mouse_press(px, py, times=2)

    def mouse_click_three(self, px=None, py=None):
        """
            鼠标左键三击
        :param px:
        :param py:
        :return:
        """
        self.mouse_press(px, py, times=3)

    def mouse_click_right(self, px=None, py=None):
        """
            鼠标右键点击
        :param px:
        :param py:
        :return:
        """
        self.mouse_press(px, py, event=(win32con.MOUSEEVENTF_RIGHTDOWN, win32con.MOUSEEVENTF_RIGHTUP))

    def mouse_click_middle(self, px=None, py=None):
        """
            鼠标中键点击
        :param px:
        :param py:
        :return:
        """
        self.mouse_press(px, py, event=(win32con.MOUSEEVENTF_MIDDLEDOWN, win32con.MOUSEEVENTF_MIDDLEUP))

    def mouse_wheel_roll(self, data):
        """
            鼠标滑轮滚动
        :param data:
        :return:
        """
        if isinstance(data, int):
            sign = 1 if data >= 0 else -1
            for i in xrange(abs(data)):
                win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 120 * sign, win32con.WHEEL_DELTA)

    def mouse_press(self, px=None, py=None, sleep_time=0.05, times=1,
                    event=(win32con.MOUSEEVENTF_LEFTDOWN, win32con.MOUSEEVENTF_LEFTUP)):
        """
            鼠标左键长按
        :param times:
        :param px:
        :param py:
        :param sleep_time:
        :param event:
        :return:
        """
        self.mouse_move(px, py)
        for i in range(times):
            win32api.mouse_event(event[0], 0, 0, 0, 0)
            time.sleep(sleep_time)
            win32api.mouse_event(event[1], 0, 0, 0, 0)

    def mouse_swipe(self, start_x, start_y, end_x, end_y, steps, duration):
        """
            鼠标左键拖动
        :param start_x:
        :param start_y:
        :param end_x:
        :param end_y:
        :param steps:
        :param duration:
        :return:
        """
        self.mouse_swipe_press(start_x, start_y, end_x, end_y, steps, duration)

    def mouse_swipe_press_right(self, start_x, start_y, end_x, end_y, steps, duration):
        """
            鼠标右键拖动
        :param start_x:
        :param start_y:
        :param end_x:
        :param end_y:
        :param steps:
        :param duration:
        :return:
        """
        self.mouse_swipe_press(start_x, start_y, end_x, end_y, steps, duration,
                               event=(win32con.MOUSEEVENTF_RIGHTDOWN, win32con.MOUSEEVENTF_RIGHTUP))

    def mouse_swipe_press(self, start_x, start_y, end_x, end_y, steps, duration, sleep_time=0.2,
                          event=(win32con.MOUSEEVENTF_LEFTDOWN, win32con.MOUSEEVENTF_LEFTUP)):
        """
            鼠标左键拖动，并长按
        :param start_x:
        :param start_y:
        :param end_x:
        :param end_y:
        :param steps:
        :param duration:
        :param sleep_time:
        :param event:
        :return:
        """
        if steps <= 0:
            raise Exception("steps = {0} is invalid, steps must more than 0".format(steps))
        start_x = float(start_x)
        start_y = float(start_y)
        end_x = float(end_x)
        end_y = float(end_y)

        x_distance = (end_x - start_x) / steps
        y_distance = (end_y - start_y) / steps
        move_x, move_y = start_x, start_y
        step_sleep = 0 if duration <= 0 else float(duration) / steps

        self.mouse_move(start_x, start_y)
        win32api.mouse_event(event[0], 0, 0, 0, 0)

        for i in range(steps):
            move_x += x_distance
            move_y += y_distance
            time.sleep(step_sleep)
            win32api.SetCursorPos((int(move_x), int(move_y)))

        win32api.SetCursorPos((int(end_x), int(end_y)))
        if sleep_time > 0:
            time.sleep(sleep_time)
        win32api.mouse_event(event[1], 0, 0, 0, 0)

    def key_input(self, string='', px=None, py=None):
        """
            输入键盘
        :param string:
        :param px:
        :param py:
        :return:
        """
        if px and py:
            self.mouse_click(px, py)
        self.key_click(string)

    def key_click(self, string='', sleep_time=0):
        """
            长按键盘
        :param string:
        :param sleep_time:
        :return:
        """
        for c in string:
            win32api.keybd_event(VK_CODE[c], 0, 0, 0)
            if sleep_time > 0:
                time.sleep(sleep_time)
        # for c in string:
            win32api.keybd_event(VK_CODE[c], 0, win32con.KEYEVENTF_KEYUP, 0)

    def key_code_input(self, string, sleep_time=0):
        """
            键盘功能键
        :param sleep_time:
        :param string:
        :return:
        """
        win32api.keybd_event(VK_CODE[string], 0, 0, 0)
        if sleep_time > 0:
            time.sleep(sleep_time)
        win32api.keybd_event(VK_CODE[string], 0, win32con.KEYEVENTF_KEYUP, 0)

    def screen_cap(self, path):
        """
            截屏并保存,双显示屏状态下副屏截屏失败
        :param path:
        :return:
        """
        try:
            # rect = win32gui.GetClientRect(self.__get_hwnd)
            # x, y = self.client_to_screen(0, 0)
            # ImageGrab.grab((rect[0] + x, rect[1] + y, rect[2] + x, rect[3] + y)).save(path)
            # return path

            # x, y = self.client_to_screen(0, 0)
            ImageGrab.grab().save(path)
            return path
        except Exception, e:
            print str(e)
            return "catch image failed"

    def set_foreground_window(self):
        """
            设置窗体前置
        :return:
        """
        win32gui.SetForegroundWindow(self.__get_hwnd)

    def set_window_max(self):
        """
            窗口最大化
        :return:
        """
        win32gui.ShowWindow(self.__get_hwnd, win32con.SW_MAXIMIZE)

    def open_process(self):
        """
            打开应用
        :return:
        """
        try:

            os.system(SourcePath.File_3DPPT_Kill)
        except:
            pass
            raise Exception(u"关闭应用失败")  # 开始运行前先排除上一次运行未杀进程情况
        time.sleep(5)
        if not os.path.exists(self.path):
            get_logger().error("open_process Error not such file:%s" % self.path)
            return False
        get_logger().info("open_test_application : %s " % self.path)
        try:
            self.process = win32process.CreateProcess(self.path, '', None, None, 0, win32process.CREATE_NO_WINDOW, None,
                                                      None, win32process.STARTUPINFO())
            time.sleep(1)
            self.set_foreground_window()
            self.set_window_max()
            return True
        except Exception, e:

            get_logger().error("open_process Error  " + str(e.message))

            return False

    def close_process(self):
        """
            关闭应用
        :return:
        """
        get_logger().info("close_test_application : %s " % self.path)
        self.hwnd = None
        if self.process:
            try:
                win32process.TerminateProcess(self.process[0], 0)
                self.process = None
            except:
                try:

                    os.system(SourcePath.File_3DPPT_Kill)
                except:
                    pass
                raise Exception(u"关闭应用失败")
        else:
            try:
                os.system(SourcePath.File_3DPPT_Kill)
            except:
                pass

    @property
    def __get_hwnd(self):
        """
            获取窗口句柄
        :return:
        """
        if not self.hwnd:
            self.hwnd = win32gui.FindWindow(None, self.title)
            if self.hwnd == 0:
                raise Exception("hwnd == 0")
        return self.hwnd


VK_CODE = {
    'backspace': 0x08,
    'tab': 0x09,
    'clear': 0x0C,
    'enter': 0x0D,
    'shift': 0x10,
    'ctrl': 0x11,
    'alt': 0x12,
    'pause': 0x13,
    'caps_lock': 0x14,
    'esc': 0x1B,
    'spacebar': 0x20,
    'page_up': 0x21,
    'page_down': 0x22,
    'end': 0x23,
    'home': 0x24,
    'left_arrow': 0x25,
    'up_arrow': 0x26,
    'right_arrow': 0x27,
    'down_arrow': 0x28,
    'select': 0x29,
    'print': 0x2A,
    'execute': 0x2B,
    'print_screen': 0x2C,
    'ins': 0x2D,
    'del': 0x2E,
    'help': 0x2F,
    '0': 0x30,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,
    'a': 0x41,
    'b': 0x42,
    'c': 0x43,
    'd': 0x44,
    'e': 0x45,
    'f': 0x46,
    'g': 0x47,
    'h': 0x48,
    'i': 0x49,
    'j': 0x4A,
    'k': 0x4B,
    'l': 0x4C,
    'm': 0x4D,
    'n': 0x4E,
    'o': 0x4F,
    'p': 0x50,
    'q': 0x51,
    'r': 0x52,
    's': 0x53,
    't': 0x54,
    'u': 0x55,
    'v': 0x56,
    'w': 0x57,
    'x': 0x58,
    'y': 0x59,
    'z': 0x5A,
    'numpad_0': 0x60,
    'numpad_1': 0x61,
    'numpad_2': 0x62,
    'numpad_3': 0x63,
    'numpad_4': 0x64,
    'numpad_5': 0x65,
    'numpad_6': 0x66,
    'numpad_7': 0x67,
    'numpad_8': 0x68,
    'numpad_9': 0x69,
    'multiply_key': 0x6A,
    'add_key': 0x6B,
    'separator_key': 0x6C,
    'subtract_key': 0x6D,
    'decimal_key': 0x6E,
    'divide_key': 0x6F,
    'F1': 0x70,
    'F2': 0x71,
    'F3': 0x72,
    'F4': 0x73,
    'F5': 0x74,
    'F6': 0x75,
    'F7': 0x76,
    'F8': 0x77,
    'F9': 0x78,
    'F10': 0x79,
    'F11': 0x7A,
    'F12': 0x7B,
    'F13': 0x7C,
    'F14': 0x7D,
    'F15': 0x7E,
    'F16': 0x7F,
    'F17': 0x80,
    'F18': 0x81,
    'F19': 0x82,
    'F20': 0x83,
    'F21': 0x84,
    'F22': 0x85,
    'F23': 0x86,
    'F24': 0x87,
    'num_lock': 0x90,
    'scroll_lock': 0x91,
    'left_shift': 0xA0,
    'right_shift ': 0xA1,
    'left_control': 0xA2,
    'right_control': 0xA3,
    'left_menu': 0xA4,
    'right_menu': 0xA5,
    'browser_back': 0xA6,
    'browser_forward': 0xA7,
    'browser_refresh': 0xA8,
    'browser_stop': 0xA9,
    'browser_search': 0xAA,
    'browser_favorites': 0xAB,
    'browser_start_and_home': 0xAC,
    'volume_mute': 0xAD,
    'volume_Down': 0xAE,
    'volume_up': 0xAF,
    'next_track': 0xB0,
    'previous_track': 0xB1,
    'stop_media': 0xB2,
    'play/pause_media': 0xB3,
    'start_mail': 0xB4,
    'select_media': 0xB5,
    'start_application_1': 0xB6,
    'start_application_2': 0xB7,
    'attn_key': 0xF6,
    'crsel_key': 0xF7,
    'exsel_key': 0xF8,
    'play_key': 0xFA,
    'zoom_key': 0xFB,
    'clear_key': 0xFE,
    '+': 0xBB,
    ',': 0xBC,
    '-': 0xBD,
    '.': 0xBE,
    '/': 0xBF,
    ';': 0xBA,
    '[': 0xDB,
    '\\': 0xDC,
    ']': 0xDD,
    "'": 0xDE,
    '`': 0xC0}


def get_windows_handler(test_path=None, windows_title=None):
    """
        获取windows操作
    :param test_path:
    :param windows_title:
    :return:
    """
    if not get_windows_handler.instance:
        path = test_path or  os.getenv(Environment.TEST_PATH)
        title = windows_title or os.getenv(Environment.WINDOWS_TITLE)
        #print "path:", path, "title:", title
        if not title or not path:
            raise EnvironmentError("env TEST_PATH or WINDOWS_TITLE error : %s,%s" % (path, title))
        get_windows_handler.instance = WindowsHandler(path, title)
    return get_windows_handler.instance


get_windows_handler.instance = None


def get_all_title():
    """
        获取所有窗口title
    :return:
    """
    enum_windows = ctypes.windll.user32.EnumWindows
    enum_windows_process = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    get_window_text = ctypes.windll.user32.GetWindowTextW
    get_window_text_length = ctypes.windll.user32.GetWindowTextLengthW
    is_window_visible = ctypes.windll.user32.IsWindowVisible

    titles = []

    def foreach_window(hwnd, param):
        if is_window_visible(hwnd):
            length = get_window_text_length(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            get_window_text(hwnd, buff, length + 1)
            titles.append(buff.value)
        return True

    enum_windows(enum_windows_process(foreach_window), 0)
    return titles
