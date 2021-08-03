from tkinter import *
from typing import Container

root = Tk()

root.title("Instagram Bot")
root.geometry("400x300")

title_frame = Frame(root, width="300",height=20, borderwidth=2,relief="sunken")
title_frame.pack(anchor="center")
#title_frame.grid(row=1,column=1,columnspan=2)

settings_frame = Frame(root, width="300", borderwidth=2,relief="ridge")
settings_frame.pack(side="top")
#settings_frame.grid(row=2,column=1,columnspan=2)



title = Label(title_frame,text="Bot Einstellungen")
title.grid(row=1,column=1,pady=2,padx=2)

target_label = Label(settings_frame,text="Ziel Account: ", borderwidth=2,relief="ridge")
target_label.grid(row=2,column=1)

target_label = Label(settings_frame,text="Ziel Account: ", borderwidth=2,relief="ridge")
target_label.grid(row=2,column=1)

target_input = Entry(settings_frame)
target_input.grid(row=2,column=2)

root.mainloop()
