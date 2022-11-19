import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

# def chgadmindet:

# def addUser

def Set():
    
    window=tk.Tk()
    window.title('Settings')
    window.geometry('800x500')
    window.configure(bg = "Purple")
                           
    BodyFrame=tk.Frame(window,bg='purple',height=1000,width=1000)
    BodyFrame.pack()

    img=Image.open("C:\\Users\\chris\Downloads\gear.png")
    resized_image=img.resize((200,200), Image.Resampling.LANCZOS)
    new_image=ImageTk.PhotoImage(resized_image)
    label=Label(BodyFrame, image=new_image)
    label.place(x=550,y=10)
    
    titleLab=tk.Label(BodyFrame,text="Admin Settings",bg='purple', fg = 'white', font = ('Times New Roman', 30))
    titleLab.place(x=270,y=10)

    usernLab=tk.Label(BodyFrame,text="Username: ",bg='purple', fg = 'white', font = ('Times New Roman', 12))
    usernLab.place(x=500,y=250)

    usernEnt=tk.Entry(BodyFrame)
    usernEnt.place(x=600,y=250)

    passLab=tk.Label(BodyFrame, text="Password: ",bg='purple', fg = 'white', font = ('Times New Roman', 12))
    passLab.place(x=500,y=300)

    passEnt=tk.Entry(BodyFrame)
    passEnt.place(x=600,y=300)

    chgpassBut=tk.Button(BodyFrame, text='Change Admin Details', padx = 10)#...command=chgadmindet)
    chgpassBut.place(x=70,y=180)

    adduserBut=tk.Button(BodyFrame, text="Add 'User'", padx = 10)#...command=addUser...
    adduserBut.place(x=70,y=280)

    chgpassBut=tk.Button(BodyFrame, text="Remove 'User'", padx = 10)#...
    chgpassBut.place(x=70,y=380)

    window.mainloop()

Set()
