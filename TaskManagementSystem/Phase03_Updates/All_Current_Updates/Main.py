'''
Main Window
'''

import datetime
from tkinter.ttk import Combobox
from tkinter import messagebox
import tkinter as tk
from tkinter import *
import Class as TC # import class file
from PIL import Image, ImageTk
import csv

def mainFunc(user):
    
    window = Tk()
    window.title('Task Management System')
    window.geometry('550x500')
    window.configure(bg="Green")
    BG_COLOR = "Green"
    FG_COLOR = "White"

    #Welcome Banner
    welcFrame = Frame(master=window)
    welcomeBanner = Label(welcFrame, text=(user[0]+"'s Calendar"),
                        bg ='Green', fg='white', font = ("Comic Sans MS",20))
    welcomeBanner.pack(side=LEFT)
    welcFrame.pack()

    #Months and Years as combo boxes + go button
    monthsFrame = Frame(master=window, bg="Green")

    monthsCombo = Combobox(monthsFrame, width=10, state="readonly")
    monthsCombo['values']= ("January", "February", "March", "April",
                    "May", "June", "July", "August",
                    "September","October","November","December")
    monthsCombo.current((datetime.date.today().month)-1)
    monthsCombo.pack(side=LEFT)
    yearsCombo = Combobox(monthsFrame, width=6, state="readonly")
    yearsCombo['values']= ("2022", "2023", "2024", "2025",
                    "2026", "2027", "2028", "2029",
                    "2030","2031","2032","2033")
    yearsCombo.current((datetime.date.today().year)-2022)
    yearsCombo.pack(side=LEFT, pady=10)

    #Changes calendar to reflect selected info
    goButtonCal = Button(monthsFrame, text="Go")
    goButtonCal.pack(side=LEFT)
    monthsFrame.pack()

    ##Calendar as buttons
    calendarFrame=Frame(master=window, bg="Green")
    dayNum=0
    days = ["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday", "Sunday"]
    dateToday = datetime.date.today()
    # if m==(datetime.date(year, month, day)).weekday()

    ##creates a label for each weekday starting with monday
    for d in range(len(days)):
        weekdayLabel = Label(calendarFrame, text=days[d],bg = 'Green', fg = 'white', font=("Comic Sans MS", 12))
        weekdayLabel.grid(column=d, row=0)

    ##Creates a button for each day
    ##when clicked, the current tasks will appear
    ##or a message saying there are no tasks for that day
        m=True##placeholder for datetime condition
    for i in range(5):
        for j in range(7):
            ##frame = tk.Frame(master=window)
            if dayNum > 30:
                break
            else:
                if m==True:
                    ##placeholder for datetime,
                    ##need int value representing day of the week (0-6)
                    ##for the 1st day of the month.
                    ##if month-1-year is on m=weekday (0-6)
                    ##print m labels
                    label= Label(calendarFrame, text="   ", bg = 'Green')
                    label.grid(row=i+1, column=j, sticky='nsew')
                    m=False
                else:
                    dayNum+=1
                    if datetime.date.today().day == dayNum:
                        button = Button(calendarFrame, text=f"{dayNum}", fg="red")#,command=)
                    else:
                        button = Button(calendarFrame, text=f"{dayNum}")
                    button.grid(row=i+1, column=j, sticky='nsew')
    calendarFrame.pack()


    ##Frame for search function
    searchFrame = Frame(master=window, bg = 'green')
    searchLabel=Label(searchFrame, text="Search by:", bg='Green', fg='white', font=("Comic Sans MS", 10))
    searchLabel.pack(side=LEFT)

    searchByCombo = Combobox(searchFrame, width=12, state='readonly')
    searchByCombo['values']= ("No Criteria", "Date", "Time",
                    "Title", "Duration", "Description")
    searchByCombo.set("No Criteria Set")

    searchByCombo.current(0)
    searchByCombo.pack(side=LEFT, pady=10)

    searchEnt = tk.Entry(searchFrame)
    searchEnt.pack(side = LEFT)
    Criteria = searchEnt.get()

    ##Frame for task related options including task list, task options (add, edit, remove)
    taskFrame = Frame(master=window, bg='Green')
    taskLabelFrame = LabelFrame(taskFrame, text = 'Current Tasks', bg = 'Green', fg = 'white')
    
        ##if tasks exist for that day. else, label says: "There are no tasks scheduled for this day"
    tasksTextBox = Text(taskLabelFrame, width = 20, height=10) ##This button is being weird. I dont know why. (i cant deselect it)
    tasksTextBox.pack()
    taskLabelFrame.pack(side=LEFT, padx=70)


    
#tasksTextBox.insert(tk.END, name+':' phone+'\n')
# .delete(1.0, tk.END)

    L = []
    def SearchFunc():
        tasksTextBox.delete(1.0, tk.END)
        with open ('UserforAdd.csv', 'r') as file:
            csvReader = csv.reader(file)
            for singleRow in csvReader:
                username = singleRow[0] # gets username of active person
        with open ('CSV.csv', 'r') as file:
            csvReader = csv.reader(file)
            for rows in csvReader:
                if rows[0]==username: # only rows of the active username
                    match searchByCombo.get(): # filter by combobox selection
                        case "Title":
                            for titles in csvReader:
                                if titles[1] == Criteria: # if entry box criteria matches, insert search result to box
                                    tasksTextBox.insert(tk.END, col[1]+','+col[2]+','+col[3]+','+col[4]+','+col[5]+'\n')
                        case "Date":
                            pass
                        case "Time":
                            pass
                        case "Duration":
                            pass
                        case "Description":
                            pass



    goButtonSearch = Button(searchFrame, text="Go", command = SearchFunc())
    goButtonSearch.pack(side=LEFT)
    searchFrame.pack()
                    
    # Buttons
    import Add
    import Edit
    import Remove
    import Settings

    addButton = Button(taskFrame, text= "Add New Task",
                    command = lambda: Add.AddFunc(window = Toplevel()))##default to selected day
    editButton = Button(taskFrame, text= "Edit Selected Task",
                        command = lambda: Edit.EditFunc(window = Toplevel())) ##if not selected, "Please select a task"
    removeButton = Button(taskFrame, text= "Remove Selected Task",
                        command = lambda: Remove.RemoveWin(window = Toplevel()))##if not select, "Please select task"
    addButton.pack(pady=5)
    editButton.pack(pady=5)
    removeButton.pack(pady=5)
    settingsButton=Button(taskFrame, text="User Settings",
                        command = lambda: Settings.Set(window = Toplevel()))
    settingsButton.pack(pady = 5)

    taskFrame.pack()

    window.mainloop()

#mainFunc(['User'])



