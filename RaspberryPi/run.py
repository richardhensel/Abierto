import time
import requests

from gpiozero import LED


run = True
queryString = "http://128.199.90.5/get/open"

unlockString="1"
lockString="0"

led = LED(2)

while run == True:

    # query the api
    response = requests.get(queryString)

    if response.status_code == 200 and response.text == unlockString:

        print "unlock"
        print "gpio high"
        led.on()
        #set gpio to high
        time.sleep(1)

        print "gpio low"
        led.off()
        #set gpio to low
        time.sleep(10)

    else:
        time.sleep(2)
    


