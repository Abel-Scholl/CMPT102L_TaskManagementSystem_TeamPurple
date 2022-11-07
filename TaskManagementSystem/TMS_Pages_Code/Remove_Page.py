'''
Team Purple
Task Managemnet System
Remove Page GUI
'''


import tkinter as tk

# Creating the window
window = tk.Tk()
window.title('Remove a Task')
window.geometry('500x300')
window.resizable(width = False, height = False)

# Frames
frame = tk.Frame(window, bg = 'lightgray', height = 300, width = 500)
frame.place(x = 1, y = 1)
task = tk.Frame(window, bg = 'white', height =  '100', width = '300')
task.place(x = 93, y = 90)

# Text
header = tk.Label(frame, text = 'Remove a Task', fg = 'black', bg = 'lightgray', font = ('Times New Roman', 20))
header.place(x = 155, y = 5)
text = tk.Label(frame, text = 'Are you sure you would like to remove the task you selected?', fg = 'black', bg = 'lightgray', font = ('Times New Roman', 10))
text.place(x = 75, y = 50)

# Buttons
yes = tk.Button(frame, text = 'Yes', bg = 'green',fg = 'black') #, command =
yes.place(x =  200, y = 220)
no = tk.Button(frame, text = 'No', bg = 'red', fg = 'black') #, command =
no.place(x = 250, y = 220)

window.mainloop()
