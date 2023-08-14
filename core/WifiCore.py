import time

wifiUser = '702'
wifiPwd = 'Hao@060802'


def do_connectWifi():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network....')
        wlan.connect(wifiUser, wifiPwd)
        while not wlan.isconnected():
            time.sleep(5)
            wlan.connect(wifiUser, wifiPwd)
        print('network config', wlan.config())


do_connectWifi()
