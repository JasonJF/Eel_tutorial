import eel
import visa

rm = visa.ResourceManager()
instrumentation = rm.list_resources()
# print(instrumentation)

@eel.expose                         # Expose this function to Javascript
def sendInst():
    return(instrumentation)

eel.init('web', allowed_extensions=['.js', '.html'])
eel.init('static_web_folder')
eel.start('SCPI.html')
