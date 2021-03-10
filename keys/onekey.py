import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
out_scan = [14,15]
in_scan  = [20,21]
GPIO.setup(out_scan, GPIO.OUT)
GPIO.setup(in_scan,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def scan(out_pins, in_pins):
    hits = []
    for o ,oPin, in enumerate(out_pins):
        GPIO.output(oPin, GPIO.HIGH)
        for i,iPin in enumerate(in_pins):
            if GPIO.input(iPin):
                hits.append((o,i))
        GPIO.output(oPin, GPIO.LOW)

    return hits


matrix = (("f","u"),("c","k"))
times = ((0,0,),(0,0))
up_down = [[0,0],[0,0]]
try:
    while True:
        hits = scan(out_scan, in_scan)

        for hit in hits:
            print(matrix[hit[1]][hit[0]],end='')
            up_down[hit[1]][hit[0]] = 1
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
print()
