import tkinter as tk

# ##############functions #############





# ################### root window ##################

root = tk.Tk()
root.geometry("200x250")
root.title("turning")

con = {
    "turning": {
        "textvariable": tk.StringVar(),
    },
    "waiting": {
        "textvariable": tk.StringVar(),
    },
    "time": {
        "textvariable": tk.StringVar(),
    },
    "date": {
        "textvariable": tk.StringVar(),
    },
}

b1 = tk.Button(root, text="Get a number")
b1.grid(row=0, column=0)
b1 = tk.Button(root, text="Get a number", height=5)
b1.grid(row=0, column=0, padx=45, pady=15)
b2 = tk.Button(root, text="Cancel", height=5, width=11, command=root.destroy)
b2.grid(row=1, column=0)
# ######################## customers #############
customer = tk.Toplevel()
customer.geometry("200x200")
customer.title("customer")
tk.Label(customer, cnf=con["turning"]).grid(row=0, column=0)
tk.Label(customer).grid(row=1, column=0)
tk.Label(customer).grid(row=2, column=0)
tk.Label(customer).grid(row=3, column=0)

# ####################### operators ##############
operators = tk.Toplevel()
operators.geometry("500x200")
operators.title("operators")

root.mainloop()
