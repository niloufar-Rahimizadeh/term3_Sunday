from tkinter import *
from time import sleep

################# function##########

def press(v, b):
    while v:
        sleep(1)
        v-=1
        b.set(v)
        root.update()


#################
root = Tk()
l1 = Label(root, text='time input')
l1.grid(row=0, column=0)

var1 = StringVar()
e1 = Entry(root, textvariable=var1, width=8)
e1.grid(row=0,column=1)

b1 = Button(root, text='START', command= lambda:press(int(var1.get()), var2))
b1.grid(row=1, column=0, columnspan=2, sticky= E + W)
    
var2 = StringVar()
var2.set('00')
l2 = Label(root, textvariable=var2)
l2.grid(row=2, column=0, columnspan=2, sticky= E + W)


root.mainloop()