from classen.classe import MPU6050
from time import sleep


mpu = MPU6050(0x68,2,250)   #0x68 adres MPU6050
                            #2 standaard range waarde voor accelerometer opstarten
                            # 250 standaard range waarde voor gyroscope opstarten


try:
    acc=input("Range accelerometer 2/4/8/16: ")
    gyro=input("Range gyroscope 250/500/1000/2000: ")
    mpu.setup(0x68)
    mpu.range_accelero(acc)
    mpu.range_gyroscoop(gyro)
    while True:
        # mpu.read_temp()
        mpu.read_accelerometer()
        # mpu.read_gyro()
        mpu.close()
        
        sleep(1)
        pass



except KeyboardInterrupt as e:
    print(e)
    mpu.close()
    #pass


finally:
    print("Script has stopped!!!")
