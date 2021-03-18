import smbus
import time

bus = smbus.SMBus(1)

DEVICE1 = 0x20

IODIRA  = 0x00
OLATA   = 0x14

IODIRB  = 0x01
OLATB   = 0x15

bus.write_byte_data(DEVICE1, IODIRA, 0x00)
bus.write_byte_data(DEVICE1, OLATA, 0)


steps1 = (0b1000, # 0
         0b1100, # 1
         0b0100, # 2
         0b0110, # 3
         0b0010, # 4
         0b0011, # 5
         0b0001, # 6
         0b1001) # 7
steps2 = steps1[::-1]
for i in range(512):
    for s in range(int(len(steps1)/2)):
        data = (steps1[s*2] << 4) + steps2[s*2]
        bus.write_byte_data(DEVICE1, OLATA, data)
        time.sleep(0.002)

