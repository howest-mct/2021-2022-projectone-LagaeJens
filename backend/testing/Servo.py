from classen.classe import MPU6050
from time import sleep
from RPi import GPIO

servo = 21
servo2 = 20
keuze_1 = 24
keuze_2 = 23
  
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)
GPIO.setup(servo2, GPIO.OUT)
GPIO.setup(keuze_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(keuze_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


mpu = MPU6050(0x68,16,250)

# waarde = spi.read_channel(0)

# 100%/20 = 50hz
pwm_servo = GPIO.PWM(servo , 50)
pwm_servo2 = GPIO.PWM(servo2 , 50)
    
pwm_servo.start(0)
pwm_servo2.start(0)

def servo_toGraden(waarde):
    duty = (waarde + 9)*(10/18)+2.5 #2.5
    duty = round(duty,5)
    # print(duty)
    # Graden = round((180/1023)*waarde,2)
    # print(f"graden{Graden}")
    # pwm_servo.ChangeDutyCycle(duty)
    return duty

prev_waarde = 0

try:
    mpu.setup(0x68)
    while True:
        knop1 = GPIO.input(keuze_1)
        knop2 = GPIO.input(keuze_2)
        waarde = mpu.read_y_waarde()
        if knop1 == 0:
            print("knop1")        
            if waarde > -9 and waarde < 9:
            # if prev_waarde - waarde > 0.1: 
                value = servo_toGraden(waarde)
                pwm_servo.ChangeDutyCycle(value)
                sleep(0.02)
                pwm_servo.ChangeDutyCycle(0)
        # pw    m_servo.ChangeDutyCycle(2.5)
        # sleep(1)
        # pwm_servo.ChangeDutyCycle(12)
        # sleep(1)
        # print(waarde)
        if knop2 == 0:
            print("knop2") 
            if waarde > -9 and waarde < 9:
                # if prev_waarde - waarde > 0.1: 
                value = servo_toGraden(waarde)
                pwm_servo2.ChangeDutyCycle(value)
                sleep(0.02)
                pwm_servo2.ChangeDutyCycle(0)
        prev_waarde = waarde
    

        
            
            
    
        

except KeyboardInterrupt as e:
    print(e)
    pwm_servo.stop()
    #pass
finally:
    print("Script has stopped!!!")