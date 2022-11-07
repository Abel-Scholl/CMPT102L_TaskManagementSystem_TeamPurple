'''
Team Purple
Task Management System
Search Page
'''

import tkinter as tk

# Creating the adujstable window
window = tk.Tk()
window.title('Search | Task Management System')
window.geometry('500x1000')
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

# Frames and Title
Top = tk.Frame(window, bg = 'white', height = 100, width = 1000)
Top.grid (row = 0, sticky = 'nsew')
Body = tk.Frame(window, bg = 'purple', height = 400, width = 1000)
Body.grid(row = 1, sticky = 'nsew')
Box = tk.Frame(Body, bg = 'white', height = 300, width = 900)
Box.place (x = 300, y = 200)

title = tk.Label(Top, text = 'Search for a Task', fg = 'Black', bg = 'white', font = ('Times New Roman', 30))
title.place(x = 600, y = 25)

# Search
Search = tk.Label(Body, text = 'Enter category and keyword:  ', fg = 'white', bg = 'purple', font = ('Bold', 12))
Search.place(x = 300, y = 120)

def result():
    label = tk.Label(Box, text = '', width = 10)
    label.place(x = 1, y = 1)
    label.config(text = clicked.get()) # Change in phase 3 to actual search result
options = ['Time', 'Duration', 'Title'] # options
clicked = tk.StringVar()
clicked.set('Select a Category') # set initial menu
drop = tk.OptionMenu(Body, clicked, *options)
drop.place(x = 510, y = 120)


entry = tk.Entry(Body, width = 50)
entry.place(x = 650, y = 120)

button = tk.Button(Body, text = 'Search', command = result).place(x = 970, y = 120)
exitBut = tk.Button(Body, text = 'Search', command = result).place(x = 970, y = 120)

# Exit button


window.mainloop()
