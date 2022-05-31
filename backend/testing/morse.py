from RPi import GPIO
from time import sleep
from smbus import SMBus


i2c = SMBus(1)


try:
    while True:
        i2c.open(1)
        waarde = i2c.read_byte(0x24)
        print(waarde)
        i2c.close()
        sleep(1)
    

except KeyboardInterrupt as e:
    print(e)

finally:
    GPIO.cleanup()
    i2c.close()
# GPIO.setmode(GPIO.BCM)

# print("Script is running!!!")

# PinB1 = 23
# PinB2 = 24
# PinB3 = 25
# PinB4 = 26

# GPIO.setup(PinB1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
# GPIO.setup(PinB2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
# GPIO.setup(PinB3,GPIO.IN,pull_up_down=GPIO.PUD_UP)
# GPIO.setup(PinB4,GPIO.IN,pull_up_down=GPIO.PUD_UP)

# try:
#     while True:

#         waarde1 = not GPIO.input(PinB1) 
#         waarde2 = not GPIO.input(PinB2)
#         waarde3 = not GPIO.input(PinB3)
#         waarde4 = not GPIO.input(PinB4)
#         # print(waarde1,waarde2,waarde3,waarde4)
        
#         result = waarde1  
#         result = result | (waarde2<<1)
#         result = result | (waarde3<<2)
#         result |= waarde4<<3
#         print(result)

#         # result = waarde1 | (waarde2 << 1) | (waarde3 << 2) | (waarde4 << 3)
#         # print(result)


# except KeyboardInterrupt as e:
#     print(e)
#     #pass
# finally:
#     GPIO.cleanup()
#     print("Script has stopped!!!")

