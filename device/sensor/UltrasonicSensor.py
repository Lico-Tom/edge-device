##################################################################################
# 超声波测量距离
##################################################################################

from machine import Pin
import time


class UltrasonicSensor:

    def __init__(self, pin_trig_serial, pin_echo_serial):
        self.value = None
        self.ultrasonic_sensor_stat = False
        self.trig = Pin(pin_trig_serial, Pin.OUT)
        self.echo = Pin(pin_echo_serial, Pin.IN)
        self.trig.value(0)
        self.echo.value(0)

    def measure(self):
        # 告诉芯片要开始测试
        global t1, t2
        self.trig.value(1)
        time.sleep_us(10)
        self.trig.value(0)

        # 检测回响信号，为低电平时，测距完成
        while self.echo.value() == 0:
            # 开始不断递增的微妙计数器 1
            t1 = time.ticks_us()
        print("----------------------------")
        print(t1)
        # 检测回响信号，为高电平时，测距开始
        while self.echo.value() == 1:
            # 开始不断递增的微妙计数器 2
            t2 = time.ticks_us()
        print(t2)
        # 计算两次调用 ticks_ms(), ticks_us(), 或 ticks_cpu()之间的时间，这里是ticks_us()
        # 这时间差就是测距总时间，在乘声音的传播速度340米/秒，除2就是距离
        # 例如 t2-t1=12848此时单位是us，转换为秒就是12848 / 1000000 此时单位是秒，此时如果乘以340计算出的单位是米，
        # 然后再乘以100就是厘米，因此，直接 用12848/10000即可
        t3 = time.ticks_diff(t2, t1) / 10000
        print(t3, t2 - t1)

        # 返回：开始测距的时间减测距完成的时间*声音的速度/2
        return t3 * 340 / 2

    def start(self):
        self.ultrasonic_sensor_stat = True
        while self.ultrasonic_sensor_stat:
            self.value = self.measure()

    def stop(self):
        self.ultrasonic_sensor_stat = False
