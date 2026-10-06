import RPi.GPIO as GPIO
import time 
class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode (GPIO.BCM)
        GPIO.setup (self.gpio_bits, GPIO.OUT, initial = 0)
    def deinit (self):
        GPIO.output (self.gpio_bits, 0)
        GPIO.cleanup()
        if self.verbose:
            print ("свет выключен, дверь закрыта")
    def set_number (self, number):
        number = max (0, min (255, int (number)))
        binary_str = '{:08b}' .format (number)
        for i, bit in enumerate (binary_str):
            GPIO.output (self.gpio_bits [i], int (bit))
        if self.verbose:
            print (f"Число: {number:3d} | Двоичный код: {binary_str}")
    def set_voltage (self, voltage):
        voltage = max (0.0, min (self.dynamic_range, voltage))
        number = int((voltage / self.dynamic_range)*255)
        self.set_number (number)
if __name__ == "__main__":
    dac = R2R_DAC ([16,20,21,25,26,17,17,22], 3.156, True)
    try:
        while True:
            try:
                voltage_str = input ("Введите напряжение в вольтах:")
                if voltage_str.lower()=='q':
                    break
                voltage = float (voltage_str)
                dac.set_voltage (voltage)
            except ValueError:
                print ("Вы ввели не число")
    finally:
        dac.deinit ()
        print("дверь закрыта, свет выключен")