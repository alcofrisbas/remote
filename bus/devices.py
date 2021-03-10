import smbus
import time

bus = smbus.SMBus(1)

DEVICE1 = 0x20 # device address
DEVICE2 = 0x21 # device address
IODIRA = 0x00 # a register set io address
OLATA = 0x14  # write address OLAT stands for outputlatch
GPIOA = 0x12  # read address

IODIRB = 0x01 # B register set io address
OLATB = 0x15  # write address
GPIOB = 0x13  # read address

# configure devices
bus.write_byte_data(DEVICE1,IODIRA,0x00) # Set all r1a pins to out
bus.write_byte_data(DEVICE1,OLATA,0)     # write 0x00

bus.write_byte_data(DEVICE1,IODIRB,0x00) # Set all r1b pins to out
bus.write_byte_data(DEVICE1,OLATB,0)     # write 0x00

bus.write_byte_data(DEVICE2,IODIRA,0x00) # Set all r2a pins to out
bus.write_byte_data(DEVICE2,OLATA,0)     # write 0x00

bus.write_byte_data(DEVICE2,IODIRB,0x00) # Set all r2b pins to out
bus.write_byte_data(DEVICE2,OLATB,0)     # write 0x00

bus.write_byte_data(DEVICE1,OLATA,1)     # write 0x01 to r1a
time.sleep(1)
bus.write_byte_data(DEVICE1,OLATA,0)     # write 0x00 to r1a
bus.write_byte_data(DEVICE2,OLATA,1)     # write 0x01 to r2a
time.sleep(1)
bus.write_byte_data(DEVICE2,OLATA,0)     # write 0x00 to r2a

bus.write_byte_data(DEVICE1,OLATB,1)     # write 0x01 to r1b
time.sleep(1)
bus.write_byte_data(DEVICE1,OLATB,0)     # write 0x00 to r1b
bus.write_byte_data(DEVICE2,OLATB,1)     # write 0x01 to r1b
time.sleep(1)
bus.write_byte_data(DEVICE2,OLATB,0)     # write 0x00 to r1b

