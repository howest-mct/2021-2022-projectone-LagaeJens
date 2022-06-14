from classen.bcd_classe import BCD
from classen.dungeons import dungeons
from Servo import Servo_Met_MPU
from classen.Class_I2C_LCD import LCD 
from classen.test_rfid import rfid_lezen
from time import sleep
from smbus import SMBus
from RPi import GPIO
import os

rfid = rfid_lezen
i2c = SMBus(1)
# rs = 23
# e = 24
# lcd = LCD(rs,e)
 
def setup():
    print("Setup")
    GPIO.setmode(GPIO.BCM)

    
    
def Shutdown(channel):
    print("Shutting Down")
    sleep(5)
    os.system("sudo poweroff")
     
servo= Servo_Met_MPU()
test=BCD()
dungeon = dungeons()
try:
    setup()
    var_a = False
    # lcd.setup_lcd()
    #     #function set
    # lcd.send_instruction(0x38)
    # sleep(0.05)
    # #display aan
    # lcd.send_instruction(0x0C | 0x02 | 0x01)
    # sleep(0.05)
    # #display leegmaken 
    # lcd.send_instruction(0x01)
    # sleep(0.05)
    test.setup()
    while True:
        if var_a == False:
            id = rfid.uitlezen()
            waarde_id = id
        # if var_a == False:
        #     i2c.open(1)
        # # i2c.write_byte(0x20, 0x00)
            # waarde=
            # servo.main_servo_met_mpu()
        #     if waarde == 1:
        #         print("1")
        #         var_a = True
        
        
        # lcd.send_instruction(0x01) #display leegmaken
        # lcd.ip_adress_ophalen() 
        # lcd.send_instruction(0x0C)
        # dungeon.dungeons_main()
        # test.main_BCD()
            sleep(1)
    
        
        
        
        
except KeyboardInterrupt as e:
    print(e)
    
    
finally:
    print("finally")
    