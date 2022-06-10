from RPi import GPIO
from time import sleep
from smbus import SMBus
from random import randint

i2c = SMBus(1)

while True:
    i2c.open(1)
    waarde = i2c.read_byte(0x24)
    cijfer = (waarde & 0x0F) ^ 0x0F 
    print(cijfer)
    # print(bin(cijfer))
    print(bin(waarde))
    # flash_led()
    i2c.close()
    sleep(0.1)