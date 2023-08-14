#################################################################
# 五线四相步进电机
#################################################################

from machine import Pin
import time


class ControlStepperMotor:
    switch_stat = False
    init_stat = (0, 0, 0, 0)

    def __init__(self, north_pin_serial=15, south_pin_serial=2, east_pin_serial=4, west_pin_serial=16, delay_time_ms=2):
        self.north_pin = Pin(north_pin_serial, Pin.OUT)
        self.south_pin = Pin(south_pin_serial, Pin.OUT)
        self.east_pin = Pin(east_pin_serial, Pin.OUT)
        self.west_pin = Pin(west_pin_serial, Pin.OUT)
        self.delay_time_ms = delay_time_ms
        self.north_pin.value(self.init_stat[0])
        self.south_pin.value(self.init_stat[1])
        self.east_pin.value(self.init_stat[2])
        self.west_pin.value(self.init_stat[3])

    def start(self):
        self.switch_stat = True
        while self.switch_stat:
            self.north_pin.value(1)
            self.south_pin.value(0)
            self.east_pin.value(0)
            self.west_pin.value(0)
            time.sleep_ms(self.delay_time_ms)

            self.north_pin.value(0)
            self.south_pin.value(1)
            self.east_pin.value(0)
            self.west_pin.value(0)
            time.sleep_ms(self.delay_time_ms)

            self.north_pin.value(0)
            self.south_pin.value(0)
            self.east_pin.value(1)
            self.west_pin.value(0)
            time.sleep_ms(self.delay_time_ms)

            self.north_pin.value(0)
            self.south_pin.value(0)
            self.east_pin.value(0)
            self.west_pin.value(1)
            time.sleep_ms(self.delay_time_ms)

    def stop(self):
        self.switch_stat = False

    def setDelayTimeMS(self, delay_time_ms):
        self.delay_time_ms = delay_time_ms
