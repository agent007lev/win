import RPi.GPIO as GPIO
import time 
dac_pins = [16,20,21,25,26,17,27,22]
dynamic_range = 3.3
def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in dac_pins:
        GPIO.setup(pin, GPIO.)