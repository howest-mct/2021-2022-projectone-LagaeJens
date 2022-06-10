from RPi import GPIO
from time import sleep
from smbus import SMBus
from subprocess import check_output

class LCD:

    def __init__(self,RS , E) -> None:  #definieer de rs en de e pin
        self.RS = RS
        self.E = E
        # self.B0 = B0
        # self.B1 = B1
        # self.B2 = B2
        # self.B3 = B3
        # self.B4 = B4
        # self.B5 = B5
        # self.B6 = B6
        # self.B7 = B7

    # def initList(self):
        # return[self.B0,self.B1,self.B2,self.B3,self.B4,self.B5,self.B6,self.B7]

    def setup_lcd(self):
        print("Start setup")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.RS, GPIO.OUT)
        GPIO.setup(self.E,GPIO.OUT)


    def send_instruction(self , value):
        # print("Ik heb iets gedaan instructions")
        GPIO.output(self.RS , GPIO.LOW)
        GPIO.output(self.E , GPIO.HIGH)
        self.sent_data_bits(value)
        GPIO.output(self.E , GPIO.LOW)
        sleep(0.01)


    def send_character(self,value):
        # print("Ik heb iets gedaan characters")
        GPIO.output(self.RS, GPIO.HIGH)
        GPIO.output(self.E , GPIO.HIGH)
        self.sent_data_bits(value)
        GPIO.output(self.E , GPIO.LOW)
        sleep(0.01)


    def sent_data_bits(self,value):    
        self.i2c_voor_lcd(value)


    def cursor_opties(self,cursoroptions):
        if cursoroptions == "aan":
            self.send_instruction(0x0C | 3) #zet de cursor aan door 3 te ORR op je 0x0C toe te voegen
        elif cursoroptions == "uit":
            self.send_instruction(0x0C)
        else:
            print("FOUTE INVOER")

    def write_message(self,message):
        for i in message:
            test = ord(i)
            # print(test)
            self.send_character(test)
            sleep(0.01)

    # limit characters to 16 daarna send naar volgende lijn
    def write_message_limit(self,message):
        count = 0
        for char in message:
            count = count + 1
            self.send_character(ord(char))
            if count == 16:
                self.send_instruction(0b10000000 | 0x40)

    def i2c_voor_lcd(self, value):
        i2c = SMBus()
        i2c.open(1)
        i2c.write_byte(0x23,value)
        print("I2C is aangemaakt" , value)
        i2c.close()

    # Haalt alle ip adressen op die verbonden zijn. Nu eth0 & wlan0 tonen
    def ip_adress_ophalen(self):
        ip_adress = check_output(['hostname', '--all-ip-addresses'])
        ip_adress = ip_adress.decode("utf-8")
        ip_adress = ip_adress.split(" ")
        ip_adress1 = ip_adress[0]
        ip_adress2 = ip_adress[1]
        self.write_message("IP adress eth0: ")
        self.send_instruction(0b10000000 | 0x40)
        self.write_message_limit(ip_adress1)
        sleep(1.5)
        self.send_instruction(0x01)
        self.write_message("IP adress wlan0: ")
        self.send_instruction(0b10000000 | 0x40)
        self.write_message_limit(ip_adress2)
        sleep(1.5)
        self.send_instruction(0x01)
