import RPi.GPIO as GPIO
import time 
dac_pins = [16,20,21,25,26,17,27,22]
dynamic_range = 3.156
def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in dac_pins:
        GPIO.setup(pin, GPIO.OUT)
def voltage_to_number (voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print (f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} B)")
        print ("Устанавливаем 0.0 В")
        return 0

    return int (voltage / dynamic_range * 255)
def number_to_dac (value):
    value = max(0, min (255, value))
    binary_str = '{:08b}' .format(value)
    for i, pin in enumerate (dac_pins):
        bit = int (binary_str [i])
        GPIO.output (pin, bit)
if __name__ == '__main__':
    setup ()
    try:
        while True:
            try:
                voltage = float (input ("Введите напряжение в Вольтах : "))
                number = voltage_to_number (voltage)
                number_to_dac (number)
                            
            except ValueError:
                print ("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        for pin in dac_pins:
            GPIO.output (pin, 0)
        GPIO.cleanup ()