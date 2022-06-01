from smbus import SMBus
from time import sleep

class MPU6050:
    def __init__(self, par_address , par_range_acc, par_range_gyro ): 
        self.bus = SMBus()
        self.address = par_address
        self.range_acc = par_range_acc
        self.range_gyro = par_range_gyro


    def range_accelero(self,range_acc):
        waarde = 0
        if self.range_acc == 2:
            waarde = 16384
        elif self.range_acc == 4:
            waarde = 8192
        elif self.range_acc == 8:
            waarde = 4096
        elif self.range_acc == 16:
            waarde = 2048
        else:
            print("Ongeldige waarde")
        return waarde


    def range_gyroscoop(self,range_gyro):
        waarde = 0
        if self.range_gyro == 250:
            waarde = 131
        elif self.range_gyro == 500:
            waarde = 65.5
        elif self.range_gyro == 1000:
            waarde = 32.8
        elif self.range_gyro == 2000:
            waarde = 16.4
        else:
            print("Ongeldige waarde")
        return waarde


    def setup(self,address):
        i2c = SMBus()
        i2c.open(1)
        i2c.write_byte_data(self.address,0x6B,0x01)
        i2c.write_byte_data(self.address,0x1C,0x00)
        i2c.write_byte_data(self.address,0x1B,0x00)
        print("Setup is aangemaakt")
        
    
    def read_temp(self):
        i2c = SMBus()
        i2c.open(1)
        temp = i2c.read_i2c_block_data(self.address,0x41, 2) #lees 2 bytes uit de register 0x41
        temp1 =  (temp[0] << 8 )| temp[1]
        waarde = self.twee_complementen(temp1)
        juiste = waarde /340 + 36.53  #berekend de temperatuur
        juist = round(juiste,2) #rond de temperatuur af naar 2 decimalen
        print("De temperatuur is: " , juist , "°C")
        
    
    def read_accelerometer(self):
        i2c = SMBus()
        i2c.open(1)
        waarde = self.__read_all(0X3B,6)
        # print(waarde)
        x =  (waarde[0] << 8 )| waarde[1]
        y =  (waarde[2] << 8 )| waarde[3] 
        z =  (waarde[4] << 8 )| waarde[5]
        # print("ik ben het",x)
        x2 = self.twee_complementen(x)
        range = self.range_accelero(self.range_acc)
        x_juist = x2 / range  #waarde 
        x_juist = round(x_juist,2)
        y2 = self.twee_complementen(y)
        y_juist = y2 / range 
        y_juist = round(y_juist,2)
        z2 = self.twee_complementen(z)
        z_juist = z2 / range
        z_juist = round(z_juist,2)
        print(f"X ", x_juist,"Y",y_juist,"Z",z_juist)
        print("som accelerometer",x_juist+y_juist+z_juist)
        
        
    def read_y_waarde(self):
        i2c = SMBus()
        i2c.open(1)
        waarde = self.__read_all(0X3B,6)
        y =  (waarde[2] << 8 )| waarde[3]
        range = self.range_accelero(self.range_acc)
        y2 = self.twee_complementen(y)
        y_juist = y2 / range 
        y_juist = round(y_juist,2)
        print(f"Y",y_juist)
        return y_juist
    
    def read_gyro(self):
        i2c = SMBus()
        i2c.open(1)
        waarde = self.__read_all(0X43,6)
        # print(waarde)
        x =  waarde[0] << 8 | waarde[1]  #lees 2 bytes uit de register 0x43 voor x as
        y =  waarde[2] << 8 | waarde[3] #lees 2 bytes uit de register 0x45 voor y as
        z =  waarde[4] << 8 | waarde[5] #lees 2 bytes uit de register 0x47 voor z as
        x2 = self.twee_complementen(x)
        range = self.range_gyroscoop(self.range_gyro)
        x_juist = x2 / range  #waarde 
        x_juist = round(x_juist,2)
        y2=self.twee_complementen(y)
        y_juist = y2 / range
        y_juist = round(y_juist,2)
        z2=self.twee_complementen(z)
        z_juist = z2 / range
        z_juist = round(z_juist,2)
        print(f"X:", x_juist,"°/s ;","Y:",y_juist,"°/s ;","Z:",z_juist,"°/s")
        sleep(1)
        

    # Haal de 6 bytes op uit de registers in 1 transactie
    def __read_all(self, register , aantal):
        i2c = SMBus()
        i2c.open(1)
        waarde = i2c.read_i2c_block_data(self.address,register, aantal)
        # print("raw data: " ,waarde)
        sleep(0.01)
        return waarde

    def close(self):
        self.bus.close()

    @staticmethod
    def twee_complementen(value):
        # waarde = (value[0] << 8) | value[1]
        # print("itse me",value)
        if value >> 15 == 1:
            value -= 2 ** 16
        return value
        