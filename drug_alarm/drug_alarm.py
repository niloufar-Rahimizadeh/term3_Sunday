import tkinter as tk
import tkinter.ttk as ttk

# function
def callback1(a, b, c):
    n1.set(var1.get())

def callback2(a, b, c):
    n2.set(var2.get())

def callback3(a, b, c):
    n3.set(var3.get())
################################
root = tk.Tk()
root.geometry('240x240')

note = ttk.Notebook(root)
note.grid(row=0, column=0)
patients = ttk.Frame(note)
note.add(patients, text="patients")
timer = ttk.Frame(note)
note.add(timer, text="timer")
# patient 1
lf1 = tk.LabelFrame(patients, text="Patient 1")
lf1.grid(row=0, column=0)
tk.Label(lf1, text="Name").grid(row=0, column=0)
var1 = tk.StringVar()
var1.trace("w", callback1)
tk.Entry(lf1, textvariable=var1, width=10).grid(row=0, column=1)
tk.Label(lf1, text="Time").grid(row=1, column=0)
t1 = tk.Frame(lf1)
t1.grid(row=1, column=1)
tk.Spinbox(t1, from_=0, to=23, state='readonly', wrap=True, width=2).grid(row=0, column=0)
tk.Spinbox(t1, from_=0, to=59, state='readonly', wrap=True, width=2).grid(row=0, column=1)
tk.Spinbox(t1, from_=0, to=59, state='readonly', wrap=True, width=2).grid(row=0, column=2)
# patient 2
lf2 = tk.LabelFrame(patients, text="Patient 2")
lf2.grid(row=1, column=0)
tk.Label(lf2, text="Name").grid(row=0, column=0)
var2 = tk.StringVar()
var2.trace("w", callback2)
tk.Entry(lf2, textvariable=var2, width=10).grid(row=0, column=1)
tk.Label(lf2, text="Time").grid(row=1, column=0)
t2 = tk.Frame(lf2)
t2.grid(row=1, column=1)
tk.Spinbox(t2, from_=0, to=23, state='readonly', wrap=True, width=2).grid(row=0, column=0)
tk.Spinbox(t2, from_=0, to=59, state='readonly', wrap=True, width=2).grid(row=0, column=1)
tk.Spinbox(t2, from_=0, to=59, state='readonly', wrap=True, width=2).grid(row=0, column=2)
#
# patient 3
lf3 = tk.LabelFrame(patients, text="Patient 3")
lf3.grid(row=2, column=0)
tk.Label(lf3, text="Name").grid(row=0, column=0)
var3 = tk.StringVar()
var3.trace("w", callback3)
tk.Entry(lf3, textvariable=var3, width=10).grid(row=0, column=1)
tk.Label(lf3, text="Time").grid(row=1, column=0)
t3 = tk.Frame(lf3)
t3.grid(row=1, column=1)
tk.Spinbox(t3, from_=0, to=23, state='readonly', wrap=True, width=2).grid(row=0, column=0)
tk.Spinbox(t3, from_=0, to=59, state='readonly', wrap=True, width=2).grid(row=0, column=1)
tk.Spinbox(t3, from_=0, to=59, state='readonly', wrap=True, width=2).grid(row=0, column=2)
################Timer#################
# the first row of timer
n1 = tk.StringVar()
n1.set("Patient1")
tk.Label(timer, textvariable=n1).grid(row=0, column=0)
n2 = tk.StringVar()
n2.set("Patient2")
tk.Label(timer, textvariable=n2).grid(row=0, column=1)
n3 = tk.StringVar()
n3.set("Patient3")
tk.Label(timer, textvariable=n3).grid(row=0, column=2)
root.mainloop()