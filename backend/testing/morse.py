from RPi import GPIO
from time import sleep
from smbus import SMBus
from random import randint



i2c = SMBus(1)
def random_nummer_genereren():
    random_nummer = randint(1,9)
    return random_nummer


def flash_led_2(nummer):
    x = (nummer)*2
    # print(x)
    for i in range(x):
        # print("aan")
        waardes = i2c.read_byte(0x24)
        cijfers = waardes ^ 0x20
        i2c.write_byte(0x24, cijfers) 
        sleep(0.5)
        
def flash_led_1(nummer):
    x = (nummer)*2
    # print(x)
    for i in range(x):
        # print("aan")
        waardes = i2c.read_byte(0x24)
        cijfers = waardes ^ 0x10
        i2c.write_byte(0x24, cijfers) 
        sleep(0.5)

def bcd_uitlezen():
        waarde = i2c.read_byte(0x24)
        cijfer = (waarde & 0x0F) ^ 0x0F 
        print(cijfer)
        print(bin(cijfer))    
        return cijfer


f = False
e = False

try:
    nummer_1 = random_nummer_genereren()
    nummer_2 = random_nummer_genereren()
    print(nummer_1)
    print(nummer_2)
    i2c.open(1)
    
          
    while True:
        if f == False:
            flash_led_1(nummer_1)
        if e == True:
            flash_led_2(nummer_2)
        sleep(0.001)
        i2c.write_byte(0x24, 255)
        sleep(0.001)
        # i2c.write_byte(0x24, 0)
        # waarde = i2c.read_byte(0x24)
        # cijfer = (waarde & 0x0F) ^ 0x0F 
        # print(cijfer)
        cijfer = bcd_uitlezen()
        # print(bin(cijfer))
        # print(bin(waarde))
        if cijfer == nummer_1:
            print("nr1 OK")
            f = True
            e = True
        if cijfer == nummer_2:
            print("nr2 OK")
            e = False
            break
        sleep(1)



except KeyboardInterrupt as e:
    print(e)
    
finally:
    GPIO.cleanup()
    i2c.close()
