import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import easygui as g
# Root window
root = tk.Tk()
root.title('Display a Text File')
root.resizable(False, False)
root.geometry('550x250')

# Text editor
text = tk.Text(root, height=12)
text.grid(column=0, row=0, sticky='nsew')


def open_text_file():
    # file type
    

    title = 'Choose your destiny'
    filename = g.fileopenbox( title )

    file = open( filename )

    # read the text file and show its content on the Text
    text.insert(file.read(),encoding ='utf-8')


# open file button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=open_text_file
)

open_button.grid(column=0, row=1, sticky='w', padx=10, pady=10)


root.mainloop()