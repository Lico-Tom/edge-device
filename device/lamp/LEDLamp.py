#############################################
#  LED灯
#############################################

import machine
import time


def LEDLamp(pin_number, sleep_second):
    pin = machine.Pin(pin_number, machine.Pin.OUT)
    while True:
        pin.value(1)  # pin2.on() 开
        time.sleep(sleep_second)
        pin.value(0)  # pin2.off() 关
        time.sleep(sleep_second)  # 睡眠一秒
