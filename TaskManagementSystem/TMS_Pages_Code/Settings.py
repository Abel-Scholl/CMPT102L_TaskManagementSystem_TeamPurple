import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import csv
            
def addUser(usernEnt, passEnt):
    user=usernEnt.get()
    password=passEnt.get()
    
    with open ('CurrentUser.csv','r') as file:
        csvReader=csv.reader(file) # 'W' mode replaces all, so the csv doesn't have to be later deleted
        for SingleRow in csvReader:
            CurrentAdmin = SingleRow[0]
            
    with open ('userLoginInfo.csv','r') as file:
        csvReader=csv.reader(file) # 'W' mode replaces all, so the csv doesn't have to be later deleted
        for member in csvReader:
            if(member[0]==CurrentAdmin):
                with open('userLoginInfo.csv','a',newline='') as file:
                    csvWriter=csv.writer(file)
                    csvWriter.writerow([user,password])
    

def changeAdmin(usernEnt, passEnt):
    adminUserNew=usernEnt.get()
    adminPassNew=passEnt.get()

    #userLoginInfo
    L=[]

    CurrentAdmin=""
    
    with open ('CurrentUser.csv','r') as file:
            csvReader=csv.reader(file) # 'W' mode replaces all, so the csv doesn't have to be later deleted
            for SingleRow in csvReader:
                CurrentAdmin = SingleRow[0]
                
    with open ('userLoginInfo.csv','r') as file:
        csvReader=csv.reader(file)
        for member in csvReader:
            if(member[2]=='TRUE'):
                pass
            else:
                L.append(member)

    L.append([adminUserNew,adminPassNew,'TRUE'])
    with open('userLoginInfo.csv','w',newline='') as file:
        csvWriter=csv.writer(file)
        csvWriter.writerows(L)

    #taskList
    with open ('taskList.csv','r') as file:
        csvReader=csv.reader(file)
        for member in csvReader:
            if(member[0]==CurrentAdmin):
                oldadmin=member[0]
                text = open('taskList.csv','r')
                text = ''.join([i for i in text]).replace(oldadmin, adminUserNew)
                x = open('taskList.csv','w',newline='')
                x.writelines(text)

    with open('CurrentUser.csv','w') as file:
        csvWriter=csv.writer(file)
        csvWriter.writerow([adminUserNew])

def removeUser(usernEnt, passEnt):
    user=usernEnt.get()
    password=passEnt.get()

    with open ('userLoginInfo.csv', 'r') as file:
        csvReader=csv.reader(file) # 'W' mode replaces all, so the csv doesn't have to be later deleted
        for member in csvReader:
            if(member[0]=='A'):
                continue
            
    Contents=[]
    with open('userLoginInfo.csv','r') as file:
        csvReader=csv.reader(file)
        for member in csvReader:
            if(member[0]==user and member[1]==password):
                continue
            Contents.append(member)

        with open('userLoginInfo.csv','w',newline='') as file:
            csvWriter=csv.writer(file)
            csvWriter.writerows(Contents)

def Set(window = None):
    
    '''window=tk.Tk()
    window.title('Settings')
    window.geometry('800x500')
    window.configure(bg = "Purple")'''

    if window is None:
        window = tk.Tk()

    window.title('Settings | Task Management System')
    window.geometry('800x500')
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)
                           
    BodyFrame=tk.Frame(window,bg='purple',height=1000,width=1000)
    BodyFrame.pack()

    # Image
    img=Image.open("SetPage.jpg")
    resized_image=img.resize((200,200), Image.Resampling.LANCZOS)
    new_image=ImageTk.PhotoImage(resized_image)
    label=Label(BodyFrame, image=new_image)
    label.place(x=550,y=10)
    
    titleLab=tk.Label(BodyFrame,text="Admin Settings", bg='purple', fg = 'white', font = ('Times New Roman', 30))
    titleLab.place(x=270,y=10)

    usernLab=tk.Label(BodyFrame,text="Username: ",bg='purple', fg = 'white', font = ('Times New Roman', 12))
    usernLab.place(x=500,y=250)

    usernEnt=tk.Entry(BodyFrame)
    usernEnt.place(x=600,y=250)

    passLab=tk.Label(BodyFrame, text="Password: ",bg='purple', fg = 'white', font = ('Times New Roman', 12))
    passLab.place(x=500,y=300)

    passEnt=tk.Entry(BodyFrame)
    passEnt.place(x=600,y=300)

    chgAdminBut=tk.Button(BodyFrame, text='Change Admin Details', padx = 10, command=lambda:changeAdmin(usernEnt, passEnt))
    chgAdminBut.place(x=70,y=180)

    adduserBut=tk.Button(BodyFrame, text="Add 'User'", padx = 10, command=lambda:addUser(usernEnt, passEnt)) 
    adduserBut.place(x=70,y=280)

    chgpassBut=tk.Button(BodyFrame, text="Remove 'User'", padx = 10, command=lambda:removeUser(usernEnt, passEnt)) 
    chgpassBut.place(x=70,y=380)

    window.mainloop()


if __name__ == "__main__":
    Set()