'''
Team Purple
Task Management System
Edit Page
'''

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import csv
import Class


def EditFunc():


    # Creating the adujstable window
    window = tk.Tk()
    window.title('Edit | Task Management System')
    window.geometry('800x500')
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)

    # Frames and Title
    Top = tk.Frame(window, bg = 'white', height = 100, width = 1000)
    Top.grid (row = 0, sticky = 'nsew')
    Body = tk.Frame(window, bg = 'purple', height = 400, width = 1000)
    Body.grid(row = 1, sticky = 'nsew')

    title = tk.Label(Top, text = 'Edit a Task', fg = 'Black', bg = 'white', font = ('Times New Roman', 30))
    title.place(x = 200, y = 25)

    # Image
    img = Image.open("C:\\Users\\sydne\OneDrive\Pictures\EditPage.png") # load image
    resized_image = img.resize((200,100), Image.Resampling.LANCZOS) # resize, remove structural padding
    new_image = ImageTk.PhotoImage(resized_image)# convert to photoimage
    label = Label(Top, image = new_image) #disply the image
    label.place(x = 400, y = 2)

    # Labels
    title = tk.Label(Body, text = 'Title: ', fg = 'white', bg = 'purple', font = ('Bold', 12))
    title.place(x = 150, y = 50)
    date = tk.Label(Body, text = 'Date: ', fg = 'white', bg = 'purple', font = ('Bold', 12))
    date.place(x = 150, y = 80)
    time = tk.Label(Body, text = 'Time: ', fg = 'white', bg = 'purple', font = ('Bold', 12))
    time.place(x = 150, y = 110)
    duration = tk.Label(Body, text = 'Duration: ', fg = 'white', bg = 'purple', font = ('Bold', 12))
    duration.place(x = 150, y = 140)
    description = tk.Label(Body, text = 'Description: ', fg = 'white', bg = 'purple', font = ('Bold', 12))
    description.place(x = 150, y = 170)

    # Entries
    titleEnt = tk.Entry(Body, width = 70)
    titleEnt.place(x = 195, y = 50)
    dateEnt = tk.Entry(Body, width = 70)
    dateEnt.place(x = 195, y = 80)
    timeEnt = tk.Entry(Body, width = 69)
    timeEnt.place(x = 200, y = 110)
    durationEnt = tk.Entry(Body, width = 65)
    durationEnt.place(x = 225, y = 140)
    descriptionEnt = tk.Entry(Body, width = 62)
    descriptionEnt.place(x = 245, y = 170)

    # Button
    save = tk.Button(Body, text = 'Save Edit', width = 6, height = 2).place(x = 350, y = 210)
    exitBut = tk.Button(Body, text = 'Exit', width = 4, height = 2).place(x = 410, y = 210)


    window.mainloop()

