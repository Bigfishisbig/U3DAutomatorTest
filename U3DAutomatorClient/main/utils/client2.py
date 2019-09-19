#!/usr/bin/env python
# coding=utf-8
"""
文件名称：client2.py
作者：ycy
版本：PPTPro
创建时间：2019/3/19 17:06
修改时间：
软件：PyCharm
"""
from xmlrpclib import ServerProxy
import pickle
from multiprocessing.connection import Client

class RPCProxy:
    def __init__(self, connection):
        self._connection = connection

    def __getattr__(self, name):
        def do_rpc(*args, **kwargs):
            self._connection.send(pickle.dumps((name, args, kwargs)))
            result = pickle.loads(self._connection.recv())
            if isinstance(result, Exception):
                raise result
            return result

        return do_rpc

c = Client(('172.18.62.138', 8080), authkey='ycy')
proxy = RPCProxy(c)
print proxy.add(3, 5)
print proxy.sub(5, 3)