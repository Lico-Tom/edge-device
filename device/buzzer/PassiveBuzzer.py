#################################################################
# 无源蜂鸣器
#################################################################

from machine import Pin
from machine import PWM
from time import sleep_ms

class PassiveBuzzer:
    def __init__(self, sig_pin):
        self.pwm = PWM(Pin(sig_pin, Pin.OUT))

    def pay(self, melodies, wait, duty):
        for note in melodies:
            print("note:{}".format(note))
            if note:
                self.pwm.freq(note)
            self.pwm.duty_ns(duty)
            sleep_ms(wait)
        self.pwm.duty_ns(0)  # 暂停PWM， 将占空比设置为0