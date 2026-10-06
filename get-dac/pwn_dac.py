import RPi.GPIO as GPIO
import time 
class PWM_DAC:
    def __init__(self, gpio_pin, pwn_frequency, dynamic_range, verbose = False): # init - конструктор
        self.gpio_pin = gpio_pin # self указывает на конкретный объект внутри класса
        self.pwm_frequency = pwn_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0) # ШИМ с нулевой скважностью
        if self.verbose:
            print ("ШИМ инициализирован на пине {self.gpio_pin} с частотой {self_frequency}, Гц")

    def deinit(self):
        self.pwm.stop() # остановка генерации импульсов 
        GPIO.output(self.gpio_pin,0) 
        GPIO.cleanup()

        if self.verbose:
            print ("Дверь закрыта, свет выключен")
    def set_voltage(self,voltage):
        voltage = max(0.0, min(self.dynamic_range,voltage))
        duty_cycle = (voltage / self.dynamic_range) * 100.0 # перевод напряжения в скважность
        self.pwm.ChangeDutyCycle(duty_cycle) # установка скважности
        if self.verbose:
            print (f"Напряжение: {voltage: .2f} B | Скважность: {duty_cycle: .2f}%")
if __name__ == "__main__":
    dac = PWM_DAC(12,5000,3.290,True)
    try:
        while True:
            try:
                
                voltage = float(input("Введите напряжение в вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print ("Не понял. По новой!\n")
    finally:
        dac.deinit()
