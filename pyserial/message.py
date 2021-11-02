message = {'+EVENT=CON_ON': 'STA 成功连接到路由器 ',
           '+EVENT=CON_OFF': 'STA 断开路由器或者未连接到路由器 ',
           '+EVENT=DHCP_OK': 'STA DHCP获取到IP',
           '+EVENT=SOCKA_ON': 'SOCKA连接建立(仅TCP Client/Server,MQTT,HTTP)',
           '+EVENT=SOCKA_OFF': 'SOCKA连接断开(仅TCP Client/Server,MQTT,HTTP)',
           '+EVENT=SOCKB_ON': 'SOCKB连接建立(仅TCP Client)',
           '+EVENT=SOCKB_OFF': 'SOCKB连接断开(仅TCP Client)',
           'AT+CMDPW': '设置/查询透传模式下发送 AT 命令的前导字符',
           'AT+EVENT': '设置/查询透传模式下事件通知功能',
           'AT+NETPIDEN': '设置/查询是否显示数据来自哪个通讯通道',
           'AT+NETPID': '设置/查询通讯通道号标记值',
           'AT+NETP': '设置/查询 SOCKA 网络协议参数',
           'AT+SOCKB': '设置/查询 SOCKB 网络协议参数',
           'AT+WMODE': '设置/查询 Wi-Fi 操作模式',
           'AT+WSMAC': '设置/查询模块的 MAC 地址参数',
           'AT+WSSSID': '设置/查询关联 AP 的SSID',
           'AT+WSKEY': '设置/查询 STA 的加密参数',
           'AT+WAP': '设置/查询 AP 的 Wi-Fi 配置参数',
           'AT+WANN': '设置/查询 STA 的网络参数',
           'AT+TCPDISB=on': '建立 SOCKB 链接',
           'AT+TCPDISB=off': '断开 SOCKB 链接',
           'AT+TCPDISB': '建立/断开 SOCKB 链接'}


def message_CN(rec_str):
    for i in message.keys():
        if i in rec_str:
            rec_str = message.get(i)
            break
    if rec_str == '#&B':
        rec_str = '心跳包'
    return rec_str
