import tkinter as tk
from tkinter.constants import  E

def print_name(b1):
    print("Hello!")

root = tk.Tk()
root.title("Information")

root.resizable(1, 1)
l1 = tk.Label(root, text="Name")
l1.grid(row=0, column=0)
e1 = tk.Entry(root)
e1.grid(row=0, column=1)
b1 = tk.Button(root, text='show', command= lambda: print_name(b1))
b1.grid(row=2, column=0, columnspan=2, sticky=tk.E + tk.W)
################
tk.mainloop()

