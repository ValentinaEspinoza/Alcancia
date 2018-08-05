import pip
import telegram
from telegram.ext import *

bot = telegram.Bot(token='537304725:AAEuW2NVHKSUHCJ2hy49qtVguOH5ftEccSU')

import time, datetime
import RPi.GPIO as GPIO
import telepot
import avance
from telepot.loop import MessageLoop
def action(msg,suma):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN) #PIR 
    GPIO.setup(18, GPIO.OUT) #Led
    try:
        time.sleep(2) # to stabilize sensor     
        while True:        
            i=GPIO.input(4)       
            if i==0:               #When output from motion sensor is LOW                            
                GPIO.output(18, 0)  #Turn OFF LED              
                #print (" No motion detected",i )                                                 
            elif i==1:             #When output from motion sensor is HIGH                                                       
                GPIO.output(18, 1)  #Turn ON LED                            
                print (" Motion detected ",i )
                moneda = avance.shoot()
                suma += moneda
    except:     
        GPIO.cleanup()
        
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'Received: %s' % command            
    message = "Cual es su meta?  "
    telegram_bot.sendMessage (chat_id, message)
    meta = input()
    if 'on' in command:
        if 'monto' in command:
            message = 'Esto lleva acumulado: '+ suma 
        if 'meta' in command:
            message = meta
        
        telegram_bot.sendMessage (chat_id, message)
    
telegram_bot = telepot.Bot('537304725:AAEuW2NVHKSUHCJ2hy49qtVguOH5ftEccSU')
print (telegram_bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()
print 'Up and Running....'
