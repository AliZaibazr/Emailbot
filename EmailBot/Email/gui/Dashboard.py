import time

from future.moves import tkinter
from selenium.webdriver.common.keys import Keys
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.realpath(__file__), '/home/ali/PycharmProjects/EmailBot')))
from tkinter import *
from start import Start
from Email.dependencies.Locators import Locators

def get_data():
    portip = port.get()
    hostt = host.get()
    print(portip)
    print(hostt)
    subject = emailSubject.get()
    emails = emailBCC.get("1.0", 'end-1c')
    end = Locators.en
    msg = Locators.msg
    email_list = emails.split(',')
    # print(email_list)
    Start.start(email_list,subject,portip,hostt, end, msg)
def client_exit():
    exit()

root = Tk()
root.geometry("600x600")

quitButton = Button(text="Quit", command=client_exit)
quitButton.place(x=500, y=500)

startButton = Button(text="Start", command=get_data)
startButton.place(x=400, y=500)

Subject_label = Label(text="Subject of email")
Subject_label.place(x=25, y=20)

emailSubject = Entry(bd="3")
emailSubject.place(x=25, y=50)


Host_label = Label(text="Host")
Host_label.place(x=230, y=20)

host = Entry(bd="1")
host.place(x=230, y=50)


port_label = Label(text="Port")
port_label.place(x=400, y=20)

port = Entry(bd="1")
port.place(x=400, y=50)



bcc_label = Label(text="Emails for BCC")
bcc_label.place(x=25, y=80)

emailBCC = Text(height=15, width=70)
emailBCC.pack()
emailBCC.place(x=20, y=100)

#size of the window

root.mainloop()