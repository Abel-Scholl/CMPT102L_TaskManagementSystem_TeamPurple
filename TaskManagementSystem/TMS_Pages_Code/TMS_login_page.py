##TMS Login
##11/5/22

import tkinter as tk

BG_COLOR = "Green"
FG_COLOR = "White"


window=tk.Tk()
window.title('Task Management System')
window.geometry('220x130')

BodyFrame=tk.Frame(window, bg=BG_COLOR, height=200, width=130)
BodyFrame.grid(row=1, sticky="nsew")

window.grid_rowconfigure(1, weight=1) ##allows user to adjust window

window.grid_columnconfigure(0, weight=1)

titleLabel = tk.Label(BodyFrame, text="Task Manager", bg = BG_COLOR, fg= FG_COLOR)
titleLabel.grid(column=2,row=0)

userLabel = tk.Label(BodyFrame, text="Username", bg = BG_COLOR, fg= FG_COLOR)
userLabel.grid(column=1,row=1)

passLabel = tk.Label(BodyFrame, text="Password", bg = BG_COLOR, fg= FG_COLOR)
passLabel.grid(column=1,row=2)

##username and password entrys
userEntry = tk.Entry(BodyFrame)
userEntry.grid(column=2,row=1)

passEntry = tk.Entry(BodyFrame)
passEntry.grid(column=2,row=2)

loginButton = tk.Button(BodyFrame, text='Log In') ##, command=login)
loginButton.grid(column=2,row=5)

exitButton=tk.Button(BodyFrame, text='Exit')
exitButton.grid(column=3, row=6)

window.mainloop()



