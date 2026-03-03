import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)

        self.pwm = GPIO.PWM(self.gpio_pin, pwm_frequency)
        self.pwm.start(0)

    def deinit(self):
        self.pwm.stop()                          # завершает работу pwm
        GPIO.cleanup(self.gpio_pin)
        if self.verbose:
            print('GPIO cleaned up')

    def set_number(self, number):
        duty_cycle = (number / 255) * 100        # устанавливает частоту в процентах 
        self.pwm.ChangeDutyCycle(duty_cycle)

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f'Напряжение выходит за динамический диапазон ЦАП (0.0 - {self.dynamic_range:.2f}B)')
            print('Устанавливаем 0.0 В')
            voltage = 0.0
        number = int((voltage / self.dynamic_range) * 255)
 
        self.set_number(number)    

if __name__ == '__main__':
    try:
        dac = PWM_DAC(12, 500, 3.290, True)
        
        while True:
            try:
                voltage = float(input('Введите напряжение в вольтах:'))

                dac.set_voltage(voltage)

            except ValueError:
                print('Вы ввели не число. Попробуйте еще раз\n')
    finally:
        dac.deinit()
