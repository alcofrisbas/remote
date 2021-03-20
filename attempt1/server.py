import multiprocessing
import queue
import time
import smbus
from gen import step

def Eightbit(q, bus, dev,reg,delay):
    """
    3bit protocol for now:
    0: Motor Select
    1: Direction Select
    2: Power Select
    """
    s0 = step()
    s1 = step()
    run0 = False
    run1 = False
    out0 = 0b0000
    out1 = 0b0000
    while True:
        # blank 8bit message
        send = 0x00

        try:
            item = q.get(False)
            stat_set = item >> 2
            backward = False
            run = False
            if 0b010 & item:
                backward = True
            if 0b100 & item:
                run = True
            if 0b001 & item:
                s1.direction(backward)
                run1 = run
            else:
                s0.direction(backward)
                run0 = run
        except queue.Empty:
            pass
        data = 0x00
        if run0:
            out0 = next(s0)
        if run1:
            out1 = next(s1) << 4
        data = out0 + out1
        print("{0:08b}".format(data))
        time.sleep(delay)
