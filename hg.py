import datetime
import json


def deleteTask():
    
    with open('l.json', 'r') as openfile:
        data = json.load(openfile)  

    value_to_remove = 1  
    updated_data = []
    removed_count = 0

    for item in data:
        if value_to_remove in item.values():
            removed_count += 1  # Count removed items
        else:
            updated_data.append(item)  # Keep the item if it doesn't match

    if removed_count > 0:
        print(f"Removed {removed_count} item(s).")
    else:
        print(f"No item found with value '{value_to_remove}'.")

    # Save the updated JSON data back to the file
    with open('l.json', 'w') as writefile:
        json.dump(updated_data, writefile, indent=2)

def updateTask():  
    with open('l.json', 'r') as openfile:
        data = json.load(openfile)
        id_to_search_for = input("Enter the task number you want to update:")



    for item in data:
        for key, value in item.items():
            if key == "description" and key in item.values():
                change = input("Update your description")
    updatedAt = datetime.datetime.now()
    #tasks["updatedAt"] = updatedAt


def addTask():
    hold = []
    id= input("What ID do you want to give:")
    description = input("Description of task:")
    status = input("test status:")
    createdAt = str(datetime.datetime.now())
    
    tasks = {
            "id": id,
            "description": description,
            "status": status,
            "createdAt": createdAt,
            "updatedAt": ""
        }
    
    hold.append(tasks) 
    with open("l.json", "w") as file:
        json.dump(hold,file,indent=2)
    
def listAllTasks():
    with open('l.json', 'r') as openfile:
        data = json.load(openfile)
    listTaskString = str(data).replace("[", "").replace("]", "").replace("'","").replace(",","\n").replace("{", "").replace("}", "")
    print(listTaskString)

def listDoneTasks():
    DoneTaskList = []
    with open('l.json', 'r') as openfile:
        data = json.load(openfile)
        for item in data:
            for key, value in item.items():
                if value == "done" and key =="status":
                    listTaskString = str(item).replace("[", "").replace("]", "").replace("'","").replace(",","\n").replace("{", "").replace("}", "")
                    DoneTaskList.append(listTaskString)
    if len(DoneTaskList) == 0:
        print("There are no done tasks")
    print(DoneTaskList)

def listNotDoneTasks():
    DoneTaskList = []
    with open('l.json', 'r') as openfile:
        data = json.load(openfile)
        for item in data:
            for key, value in item.items():
                if value == "Not Done" and key =="status":
                    listTaskString = str(item).replace("[", "").replace("]", "").replace("'","").replace(",","\n").replace("{", "").replace("}", "")
                    DoneTaskList.append(listTaskString)
    if len(DoneTaskList) == 0:
        print("There are no done tasks")
    print(DoneTaskList)

def listInProgressTasks():
    DoneTaskList = []
    with open('l.json', 'r') as openfile:
        data = json.load(openfile)
        for item in data:
            for key, value in item.items():
                if value == "In Progress" and key =="status":
                    listTaskString = str(item).replace("[", "").replace("]", "").replace("'","").replace(",","\n").replace("{", "").replace("}", "")
                    DoneTaskList.append(listTaskString)
    if len(DoneTaskList) == 0:
        print("There are no done tasks")
    print(DoneTaskList)

    #these functions are used to list all tasks, done tasks, not done tasks, and in progress tasks
    #I think they could b more efficient ngl