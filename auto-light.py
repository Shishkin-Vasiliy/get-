import RPIO.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
sensor = 6

GPIO.setup(led, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN) 

while True:
    state = GPIO.input(sensor)  # 1 - светло, 0 - темно
    GPIO.output(led, not state)  # темно - led on (инвертируем)
    time.sleep(0.1)