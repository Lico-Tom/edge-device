################################
#  呼吸灯
################################
from machine import Pin, PWM


def PWMLamp(pin_number, frequent, duty_number):
    pwm = PWM(Pin(pin_number))  # create PWM object from a pin
    freq = pwm.freq()  # get current frequency
    pwm.freq(frequent)  # set PWM frequent from 1HZ to 40MHZ
    duty = pwm.duty_ns()  # get current duty cycle, range 0-1023
    pwm.duty_ns(duty_number)  # set duty cycle from 0 to 1023 as a ratio duty/1023
