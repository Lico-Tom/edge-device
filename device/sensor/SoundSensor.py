################################################################################
# 声音传感器
################################################################################

import time
from machine import Pin, ADC


class SoundSensor:

    has_sound = False

    def __init__(self, sound_pin_serial):
        sound_analog = ADC(Pin(sound_pin_serial))
        sound_analog.atten(ADC.ATTN_11DB)  # 配置测量量程为3.3V
        # 数字量
        pin = Pin(sound_pin_serial, Pin.IN)
        pin.irq(trigger=Pin.IRQ_RISING, handler=self.sound_func)
        while True:
            self.sound_value = sound_analog.read_u16()
            time.sleep_ms(100)

    def value(self):
        return self.sound_value

    def sound_func(self, *argc):
        print("has sound.")
        self.has_sound = True
