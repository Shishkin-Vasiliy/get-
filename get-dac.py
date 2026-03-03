import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pins = [16, 20, 21, 25, 26, 17, 27, 22]

GPIO.setup(pins, GPIO.OUT)

dynrange = 3.1

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynrange):
        print(f'Напряжение выходит за динамический диапазон ЦАП (0.0 - {dynrange:.2f}B)')
        print('Устанавливаем 0.0 В')
        return 0
    return int(voltage / dynrange * 255)

def number_to_dac(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while True:
        try:
            voltage = float(input('Введите напряжение в вольтах:'))
            number = voltage_to_number(voltage)
            GPIO.output(pins, number_to_dac(number))
            print(f"Установлено: {number}/255, расчетное напряжение: {(number/255)*dynrange:.3f} В")
        except ValueError:
            print('Вы ввели не число. Попробуйте еще раз\n')
finally:
    GPIO.output(pins, 0)
    GPIO.cleanup()                    