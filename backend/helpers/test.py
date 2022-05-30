import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        while True:

                id, text = reader.read()
                print(id)
                print(text)


except KeyboardInterrupt as e:
    print(e)
    #pass



finally:
        GPIO.cleanup()