import datetime
import json



tasks = {}
def deleteTask():
    delTak = ""

def updateTask():  
    updatedAt = datetime.datetime.now()
    tasks["updatedAt"] = updatedAt


def createTask():
    id= input("test id:")#gonna have to
    description = input("Description of task:")
    status = input("test status:")
    createdAt = str(datetime.datetime.now())
    

    
    tasks["id"] = id
    tasks["description"] = description
    tasks["status"] = status
    tasks["createdAt"] = createdAt
    tasks["updatedAt"]  = ""
    #data = tasks.json() 
    with open("l.json", "w") as file:
        json.dump(tasks,file)
    print(tasks)

createTask()  
