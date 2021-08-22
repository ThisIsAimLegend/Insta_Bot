from tkinter import *
from typing import Container, Sized
import time

def output():
    from ProcessManagement import ProcessManager
    account = acc.get()
    account = account.split(",")
    bots = bot_num.get()
    likes = like_num.get()
    comments = com_num.get()
    comsperpost = cpp.get()
    topics = topic.get()
    if account == "":
        print("You need to select a tageted account")
    elif bots == "":
        bots = None
    elif likes == "":
        likes = None
    elif comments == 0:
        ProcessManager(account,bots,likes,comments,0,"")
    else:
        pass
    ProcessManager(account,bots,likes,comments,comsperpost,topics)

def restart():
    root.destroy()


if __name__ == "__main__":
    #creating standard sizes
    elem_width = 20
    input_width = 21
    rl = "flat"  

    #functions in GUI
    def darkMode():
        root["bg"]="#000000"
        title["bg"]="#000000"
        title["fg"]="#ffffff"
        command1["bg"]="#000000"
        command1["fg"]="#ffffff"
        command2["bg"]="#000000"
        command2["fg"]="#ffffff"
        command3["bg"]="#000000"
        command3["fg"]="#ffffff"
        command4["bg"]="#000000"
        command4["fg"]="#ffffff"
        command5["bg"]="#000000"
        command5["fg"]="#ffffff"
        command6["bg"]="#000000"
        command6["fg"]="#ffffff"
        dark["bg"]="#000000"
        dark["fg"]="#ffffff"

        acc.configure(bg="gray50",fg="white")
        bot_num.configure(bg="gray50",fg="white")
        like_num.configure(bg="gray50",fg="white")
        com_num.configure(bg="gray50",fg="white")
        cpp.configure(bg="gray50",fg="white")
        topic.configure(bg="gray50",fg="white")

        on.configure(bg="gray30",fg="white")
        off.configure(bg="gray30",fg="white")
        start.configure(bg="gray30",fg="white")
        close.configure(bg="gray30",fg="white")


    def lightMode():
        root["bg"]=defaultbg
        title["bg"]=defaultbg
        title["fg"]="#000000"
        command1["bg"]=defaultbg
        command1["fg"]="#000000"
        command2["bg"]=defaultbg
        command2["fg"]="#000000"
        command3["bg"]=defaultbg
        command3["fg"]="#000000"
        command4["bg"]=defaultbg
        command4["fg"]="#000000"
        command5["bg"]=defaultbg
        command5["fg"]="#000000"
        command6["bg"]=defaultbg
        command6["fg"]="#000000"
        dark["bg"]=defaultbg
        dark["fg"]="#000000"

        acc.configure(bg="white",fg="black")
        bot_num.configure(bg="white",fg="black")
        like_num.configure(bg="white",fg="black")
        com_num.configure(bg="white",fg="black")
        cpp.configure(bg="white",fg="black")
        topic.configure(bg="white",fg="black")

        on.configure(bg=defaultbg,fg="black")
        off.configure(bg=defaultbg,fg="black")
        start.configure(bg=defaultbg,fg="black")
        close.configure(bg=defaultbg,fg="black")


    #creating the GUI
    root = Tk()
    defaultbg = root.cget('bg')
        
    #content of GUI
    root.title("Instagram Bot")
    title = Label(root, text="Bot Settings")
    command1 = Label(root, text="target account", width=elem_width,relief=rl)
    command2 = Label(root, text="number of bots", width=elem_width,relief=rl)
    command3 = Label(root, text="number of likes", width=elem_width,relief=rl)
    command4 = Label(root, text="number of comments", width=elem_width,relief=rl)
    command5 = Label(root, text="number of comments p.p.", width=elem_width,relief=rl)
    command6 = OptionMenu(root, "Kunst","Sport","Freunde","Girls","Influencer", width=elem_width,relief=rl)
    dark = Label(root, text="Dark Mode")
    on = Button(root, text="ON", command=darkMode,width=input_width)
    off = Button(root, text="OFF", command=lightMode,width=input_width)
    acc = Entry(root,width=input_width)
    bot_num = Entry(root,width=input_width)
    like_num = Entry(root,width=input_width)
    com_num = Entry(root,width=input_width)
    cpp = Entry(root,width=input_width)
    topic = Entry(root,width=input_width)
    start = Button(root, text="START", command=output)
    close = Button(root,text="CLOSE", command=root.destroy)

    #styling of GUI
    root.geometry("900x200")
    title["font"]="Ariel", 20

    #placing elements
    title.grid(row=0, column=0,columnspan=6)
    command1.grid(row=3, column=0,sticky="nesw")
    command2.grid(row=3, column=1,sticky="nesw")
    command3.grid(row=3, column=2,sticky="nesw")
    command4.grid(row=3, column=3,sticky="nesw")
    command5.grid(row=3, column=4,sticky="nesw")
    command6.grid(row=3, column=5,sticky="nesw")
    dark.grid(row=1, column=0,columnspan=2)
    on.grid(row=2, column=0,sticky="nws")
    off.grid(row=2, column=1,sticky="nws")
    acc.grid(row=4,column=0,sticky="nesw")
    bot_num.grid(row=4,column=1,sticky="nesw")
    like_num.grid(row=4,column=2,sticky="nesw")
    com_num.grid(row=4,column=3,sticky="nesw")
    cpp.grid(row=4,column=4,sticky="nesw")
    topic.grid(row=4,column=5,sticky="nesw")
    start.grid(row=5, column=0,columnspan=6,sticky="nesw",pady=(10,0))
    close.grid(row=6,column=0,columnspan=6,sticky="nesw")

    #creates mainloop
    root.mainloop()
