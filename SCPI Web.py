import eel
import visa
import random
rm = visa.ResourceManager()
instrumentation = rm.list_resources()
# print(instrumentation)

@eel.expose                         # Expose this function to Javascript
def sendInst():
    return(instrumentation)
@eel.expose
def py_random():
    return random.random()

def print_num(n):
    print('Got this from Javascript:', n)


eel.init('web', allowed_extensions=['.js', '.html'])
eel.init('static_web_folder')
eel.start('SCPI.html', size=(500,500))
