import tkinter as tk

expression = ''
def press(i):
    global expression
    expression = expression + i
    var.set(expression)

def clear():
    global expression
    expression = ''
    var.set(expression)

def equal():
    ex = var.get()
    if '+' in ex:
        ex_list = ex.split('+')
        tem = int(ex_list[0])+int(ex_list[1])
        var.set(tem)
    elif '-' in ex:
        ex_list = ex.split('-')
        tem = int(ex_list[0])-int(ex_list[1])
        var.set(tem)
    elif '/' in ex:
        ex_list = ex.split('/')
        tem = int(ex_list[0])/int(ex_list[1])
        var.set(tem)
    elif '*' in ex:
        ex_list = ex.split('*')
        tem = int(ex_list[0])*int(ex_list[1])
        var.set(tem)




root = tk.Tk()

var = tk.StringVar()
tk.Entry(root, textvariable=var, width=30).grid(row=0, column=0)

f = tk.Frame(root)
f.grid(row=1, column=0)
tk.Button(f, text=' 1 ', command= lambda: press('1')).grid(row=0,column=0)
tk.Button(f, text=' 2 ', command= lambda: press('2')).grid(row=0,column=1)
tk.Button(f, text=' 3 ', command= lambda: press('3')).grid(row=0,column=2)
tk.Button(f, text=' C ', command=clear).grid(row=0,column=3)
tk.Button(f, text=' 4 ', command= lambda: press('4')).grid(row=1,column=0)
tk.Button(f, text=' 5 ', command= lambda: press('5')).grid(row=1,column=1)
tk.Button(f, text=' 6 ', command= lambda: press('6')).grid(row=1,column=2)
tk.Button(f, text=' + ', command= lambda: press('+')).grid(row=1,column=3)
tk.Button(f, text=' 7 ', command= lambda: press('7')).grid(row=2,column=0)
tk.Button(f, text=' 8 ', command= lambda: press('8')).grid(row=2,column=1)
tk.Button(f, text=' 9 ', command= lambda: press('9')).grid(row=2,column=2)
tk.Button(f, text=' - ', command= lambda: press('-')).grid(row=2,column=3)
tk.Button(f, text=' . ', command= lambda: press('.')).grid(row=3,column=0)
tk.Button(f, text=' = ', command=equal).grid(row=3,column=1)
tk.Button(f, text=' / ', command= lambda: press('/')).grid(row=3,column=2)
tk.Button(f, text=' * ', command= lambda: press('*')).grid(row=3,column=3)

root.mainloop()