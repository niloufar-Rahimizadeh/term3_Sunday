import tkinter as tk
from tkinter import font

root = tk.Tk()
root.geometry("300x300")
root.title("Registration")

################Lable
# tk.Label(root, text="Name", bg="yellow").grid(row=0, column=0)

################ The second way
l1 =tk.Label(root, text="Name", font="40",fg="red", bg="yellow", width=20, height=10)
l1.grid(row=0, column=0, padx=50, pady=50)
print(l1.config())
#############
root.mainloop()

