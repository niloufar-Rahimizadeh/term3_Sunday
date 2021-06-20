import tkinter as tk
root = tk.Tk()
root.geometry("300x300")
root.title("Page 1")
root.configure(bg='#b08d8b')
l1 = tk.Label(root, text="Name: ")
l1.grid(row=0, column=0)
e1 = tk.Entry(root, bg="#e60707")
e1.grid(row=0, column=1)
l2 = tk.Label(root, text="Family: ")
l2.grid(row=1, column=0)
e2 = tk.Entry(root, bg="#e60707")
e2.grid(row=1, column=1)
l3 = tk.Label(root, text="Age: ")
l3.grid(row=2, column=0)
s1 = tk.Spinbox(root, from_=20, to=25, wrap=True, state="readonly")
s1.grid(row=2, column=1)
root.mainloop()



