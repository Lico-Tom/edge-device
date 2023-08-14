############################################################################
# 彩色RGB灯珠
############################################################################

from machine import Pin, PWM
import time


class RGBLamp:
    RGBLamp_stat = False

    def __init__(self, pin_r_serial, pin_b_serial, pin_g_serial):
        # 创建引脚对象
        led_r = Pin(pin_r_serial, Pin.OUT)
        led_b = Pin(pin_b_serial, Pin.OUT)
        led_g = Pin(pin_g_serial, Pin.OUT)

        # 创建PWM对象
        pwm_led_r = PWM(led_r)
        pwm_led_r.freq(1000)
        # 占空比如果设置为1023可以理解为全部是高电平，0表示全部是低电平，又因为对应LED引脚输出00即低电平才量，所以要用1023减去
        # pwm_led_r.duty_ns(1023 - int(255 / 255 * 1023))

        pwm_led_b = PWM(led_b)
        pwm_led_b.freq(1000)
        # pwm_led_b.duty_ns(1023 - int(70 / 255 * 1023))

        pwm_led_g = PWM(led_g)
        pwm_led_g.freq(1000)
        # pwm_led_g.duty_ns(1023 - int(206 / 255 * 1023))

        time.sleep(1)

        pwm_led_r.duty_ns(1023)
        pwm_led_g.duty_ns(1023)
        pwm_led_b.duty_ns(1023)

        self.leds = (pwm_led_r, pwm_led_b, pwm_led_g)

    def start(self):
        self.RGBLamp_stat = True
        while self.RGBLamp_stat:
            for led_pwm_obj in self.leds:
                for i in range(1023, -1, -1):
                    led_pwm_obj.duty_ns(i)
                    time.sleep_ms(1)
                for i in range(1024):
                    led_pwm_obj.duty_ns(i)
                    time.sleep_ms(1)
                led_pwm_obj.duty_ns(1023)

    def stop(self):
        self.RGBLamp_stat = False
