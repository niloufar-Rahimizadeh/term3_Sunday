import tkinter as tk
import tkinter.ttk as ttk

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
tk.Entry(lf1, width=10).grid(row=0, column=1)
tk.Label(lf1, text="Time").grid(row=1, column=0)

# patient 2
lf2 = tk.LabelFrame(patients, text="Patient 2")
lf2.grid(row=1, column=0)
tk.Label(lf2, text="Name").grid(row=0, column=0)
tk.Entry(lf2, width=10).grid(row=0, column=1)
tk.Label(lf2, text="Time").grid(row=1, column=0)
# patient 3
lf3 = tk.LabelFrame(patients, text="Patient 3")
lf3.grid(row=2, column=0)
tk.Label(lf3, text="Name").grid(row=0, column=0)
tk.Entry(lf3, width=10).grid(row=0, column=1)
tk.Label(lf3, text="Time").grid(row=1, column=0)
#################################

root.mainloop()