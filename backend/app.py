import time
from RPi import GPIO
from helpers.klasseknop import Button
import threading
from multiprocessing import Process, Queue
from smbus import SMBus
from mfrc522 import SimpleMFRC522
from datetime import datetime

from flask_cors import CORS
from flask_socketio import SocketIO, emit, send
from flask import Flask, jsonify
from repositories.DataRepository import DataRepository

from selenium import webdriver

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

i2c = SMBus(1)
reader = SimpleMFRC522()

id = Queue()
# ledPin = 21
# btnPin = Button(20)

# Code voor Hardware
def setup_gpio():
    GPIO.setwarnings(False)
    # GPIO.setmode(GPIO.BCM)

    # GPIO.setup(ledPin, GPIO.OUT)
    # GPIO.output(ledPin, GPIO.LOW)

prevwaarde = 0

def lees_knop():
    global prevwaarde
    i2c.open(1)
    waarde = i2c.read_byte(0x21)
    # print(waarde)
    i2c.close()
    if waarde != prevwaarde:
        if waarde == 254:
            print(waarde)
            socketio.emit('knop', {'knop': 'Reedcontact 1'}, broadcast=True)
            DataRepository.insert_data(1, 1, 1, datetime.now(), waarde , 'Reedcontact 1')
        if waarde == 253:
            print(waarde)
            socketio.emit('knop', {'knop': 'Reedcontact 2'}, broadcast=True)
            DataRepository.insert_data(2, 2, 2, datetime.now(), waarde , 'Reedcontact 2')
        if waarde == 251:
            print(waarde)
            socketio.emit('knop', {'knop': 'Reedcontact 3'}, broadcast=True)
            DataRepository.insert_data(3, 3, 3, datetime.now(), waarde , 'Reedcontact 3')
        elif waarde == 255:
            print(waarde)
            socketio.emit('knop', {'knop': 'released'}, broadcast=True)
    prevwaarde =  waarde


def lees_rfid(badgeid):
    try:
        id, text = reader.read()
        badgeid.put([id])
        # print("lees rfid")
        print(id)
        print(text)
    except:
        print("errortrr")
    
        

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


def start_thread_lees_knop():
    while True:
        lees_knop()
        time.sleep(0.5)

def rfid_thread(id):
    try:
        while True:
            # print('test')
            lees_rfid(id)
    except:
        print('error')
  
def rfid_ID_thread():
    try:
        while True:
            lijst = id.get()
            print(lijst[0])
    except:
        print('error')


def rfid_ID_thread_main():
    print('rfid_ID_thread_main')
    thread = threading.Thread(target=rfid_ID_thread, args=(), daemon=True)
    thread.start()

def start_thread():
    print("**** knop thread test ****")
    thread = threading.Thread(target=start_thread_lees_knop, args=(), daemon=True)
    thread.start()
    
    
def rfid_thread_main():
    print("**** knop thread test ****")
    # thread = threading.Thread(target=rfid_thread, args=(), daemon=True)
    # thread.start()
    p = Process(target=rfid_thread, args=(id,))
    p.start()
    

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
        rfid_thread_main()
        rfid_ID_thread_main()
        start_chrome_thread()
        print("**** Starting APP ****")
        socketio.run(app, debug=False, host='0.0.0.0')
    except KeyboardInterrupt:
        print ('KeyboardInterrupt exception is caught')
    finally:
        GPIO.cleanup()

