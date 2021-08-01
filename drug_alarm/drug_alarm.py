import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('200x200')

note = ttk.Notebook(root)
note.grid(row=0, column=0)
patients = ttk.Frame(note)
note.add(patients, text="patients")
timer = ttk.Frame(note)
note.add(timer, text="timer")

lf1 = tk.LabelFrame(patients, text="Patient 1")
lf1.grid(row=0, column=0)
tk.Label(lf1, text="Name").grid(row=0, column=0)
tk.Label(lf1, text="Time").grid(row=1, column=0)
root.mainloop()