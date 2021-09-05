import tkinter as tk
from tkinter import  messagebox

def press():
    w = float(var1.get())
    h = float(var2.get())**2
    o = (w/h)
    var3.set(o)
    if o < 19:
        messagebox.showinfo('Analysis',  'you suffer from underweight!')
    elif 19<=int(o) & int(o) <= 24:
        messagebox.showinfo('Analysis', 'Congratulation! your weight is balanced!')
    else:
        messagebox.showinfo('Analysis', 'Sorry! you suffer from overweight!')        



root = tk.Tk()

tk.Label(root, text='Weight').grid(row=0, column=0)
var1 = tk.StringVar()
tk.Entry(root, textvariable=var1).grid(row=0, column=1)
tk.Label(root, text='Height').grid(row=1, column=0)
var2 = tk.StringVar()
tk.Entry(root, textvariable=var2).grid(row=1, column=1)
tk.Button(root, text='Calculation', command=press).grid(row=2, column=0)
var3 = tk.StringVar()
tk.Label(root, textvariable=var3).grid(row=2, column=1)

root.mainloop()