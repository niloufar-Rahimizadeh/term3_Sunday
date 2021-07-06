import tkinter as tk


root = tk.Tk()
root.geometry("200x250")
root.title("turning")
b1 = tk.Button(root, text="Get a number")
b1.grid(row=0, column=0)
b1 = tk.Button(root, text="Get a number", height=5)
b1.grid(row=0, column=0, padx=45, pady=15)

b2 = tk.Button(root, text="Cancel", height=5, width=11)
b2.grid(row=1, column=0)
root.mainloop()
