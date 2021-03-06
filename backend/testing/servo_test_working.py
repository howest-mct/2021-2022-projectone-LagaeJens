from time import sleep
from RPi import GPIO

servo = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)


# waarde = spi.read_channel(0)

# 100%/20 = 50hz
pwm_servo = GPIO.PWM(servo , 50)
    
pwm_servo.start(0)

def servo_toGraden(waarde):
    duty = (waarde + 9)*(10/18)+2.5
    print(duty)
    # Graden = round((180/1023)*waarde,2)
    # print(f"graden{Graden}")
    pwm_servo.ChangeDutyCycle(duty)


try:
    
    while True:
            
        pwm_servo.ChangeDutyCycle(2.5)
        sleep(1)
        pwm_servo.ChangeDutyCycle(12)
        sleep(1)

except KeyboardInterrupt as e:
    print(e)
    pwm_servo.stop()
    #pass
finally:
    print("Script has stopped!!!")