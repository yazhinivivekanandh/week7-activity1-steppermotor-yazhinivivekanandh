from machine import Pin
import time

my_list = [[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]]

in1 = Pin(5, Pin.OUT)
in2 = Pin(18, Pin.OUT)
in3 = Pin(19, Pin.OUT)
in4 = Pin(21, Pin.OUT)

#full step using lists
while True:
    for i in my_list:
        print (i)
        in1.value(i[0])
        in2.value(i[1])
        in3.value(i[2])
        in4.value(i[3])
        time.sleep_ms(5)
