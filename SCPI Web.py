import eel
import visa
import visa_instrument as vi
import random
# rm = visa.ResourceManager()
# instrumentation = rm.list_resources()
# wfg = rm.open_resource('USB0::0x0957::0x1607::MY50003327::INSTR') //old code
# print(instrumentation)
#VISA section
instList = vi.InstrumentList()  #create instance of visa instrument list
instruments = instList.instruments  #this creates an array of the instrument visa addresses

@eel.expose                         # Expose this function to Javascript
def sendInst():
    return(instruments)
@eel.expose
def py_random():
    return random.random()

def print_num(n):
    print('Got this from Javascript:', n)

@eel.expose
def idnButton():
    print("IDN pressed")
    # myInstID = wfg.query('*IDN?')
    # print(myInstID)
    # eel.printResponse('\n' + myInstID)
    eel.sendDropDown()(output)


def output(outputValue):
    print(outputValue)
eel.init('web', allowed_extensions=['.js', '.html'])
eel.init('static_web_folder')
eel.start('SCPI.html', size=(550,550))
