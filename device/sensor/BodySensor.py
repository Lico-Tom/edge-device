#############################################################################
# 人体感应传感器(HC-SR501)
#############################################################################
from machine import Pin


class BodySensor:
    def __init__(self, pin_serial, fun):  # fun 回调函数
        pin = Pin(pin_serial, Pin.IN)
        pin.irq(fun, Pin.IRQ_RISING)
