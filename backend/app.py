import time
import os
from RPi import GPIO
# from helpers.klasseknop import Button
import threading
from multiprocessing import Process, Queue
from smbus import SMBus
from mfrc522 import SimpleMFRC522
from datetime import datetime
# classes voor games
from testing.classen.bcd_classe import BCD
from testing.Servo import Servo_Met_MPU
from testing.classen.dungeons import dungeons
from testing.classen.Class_I2C_LCD import LCD

from flask_cors import CORS
from flask_socketio import SocketIO, emit, send
from flask import Flask, jsonify
from repositories.DataRepository import DataRepository

from selenium import webdriver

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
rs = 19
e = 26
lcd = LCD(rs,e)
i2c = SMBus(1)
servo = Servo_Met_MPU()	
bcd = BCD()
led_game = dungeons()
# reader = SimpleMFRC522()

id = Queue()   


# Code voor Hardware



def setup_gpio():
    GPIO.setwarnings(False)
    # servo.setup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(25, GPIO.OUT)
    GPIO.output(25, GPIO.HIGH)
    GPIO.add_event_detect(18, GPIO.FALLING, callback=Shutdown, bouncetime=2000)
    # GPIO.setup(ledPin, GPIO.OUT)
    # GPIO.output(ledPin, GPIO.LOW)

def Shutdown(channel):
    print("Shutting down")
    lcd.send_instruction(0x01)
    lcd.write_message("Pi switched off")
    time.sleep(5)
    # os.system("sudo shutdown -h now")


prevwaarde = 1

def lees_knop():
    try:
        prevwaarde = 1
        i2c.open(1)
        i2c.write_byte(0x22, 0b01111111)
        i2c.close()
        while True:    
                i2c.open(1)
                waarde = i2c.read_byte(0x22)
                print(waarde)
                i2c.close()
                if waarde != prevwaarde:
                    if (waarde & 0x01) == 0 :
                        print(waarde)
                        socketio.emit('knop', {'knop': 'Reedcontact 1'}, broadcast=True)
                        DataRepository.insert_data(1, 1, 1, datetime.now(), waarde , 'Reedcontact 1')
                    if (waarde & 0x02) == 0:
                        print(waarde)
                        socketio.emit('knop', {'knop': 'Reedcontact 2'}, broadcast=True)
                        DataRepository.insert_data(2, 2, 2, datetime.now(), waarde , 'Reedcontact 2')
                    if (waarde & 0x04) == 0:
                        print(waarde)
                        socketio.emit('knop', {'knop': 'Reedcontact 3'}, broadcast=True)
                        DataRepository.insert_data(3, 3, 3, datetime.now(), waarde , 'Reedcontact 3')
                    if (waarde & 0x08) == 0:
                        print(waarde)
                        socketio.emit('knop', {'knop': 'Reedcontact 4'}, broadcast=True)
                        DataRepository.insert_data(3, 3, 3, datetime.now(), waarde , 'Reedcontact 4')
                    if (waarde & 16) == 0:
                        print(waarde)
                        socketio.emit('knop', {'knop': 'Reedcontact 5'}, broadcast=True)
                        DataRepository.insert_data(3, 3, 3, datetime.now(), waarde , 'Reedcontact 5')
                    if (waarde & 32) == 0:
                        print(waarde)
                        socketio.emit('knop', {'knop': 'Reedcontact 6'}, broadcast=True)
                        DataRepository.insert_data(3, 3, 3, datetime.now(), waarde , 'Reedcontact 6')
                    if waarde == 64:
                        print('done')
                        socketio.emit('knop', {'knop': 'allemaal connected'}, broadcast=True)
                        DataRepository.insert_data(3, 3, 3, datetime.now(), waarde , 'Puzzlespel is klaar')
                        i2c.open(1)
                        i2c.write_byte(0x22, 0b10111111)
                        i2c.close()
                        return 1
                    elif waarde == 255:
                        print(waarde)
                        socketio.emit('knop', {'knop': 'released'}, broadcast=True)
                    prevwaarde =  waarde
                    time.sleep(1)
    except Exception as e:
        print(e)


# def lees_rfid(badgeid):
#     try:
#         id, text = reader.read()
#         badgeid.put([id])
#         # print("lees rfid")
#         print(id)
#         print(text)
#     except:
#         print("errortrr")
    
        
# test
# Code voor Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'geheim!'
socketio = SocketIO(app, cors_allowed_origins="*", logger=False,
                    engineio_logger=False, ping_timeout=1)

CORS(app)


@socketio.on_error()        # Handles the default namespace
def error_handler(e):
    print(e)



# API ENDPOINTS


@app.route('/')
def hallo():
    return "Server is running, er zijn momenteel geen API endpoints beschikbaar."


@socketio.on('connect')
def initial_connection():
    print('A new client connect')
    # # Send to the client!
    # vraag de status op van de lampen uit de DB
    # status = DataRepository.read_status_lampen()
    # emit('B2F_status_lampen', {'lampen': status}, broadcast=True)


# START een thread op. Belangrijk!!! Debugging moet UIT staan op start van de server, anders start de thread dubbel op
# werk enkel met de packages gevent en gevent-websocket.

var_d = False
var_e = False
var_f= False
var_g = False


def start_thread_lees_knop():
    try:
        var_d = False
        var_e = False
        var_f = False
        var_g = False
        bcd.setup()
        while True:
            if var_d == False:
                waarde_bcd = bcd.main_BCD()
                if waarde_bcd == 1:
                    var_d = True
                    print("bcd 1")
            if var_g == False:
                if var_d == True:
                    if var_e == False:    
                        waarde_knop = lees_knop()
                        print(waarde_knop)
                    if waarde_knop == 1:
                        var_e = True
                        print("e is true")
                    if var_e == True:     
                        if var_f == False:
                            time.sleep(0.5)
                            waarde_dungeons = led_game.dungeons_main()
                            print(waarde_dungeons,"testtt")
                            if waarde_dungeons == 1:
                                var_f = True
                                var_g = True
                                print("is true")
            var_g == True
            time.sleep(1)
                # servo.main_servo_met_mpu()
            
            
            if var_g == True:
                print("truuuuuuuue")
                
                time.sleep(5)
            
    except Exception as e:
        print(e)


def lcd_ip():
    try:
        lcd.setup_lcd()
        #function set
        lcd.send_instruction(0x38)
        time.sleep(0.05)
        #display aan
        lcd.send_instruction(0x0C | 0x02 | 0x01)
        time.sleep(0.05)
        #display leegmaken 
        lcd.send_instruction(0x01)
        time.sleep(0.05)
        lcd.wifi_adress()
        
        while True:
            time.sleep(1)
    except Exception as e:
        print(e)
        
        
# def rfid_thread(id):
#     try:
#         while True:
#             # print('test')
#             lees_rfid(id)
#     except:
#         print('error')
  
# def rfid_ID_thread():
#     try:
#         while True:
#             lijst = id.get()
#             print(lijst[0])
#     except:
#         print('error')

# def rfid_ID_thread_main():
#     print('rfid_ID_thread_main')
#     thread = threading.Thread(target=rfid_ID_thread, args=(), daemon=True)
#     thread.start()

# def rfid_thread_main():
#     print("**** knop thread test ****")
#     # thread = threading.Thread(target=rfid_thread, args=(), daemon=True)
#     # thread.start()
#     p = Process(target=rfid_thread, args=(id,))
#     p.start()


def lees_bcd_thread():
    try:
        vorige_waarde_bcd = 0
        while True:
                # print('test')
                waarde = bcd.bcd_uitlezen()
                socketio.emit('BCD', {'BCD': waarde}, broadcast=True)

                if waarde != vorige_waarde_bcd:
                    print("ke geschreven")
                    DataRepository.insert_data(9, 9, 9, datetime.now(), waarde , 'BCD waarde')
                    time.sleep(0.5)
                else:
                    time.sleep(0.5)
                    print('niet juste')
                vorige_waarde_bcd = waarde
                time.sleep(1)
    except Exception as e:
        print(e)


    
def thread_read_bcd():
    print("Thread BCD_reading")
    thread = threading.Thread(target=lees_bcd_thread, args=(), daemon=True)
    thread.start() 

def lcd_thread():
    print("Thread lcd")
    thread = threading.Thread(target=lcd_ip, args=(), daemon=True)
    thread.start() 
    
def start_thread():
    print("**** knop thread test ****")
    thread = threading.Thread(target=start_thread_lees_knop, args=(), daemon=True)
    thread.start()

def start_chrome_kiosk():
    import os

    os.environ['DISPLAY'] = ':0.0'
    options = webdriver.ChromeOptions()
    # options.headless = True
    # options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    # options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    # options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--kiosk')
    # chrome_options.add_argument('--no-sandbox')         
    # options.add_argument("disable-infobars")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost")
    while True:
        pass


def start_chrome_thread():
    print("**** Starting CHROME ****")
    chromeThread = threading.Thread(target=start_chrome_kiosk, args=(), daemon=True)
    chromeThread.start()



# ANDERE FUNCTIES


if __name__ == '__main__':
    try:
        setup_gpio()
        # thread_read_bcd()
        start_thread()
        # rfid_thread_main()
        # rfid_ID_thread_main()
        lcd_thread()
        start_chrome_thread()
        print("**** Starting APP ****")
        socketio.run(app, debug=False, host='0.0.0.0')
    except KeyboardInterrupt:
        print ('KeyboardInterrupt exception is caught')
    finally:
        GPIO.cleanup()

