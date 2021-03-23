import unittest
import server
import time
import multiprocessing
from server import Eightbit
import smbus
class ServerTest(unittest.TestCase):
    def test_test(self):
        self.assertEqual(4,4)

    def test_8bit1(self):
        q0 = multiprocessing.Queue()
        bus = smbus.SMBus(1)
        dev = 0x20
        ioA = 0x00
        ioB = 0x01

        olA = 0x14
        olB = 0x15

        
        bus.write_byte_data(dev, ioA, 0x00)
        bus.write_byte_data(dev, ioB, 0x00)

        bus.write_byte_data(dev, olA, 0x00)
        bus.write_byte_data(dev, olA, 0x00)
        
        p1 = multiprocessing.Process(target=Eightbit, args=(q0,bus,0x20,0x14,0.002,))
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


        bus.write_byte_data(dev, olA, 0x00)
        bus.write_byte_data(dev, olA, 0x00)

    
if __name__ == "__main__":
    unittest.main()
