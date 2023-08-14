###################################################################################
# 震动报警器
###################################################################################
from machine import Pin


class VibrationAlarm:
    def __init__(self, pin_serial=13):  # 默认引脚13
        self.pin = Pin(pin_serial, Pin.IN)

    def value(self):
        self.pin.value()  # 读取传感器数据
