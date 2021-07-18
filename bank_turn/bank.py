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
    "op1": {
        "text": "Operator1",
        "width": 8,
        "height": 5,
        "bg": "light blue"
    },
    "op2": {
        "text": "Operator2",
        "width": 8,
        "height": 5,
        "bg": "light blue"
    },
    "op3": {
        "text": "Operator3",
        "width": 8,
        "height": 5,
        "bg": "light blue"
    },
    "lop1": {
        "textvariable": tk.StringVar(),
        "bg": "pink",
        "width": 8,
        "height": 5,
    },
    "lop2": {
        "textvariable": tk.StringVar(),
        "bg": "pink",
        "width": 8,
        "height": 5,
    },
    "lop3": {
        "textvariable": tk.StringVar(),
        "bg": "pink",
        "width": 8,
        "height": 5,
    }
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
tk.Label(customer, cnf=con["waiting"]).grid(row=1, column=0)
tk.Label(customer, cnf=con["time"]).grid(row=2, column=0)
tk.Label(customer, cnf=con["date"]).grid(row=3, column=0)

# ####################### operators ##############
operators = tk.Toplevel()
operators.geometry("500x200")
operators.title("operators")

tk.Button(operators, cnf=con["op1"]).grid(row=0, column=0, padx=35, pady=10)
tk.Button(operators, cnf=con["op2"]).grid(row=0, column=1, padx=35, pady=10)
tk.Button(operators, cnf=con["op3"]).grid(row=0, column=2, padx=35, pady=10)

tk.Label(operators, cnf=con["lop1"]).grid(row=1, column=0)
tk.Label(operators, cnf=con["lop2"]).grid(row=1, column=1)
tk.Label(operators, cnf=con["lop3"]).grid(row=1, column=2)


root.mainloop()
