'''
Team Purple
Task Managemnet System
Remove Page GUI
'''
import tkinter as tk
import csv

def RemoveWin(window = None):

    if window is None:
        window = tk.Tk()
    
    # Creating the window
    #window = tk.Tk()
    window.title('Remove a Task')
    window.geometry('500x200')
    window.resizable(width = False, height = False)

    # Frames
    frame = tk.Frame(window, bg = 'lightgray', height = 300, width = 500)
    frame.place(x = 1, y = 1)
    task = tk.Entry(window, width = 50)
    task.place(x = 85, y = 72)

    # Text
    header = tk.Label(frame, text = 'Remove a Task', fg = 'black', bg = 'lightgray', font = ('Times New Roman', 20))
    header.place(x = 155, y = 5)
    text = tk.Label(frame, text = 'Please enter the title of the task you would like to remove: ', fg = 'black', bg = 'lightgray', font = ('Times New Roman', 10))
    text.place(x = 75, y = 50)


    # Gets username
    with open ('CurrentUser.csv', 'r') as file:
        csvReader = csv.reader(file)
        for SingleRow in csvReader:
            username = SingleRow[0]

    # Functions
    
    def RemoveFunc():
        L = []
        TitleToRemove = task.get()
        with open ('taskList.csv', 'r') as file:
            csvReader = csv.reader(file)
            for row in csvReader:
                print (row[0], row[1], username, TitleToRemove)
                if (row[0] == username and row[1] == TitleToRemove):
                    pass
                else:
                    L.append(row)
        file.close()
        with open ('taskList.csv', 'w', newline = '') as file:
            csvWriter = csv.writer(file)
            csvWriter.writerows(L)
        window.destroy()

    def CancelFunc():
        window.destroy()

    # Buttons
    yes = tk.Button(frame, text = 'Remove', bg = 'green',fg = 'black', command=RemoveFunc) 
    yes.place(x =  170, y = 120)
    no = tk.Button(frame, text = 'Cancel', bg = 'red', fg = 'black', command = CancelFunc )
    no.place(x = 240, y = 120)

    window.mainloop()

if __name__ == "__main__":
    RemoveWin()
