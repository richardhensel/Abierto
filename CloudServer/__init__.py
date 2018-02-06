from flask import Flask
app = Flask(__name__)


def setOpen(openCommand):
 #   try:
#        open('data/openState.txt', 'w')
    with open('/var/www/Flask/Abierto/data/openState.txt', 'w') as the_file:
        if openCommand == 1 or openCommand == 0:
            the_file.write(str(openCommand))
    return '1'
   # except IOError as e:
   #     return "I/O error({0}): {1}".format(e.errno, e.strerror)
   # except:
   #     return "Unexpected error:", sys.exc_info()[0]
    #return 'success'
#    except:
#        return "error with the file"

def getOpen():
    #try:
        with open('/var/www/Flask/Abierto/data/openState.txt', 'r') as f:
            first_line = f.readline()
        if first_line == '0' or first_line == '1':
            return first_line
        else:
            setOpen(0) ## to make sure that any badly formatted file entries are written over. 
            return '0'
    #except IOError as e:
    #    return "I/O error({0}): {1}".format(e.errno, e.strerror)
    #except:
    #    return "Unexpected error:", sys.exc_info()[0]

#@app.route("/")
#def hello():
#    return "Hello, Welcome to Abierto! 1\n"

@app.route("/set/open")
def setOpenEndpoint():
    #setOpen(1)
    status = setOpen(1)
    if status == '1':
        return "Successfully Recieved Command: Open \n"
    #return "Abren La Puerta! \n"    

@app.route("/get/open")
def getOpenEndpoint():
    #return getOpen()
    openCommand = getOpen()
    if openCommand == '1':
        setOpen(0)
        return '1'
    elif openCommand =='0':
        return '0'
    #else:
    #    return openCommand

if __name__ == "__main__":
    app.run()
