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

    def deinit(self): #Деструктор: останавливает ШИМ, сбрасывает настройки GPIO.
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
    def generate_triangle(self, frequency=1.0, steps=100):
        # генерация треугольного сигнала; frequency - частота - кол-во полных треугольников в секунду; steps - количество шагов на одну половину треугольника. 
        if self.verbose:
            print ("Генерация треугольного сигнала с частотой {frequency} Гц")
            # Период одного полного треугольника 
            period = 1.0 / frequency
            # Time for one step
            step_delay = period / (steps * 2)
            try:
                while True:
                    for i in range(steps+1):
                        voltage = (i / steps) * self.dynamic_range
                        self.set_voltage(voltage)
                        time.sleep(step_delay)
                        for i in range(steps, -1, -1):
                            voltage = (i / steps) * self.dynamic_range
                            self.set_voltage(voltage)
                            time.sleep(step_delay)
            except KeyboardInterrupt:
                if self_verbose:
                    print ("Генерация остановлена!") 
if __name__ == "__main__":
    dac = PWM_DAC(12,5000,3.290,True)
    try:
        print("Change type")
        print ("type 1 - ручной ввод; type 2 - генерация треугольников")
        mode = input("Введите 1 или 2")
        if mode == "1":
           while True:
            try:
                
                voltage = float(input("Введите напряжение в вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print ("Не понял. По новой!\n")
        elif mode == "2":
            dac.generate_triangle(frequency=0.5, steps=100)
        else:
            print ("Неверный режим")
    except KeyboardInterrupt:
        print ("Программа завершена пользователем")
    finally:
        dac.deinit()
