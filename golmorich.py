#! /usr/bin/python3.6

import os
import tkinter as tk
import tkinter.filedialog

filename = None

def newFile():
    global filename
    filename = None
    text.delete(0.0, tk.END)

def saveFile():
    global filename
    if filename == None:
        filename = tk.filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if filename is not None:
        t = text.get(0.0, tk.END)
        filename.write(t)

def saveAs():
    f = tk.filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, tk.END)
    f.write(t.rstrip())
    f.close()

def openFile():
    global filename
    filename = tk.filedialog.askopenfile(mode = 'r+')
    t = filename.read()
    text.delete(0.0, tk.END)
    text.insert(0.0, t)

root = tk.Tk()
root.title("Golmorich Text Editor | Version 1.0")
root.minsize(width=800, height=800)
root.maxsize(width=800, height=800)

text = tk.Text(root, width=800, height=800)
text.pack()

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label= "Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()