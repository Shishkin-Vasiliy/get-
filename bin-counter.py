import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0) 

up = 5    
down = 6 

GPIO.setup(up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(down, GPIO.IN, pull_up_down=GPIO.PUD_UP)

num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

try:
    while True:
        up_pressed = not GPIO.input(up)
        down_pressed = not GPIO.input(down)

        if up_pressed and down_pressed:
            num = 255
        elif up_pressed and not down_pressed:
            num += 1
        elif down_pressed and not up_pressed:
            num -= 1

        if num > 255 or num < 0:
            num = 0
            if up_pressed or down_pressed:
                print('Выход за границы байта! Число сброшено в 0.')    
        
        GPIO.output(leds, dec2bin(num))
        time.sleep(0.05)

finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()