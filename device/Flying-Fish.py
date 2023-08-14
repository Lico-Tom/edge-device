from machine import Pin, ADC
import time

# 模拟量
anlogPin = ADC(Pin(33))
anlogPin.atten(ADC.ATTN_11DB)  # 配置测量量程为3.3v

# 数字量
digitalPin = Pin(15, Pin.IN)

while True:
    print(anlogPin.read())
    print(digitalPin.value())
    time.sleep(0.1)
