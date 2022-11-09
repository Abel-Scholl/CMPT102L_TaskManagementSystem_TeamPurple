import tkinter as tk

window=tk.Tk()
window.title('Settings')
window.geometry('1000x600')

BodyFrame=tk.Frame(window,bg='purple',height=1000,width=1000)
BodyFrame.pack()

greeting=tk.Label(text="Admin Settings")
greeting.pack()

usernLab=tk.Label(text="Username")
usernLab.place(x=600,y=250)

usernEnt=tk.Entry()
usernEnt.place(x=700,y=250)

passLab=tk.Label(text="Password")
passLab.place(x=600,y=300)

passEnt=tk.Entry()
passEnt.place(x=700,y=300)

chgpassBut=tk.Button(text='Change Admin Details')#...command=addition)
chgpassBut.place(x=170,y=180)

adduserBut=tk.Button(text="Add 'User'")#...command=add...
adduserBut.place(x=170,y=280)

chgpassBut=tk.Button(text="Remove 'User'")#...
chgpassBut.place(x=170,y=380)

window.mainloop()


'''
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
'''


'''
Retrieving text with .get()
Deleting text with .delete()
Inserting text with .insert()
'''
