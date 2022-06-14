import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

class rfid_lezen: 

        def __init__(self) -> None:
                self.reader = SimpleMFRC522()

        

        def uitlezen():
                try:
                        while True:
                                reader = SimpleMFRC522()
                                id = reader.read()
                                print(id[0])
                                sleep(0.005)
                                return id[0]


                except KeyboardInterrupt as e:
                        print(e)