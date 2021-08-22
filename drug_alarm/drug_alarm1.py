import tkinter
import tkinter as tk
import tkinter.ttk as ttk
from time import sleep
# function
def callback1(a, b, c):
    n1.set(var1.get())

def callback2(a, b, c):
    n2.set(var2.get())

def callback3(a, b, c):
    n3.set(var3.get())

def callback_t_1(a, b, c):
    h1 = int(h_p_1.get())
    m1 = int(m_p_1.get())
    s1 = int(s_p_1.get())
    t_1.set('%02d:%02d:%02d'%(h1, m1, s1))

def callback_t_2(a, b, c):
    h2 = int(h_p_2.get())
    m2 = int(m_p_2.get())
    s2 = int(s_p_2.get())
    t_2.set('%02d:%02d:%02d'%(h2, m2, s2))

def callback_t_3(a, b, c):
    h3 = int(h_p_3.get())
    m3 = int(m_p_3.get())
    s3 = int(s_p_3.get())
    t_3.set('%02d:%02d:%02d'%(h3, m3, s3)) # 12:30:30
################################
def time_format():
    pass

def counter(seconds, var, button):
    button.config(state=tk.DISABLED)
    while seconds:
        sleep(1)
        seconds -= 1
        var.set(time_format(seconds))
    button.config(state=tk.ACTIVE)
###############################
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
h_p_1 = tk.StringVar()
h_p_1.set("12")
tk.Spinbox(t1, textvariable=h_p_1, from_=0, to=23, state='readonly', wrap=True, width=2).grid(row=0, column=0)
m_p_1 = tk.StringVar()
m_p_1.set("30")
tk.Spinbox(t1, textvariable=m_p_1, from_=0, to=59, state='readonly', wrap=True, width=2).grid(row=0, column=1)
s_p_1 = tk.StringVar()
s_p_1.set("30")
tk.Spinbox(t1, textvariable=s_p_1, from_=0, to=59, state='readonly', wrap=True, width=2).grid(row=0, column=2)
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
h_p_2 = tk.StringVar()
h_p_2.set('12')
tk.Spinbox(t2, textvariable=h_p_2, from_=0, to=23, state='readonly', wrap=True, width=2).grid(row=0, column=0)
m_p_2 = tk.StringVar()
m_p_2.set('30')
tk.Spinbox(t2, textvariable=m_p_2, from_=0, to=59, state='readonly', wrap=True, width=2).grid(row=0, column=1)
s_p_2 = tk.StringVar()
s_p_2.set('30')
tk.Spinbox(t2, textvariable=s_p_2, from_=0, to=59, state='readonly', wrap=True, width=2).grid(row=0, column=2)
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
h_p_3 = tk.StringVar()
h_p_3.set("12")
tk.Spinbox(t3, textvariable=h_p_3, from_=0, to=23, state='readonly', wrap=True, width=2).grid(row=0, column=0)
m_p_3 = tk.StringVar()
m_p_3.set("30")
tk.Spinbox(t3, textvariable=m_p_3, from_=0, to=59, state='readonly', wrap=True, width=2).grid(row=0, column=1)
s_p_3 = tk.StringVar()
s_p_3.set("30")
tk.Spinbox(t3, textvariable=s_p_3, from_=0, to=59, state='readonly', wrap=True, width=2).grid(row=0, column=2)
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
# the second row of timer
t_1 = tk.StringVar()
t_1.set("00:00:00")
tk.Label(timer, textvariable=t_1).grid(row=1, column=0)
t_2 = tk.StringVar()
t_2.set("00:00:00")
tk.Label(timer, textvariable=t_2).grid(row=1, column=1)
t_3 = tk.StringVar()
t_3.set("00:00:00")
tk.Label(timer, textvariable=t_3).grid(row=1, column=2)
# the third row of timer
tk.Button(timer, text='Start').grid(row=2, column=0)
tk.Button(timer, text='Start').grid(row=2, column=1)
tk.Button(timer, text='Start').grid(row=2, column=2)
##############
h_p_1.trace("w", callback_t_1)
m_p_1.trace("w", callback_t_1)
s_p_1.trace("w", callback_t_1)
h_p_2.trace("w", callback_t_2)
m_p_2.trace("w", callback_t_2)
s_p_2.trace("w", callback_t_2)
h_p_3.trace("w", callback_t_3)
m_p_3.trace("w", callback_t_3)
s_p_3.trace("w", callback_t_3)

root.mainloop()
