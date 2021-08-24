
from threading import Thread
import tkinter as tk
import tkinter.ttk as ttk
from time import sleep

def time_format(seconds):
    h = int(seconds/3600)
    tem = seconds % 3600
    m = tem/60
    s = tem % 60
    return "%02d:%02d:%02d" % (h, m, s)

def counter(seconds, var, button):
    button.configure(state = tk.DISABLED)
    while seconds:
        sleep(1)
        seconds -= 1
        var.set(time_format(seconds))
    button.config(state=tk.ACTIVE)

root = tk.Tk()
b1 = tk.Button(root, text='Start', command=lambda:counter(3800, t_1, b1)).grid(row=2, column=0)
t_1 = tk.StringVar()
t_1.set("00:00:00")
tk.Label(root, textvariable=t_1).grid(row=1, column=0)


root.mainloop()