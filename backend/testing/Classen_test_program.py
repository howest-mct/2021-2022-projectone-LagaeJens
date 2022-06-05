from classen.bcd_classe import BCD
from classen.dungeons import dungeons
from Servo import Servo_Met_MPU
from time import sleep

servo= Servo_Met_MPU()
test=BCD()
dungeon = dungeons()
try:
    test.setup()
    while True:
        servo.main_servo_met_mpu()
        # dungeon.dungeons_main()
        # test.main()
        
        
        
        
        
except KeyboardInterrupt as e:
    print(e)
    
    
finally:
    print("finally")
    