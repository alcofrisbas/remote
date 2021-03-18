import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
out_scan = [14,15]
in_scan = [20,21]
GPIO.setup(out_scan, GPIO.OUT)
GPIO.setup(in_scan, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def scan(out_pins,in_pins):
    hits = []
    for o, oPin in enumerate(out_pins):
        GPIO.output(oPin,GPIO.HIGH)
        for i, iPin in enumerate(in_pins):
            if GPIO.input(iPin):
                hits.append((o,i))
        GPIO.output(oPin,GPIO.LOW)
    return hits
last = []
try:
    while True:
       
        hits = scan(out_scan, in_scan)
        for hit in hits:
            if hit not in last:
                print(f"KeyPressed: {hit}")
        for l in last:
            if l not in hits:
                print(f"KeyReleased: {l}")
        last = hits
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print()
