"""
@author: yangjj
@file: sent_serial.py
@time: 2021/11/1 12:13
@file_desc:
"""
# !/usr/bin/python
# -*-coding: utf-8 -*-

import serial
import threading
import binascii
from datetime import datetime
import struct
from message import message_CN


class SerialPort:
    def __init__(self, port, buand):
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
                # rec_str = decode(rec_str)
                # data_bytes = data_bytes + rec_str
                # print('当前数据接收总字节数：'+str(len(data_bytes))+' 本次接收字节数：'+str(len(rec_str)))
                # print(str(datetime.now()), ':', binascii.b2a_hex(rec_str))
                print(str(datetime.now()), ':', rec_str)


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
    # mSerial_IOT_sent = SerialPort(sentPort, baudRate)
    mSerial_IOT_recv = SerialPort(recvPort, baudRate)

    # # 文件写入操作
    # filename = input('请输入文件名：比如test.csv:')
    # dt = datetime.now()
    # nowtime_str = dt.strftime('%y-%m-%d %I-%M-%S')  # 时间
    # filename = nowtime_str + '_' + filename
    # out = open(filename, 'a+')
    # csv_writer = csv.writer(out)

    # 开始数据读取线程
    # t1 = threading.Thread(target=mSerial_IOT_sent.read_data)
    t2 = threading.Thread(target=mSerial_IOT_recv.read_data)

    # t1.setDaemon(True)
    t2.setDaemon(True)

    # t1.start()
    t2.start()

    while not is_exit:
        # 主线程:对读取的串口数据进行处理
        data_len = len(data_bytes)
        i = 0
        while (i < data_len - 1):
            if (data_bytes[i] == 0xFF and data_bytes[i + 1] == 0x5A):
                frame_code = data_bytes[i + 2]
                frame_len = struct.unpack('<H', data_bytes[i + 4:i + 6])[0]
                frame_time = struct.unpack('<I', data_bytes[i + 6:i + 10])[0]
                print('帧类型：', frame_code, '帧长度：', frame_len, '时间戳：', frame_time)
                print(frame_code, frame_len, frame_time)
                if frame_code == 0x03:  # 判断帧类型
                    # struct 解析数据帧
                    accelerated_x, accelerated_y, accelerated_z, angular_x, angular_y, angular_z, tem, speed_x, speed_y, speed_z, \
                    angular_v_x, angular_v_y, angular_v_z = struct.unpack('<fffffffffffff',
                                                                          data_bytes[i + 12:i + 12 + frame_len - 6])
                    dt = datetime.now()
                    nowtime_str = dt.strftime('%y-%m-%d %I:%M:%S')  # 时间
                    loc_str = [nowtime_str, frame_time, accelerated_x, accelerated_y, accelerated_z, angular_x,
                               angular_y, angular_z, tem, speed_x, speed_y, speed_z, \
                               angular_v_x, angular_v_y, angular_v_z]
                    print(loc_str)

                    # # 写入csv文件
                    # try:
                    #     csv_writer.writerow(loc_str)
                    # except Exception as e:
                    #     raise e
                i = i + 6 + frame_len + 3
            else:
                i = i + 1
        data_bytes[0:i] = b''
