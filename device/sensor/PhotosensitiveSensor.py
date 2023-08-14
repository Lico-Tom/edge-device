############################################################################
# 光敏传感器
############################################################################
from machine import Pin, ADC


class PhotosensitiveSensor:
    def __init__(self, adc_pin_serial, number_pin_serial):
        # 模拟量
        ps2_y = ADC(Pin(adc_pin_serial))
        ps2_y.atten(ADC.ATTN_11DB)  # 这里配置测量量程为3.3V

        pin = Pin(number_pin_serial, Pin.IN)

        while True:
            self.val_y = ps2_y.read_u16()
            self.light = pin.value()

    def value(self):
        return self.val_y, self.light
