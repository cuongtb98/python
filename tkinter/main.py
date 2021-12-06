from tkinter import *
from tkinter import ttk
root = Tk()
e = Entry(root)
e.grid(row=5)
# ============= defind variable =============
# Lable
Label1 = Label(root, text="Hello Cuong")

# function
def getName():
    Label_get_name = Label(root, text="Hello: " + e.get())
    Label_get_name.grid()

# button
Button1 = Button(root, text="Click me!", command=getName)
Button2 = Button(root, text="Quit", command=root.destroy)

# ============= end defind variable =============

Button1.grid(column=0, row=0)


Label1.grid(column=0, row=1)




Button2.grid(column=0, row=2)
root.geometry("200x200")
root.mainloop()