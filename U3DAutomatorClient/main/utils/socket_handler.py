# -*- coding: UTF-8 -*-

import json
import socket
import struct
import threading
import time
from main.log.logger import get_logger

__author__ = "Junpeng Chen"

mutex = threading.Lock() # 创建锁
class SocketHandler:
    """
        socket客户端
    """

    def __init__(self, host='localhost', port=43690):
        self.__host = host
        self.__port = port
        self.__socket = None
        if not self.__host or not self.__port or self.__port >= 65535:
            raise EnvironmentError("SocketHandler host or port error!")

    @property
    def get_socket(self):
        if self.__socket is None:
            self.connect()
        return self.__socket

    def connect(self):
        get_logger().info("connect host : %s ,port : %d" % (self.__host, self.__port))
        for i in xrange(5):
            get_logger().info("try to connect server : %d" % i)
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            value = self.__socket.connect_ex((self.__host, self.__port))
            if value == 0:
                return
            time.sleep(1)
        raise Exception("socket error")

    def shutdown(self):
        if self.__socket:
            self.__socket.shutdown(2)

    def _send_request(self, data):
        """
            发送数据
        :param data:
        :return:
        """
        try:
            serialized = json.dumps(data, ensure_ascii=False)
            # print "serialized", serialized
        except (TypeError, ValueError):
            raise Exception('You can only send JSON-serializable data')

        length = len(serialized)
        buff = struct.pack("i", length)
        self.get_socket.send(buff)
        get_logger().info("send cmd : %s" % serialized)
        send_size = self.get_socket.send(serialized)
        if length != send_size:
            raise Exception("send size error:length=%d , send_size=%d" % (length, send_size))

    def _receive_response(self):
        """
            接收数据
        :return:
        """
        length_buffer = self.get_socket.recv(4)
        if length_buffer:
            total = struct.unpack_from("i", length_buffer)[0]
        else:
            raise Exception('receive length is None?')
        view = memoryview(bytearray(total))
        next_offset = 0
        while total - next_offset > 0:
            receive_size = self.get_socket.recv_into(view[next_offset:], total - next_offset)
            next_offset += receive_size
        try:
            deserialized = json.loads(view.tobytes())
            get_logger().info("receive response : %s" % deserialized)
        except (TypeError, ValueError):
            raise Exception('Data received was not in JSON format')
        if deserialized['ResponseStatus'] != 0:
            raise Exception(
                "ResponseStatus: " + str(deserialized['ResponseStatus']) + ", Obj: " + str(deserialized['Obj']))
        return deserialized['Obj']

    def send_command(self, cmd, params=None, timeout=30):
        """
            发送命令
        :param cmd:
        :param params:
        :param timeout:
        :return:
        """
        if params and not (
                            isinstance(params, dict) or isinstance(params, list) or isinstance(params,
                                                                                               str) or isinstance(
                    params, unicode)):
            raise Exception('Params should be dict')
        if not params:
            params = ""
        mutex.acquire(10) # 可以加等待时间，不加就一直等待（堵塞）
        command = dict()
        command["Cmd"] = cmd
        command["Json"] = str(params)
        try:
            for retry in range(2):
                try:
                    self.get_socket.settimeout(timeout)
                    self._send_request(command)
                    return self._receive_response()
                except socket.timeout:
                    self.shutdown()
                    time.sleep(10)
                    self.connect()
                    raise Exception("Received Data From SDK timeout")
                except socket.error as e:
                    get_logger().info("Retry...%d" % e.errno)
                    self.shutdown()
                    time.sleep(10)
                    self.connect()
                    continue
                except Exception as e:
                    raise e
            raise Exception('Socket Error')
        finally:
            mutex.release()
