from RPi import GPIO
from smbus import SMBus
from time import sleep


i2c = SMBus(1)

teller = 0

standaard = 0b11110011

leds = [0b11110011, 0b11100111,0b11101110, 0b11111100, 0b11111001, 0b11110011]

# def buttons():
#     i2c.open(1)
#     waarde = i2c.read_byte(0x20)
#     # print(waarde)
#     if waarde == 254:
#         ledwaarde = i2c.read_byte(0x22)
#         if(ledwaarde & 1 > 0):
#             print(bin(ledwaarde))
#             ledwaardes = ledwaarde << 1 | 0b00000001
#             print(bin(ledwaardes))
#             i2c.write_byte(0x22,ledwaardes)
#         else:
#             print(ledwaarde)
#             ledwaardes = ledwaarde << 1
#             print(ledwaardes)
#             i2c.write_byte(0x22,ledwaardes)
#     i2c.close()

def buttons():
    global teller
    i2c.open(1)
    waarde = i2c.read_byte(0x20)
    print(waarde)
    if teller > 6:
        teller = 4
    if waarde == 254:
        if teller == 5:
            teller = 0
        else:
            teller += 1
            print(teller)
            i2c.write_byte(0x22,leds[teller])
            print(bin(leds[teller]))
    if waarde == 253:
        if teller == 0:
            teller = 5 
        else:     
            teller -= 1
            print(teller)
            i2c.write_byte(0x22,leds[teller])
            print(bin(leds[teller]))
            if teller <= 0:
                teller = 5
    if waarde == 252:
        test =  not leds[teller]
        i2c.write_byte(0x22,test)

    i2c.close()
    
# def leds():
#     i2c.open(1)
#     i2c.write_byte(0x20,standaard)
#     pass

try:
    i2c.open(1)
    i2c.write_byte(0x22,standaard)
    i2c.close()
    while True:
        i2c.open(1)
        # test=i2c.read_byte(0x20)
        # i2c.write_byte(0x22,~standaard)
        # test1=i2c.read_byte(0x22)
        # print(test)
        buttons()
        sleep(0.12)
        i2c.close()
        

except KeyboardInterrupt as e:
    GPIO.cleanup()
    i2c.close()

finally:
    print("Script has stopped!!!")