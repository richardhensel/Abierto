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
    s = [0,1]
    testAck = True
    while testAck == True:
        ser.write('50100.'.encode('utf-8'))
        read_serial=ser.readline()
        s[0] = str(ser.readline())
        print s[0]
        if "unlock" in s[0]:
            testAck = False
            return True
        time.sleep(2)


if __name__ == "__main__":
    #led = LED(2)
    ser = serial.Serial('/dev/ttyACM0',9600)

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
    


