from tkinter import *
from tkinter import ttk
root = Tk()

# ============= defind variable =============
# Lable
Label1 = Label(root, text="Hello Cuong")
Label2 = Label(root, text="Do you like Python")
Label3 = Label(root, text="Let go")

# button
Button1 = Button(root, text="Click me!")
Button2 = Button(root, text="Quit")

# ============= end defind variable =============

Button1.grid(column=0, row=0)
Button2.grid(column=0, row=2)
# Label1.grid(column=0, row=0)
Label2.grid(column=0, row=1)
# Label3.grid(column=0, row=2)


root.geometry("200x200")
root.mainloop()