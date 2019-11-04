import datetime
# from tkinter import *
#
#
# def get_emails():
#     emails = emailBCC.get()
#
#
# class Window(Frame):
#
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.master = master
#         self.init_window()
#
#     #Creation of init_window
#     def init_window(self):
#
#         # changing the title of our master widget
#         self.master.title("Email Automation Robot")
#
#         # allowing the widget to take the full space of the root window
#         self.pack(fill=BOTH, expand=1)
#
#         # creating a button instance
#         quitButton = Button(self, text="Quit", command=self.client_exit)
#         quitButton.place(x=500, y=500)
#
#         startButton = Button(self, text="Start", command=get_emails)
#         startButton.place(x=400, y=500)
#
#         Subject_label = Label(self, text="Subject of email")
#         Subject_label.place(x=25, y=20)
#
#
#         emailSubject = Entry(self, bd="3")
#         emailSubject.place(x=25, y=50)
#
#         bcc_label = Label(self, text="Emails for BCC")
#         bcc_label.place(x=25, y=80)
#
#         emailBCC = Text(self, height=15, width=70)
#         emailBCC.pack()
#         emailBCC.place(x=20, y=100)
#
#     def client_exit(self):
#         exit()
# root = Tk()
#
# #size of the window
# root.geometry("600x600")
#
# app = Window(root)
# root.mainloop()
end = "2019-11-03 21:42:43.053036"
end2 = "2019-11-03 22:39:26.193686"
end3 = "2019-11-03 22:41:10.683584"
now = datetime.datetime.now()
print(str(now))
# print(str(now.month))
# print(str(now.day))
if end2 < end3:
    print("in")
else:
    print('out')
# a = ['0','1','2','3','4','5','6','7','8','9','a','s','d','u','v']
# y=0
# for x in range(5):
#     while a:
#         print(a.pop(-1))
#         print(a)
#         y=y+1
#         if y == 3:
#             break
#     print('yes')
#     y=0
#     time.sleep(5)
#
# print('out')
# y=0
# # r=0
# le=(len(x))
# rang1= 0
# rang2= 3
# # chunk = 5
# # limit = le/chunk
# # v = int(limit)
# count = 0
# for z in range(5):
#     for x in range(rang1, rang2):
#         # print(y)
#         if y == 3:
#             break
#         y = y+1
#
#         # print(y)
#         print(x)
#
#
#         # r=+3
#         # v=+3
#     print('1st 3')
#     y=0
#     rang1 = rang1 + 3
#     rang2 = rang2 + 3