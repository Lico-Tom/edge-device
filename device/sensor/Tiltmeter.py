############################################################################
# 倾斜传感器
############################################################################
from machine import Pin


class Tiltmeter:
    def __init__(self, pin_serial=13):
        self.pin = Pin(pin_serial, Pin.IN)

    def value(self):
        return self.pin.value()
