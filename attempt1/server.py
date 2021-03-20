import multiprocessing
import queue
import time
import smbus

def 8bit(q, bus):
    while True:
        try:
            item = q.get(False)
        except queue.Empty:
            pass
