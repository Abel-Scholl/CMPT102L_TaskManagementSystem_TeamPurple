##TMS Login
##11/5/22


import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import csv
import Class


def LogFunc():

    BG_COLOR = "Green"
    FG_COLOR = "White"


    window=tk.Tk()
    window.title('Task Management System')
    window.geometry('450x200')
    window.configure(bg = 'Green')
    BodyFrame=tk.Frame(window, bg=BG_COLOR, height=300, width=200)
    BodyFrame.grid(row=1, column = 2)
    PicFrame = tk.Frame(window, bg = BG_COLOR, height = 300, width = 200)
    PicFrame.grid(row = 1, column = 1)

    window.resizable(width = False, height = False)

    titleLabel = tk.Label(BodyFrame, text="Task Manager", bg = BG_COLOR, fg= FG_COLOR)
    titleLabel.grid(column=2,row=0)

    userLabel = tk.Label(BodyFrame, text="Username", bg = BG_COLOR, fg= FG_COLOR)
    userLabel.grid(column=1,row=1)

    passLabel = tk.Label(BodyFrame, text="Password", bg = BG_COLOR, fg= FG_COLOR)
    passLabel.grid(column=1,row=2)

    # Image
    img = Image.open("C:\\Users\\sydne\OneDrive\Pictures\LogPage.png") # load image
    resized_image = img.resize((200,200), Image.Resampling.LANCZOS) # resize, remove structural padding
    new_image = ImageTk.PhotoImage(resized_image)# convert to photoimage
    label = Label(PicFrame, image = new_image) #disply the image
    label.grid(row=2, column = 4)


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
