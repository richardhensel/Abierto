#! /usr/bin/python

import time
import requests
import serial

#from gpiozero import LED

import serial


#def runLed():
#    print "unlock"
#    print "gpio high"
#    led.on()
#    #set gpio to high
#    time.sleep(1)
#
#    print "gpio low"
#    led.off()
#    #set gpio to low

def sendUnlock():
    while True:
        #ser.write('.9000.'.encode('utf-8'))
        ser.write('9000.'.encode('utf-8'))
        read_serial=str(ser.readline())
        print read_serial
        if "2001" in read_serial:
            #break
            return True
        time.sleep(2)


if __name__ == "__main__":
    #led = LED(2)
    ser = serial.Serial('/dev/ttyUSB0',9600)

    run = True
    queryString = "http://128.199.90.5/get/open"
    
    unlockString="1"
    lockString="0"
    
    while run == True:
    
        # query the api
        response = requests.get(queryString)
    
        if response.status_code == 200 and response.text == unlockString:
            print "response from api"
            sendUnlock()
    
            time.sleep(10)
        else:
            time.sleep(2)
    


