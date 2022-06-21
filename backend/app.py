import time
import os
from RPi import GPIO
# from helpers.klasseknop import Button
import threading
from multiprocessing import Process, Queue
from smbus import SMBus
from datetime import datetime
# classes voor games
from mfrc522 import SimpleMFRC522
from testing.classen.bcd_classe import BCD
from testing.Servo import Servo_Met_MPU
from testing.classen.dungeons import dungeons
from testing.classen.Class_I2C_LCD import LCD
from testing.class_neopixel import neopixel_class
from testing.classen.test_rfid import rfid_lezen
from testing.classen.classe_mpu import MPU6050

from flask_cors import CORS
from flask_socketio import SocketIO, emit, send
from flask import Flask, jsonify , request
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
neopixel = neopixel_class()
rfid = rfid_lezen
reader = SimpleMFRC522()
mpu = MPU6050(0x68,16,250)

# Code voor Hardware
starttijd = 0
eindtijd = 0
var_b = False
var_c = False
var_d = False
var_e = False
var_f= False
var_g = False
var_h = False
var_i = False
var_j = False
id_rfid = 0
speler = ''

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
    os.system("sudo shutdown -h now")


prevwaarde = 1

def quiz_game():
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
                        DataRepository.insert_data(1, 1, datetime.now(), waarde , 'Reedcontact 1')
                    if (waarde & 0x02) == 0:
                        print(waarde)
                        socketio.emit('knop', {'knop': 'Reedcontact 2'}, broadcast=True)
                        DataRepository.insert_data(2, 2, datetime.now(), waarde , 'Reedcontact 2')
                    if (waarde & 0x04) == 0:
                        print(waarde)
                        socketio.emit('knop', {'knop': 'Reedcontact 3'}, broadcast=True)
                        DataRepository.insert_data(3, 3, datetime.now(), waarde , 'Reedcontact 3')
                    if (waarde & 0x08) == 0:
                        print(waarde)
                        socketio.emit('knop', {'knop': 'Reedcontact 4'}, broadcast=True)
                        DataRepository.insert_data(4, 3, datetime.now(), waarde , 'Reedcontact 4')
                    if (waarde & 16) == 0:
                        print(waarde)
                        socketio.emit('knop', {'knop': 'Reedcontact 5'}, broadcast=True)
                        DataRepository.insert_data(5,3, datetime.now(), waarde , 'Reedcontact 5')
                    if (waarde & 32) == 0:
                        print(waarde)
                        socketio.emit('knop', {'knop': 'Reedcontact 6'}, broadcast=True)
                        DataRepository.insert_data(6,3, datetime.now(), waarde , 'Reedcontact 6')
                    if waarde == 64:
                        print('done')
                        socketio.emit('knop', {'knop': 'allemaal connected'}, broadcast=True)
                        DataRepository.insert_data(1, 3, datetime.now(), waarde , 'Puzzlespel is klaar')
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


@app.route('/api/v1/historiek/' , methods=['GET'])
def historiek():
    if request.method == 'GET':
        print('Historiek')
        data = DataRepository.historiek_data_ophalen()
        return jsonify(geschiedenis=data)
    
    
@app.route('/api/v1/vragen/' , methods=['GET'])
def vragen():
    if request.method == 'GET':
        print('Vragen')
        data = DataRepository.ophalen_vragen()
        return jsonify(vragen=data)
    
@app.route('/api/v1/spelersinfo/<spelerid>/' , methods=['GET'])
def historiek_speler(spelerid):
    if request.method == 'GET':
        print('Historiek speler')
        print(f'spelerid' , speler)
        data = DataRepository.get_tijden(spelerid)
        print(data)
        return jsonify(geschied_speler=data)

@app.route('/api/v1/spelerinlog/' , methods=['GET','POST'])
def top_times():
    global speler
    if request.method == 'GET':
        print('Top times')
        data = DataRepository.get_top_times()
        print(data)	
        return jsonify(top_times=data)
    if request.method == 'POST':
        print('add speler')
        # print(request)
        gegevens = DataRepository.json_or_formdata(request)
        data = DataRepository.add_speler(gegevens['naam'],gegevens['kaartnummer'],datetime.now())
        speler = data
        print(f'spelerid', speler)
        socketio.emit('b2f_id', {'id': speler} )
        return jsonify(speler=data), 200 
    
@app.route('/api/v1/spelerhistory/' , methods=['GET'])
def spelers_history():
    if request.method == 'GET':
        print('Speler historiek')
        data = DataRepository.get_list_spelen()
        print(data)
        return jsonify(historiek=data)



@socketio.on('f_2_b_servo')
def f_2_b_servo():
    servo.test_range()


    
@socketio.on('f_2_b_poweroff')
def f_2_b_poweroff():
    print("Shutting down")
    lcd.send_instruction(0x01)
    lcd.write_message("Pi switched off")
    time.sleep(5)
    os.system("sudo shutdown -h now")
    

# START een thread op. Belangrijk!!! Debugging moet UIT staan op start van de server, anders start de thread dubbel op
# werk enkel met de packages gevent en gevent-websocket.

# convert mysql data to list
# def convert_to_list():
#     global spelerid
#     data = DataRepository.get_tijden(spelerid)
#     print(data)
#     list = []
#     # print(data)
#     spel1 = data['spel_1']
#     spel2 = data['spel_2']
#     spel3 = data['spel_3']
#     spel4 = data['spel_4']
#     totale_tijd = data['totale_tijd']
#     nieuwe_lijst = [spel1, spel2, spel3, spel4, totale_tijd]    
#     list.append(nieuwe_lijst)
#     print(list)
#     socketio.emit('b2f_tijden', {'tijden': list} )
#     time.sleep(100)
    
@socketio.on('f_2_b_knop')
def f_2_b_knop():
    global var_b
    global var_c
    global var_i
    global var_h
    var_i = False
    print(f'i',var_i)
    var_h = False
    print(f'h',var_h)
    var_c = False
    print(f'c',var_c)
    var_b = True
    print(f'b',var_b)
    bcd.setup()
    neopixel.all_red()
    print('f_2_b_knop')
    
    
def start_thread_lees_knop():
    try:
        global starttijd
        global eindtijd
        global var_b
        global var_c
        global var_d
        global var_e
        global var_f
        global var_g
        global var_h
        global var_i
        global var_j
        global id_rfid
        global speler
        prev = 0
        waarde = 0
        mpu.setup(0x68)
        while True:
            if var_b == True:
                print('starting thread')
                if var_c == False:
                    socketio.emit('gestart')
                    i2c.open(1)
                    time.sleep(0.1)
                    i2c.write_byte(0x20,0b11101111)
                    time.sleep(0.01)
                    i2c.write_byte(0x26,0b11111101)
                    time.sleep(0.01)
                    i2c.write_byte(0x22, 0b10111111)
                    neopixel.all_red()
                    print('rfid actief')
                    lcd.send_instruction(0x01)
                    time.sleep(0.1)
                    lcd.write_message('RFID SCANNEN')
                    time.sleep(5)
                    waarde_id = id_rfid
                    # print(waarde_id)
                    if waarde_id != 0:
                        DataRepository.insert_data(13,  1, datetime.now(), waarde_id , 'RFID gescand')
                        waarde_id = 0
                        var_c = True
                        var_j = True
                        var_g = False
                        starttijd = datetime.now()
                        lcd.send_instruction(0x01)
                        time.sleep(0.1)
                        lcd.wifi_adress()
                    if var_g == False:
                        if var_d == False:
                            if var_c == True:
                                print('rfid gescand, bij bcd')
                                waarde_bcd = bcd.main_BCD()
                                if waarde_bcd == 1:
                                    socketio.emit('BCD_B2F', {'BCD B2F': 'B2F'}, broadcast=True)
                                    spel_1 = datetime.now()
                                    var_d = True
                                    var_j = False
                                    print("bcd 1")
                    if var_d == True:
                        if var_e == False:
                            time.sleep(0.1)    
                            neopixel.green_red_1_4()
                            time.sleep(0.1)
                            waarde_knop = quiz_game()
                            print(waarde_knop)
                        if waarde_knop == 1:
                            spel_2 = datetime.now()
                            var_e = True
                            var_i = True
                            print("e is true")
                    if var_e == True:     
                        if var_f == False:
                            time.sleep(0.5)
                            neopixel.green_red_2_4()
                            waarde_dungeons = led_game.dungeons_main()
                            print(waarde_dungeons,"testtt")
                            if waarde_dungeons == 1:
                                spel_3 = datetime.now()
                                var_i = False
                                var_f = True
                                print("is true")
                    if var_f == True:
                        # i2c.open(1)
                        # i2c.write_byte(0x26, 0b11111101)
                        # time.sleep(0.01)
                        waarde_servogame = 0
                        if var_g == False:
                            neopixel.green_red_3_4()
                            waarde_servogame = servo.main_servo_met_mpu()
                            print(waarde_servogame , "servo")
                            if waarde_servogame == 1:
                                spel_4 = datetime.now()
                                var_g = True
                                var_d = False
                                var_e = False
                                var_f = False
    
    
            # va    r_h == True
                
            # ti    me.sleep(1)
            #         # servo.main_servo_met_mpu()
                
                
                if var_g == True:
                    var_f = False
                    print("truuuuuuuue")
                    neopixel.all_green()
                    if GPIO.input(13) == 1:
                        waarde = GPIO.input(13)
                        print("button pressed")
                        neopixel.rainbow_cycle()
                        if waarde != prev:
                            socketio.emit('b2f_einde')
                            print("spelerinfo geschreven in database")
                            var_b = False
                            var_g = False
                            var_h = True
                            id_rfid = 0
                            eindtijd = datetime.now()
                            spel_1_d = spel_1 - starttijd
                            spel_2_d = spel_2 - spel_1
                            spel_3_d = spel_3 - spel_2 
                            spel_4_d = spel_4 - spel_3
                            tijd_database = eindtijd - starttijd
                            DataRepository.update_tijden(spel_1_d, spel_2_d, spel_3_d , spel_4_d , tijd_database,speler)
                            print(tijd_database)
                            DataRepository.insert_data(7, 10, datetime.now(), waarde , 'Eindknop')
                    waarde = prev
                if var_h == True:
                    neopixel.rainbow_cycle()
                        # time.sleep(1000)
                
            else:
                time.sleep(1)
                
            
    except Exception as e:
        print(e)


def lcd_ip():
    try:
        time.sleep(10)
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
        
        
def rfid_thread():
    try:
        global id_rfid
        while True:
                    print("rfid running")
                    id_rfid = reader.read()
                    id_rfid = id_rfid[0]
                    print(id_rfid)
                    time.sleep(0.5)
                    
    except:
        print('error')
  


def rfid_ID_thread_main():
    print('rfid_ID_thread_main')
    thread = threading.Thread(target=rfid_thread, args=(), daemon=True)
    thread.start()


def lees_mpu_thread_function():
    try:
        while True:
            try:
                waarde = servo.mpu_data_to_front()
                socketio.emit('b2f_mpu', {'b2f_mpu': waarde})
                if var_f == True:
                    # print('test')
                    waarde = servo.mpu_data_to_front()
                    DataRepository.insert_data(8, 8, datetime.now(), waarde , 'MPU data naar front')
                    time.sleep(1)
                else:
                    time.sleep(1)
            except Exception as e:
                print("mpu error:" , e)
    except Exception as e:
        print(e)

def thread_read_mpu():
    print("Thread MPU_reading")
    thread = threading.Thread(target=lees_mpu_thread_function, args=(), daemon=True)
    thread.start()

def lees_buttons():
    try:
        global var_i
        while True:
            try:
                # print('test')
                if var_i == True:
                    waarde = led_game.read_buttons()
                    print(waarde)
                    socketio.emit('Buttons', {'Button': waarde}, broadcast=True)
                    if waarde != 223:
                        print("ke buttons geschreven")
                        DataRepository.insert_data(9, 9, datetime.now(), waarde , 'Buttons')
                    time.sleep(0.5)
                else:
                    time.sleep(1)
                #     print('niets buttons geschreven')
            except Exception as e:
                print("lees_buttons:" ,e)
    except Exception as e:
        print(e)


    
def thread_read_buttons():
    print("Thread buttons")
    thread = threading.Thread(target=lees_buttons, args=(), daemon=True)
    thread.start()



def lees_bcd_thread():
    try:
        vorige_waarde_bcd = 0
        while True:
            waarde = bcd.bcd_uitlezen()
            socketio.emit('BCD', {'BCD': waarde}, broadcast=True)
            if var_j == True:
                i2c.open(1)
                waarde = i2c.read_byte(0x24)
                i2c.close()
                # print('test')
                waarde = bcd.bcd_uitlezen()
                socketio.emit('BCD', {'BCD': waarde}, broadcast=True)
                if waarde != vorige_waarde_bcd:
                    print("ke geschreven")
                    DataRepository.insert_data(9, 9, datetime.now(), waarde , 'BCD waarde')
                    time.sleep(0.5)
                else:
                    time.sleep(0.5)
                    print('niets geschreven')
                vorige_waarde_bcd = waarde
            else:
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
        start_thread()
        rfid_ID_thread_main()
        thread_read_mpu()
        thread_read_bcd()
        thread_read_mpu()
        thread_read_buttons()
        lcd_thread()
        start_chrome_thread()
        print("**** Starting APP ****")
        socketio.run(app, debug=False, host='0.0.0.0')
    except KeyboardInterrupt:
        print ('KeyboardInterrupt exception is caught')
    finally:
        GPIO.cleanup()

