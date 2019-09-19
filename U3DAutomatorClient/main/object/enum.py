__author__ = "Junpeng Chen"

from collections import namedtuple

"""
def enum_string(*keys):
    return namedtuple('enum_string', keys)(*keys)


def enum_auto_int(*keys):
    return namedtuple('enum_auto_int', keys)(*keys)


def enum(**kwargs):
    return namedtuple('Enum', kwargs.keys())(*kwargs.values())
"""

class Cmd():
    def __init__(self):
        pass

    Exit = 0

    DumpTree = 100
    GetVersion = 101
    GetFps = 102
    GetTrafficData = 103
    GetCurrentScene = 104
    GetMemory = 105
    GetCpu = 106
    GetPerformance = 107
    GetGpu = 108

    GetElementWorldBound = 200
    GetObjectField = 201
    GetTouchableElements = 202
    SetObjectField = 203  # S3 engine

    TouchEvents = 300
    SetInputText = 301
    TouchNotify = 302
    EnterRecord = 310
    LeaveRecord = 311

    FindElementByPos = 400
    FindElementPath = 401
    FindElements = 402

    GetRegisteredHandlers = 500
    CallRegisterHandler = 501

    CustomCommand = 600  # S3 engine


class Platform:
    def __init__(self):
        pass

    Windows = "windows"
    Android = "android"
    VR = "vr"
    S3Windows = "s3window"


class Environment:
    def __init__(self):
        pass

    HOST = "HOST"
    SERVER_PORT = "SERVER_PORT"
    ADB_PORT = "ADB_PORT"
    VERSION = "VERSION"
    PLATFORM = "PLATFORM"
    REPORT_MODEL = "REPORT_MODEL"
    MODULE = "MODULE"
    TEST_PATH = "TEST_PATH"
    WINDOWS_TITLE = "WINDOWS_TITLE"
    DEVICE_LIST = "DEVICE_LIST"
    DEVICE_ID = "DEVICE_ID"
    APK_PATH = "APK_PATH"
    PACKAGE = "PACKAGE"
    SRC_SCREEN_WIDTH = "SRC_SCREEN_WIDTH"
    SRC_SCREEN_HEIGHT = "SRC_SCREEN_HEIGHT"

    Result_id = "Result_id"
    IP = "IP"
    DataFlag = "DataFlag"
    StartTime = "StartTime"
    isTransSTAF = "isTransSTAF"
    XlsRow = "XlsRow"

class Version:
    def __init__(self):
        pass

    Debug = "debug"
    Release = "release"


class ReportModel:
    def __init__(self):
        pass

    Html = "html"
    Control = "control"


class KeyCode:
    def __init__(self):
        pass

    backspace = 'backspace'
    tab = 'tab'
    clear = 'clear'
    enter = 'enter'
    shift = 'shift'
    ctrl = 'ctrl'
    alt = 'alt'
    pause = 'pause'
    caps_lock = 'caps_lock'
    esc = 'esc'
    spacebar = 'spacebar'
    page_up = 'page_up'
    page_down = 'page_down'
    end = 'end'
    home = 'home'
    left_arrow = 'left_arrow'
    up_arrow = 'up_arrow'
    right_arrow = 'right_arrow'
    down_arrow = 'down_arrow'
    select = 'select'
    print_ = 'print'
    execute = 'execute'
    print_screen = 'print_screen'
    ins = 'ins'
    del_ = 'del'
    help = 'help'
    numpad_0 = 'numpad_0'
    numpad_1 = 'numpad_1'
    numpad_2 = 'numpad_2'
    numpad_3 = 'numpad_3'
    numpad_4 = 'numpad_4'
    numpad_5 = 'numpad_5'
    numpad_6 = 'numpad_6'
    numpad_7 = 'numpad_7'
    numpad_8 = 'numpad_8'
    numpad_9 = 'numpad_9'
    multiply_key = 'multiply_key'
    add_key = 'add_key'
    separator_key = 'separator_key'
    subtract_key = 'subtract_key'
    decimal_key = 'decimal_key'
    divide_key = 'divide_key'
    F1 = 'F1'
    F2 = 'F2'
    F3 = 'F3'
    F4 = 'F4'
    F5 = 'F5'
    F6 = 'F6'
    F7 = 'F7'
    F8 = 'F8'
    F9 = 'F9'
    F10 = 'F10'
    F11 = 'F11'
    F12 = 'F12'
    F13 = 'F13'
    F14 = 'F14'
    F15 = 'F15'
    F16 = 'F16'
    F17 = 'F17'
    F18 = 'F18'
    F19 = 'F19'
    F20 = 'F20'
    F21 = 'F21'
    F22 = 'F22'
    F23 = 'F23'
    F24 = 'F24'
    num_lock = 'num_lock'
    scroll_lock = 'scroll_lock'
    left_shift = 'left_shift'
    right_shift = 'right_shift '
    left_control = 'left_control'
    right_control = 'right_control'
    left_menu = 'left_menu'
    right_menu = 'right_menu'
    browser_back = 'browser_back'
    browser_forward = 'browser_forward'
    browser_refresh = 'browser_refresh'
    browser_stop = 'browser_stop'
    browser_search = 'browser_search'
    browser_favorites = 'browser_favorites'
    browser_start_and_home = 'browser_start_and_home'
    volume_mute = 'volume_mute'
    volume_Down = 'volume_Down'
    volume_up = 'volume_up'
    next_track = 'next_track'
    previous_track = 'previous_track'
    stop_media = 'stop_media'
    play_or_pause_media = 'play/pause_media'
    start_mail = 'start_mail'
    select_media = 'select_media'
    start_application_1 = 'start_application_1'
    start_application_2 = 'start_application_2'
    attn_key = 'attn_key'
    crsel_key = 'crsel_key'
    exsel_key = 'exsel_key'
    play_key = 'play_key'
    zoom_key = 'zoom_key'
    clear_key = 'clear_key'
