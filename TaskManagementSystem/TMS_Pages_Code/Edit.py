'''
Team Purple
Task Management System
Edit Page
'''

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import csv


def EditFunc(window = None):


    # Creating the adujstable window
    '''window = tk.Tk()
    window.title('Edit | Task Management System')
    window.geometry('800x500')
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)'''

    if window is None:
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
    img = Image.open("EditPage.png") # load image
    resized_image = img.resize((200,100)) # resize, remove structural padding #  Image.Resampling.LANCZOS
    new_image = ImageTk.PhotoImage(resized_image)# convert to photoimage
    label = Label(Top, image = new_image) #disply the image
    label.place(x = 400, y = 2)

    # Labels
    title = tk.Label(Body, text = 'Title of the task you would like to edit: ', fg = 'white', bg = 'purple', font = ('Bold', 12))
    title.place(x = 250, y = 20)
    details = tk.Label(Body, text = 'New Task Details: ', fg = 'white', bg = 'purple', font = ('Bold', 12))
    details.place(x = 300, y = 95)
    date = tk.Label(Body, text = 'Date: ', fg = 'white', bg = 'purple', font = ('Bold', 12))
    date.place(x = 150, y = 130)
    time = tk.Label(Body, text = 'Time: ', fg = 'white', bg = 'purple', font = ('Bold', 12))
    time.place(x = 150, y = 160)
    duration = tk.Label(Body, text = 'Duration: ', fg = 'white', bg = 'purple', font = ('Bold', 12))
    duration.place(x = 150, y = 190)
    description = tk.Label(Body, text = 'Description: ', fg = 'white', bg = 'purple', font = ('Bold', 12))
    description.place(x = 150, y = 220)

    # Entries
    titleEnt = tk.Entry(Body, width = 60)
    titleEnt.place(x = 205, y = 45)
    dateEnt = tk.Entry(Body, width = 70)
    dateEnt.place(x = 195, y = 130)
    timeEnt = tk.Entry(Body, width = 69)
    timeEnt.place(x = 200, y = 160)
    durationEnt = tk.Entry(Body, width = 65)
    durationEnt.place(x = 225, y = 190)
    descriptionEnt = tk.Entry(Body, width = 62)
    descriptionEnt.place(x = 245, y = 220)

    # Gets username
    with open ('CurrentUser.csv', 'r') as file:
        csvReader = csv.reader(file)
        for SingleRow in csvReader:
            username = SingleRow[0]

    # Function
    def ExitWin():
        window.destroy()
    def EditFunc():
        L = []
        TaskToEdit = titleEnt.get()
        dateNew = dateEnt.get()
        timeNew = timeEnt.get()
        durationNew = durationEnt.get()
        descrNew = descriptionEnt.get()
        
        with open ('taskList.csv', 'r') as file:
            csvReader = csv.reader(file) 
            for row in csvReader:
                if (row[0] == username and row[1] == TaskToEdit): #finding old task info to edit, leave out of list
                    L.append([username, TaskToEdit, dateNew, timeNew, durationNew, descrNew]) #add new task info to list
                else:
                    L.append(row)
        
        file.close()
        with open ('taskList.csv', 'w', newline = '') as file: #write all task info in List back in to taskList.csv
            csvWriter = csv.writer(file)
            csvWriter.writerows(L)
        window.destroy()
        
    # Button
    save = tk.Button(Body, text = 'Save Edit', width = 6, height = 2, command=EditFunc).place(x = 350, y = 260)
    exitBut = tk.Button(Body, text = 'Exit', width = 4, height = 2, command=ExitWin).place(x = 410, y = 260)


    window.mainloop()

if __name__ == "__main__":
    EditFunc()
