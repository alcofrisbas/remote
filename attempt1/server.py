import multiprocessing
import queue
import time
import smbus
from gen.py import step

def Eightbit(q, bus, dev,reg):
    s1 = step()
    s2 = step()
    while True:
        try:
            item = q.get(False)
        except queue.Empty:
            pass

if __name__ == "__main__":
    g = step()
    for i in range(4):
        print(next(g))
    g.backward()
    for i in range(4):
        print(next(g))
