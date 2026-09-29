import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)
led = 26
GPIO.setup(led,GPIO.OUT)
state = 0
light = 6
GPIO.setup(light,GPIO.IN)

try:
    while True:
        home=GPIO.input (light)
        GPIO.output(led, not home)
        time.sleep (0.2)
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()


