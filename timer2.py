from tkinter import *
from time import sleep

################# function##########
doTick=True
def press(v, b):
    global doTick
    doTick=True
    while v:
        if not doTick:
            return
        sleep(1)
        v-=1
        b.set(v)
        root.update()

def stop():
    global doTick
    doTick = False
    var1.set(var2.get())
    

#################
root = Tk()
l1 = Label(root, text='time input')
l1.grid(row=0, column=0)

var1 = StringVar()
e1 = Entry(root, textvariable=var1, width=8)
e1.grid(row=0,column=1)

b1 = Button(root, text='START', command= lambda:press(int(var1.get()), var2))
b1.grid(row=1, column=0, columnspan=2, sticky= E + W)

b2 = Button(root, text='Stop', command= stop)
b2.grid(row=2, column=0, columnspan=2, sticky= E + W)

var2 = StringVar()
var2.set('00')
l2 = Label(root, textvariable=var2)
l2.grid(row=3, column=0, columnspan=2, sticky= E + W)


root.mainloop()