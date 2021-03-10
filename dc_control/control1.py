import RPi.GPIO as GPIO
import time
a_pins = [14,15]
b_pins = [20,21]
GPIO.setmode(GPIO.BCM)
GPIO.setup([*a_pins,*b_pins],GPIO.OUT)

def spin1(sec):
    GPIO.output(14,True)
    GPIO.output(15,False)
    time.sleep(sec)
def spin2(sec):
    GPIO.output(15,True)
    GPIO.output(14,False)
    time.sleep(sec)


spin1(3)
spin2(3)
GPIO.cleanup()
