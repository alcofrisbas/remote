import smbus
import time

bus = smbus.SMBus(1)

DEVICE = 0x20 # device address
IODIRA = 0x00 # a register set io address
OLATA = 0x14  # write address OLAT stands for outputlatch
GPIOA = 0x12  # read address

IODIRB = 0x01 # B register set io address
OLATB = 0x15  # write address
GPIOB = 0x13  # read address


bus.write_byte_data(DEVICE,IODIRA,0x00)
bus.write_byte_data(DEVICE,OLATA,0)

for i in range(1,8):
    bus.write_byte_data(DEVICE,OLATA,i)
    print(hex(i))
    time.sleep(.25)

bus.write_byte_data(DEVICE,OLATA,0)

bus.write_byte_data(DEVICE,IODIRB,0x00)
bus.write_byte_data(DEVICE, OLATB,0)

for i in range(1,8):
    bus.write_byte_data(DEVICE,OLATB,i)
    print(hex(i))
    time.sleep(.25)

bus.write_byte_data(DEVICE,OLATB,0)
