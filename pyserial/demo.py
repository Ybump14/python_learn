"""
@author: yangjj
@file: demo.py
@time: 2021/11/2 20:04
@file_desc:
"""
import binascii
from datetime import datetime

from pyserial.message import message_CN
from pyserial.sent_serial import decode

data = b'23264230990200175055422f45503530302f323130313030303030313336390101100046007bf6000100640003000001f40000000000000000000000000000000000870000000000000000000000000000000114e90003004d00430000000114e900000000006403e802260320014d014d014d014d014d014d014d014d014d014b014d014d014d014d014d014d00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'


def modbus_decode(data):
    # 获取寄存器写入起始位
    data_start = data[0:4]
    data_start_register = int(data_start, 16)

    # 获取寄存器写入数量
    data_read_len = data[4:8]

    # 获取寄存器写入字节数
    data_read_len_bytes = data[8:10]
    data_read_len_bytes_len = int(data_read_len_bytes, 16)

    # modbus串
    data_modbus = data[10:10 + data_read_len_bytes_len]

    # 剩余数据
    data_last = data[data_read_len_bytes_len:]
    print(data_last)

    if data_start_register == 0:
        print(str(datetime.now()), ':', '上报基本数据',
              '010110' + data_start + data_read_len + data_read_len_bytes + data_modbus)
    elif data_start_register == 70:
        print(str(datetime.now()), ':', '上报附加数据',
              '010110' + data_start + data_read_len + data_read_len_bytes + data_modbus)
    elif data_start_register == 3000:
        print(str(datetime.now()), ':', '上报可读写数据',
              '010110' + data_start + data_read_len + data_read_len_bytes + data_modbus)


def data_split(data):
    str_data = str(data).replace('b\'', '').replace('\'', '')
    if "010110" in str_data:
        ascii = str_data.split('010110')[0]
        modbus = str_data.split('010110')[1]

        ascii = decode(ascii)
        ascii = message_CN(ascii)

        print(str(datetime.now()), ':', ascii)
        modbus_decode(modbus)

data_split(data)