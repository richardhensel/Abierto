import time
import serial

#def sendUnlock():
#    ser.write('unlock'.encode('utf-8'))
#
#if __name__ == "__main__":
#    ser = serial.Serial('/dev/ttyACM0',9600)
#
#    s = [0,1]
#
#    while True:
#        sendUnlock()
#        read_serial=ser.readline()        
#        s[0] = str(ser.readline())
#        print s[0]
#        time.sleep(1)

def sendUnlock():
    s = [0,1]
    testAck = True
    while testAck == True:
        ser.write('unlock'.encode('utf-8'))
        read_serial=ser.readline()        
        s[0] = str(ser.readline())
        print s[0]
        if "unlock" in s[0]:
            testAck = False
            return True
        time.sleep(1)

if __name__ == "__main__":
    ser = serial.Serial('/dev/ttyACM0',9600)

    sendUnlock()
