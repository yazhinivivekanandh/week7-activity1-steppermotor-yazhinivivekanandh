#Write your code here to run the stepper motor without using any loop

from machine import Pin
import time

in1 = Pin(5, Pin.OUT)
in2 = Pin(18, Pin.OUT)
in3 = Pin(19, Pin.OUT)
in4 = Pin(21, Pin.OUT)

#wave drive
while True:
    in1.value(1)
    in2.value(0)
    in3.value(0)
    in4.value(0)
    time.sleep_ms(5)
    
    in1.value(0)
    in2.value(1)
    in3.value(0)
    in4.value(0)
    time.sleep_ms(5)
    
    in1.value(0)
    in2.value(0)
    in3.value(1)
    in4.value(0)
    time.sleep_ms(5)
    
    in1.value(0)
    in2.value(0)
    in3.value(0)
    in4.value(1)
    time.sleep_ms(5)  
