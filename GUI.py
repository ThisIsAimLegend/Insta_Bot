from tkinter import *
from typing import Container, Sized
import time
from sys import exit
import test_file as tf
from actions.structural_actions import chooseAccounts
import insta_bot as ib
from main import one

root = Tk()


#funtions in GUI
def darkMode():
    root["bg"]="#000000"
    title["bg"]="#000000"
    title["fg"]="#ffffff"
    command1["bg"]="#000000"
    command1["fg"]="#ffffff"
    command2["bg"]="#000000"
    command2["fg"]="#ffffff"
    dark["bg"]="#000000"
    dark["fg"]="#ffffff"
    return

def lightMode():
    root["bg"]="#ffffff"
    title["bg"]="#ffffff"
    title["fg"]="#000000"
    command1["bg"]="#ffffff"
    command1["fg"]="#000000"
    command2["bg"]="#ffffff"
    command2["fg"]="#000000"
    dark["bg"]="#ffffff"
    dark["fg"]="#000000"
    return

#content of GUI
root.title("Instagram Bot")
title = Label(root, text="Bot Settings", )
command1 = Label(root, text="target account")
command2 = Label(root, text="number of bots")
dark = Label(root, text="Dark Mode")
on = Button(root, text="ON", command=darkMode)
off = Button(root, text="OFF", command=lightMode)
start = Button(root, text="START", command=one)

#styling of GUI
root.geometry("1100x800")
title["font"]="Ariel", 20

#placing elements
title.grid(row=0, column=0)
command1.grid(row=1, column=0,)
command2.grid(row=1, column=1)
dark.grid(row=2, column=0)
on.grid(row=2, column=1)
off.grid(row=2, column=2)
start.grid(row=3, column=0)


root.mainloop()
