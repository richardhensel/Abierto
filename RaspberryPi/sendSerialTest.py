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

#def sendUnlock():
#    s = [0,1]
#    testAck = True
#    while testAck == True:
#        ser.write('unlock'.encode('utf-8'))
#        read_serial=ser.readline()        
#        s[0] = str(ser.readline())
#        print s[0]
#        if "unlock" in s[0]:
#            testAck = False
#            return True
#        time.sleep(1)
#
#if __name__ == "__main__":
#    ser = serial.Serial('/dev/ttyACM0',9600)
#
#    sendUnlock()

class SerialManager:
    def __init__(self, tty, baud):
        self.ser = serial.Serial(tty, baud)
        self.packetReader = SerialPacketReader()


    def send(code):
        print "do nothing"

        ## transmit something

        ## listen for response

    def recieve():
        print "do nothing"
        ## listen for something
        
        ## send the response

    def transmitSingle(code):

        self.ser.write(code.encode('utf-8'))

    def listenSingle():
        success = False
        while not success:
            if self.ser.in_waiting():
                success = self.packetReader.readChar(self.ser.read)
        return self.packetReader.availablePacket
                

class SerialPacketReader:

    def __init__(self):
        self.packetSize = 4
        self.delimiter = '.'
    
        self.workingPacket = ''
        self.availablePacket = ''
        self.packetComplete = False

    def reset(self):
        self.workingPacket = ''
        self.packetComplete = False

    def readChar(self,char):
        if char.isdigit():
            if len(self.workingPacket) < self.packetSize:
                self.workingPacket += char
            else:
                self.reset()

        elif char == self.delimiter:
            if len(self.workingPacket) == self.packetSize:
                self.packetComplete = True
                self.availablePacket = self.workingPacket
            self.reset()

        return self.packetComplete


#def sendUnlock():
#    s = [0,1]
#    testAck = True
#    while testAck == True:
#        ser.write('unlock'.encode('utf-8'))
#        while ser.in_waiting():
#        
#        read_serial=ser.read() 
#        print s[0]
#        if "unlock" in s[0]:
#            testAck = False
#            return True
#        time.sleep(1)

if __name__ == "__main__":
    ser = serial.Serial('/dev/ttyACM0',9600)

    #ser.write('9000.')
    #ser.write('9000.'.encode('utf-8'))
    #print ser.readline()

    #charList = [u'9',u'0',u'0',u'0',u'.']
    #charList = ['9','0','0','0','.']
    #for char in charList:
    #    #ser.write(char.encode('utf-8'))
    #    time.sleep(0.1)
    #    print ser.readline()
       
    while True:
        ser.write('.9000.'.encode('utf-8'))
        print ser.readline()

 
#if __name__ == "__main__":
#    #ser = serial.Serial('/dev/ttyACM0',9600)
#    #sendUnlock()
#    packetReader = SerialPacketReader()
#
#    charlist = ['1','0','0','0','.','0','0','1','3','.','1','3','.','0','0','1','3','3']
#
#    for char in charlist:
#        print char
#        success = packetReader.readChar(char)
#        print packetReader.workingPacket
#        if success:
#            print packetReader.availablePacket
#            packetReader.reset()
