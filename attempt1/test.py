import unittest
import server
import time
import multiprocessing
from server import Eightbit

class ServerTest(unittest.TestCase):
    def test_test(self):
        self.assertEqual(4,4)

    def test_8bit1(self):
        q0 = multiprocessing.Queue()
        bus = 4
        p1 = multiprocessing.Process(target=Eightbit, args=(q0,bus,0x20,0x14,0.2,))
        p1.start()
        time.sleep(1)
        q0.put(0b100)
        time.sleep(1)
        q0.put(0b000)
        time.sleep(1)
        q0.put(0b101)
        time.sleep(1)
        q0.put(0b001)
        time.sleep(1)
        p1.terminate()
if __name__ == "__main__":
    unittest.main()
