# import Adafruit_DHT
# import sys
# import time
# import random
# import datetime
# import telepot
# import RPi.GPIO as GPIO

# sensor = Adafruit_DHT.DHT11

# GPIO.setmode(GPIO.BOARD)
# # set up GPIO output channel
# GPIO.setup(4, GPIO.OUT)

# while True:
#     humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
#     print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))

# time.sleep(1)
import sys
import time, datetime
import telepot
import subprocess
import RPi.GPIO as GPIO
from telepot.loop import MessageLoop

PINf = 21
PIR = 17
led = 2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PINf, GPIO.IN)
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 0)

temper = subprocess.check_output('python DHT11.py', shell=True)

def handle(msg):
    global chat_id
    global command
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Menerima pesan dari ' + str(chat_id))
    if command == '/temp':
        bot.sendMessage(chat_id, temper)
    elseif command == '/off_led':
        print('LED MATI')
        GPIO.output(led, 0)
        bot.sendMessage(chat_id, 'LED MATI')
    elseif command == '/start':
        bot.sendMessage(chat_id, 'Selamat Datang')
        while True:
        if GPIO.input(PINf) == 1 and GPIO.input(PIR) == 1 :
            print ("ADA API dan ADA ORANG")
            bot.sendMessage(chat_id, 'Ada api dikamar dan ada seseorang')
            bot.sendMessage(chat_id, str(datetime.datetime.now()))
            bot.sendMessage(chat_id, temper)
            break
        elseif GPIO.input(PINf) == 0 and GPIO.input(PIR) == 1 :
            print ("TIDAK ADA API dan ADA ORANG")
            bot.sendMessage(chat_id, 'Tidak ada api dikamar dan ada seseorang')
            bot.sendMessage(chat_id, str(datetime.datetime.now()))
            bot.sendMessage(chat_id, temper)
            break
        elseif GPIO.input(PINf) == 1 and GPIO.input(PIR) == 0 :
            print ("ADA API dan TIDAK ADA ORANG")
            bot.sendMessage(chat_id, 'Ada api dikamar dan tidak ada seseorang')
            bot.sendMessage(chat_id, str(datetime.datetime.now()))
            bot.sendMessage(chat_id, temper)
            break
        elseif GPIO.input(PINf) == 0 and GPIO.input(PIR) == 0 :
            print ("Kamar aman")

bot = telepot.Bot('1939969230:AAF3c9yFvb5uGOfBLxJM0i8AJ388PlFIPKA')
bot.message_loop(handle)
print 'Ketik /start untuk memulai'
print 'Ketik /temp untuk mengetahui suhu'
while 1:
    time.sleep(10)
