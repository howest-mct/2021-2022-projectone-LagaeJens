from RPi import GPIO
from smbus import SMBus
from time import sleep

class dungeons:

    def __init__(self) -> None:
        self.i2c = SMBus(1)
        self.standaard = 0b10110011
        self.leds = [0b11110011, 0b11100111,0b11101110, 0b11111100, 0b11111001, 0b11110011]

    # def buttons():
    #     global teller
    #     i2c.open(1)
    #     waarde = i2c.read_byte(0x20)
    #     print(waarde)
    #     if teller > 6:
    #         teller = 4
    #     if waarde == 254:
    #         if teller == 5:
    #             teller = 0
    #         else:
    #             teller += 1
    #             print(teller)
    #             i2c.write_byte(0x21,leds[teller])
    #             print(bin(leds[teller]))
    #     if waarde == 253:
    #         if teller == 0:
    #             teller = 5 
    #         else:     
    #             teller -= 1
    #             print(teller)
    #             i2c.write_byte(0x21,leds[teller])
    #             print(bin(leds[teller]))
    #             if teller <= 0:
    #                 teller = 5
    #     if waarde == 252:
    #         test =  not leds[teller]
    #         i2c.write_byte(0x21,test)

    #     i2c.close()

    def button_test(self):
        self.i2c.open(1)
        waarde = self.i2c.read_byte(0x20)
        # print(waarde)
        if (waarde & 0x01) == 0:
            led = self.i2c.read_byte(0x21)
            var = (led & 0x10) >> 4 # neem de waarde van de 5de bit en plaats deze op de 1ste bit zodat volgorde aan/uit gerespecteerde wordt
            x = ((led & 0x1F)<< 1) | var # bitjes voor leds
            y = led & 0xE0  #bitjes voor rgb niet veranderd
            result = x | y
            self.i2c.write_byte(0x21,result)
        if (waarde & 0x02) == 0:
            led = self.i2c.read_byte(0x21)
            var = (led & 0x01) << 4
            x = ((led & 0x1F)>> 1)| var  # bitjes voor leds
            y = led & 0xE0  #bitjes voor rgb niet veranderd
            result = x | y
            self.i2c.write_byte(0x21,result)
        if (waarde & 0x04) == 0:
            led = self.i2c.read_byte(0x21)
            # ledz = led ^ 0x08
            # leds = ledz ^ 0x02
            self.i2c.write_byte(0x21,led ^ 0x0A) #flip de 4de & 2de bit
        if (waarde & 0x08) == 0:
            led = self.i2c.read_byte(0x21)
            # ledz = led ^ 0x08
            # leds = ledz ^ 0x04
            # ledd = leds ^ 0x02
            self.i2c.write_byte(0x21,led ^ 0x0E) #flip 3 middel bits 
        self.i2c.close()


    def dungeons_main(self): 
        try:
            self.i2c.open(1)
            self.i2c.write_byte(0x21,self.standaard)
            self.i2c.close()
            while True:
                i2c=SMBus(1)
                i2c.open(1)
                # test=i2c.read_byte(0x20)
                # i2c.write_byte(0x21,~standaard)
                # test1=i2c.read_byte(0x21)
                # print(test)
                self.button_test()
                led = i2c.read_byte(0x21)
                # print(bin(led))
                if led  == 0xA0:
                    print("test")
                    break
                i2c.close()
                sleep(0.15)


        except Exception as e:
            print(e)