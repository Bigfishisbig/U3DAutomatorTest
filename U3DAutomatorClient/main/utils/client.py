#!/usr/bin/env python
# coding=utf-8
"""
文件名称：client.py
作者：ycy
版本：PPTPro
创建时间：2019/3/19 16:41
修改时间：
软件：PyCharm
"""
from xmlrpclib import ServerProxy

if __name__ == '__main__':
    s = ServerProxy("http://127.0.0.1:8080")
    print s.add(3, 4)