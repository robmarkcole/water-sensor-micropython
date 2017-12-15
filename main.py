import time
import machine

# Moisture sensor
adc = machine.ADC()
apin = adc.channel(pin='P16', attn=3)


# Function for taking average of 100 readings
def smooth_reading():
    avg = 0
    _AVG_NUM = 100
    for _ in range(_AVG_NUM):
        avg += apin()
    avg /= _AVG_NUM
    return(avg)


while True:
    _THRESHOLD = 3000
    analog_val = smooth_reading()
    print(analog_val)
    if analog_val < _THRESHOLD:
        print("Water detected!")
    time.sleep(1)
