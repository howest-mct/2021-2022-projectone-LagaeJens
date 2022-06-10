from testing.classen.classe_mpu import MPU6050
from time import sleep
from RPi import GPIO


class Servo_Met_MPU():
    
    def __init__(self) -> None:
        self.servo = 21
        self.servo2 = 20
        self.keuze_1 = 24
        self.keuze_2 = 23
        self.mpu = MPU6050(0x68,16,250)
        self.prev_waarde = 0
        
        
    def setup(self):  
        # GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servo, GPIO.OUT)
        GPIO.setup(self.servo2, GPIO.OUT)
        GPIO.setup(self.keuze_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.keuze_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


    

    # waarde = spi.read_channel(0)

    # 100%/20 = 50hz


  

    def servo_toGraden(self,waarde):
        duty = (waarde + 9)*(10/18)+2.5 #2.5
        duty = round(duty,5)
        # print(duty)
        # Graden = round((180/1023)*waarde,2)
        # print(f"graden{Graden}")
        # pwm_servo.ChangeDutyCycle(duty)
        return duty

    
    def main_servo_met_mpu(self):
        try:
            self.setup()
            self.mpu.setup(0x68)
            pwm_servo = GPIO.PWM(self.servo , 50)
            pwm_servo2 = GPIO.PWM(self.servo2 , 50)  
            pwm_servo.start(0)
            pwm_servo2.start(0)
            while True:
                knop1 = GPIO.input(self.keuze_1)
                knop2 = GPIO.input(self.keuze_2)
                waarde = self.mpu.read_y_waarde()
                if knop1 == 0:
                    print("knop1")        
                    if waarde > -9 and waarde < 9:
                    # if prev_waarde - waarde > 0.1: 
                        value = self.servo_toGraden(waarde)
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
                        value = self.servo_toGraden(waarde)
                        pwm_servo2.ChangeDutyCycle(value)
                        sleep(0.02)
                        pwm_servo2.ChangeDutyCycle(0)
                self.prev_waarde = waarde








        except Exception as e:
            print(e)
            #pass