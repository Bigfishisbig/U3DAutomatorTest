#!/usr/bin/env python
# coding=utf-8
"""
文件名称：server.py
作者：ycy
版本：PPTPro
创建时间：2019/2/28 16:38
修改时间：
软件：PyCharm
"""
from SimpleXMLRPCServer import SimpleXMLRPCServer
import sys

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class Server:
    def add(x, y):
        #print "RPC Test"
        return x + y

    if __name__ == '__main__':
        s = SimpleXMLRPCServer(('', 8080))
        s.register_function(add, 'add')
        s.serve_forever()
