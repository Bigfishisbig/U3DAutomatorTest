#!/usr/bin/env python
# coding=utf-8
"""
文件名称：server2.py
作者：ycy
版本：PPTPro
创建时间：2019/3/19 17:40
修改时间：
软件：PyCharm
"""
import pickle
from multiprocessing.connection import Listener
from threading import Thread


class RPCHandler:
    def __init__(self):
        self._functions = {}

    def register_function(self, func):
        self._functions[func.__name__] = func

    def handle_connection(self, connection):
        try:
            while True:
                # Receive a message
                func_name, args, kwargs = pickle.loads(connection.recv())
                # Run the RPC and send a response
                try:
                    r = self._functions[func_name](*args, **kwargs)
                    connection.send(pickle.dumps(r))
                except Exception as e:
                    connection.send(pickle.dumps(e))
        except EOFError:
            pass


def rpc_server(handler, address, authkey):
    sock = Listener(address, authkey=authkey)
    while True:
        client = sock.accept()
        t = Thread(target=handler.handle_connection, args=(client,))
        t.daemon = True
        t.start()


# Some remote functions
def add(x, y):
    return x + y


def sub(x, y):
    return x - y


# Register with a handler
handler = RPCHandler()
handler.register_function(add)
handler.register_function(sub)

# Run the server
rpc_server(handler, ('172.18.62.138', 8080), authkey='ycy')
