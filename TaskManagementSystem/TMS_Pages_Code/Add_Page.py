'''
Team Purple
Task Management System
Add Page
'''

import tkinter as tk

# Creating the adujstable window
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
title.place(x = 300, y = 25)

# Labels
title = tk.Label(Body, text = 'Title: ', fg = 'white', bg = 'purple', font = ('Bold', 12))
title.place(x = 150, y = 50)
time = tk.Label(Body, text = 'Time: ', fg = 'white', bg = 'purple', font = ('Bold', 12))
time.place(x = 150, y = 80)
duration = tk.Label(Body, text = 'Duration: ', fg = 'white', bg = 'purple', font = ('Bold', 12))
duration.place(x = 150, y = 110)
description = tk.Label(Body, text = 'Description: ', fg = 'white', bg = 'purple', font = ('Bold', 12))
description.place(x = 150, y = 140)

# Entries
titleEnt = tk.Entry(Body, width = 70)
titleEnt.place(x = 195, y = 50)
timeEnt = tk.Entry(Body, width = 69)
timeEnt.place(x = 200, y = 80)
durationEnt = tk.Entry(Body, width = 65)
durationEnt.place(x = 225, y = 110)
descriptionEnt = tk.Entry(Body, width = 62)
descriptionEnt.place(x = 245, y = 140)

# Button
save = tk.Button(Body, text = 'Save', width = 4, height = 2).place(x = 350, y = 180)
exitBut = tk.Button(Body, text = 'Exit', width = 4, height = 2).place(x = 400, y = 180)


window.mainloop()
