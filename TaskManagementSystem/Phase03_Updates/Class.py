# Class template for now
class User():
    
    def __init__(self,u,p):
        self.username=u
        self.password=p
        self.numOfTasks=0
        self.admin=False
        self.loggedIn=False

    def setUsername(self,u): #userame:str
        self.username=u 
    def setPassword(self,p): #password:str
        self.password=p
    def setNumOfTasks(self,n): #numOfTasks:int
        self.numOfTasks=n
    def setAdminStatus(self,a): #admin:boolean
        self.admin=a
    def setLoginStatus(self,log): #loggedIn:boolean
        self.loggedIn = log
        
    def getUsername(self):
        return self.username
    def getPassword(self):
        return self.password
    def getnumOfTasks(self):
        return self.numOfTasks
    def getAdminStatus(self):
        return self.admin
    def getLoginStatus(self):
        return self.loggedIn

    def addToTaskCount(self): ##adds to the number of tasks saved counter for the user
        self.numOfTasks+=1
        return self.numOfTasks

    def removeFromTaskCount(self): ##subtracts from the number of tasks saved counter for the user
        self.numOfTasks-=1
        return self.numOfTasks
    


class Task(User):
    '''Class representing a task in TMS'''
    def __init__(self,u,p,t,dat,tim,dur,des):
        User.__init__(self,u,p) #(self,u,p,n,a)
        self.title=t
        self.date=dat
        self.time=tim ##use military time (it'll be easier) unless datetime object works
        self.duration=dur ##in hours or minutes? I think hours.
        self.description=des

    def setTitle(self,t):
        self.title=t
    def setDate(self,dat):
        self.date=dat
    def setTime(self,tim):
        self.time=tim
    def setDuration(self,dur):
        self.duration=dur
    def setDescription(self,des):
        self.description=des

    def getTitle(self):
        return self.title    
    def getDate(self):
        return self.date    
    def getTime(self):
        return self.time  
    def getDuration(self):
        return self.duration  
    def getDescription(self):
        return self.description

    def saveTask(self):
        ##this is where the username and
        ##all Task attributes will be saved to a csv file.
        infoList = [super().username, super().title, self.date, self.time, self.duration, self.description]
        with open ('CSV.csv', 'a', newline = '') as file:
            csvWriter = csv.writer(file)
            csvWriter.writerow(infoList)
