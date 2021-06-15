from tkinter import *

dic = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violent': 7,
    'gray': 8,
    'white': 9
}


def press():
    number1 = int(dic[num1.get()])
    number2 = int(dic[num2.get()])
    number3 = int(dic[num3.get()])
    out = (number1*10 + number2)*(10**number3)
    var.set(out)


root = Tk()
root.configure(bg='light green')
l1 = Label(root, text='First Color: ', bg='light green')
l1.place(x=7, y=0)

num1 = StringVar()
e1 = Entry(root, textvariable=num1, width=5)
e1.place(x=97, y=0)

l2 = Label(root, text='Second Color: ', bg='light green')
l2.place(x=0, y=30)

num2 = StringVar()
e2 = Entry(root, textvariable=num2, width=5)
e2.place(x=97, y=30)

l3 = Label(root, text='Third Color: ', bg='light green')
l3.place(x=6, y=60)

num3 = StringVar()
e3 = Entry(root, textvariable=num3, width=5)
e3.place(x=97, y=60)

b1 = Button(root, text="Calculate", command=press, bg='light pink')
b1.place(x=57, y=90)

var = StringVar()
var.set("00")
l4 = Label(root, textvariable=var, bg='orange', width=10)
l4.place(x=60, y=120)
root.mainloop()