"""
@author: yangjj
@file: sent_serial.py
@time: 2021/11/1 12:13
@file_desc:
"""
# !/usr/bin/python
# -*-coding: utf-8 -*-
from time import sleep

import serial
import threading
import binascii
from datetime import datetime
from message import message_CN


class SerialPort:
    def __init__(self, port, buand, type):
        self.type = type
        self.port = serial.Serial(port, buand)
        self.port.close()
        if not self.port.isOpen():
            self.port.open()

    def port_open(self):
        if not self.port.isOpen():
            self.port.open()

    def port_close(self):
        self.port.close()

    def send_data(self):
        self.port.write('')

    def read_data(self):
        global is_exit
        global data_bytes
        while not is_exit:
            count = self.port.inWaiting()
            if count > 0:
                rec_str = self.port.read(count)
                rec_str = binascii.b2a_hex(rec_str)
                rec_str = decode(rec_str)
                rec_str = message_CN(rec_str)
                if self.type == '发送串口 指令':
                    print(str(datetime.now()), ':', "\033[31;1m" + self.type + "\033[0m", rec_str)
                elif self.type == '接收串口 指令':
                    print(str(datetime.now()), ':', "\033[32;1m" + self.type + "\033[0m", rec_str)
                sleep(0.02)


def hex_list():
    test = []
    i = 0
    while i <= 255:
        data_hex = hex(i)
        if len(data_hex) < 4:
            data_replace = data_hex[0:2] + '0' + data_hex[2]
            data_replace = data_replace.lstrip('0')
        else:
            data_replace = data_hex.lstrip('0')
        test.append(data_replace)
        i += 1
    return test


def decode(data):
    data_str = str(binascii.a2b_hex(data))
    for x in hex_list():
        data_str = data_str.replace('b\'', ''). \
            replace('\'', '').replace('\\n', ''). \
            replace('\\r', '').replace('\\' + x, '')
    return data_str


sentPort = 'COM6'  # 串口
recvPort = 'COM3'  # 串口
baudRate = 115200  # 波特率
is_exit = False
data_bytes = bytearray()

if __name__ == '__main__':
    # 打开串口
    mSerial_IOT_sent = SerialPort(sentPort, baudRate, '发送串口 指令')
    mSerial_IOT_recv = SerialPort(recvPort, baudRate, '接收串口 指令')

    # 开始数据读取线程
    t1 = threading.Thread(target=mSerial_IOT_sent.read_data, name='IOT SENT')
    t2 = threading.Thread(target=mSerial_IOT_recv.read_data, name='IOT RECV')

    # t1.setDaemon(True)
    # t2.setDaemon(True)

    t1.start()
    t2.start()
