#! /usr/bin/env python
# coding=utf-8
import logging
import logging.config
import time
import os
import sys

from main.object.enum import Environment, Platform
from main.utils.path import get_root_path

__author__ = "Junpeng Chen"
__all__ = ["get_logger"]
log_format = logging.Formatter("[ %(asctime)s  %(levelname)s/%(name)s ] at %(filename)s(%(lineno)s) : %(message)s")


#  多进程使用logging写同一个文件，会出现安全异常，采用以下配置文件，可解决，待验证
# logging.config.dictConfig({
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#         'verbose': {
#             'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#             'datefmt': "%Y-%m-%d %H:%M:%S"
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'null': {
#             'level': 'DEBUG',
#             'class': 'logging.NullHandler',
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose'
#         },
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.RotatingFileHandler',
#             # 当达到10MB时分割日志
#             'maxBytes': 1024 * 1024 * 10,
#             # 最多保留50份文件
#             'backupCount': 50,
#             # If delay is true,
#             # then file opening is deferred until the first call to emit().
#             'delay': True,
#             'filename': 'logs/mysite.log',
#             'formatter': 'verbose'
#         }
#     },
#     'loggers': {
#         '': {
#             'handlers': ['file'],
#             'level': 'info',
#         },
#     }
# })

def get_logger():
    if not get_logger.instance:
        platform = os.getenv(Environment.PLATFORM)
        logfile_name = time.strftime("%Y-%m-%d.log", time.localtime())
        device_id = os.getenv(Environment.DEVICE_ID)

        if not platform:
            log_path = get_root_path("log", logfile_name)
            log_name = None
        elif platform == Platform.Android and device_id:
            log_path = get_root_path("log", platform, device_id, logfile_name)
            log_name = device_id
        else:
            log_path = get_root_path("log", platform, logfile_name)
            log_name = platform

        get_logger.instance = logging.getLogger(log_name)

        # 文件日志
        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(log_format)
        get_logger.instance.addHandler(file_handler)

        # 控制台日志
        # console_handler = logging.StreamHandler(sys.stdout)
        # console_handler.setFormatter(log_format)
        # logging.getLogger('').addHandler(console_handler)

        # 指定日志的最低输出级别，默认为WARN级别
        get_logger.instance.setLevel(logging.INFO)
    return get_logger.instance


get_logger.instance = None

"""
#log Decorator
def currentframe():
    try:
        raise Exception
    except:
        return sys.exc_info()[2].tb_frame.f_backs


_srcfile = os.path.normcase(currentframe.__code__.co_filename)
if hasattr(sys, '_getframe'): currentframe = lambda: sys._getframe(3)
logging.currentframe = currentframe
logging._srcfile = _srcfile


def log_info(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_list = []
        names = inspect.getargspec(func).args
        args_list.extend(["%s = %s" % (names[i], args[i]) for i in xrange(len(args))])
        args_list.extend(["%s = %s" % (k, v) for k, v in kwargs.items()])
        get_logger().info("%s >>> %s " % (func.__name__, ", ".join(args_list)))
        return func(*args, **kwargs)

    return wrapper
"""
