from RPi import GPIO
from smbus import SMBus
from time import sleep

class dungeons:

    def __init__(self) -> None:
        self.i2c = SMBus(1)
        self.standaard = 0b10110011
        self.f = False
        # self.leds = [0b11110011, 0b11100111,0b11101110, 0b11111100, 0b11111001, 0b11110011]


    def buttons(self):
        self.i2c.open(1)
        waarde = self.i2c.read_byte(0x20)
        # print(waarde)
        if (waarde & 0x01) == 0:
            print("button 1")
            led = self.i2c.read_byte(0x21)
            var = (led & 0x10) >> 4 # neem de waarde van de 5de bit en plaats deze op de 1ste bit zodat volgorde aan/uit gerespecteerde wordt
            x = ((led & 0x1F)<< 1) | var # bitjes voor leds
            y = led & 0xE0  #bitjes voor rgb niet veranderd
            result = x | y
            self.i2c.write_byte(0x21,result)
        if (waarde & 0x02) == 0:
            print("button 2")
            led = self.i2c.read_byte(0x21)
            var = (led & 0x01) << 4
            x = ((led & 0x1F)>> 1)| var  # bitjes voor leds
            y = led & 0xE0  #bitjes voor rgb niet veranderd
            result = x | y
            self.i2c.write_byte(0x21,result)
        if (waarde & 0x04) == 0:
            print("button 3")
            led = self.i2c.read_byte(0x21)
            # ledz = led ^ 0x08
            # leds = ledz ^ 0x02
            self.i2c.write_byte(0x21,led ^ 0x0A) #flip de 4de & 2de bit
        if (waarde & 0x08) == 0:
            print("button 4")
            led = self.i2c.read_byte(0x21)
            # ledz = led ^ 0x08
            # leds = ledz ^ 0x04
            # ledd = leds ^ 0x02
            self.i2c.write_byte(0x21,led ^ 0x0E) #flip 3 middel bits 
        self.i2c.close()
    
    def read_leds(self):  #gemaakt om leds uit te lezen om in database te zetten
        self.i2c.open(1)
        leds = self.i2c.read_byte(0x21)
        self.i2c.close()
        return leds
    
    def read_buttons(self):  #gemaakt om buttons uit te lezen om in database te zetten
        self.i2c.open(1)  
        buttons = self.i2c.read_byte(0x20)
        self.i2c.close()
        return buttons
    
    f = False

    def dungeons_main(self): 
        try:
            f = False
            self.i2c.open(1)
            self.i2c.write_byte(0x21,self.standaard)
            self.i2c.close()
            while True:
                if self.f == False:
                    i2c=SMBus(1)
                    i2c.open(1)
                    sleep(0.01)
                        # test=i2c.read_byte(0x20)
                        # i2c.write_byte(0x21,~standaard)
                        # test1=i2c.read_byte(0x21)
                        # print(test)
                    self.buttons()
                    led = i2c.read_byte(0x21)                        # print(bin(led))
                    if led == 0xA0:
                        f = True
                        print(f, "waarde f")
                        return 1
                    i2c.close()
                    sleep(0.20)

                else:
                    print("solveddddddd")
                    exit()
                        

        except Exception as e:
            print(e)