#------------------------------------------------------------------------------------------------------------------#
# Python Project Name   : SCPI Command Debugger
# Creator               : Jason Folding
# Date                  : 15/02/2019
#
#-------------------------------------------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk
from instListModule import *
#from visa_comm import *
#import instListClass as ilc

root = Tk()

root.title("SCPI Command Debugger")
#Variables
cmdButtons = ["READ", "WRITE", "QUERY"]
textoutput = ""
command = ""
recievedText = ""




##Functions
def btnPress(cmd):
    #print(cmdButtons[cmdButtons.index(cmd)])
    if cmdButtons.index(cmd) == 0:
        print("read was pressed")
        inst = getInst()
        scope = vi.Instrument(inst)
        recievedText = (scope.sendRead())
        writeToWindow(recievedText)
        #writeToWindow(cmdButtons[cmdButtons.index(cmd)])
    elif cmdButtons.index(cmd) == 1:
        writeToWindow("Write was pressed")
        command = commandEntry.get()
        print(command)
        inst = getInst()
        scope = vi.Instrument(inst)
        scope.sendCommand(command)
    elif cmdButtons.index(cmd) == 2:
        print("query was pressed")
        command = commandEntry.get()
        print(command)
        inst = getInst()
        scope = vi.Instrument(inst)
        recievedText=(scope.sendQuery(command))
        writeToWindow(recievedText)

def writeToWindow(textoutput):
    textDisplay.configure(state="normal")
    textDisplay.insert(END, textoutput +"\n")
    textDisplay.see("end")
    textDisplay.configure(state="disabled")
#Create Notebook and tabs
tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='SCPI')
tab_control.add(tab2, text='Instrument Setup')
#page = ilc.instList(tab2)
createInstList(tab2)





#placeholder labels
'''lbl1 = Label(f1, text="SCPI Command:")
lbl1.grid(column=0, row=0)
lbl2 = Label(tab2, text='label2')
lbl2.grid(column=0, row=0)'''

#Pack Notebook
tab_control.pack(expand=1, fill='both')
#Create new frames
f1 = Frame(tab1, padx=5, pady=5)
f2 = Frame(tab1, padx=5, pady=5)
f3 = Frame(tab1, padx=5, pady=5)
f1.pack()
f2.pack()
f3.pack()
##Labels
lbl1 = Label(f1, text="SCPI Command:").pack()

## Start coding here
#Setup Entry Box
commandEntry = Entry(f1, width=50)
commandEntry.pack(fill=X)
commandEntry.focus_set()

#Setup Buttons
for cmd in cmdButtons:
    button = Button(f2, text=cmd, padx=7, pady=3, command=lambda c=cmd: btnPress(c))
    button.grid(row=1, column=cmdButtons.index(cmd))

#Setup text display box
textDisplay = Text(f3, width=50, height=5)
s = Scrollbar(f3, command=textDisplay.yview)
textDisplay.configure(state="disabled")   #to prevent user from entering text
textDisplay.pack(side=LEFT)
s.pack(side=RIGHT)

## END
root.mainloop()
