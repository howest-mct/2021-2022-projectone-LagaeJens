from RPi import GPIO
from time import sleep
from smbus import SMBus
from random import randint

class BCD:

    def __init__(self) -> None:
        self.f = False
        self.e = False
        self.i2c = SMBus(1)
        self.i2c.open(1)
    
    
    def random_nummer_genereren(self):
        random_nummer = randint(1,9)
        return random_nummer
    
    def flash_led_2(self,nummer):  
        x = (nummer)*2
        # print(x)
        for i in range(x):
            # print("aan")
            waardes = self.i2c.read_byte(0x24)
            cijfers = waardes ^ 0x20
            self.i2c.write_byte(0x24, cijfers) 
            sleep(0.5)
           
           
    def flash_led_1(self,nummer):
        x = (nummer)*2
        # print(x)
        for i in range(x):
            # print("aan")
            waardes = self.i2c.read_byte(0x24)
            cijfers = waardes ^ 0x10
            self.i2c.write_byte(0x24, cijfers) 
            sleep(0.5)
        
    def bcd_uitlezen(self): 
        waarde = self.i2c.read_byte(0x24)
        cijfer = (waarde & 0x0F) ^ 0x0F 
        print(cijfer)
        print(bin(cijfer)) 
        return cijfer
    
    def setup(self):
        self.nummer_1 = self.random_nummer_genereren()
        sleep(0.002)
        self.nummer_2 = self.random_nummer_genereren() 
        if self.nummer_1 == self.nummer_2:
            self.nummer_2 = self.random_nummer_genereren()
        self.f = False
        self.e = False
        print(self.nummer_1)
        print(self.nummer_2)
    
    def main_BCD(self):	
        try:
            # self.i2c.open(1)
            self.i2c.write_byte(0x24, 0b10111111)
            print('main')
            while True:
                i2c = SMBus(1)
                i2c.open(1)
                if self.f == False:
                    print('flash_led_1')
                    self.flash_led_1(self.nummer_1)
                if self.e == True:
                    self.flash_led_2(self.nummer_2)
                sleep(0.001)
                # i2c.write_byte(0x24, 255)
                sleep(0.001)
                # i2c.write_byte(0x24, 0)
                # waarde = i2c.read_byte(0x24)
                # cijfer = (waarde & 0x0F) ^ 0x0F 
                # print(cijfer)
                cijfer = self.bcd_uitlezen()
                # print(bin(cijfer))
                # print(bin(cijfer))
                # print(bin(waarde))
                if cijfer == self.nummer_1:
                    print("nr1 OK")
                    self.f = True
                    self.e = True
                if cijfer == self.nummer_2 and self.f == True:
                    print("nr2 OK")
                    i2c.write_byte(0x24, 0b01111111)
                    self.e = False
                    
                    return 1
                    # break
                i2c.close()
                sleep(0.5)



        except Exception as e:
            self.i2c.close()
            print(e)


