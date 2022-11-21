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
from tkinter import messagebox

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
    window.geometry('800x600')
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.configure(bg='purple')


    # Frames and Title
    Top = tk.Frame(window, bg = 'white', height = 100, width = 1000)
    Top.pack (fill=BOTH, expand=True)
    frame1 = tk.Frame(window, bg = 'purple') ##title
    frame2 = tk.Frame(window, bg = 'purple')##date
    frame3 = tk.Frame(window, bg = 'purple')##time
    frame4 = tk.Frame(window, bg = 'purple')##duration
    frame5 = tk.Frame(window, bg = 'purple')##Description
    frame6 = tk.Frame(window, bg = 'purple')##buttons
    frame1.pack (fill=BOTH, expand=True)
    frame2.pack (fill=BOTH, expand=True)
    frame3.pack (fill=BOTH, expand=True)
    frame4.pack (fill=BOTH, expand=True)
    frame5.pack (fill=BOTH, expand=True)
    frame6.pack(fill=BOTH, expand=True, padx=345)

    pageTitle = tk.Label(Top, text = 'Add a Task', fg = 'Black', bg = 'white', font = ('Times New Roman', 30))
    pageTitle.pack()

    # Image
    img = Image.open("AddImage.jpg") # load image
    resized_image = img.resize((200,100)) # resize, remove structural padding # Image.Resampling.LANCZOS
    new_image = ImageTk.PhotoImage(resized_image)# convert to photoimage
    imageLabel = Label(Top, image = new_image) #display the image
    imageLabel.pack()



    # Labels
    title = tk.Label(frame1, text = 'Title: ', fg = 'white', bg = 'purple', font = ('Bold', 12))
    date = tk.Label(frame2, text = 'Date (format: mm/dd/yyyy): ', fg = 'white', bg = 'purple', font = ('Bold', 12))
    time = tk.Label(frame3, text = 'Time (military time, include colon): ', fg = 'white', bg = 'purple', font = ('Bold', 12))
    duration = tk.Label(frame4, text = 'Duration(hours): ', fg = 'white', bg = 'purple', font = ('Bold', 12))
    description = tk.Label(frame5, text = 'Description: ', fg = 'white', bg = 'purple', font = ('Bold', 12))

    # Entries
    titleEnt = tk.Entry(frame1)
    dateEnt = tk.Entry(frame2)
    timeEnt = tk.Entry(frame3)
    durationEnt = tk.Entry(frame4)
    descriptionEnt = tk.Entry(frame5)

    title.pack()
    titleEnt.pack()
    date.pack()
    dateEnt.pack()
    time.pack()
    timeEnt.pack()
    duration.pack()
    durationEnt.pack()
    description.pack()
    descriptionEnt.pack()

            

    
    # Function
       
    def Save():
        with open ('CurrentUser.csv', 'r') as file:
            csvReader = csv.reader(file)
            for singleRow in csvReader:
                U = singleRow[0]

        titleInp = titleEnt.get()
        dateInp = dateEnt.get()
        timeInp = timeEnt.get()
        durationInp = durationEnt.get()
        descrInp = descriptionEnt.get()

        try:
            if dateInp.find("/"):
                d = dateInp.split("/")
                t=timeInp.split(":")
                condition1 = (int(d[-1]) >= 2022 and int(d[-1]) < 2033)
                condition2 = len(timeInp)==5
                if condition1 and condition2:
                    infoList = [U, titleInp, dateInp, timeInp, durationInp, descrInp]
                    with open ('taskList.csv', 'a', newline = '') as file:
                        csvWriter = csv.writer(file)
                        csvWriter.writerow(infoList)
                    window.destroy()
                elif (int(d[0]) < 2022 or int(d[0]) > 2033):
                    messagebox.showwarning('Invalid Input', 'Please enter a valid date between year 2022 and 2032.')
                    
                else:
                    messagebox.showwarning('Invalid Input', 'Please enter a valid date and time following the given formats.')
        except:
            messagebox.showwarning('Invalid Input', 'Please enter a valid date and time following the given formats.')
            
        
    def Exit():
        window.destroy()

    
    # Exit Button
    save = tk.Button(frame6, text = 'Save', width = 4, height = 2, command = Save).grid(column=0, row=0, padx=10)
    exitBut = tk.Button(frame6, text = 'Exit', width = 4, height = 2, command = Exit).grid(column=1, row=0)

    window.mainloop()
                       

if __name__ == "__main__":
    AddFunc()