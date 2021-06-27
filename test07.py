import tkinter as tk
from tkinter.ttk import Combobox
# function
def press():
    f = open("information.txt", "a")
    f.write(f"name: {var1.get()}, family:{var2.get()}, age:{var3.get()}, country: {var6.get()}")
    f.close()
###################################


root = tk.Tk()
root.geometry("300x300")
root.title("Page 1")
root.configure(bg='#b08d8b')

################ first row
l1 = tk.Label(root, text="Name: ", bg='#b08d8b')
l1.grid(row=0, column=0)
var1 = tk.StringVar()
e1 = tk.Entry(root, textvariable=var1, bg='#b08d8b')
e1.grid(row=0, column=1)
############### second row
l2 = tk.Label(root, text="Family: ", bg='#b08d8b')
l2.grid(row=1, column=0)
var2 = tk.StringVar()
e2 = tk.Entry(root, textvariable=var2, bg='#b08d8b')
e2.grid(row=1, column=1)
############### third row
l3 = tk.Label(root, text="Age: ", bg='#b08d8b')
l3.grid(row=2, column=0)
var3 = tk.StringVar()
s1 = tk.Spinbox(root, textvariable=var3, from_=20, to=25, wrap=True, state="readonly")
s1.grid(row=2, column=1)
############## forth row
l4 = tk.Label(root, text="Gender: ", bg='#b08d8b')
l4.grid(row=3, column=0)
r1 = tk.Radiobutton(root, text="Female", value=0, bg='#b08d8b')
r1.grid(row=3, column=1)
############# fifth row
r2 = tk.Radiobutton(root, text="male", value=1, bg='#b08d8b')
r2.grid(row=4, column=1)
l5 = tk.Label(root, text="Country: ", bg='#b08d8b')
l5.grid(row=5, column=0)

var6 = tk.StringVar()
c1 = Combobox(root, textvariable=var6, values=["Iran", "Netherlands", "France"])
c1.grid(row=5, column=1)

b1 = tk.Button(root, text="Save", command= press())
b1.grid(row=6, column=0, columnspan=2, sticky="we")
root.mainloop()



