CON_ON = '+EVENT=CON_ON'
CON_ON_MESSAGE = 'STA 成功连接到路由器 '

CON_OFF = '+EVENT=CON_OFF'
CON_OFF_MESSAGE = 'STA 断开路由器或者未连接到路由器 '

DHCP_OK = '+EVENT=DHCP_OK'
DHCP_OK_MESSAGE = 'STA DHCP获取到IP'

SOCKA_ON = '+EVENT=SOCKA_ON'
SOCKA_ON_MESSAGE = 'SOCKA连接建立(仅TCP Client/Server,MQTT,HTTP)'

SOCKA_OFF = '+EVENT=SOCKA_OFF'
SOCKA_OFF_MESSAGE = 'SOCKA连接断开(仅TCP Client/Server,MQTT,HTTP)'

SOCKB_ON = '+EVENT=SOCKB_ON'
SOCKB_ON_MESSAGE = 'SOCKB连接建立(仅TCP Client)'

SOCKB_OFF = '+EVENT=SOCKB_OFF'
SOCKB_OFF_MESSAGE = 'SOCKB连接断开(仅TCP Client)'


def message_CN(rec_str):
    if CON_ON in rec_str:
        rec_str = CON_ON_MESSAGE
    elif CON_OFF in rec_str:
        rec_str = CON_OFF_MESSAGE
    elif DHCP_OK in rec_str:
        rec_str = DHCP_OK_MESSAGE
    elif SOCKA_ON in rec_str:
        rec_str = SOCKA_ON_MESSAGE
    elif SOCKA_OFF in rec_str:
        rec_str = SOCKA_OFF_MESSAGE
    elif SOCKB_ON in rec_str:
        rec_str = SOCKB_ON_MESSAGE
    elif SOCKB_OFF in rec_str:
        rec_str = SOCKB_OFF_MESSAGE
    return rec_str
