import eel
import visa
import random
rm = visa.ResourceManager()
instrumentation = rm.list_resources()
wfg = rm.open_resource('USB0::0x0957::0x1607::MY50003327::INSTR')
# print(instrumentation)

@eel.expose                         # Expose this function to Javascript
def sendInst():
    return(instrumentation)
@eel.expose
def py_random():
    return random.random()

def print_num(n):
    print('Got this from Javascript:', n)

@eel.expose
def idnButton():
    print("IDN pressed")
    myInstID = wfg.query('*IDN?')
    print(myInstID)



eel.init('web', allowed_extensions=['.js', '.html'])
eel.init('static_web_folder')
eel.start('SCPI.html', size=(550,550))
