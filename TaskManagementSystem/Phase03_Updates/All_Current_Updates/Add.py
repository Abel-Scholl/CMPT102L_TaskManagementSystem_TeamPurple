'''
Team Purple
Task Management System
Add Page
'''

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import csv
import Class as TC

def AddFunc(window = None):
    # Creating the adujstable window
    '''window = tk.Tk()
    window.title('Add | Task Management System')
    window.geometry('800x500')
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)'''
    if window is None:
        window = tk.Tk()
    
    window.title('Add | Task Management System')
    window.geometry('800x500')
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)


    # Frames and Title
    Top = tk.Frame(window, bg = 'white', height = 100, width = 1000)
    Top.grid (row = 0, sticky = 'nsew')
    Body = tk.Frame(window, bg = 'purple', height = 400, width = 1000)
    Body.grid(row = 1, sticky = 'nsew')

    title = tk.Label(Top, text = 'Add a Task', fg = 'Black', bg = 'white', font = ('Times New Roman', 30))
    title.place(x = 200, y = 25)

    # Image
    img = Image.open("AddImage.jpg") # load image
    resized_image = img.resize((200,100)) # resize, remove structural padding # Image.Resampling.LANCZOS
    new_image = ImageTk.PhotoImage(resized_image)# convert to photoimage
    label = Label(Top, image = new_image) #display the image
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

    # Function
       
    def Save():
        with open ('UserForAdd.csv', 'r') as file:
            csvReader = csv.reader(file)
            for singleRow in csvReader:
                U = singleRow[0]

        titleInp = titleEnt.get()
        dateInp = dateEnt.get()
        timeInp = timeEnt.get()
        durationInp = durationEnt.get()
        descrInp = descriptionEnt.get()

        infoList = [U, titleInp, dateInp, timeInp, durationInp, descrInp] # [U, ...

        with open ('CSV.csv', 'a', newline = '') as file:
            csvWriter = csv.writer(file)
            csvWriter.writerow(infoList)

        window.destroy()
        
    def Exit():
        window.destroy()

    # Button
    save = tk.Button(Body, text = 'Save', width = 4, height = 2, command = Save).place(x = 350, y = 210)
    exitBut = tk.Button(Body, text = 'Exit', width = 4, height = 2, command = Exit).place(x = 400, y = 210)

    window.mainloop()
                       

if __name__ == "__main__":
    AddFunc()


