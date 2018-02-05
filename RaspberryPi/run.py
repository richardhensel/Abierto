
import requests

run = True
queryString = "http:// "

unlockString="unlock"
lockString="lock"

while run == True:

    # query the api
    response = requests.get(queryString)

    if response.status_code == 200 and response == unlockString:
        #set gpio to high
        sleep(1)
        #set gpio to low
        sleep(10)

    else:
        sleep(2)
    


