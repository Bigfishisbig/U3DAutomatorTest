import os
import platform
import socket
import uuid
from win32api import GetSystemMetrics
from main.object.enum import Platform, Environment
from main.utils.adb_handler import get_adb_handler

__author__ = "Junpeng Chen"
__all__ = ["get_device_info"]


class PCInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_mac():
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e + 2] for e in xrange(0, 11, 2)])

    @staticmethod
    def get_name():
        return socket.getfqdn(socket.gethostname())

    @staticmethod
    def get_id():
        return socket.gethostbyname(PCInfo.get_name())

    @staticmethod
    def get_version():
        return "%s-%s" % (platform.platform(), platform.architecture()[0])

    @staticmethod
    def get_screen():
        return "%dx%d" % (GetSystemMetrics(0), GetSystemMetrics(1))


class MobileInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_mac():
        return get_adb_handler().get_mac()

    @staticmethod
    def get_name():
        return get_adb_handler().get_name()

    @staticmethod
    def get_id():
        return get_adb_handler().deviceId

    @staticmethod
    def get_version():
        return get_adb_handler().get_version()

    @staticmethod
    def get_screen():
        return get_adb_handler().get_screen()


def get_device_info():
    if not get_device_info.instance:
        platform_name = os.getenv(Environment.PLATFORM)
        if platform_name == Platform.Windows:
            get_device_info.instance = PCInfo
        elif platform_name == Platform.Android:
            get_device_info.instance = MobileInfo
        else:
            get_device_info.instance = PCInfo
    return get_device_info.instance


get_device_info.instance = None
