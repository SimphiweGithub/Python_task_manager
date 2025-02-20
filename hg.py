import datetime
import json
import random



tasks = {}
hold = []

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
        if id_to_search_for in item.values():
          print() 

    updatedAt = datetime.datetime.now()
    tasks["updatedAt"] = updatedAt


def addTask():
    id= input("What ID do you want to give:")
    description = input("Description of task:")
    status = input("test status:")
    createdAt = str(datetime.datetime.now())
    

    
    tasks["id"] = id
    tasks["description"] = description
    tasks["status"] = status
    tasks["createdAt"] = createdAt
    tasks["updatedAt"]  = ""
    
    hold.append(tasks) 
    with open("l.json", "w") as file:
        json.dump(hold,file,indent=2)
    
def listAllTasks():
    with open('l.json', 'r') as openfile:
        data = json.load(openfile)
        print(data)
        lm = str(data)
    lm = str(data).replace("[", "").replace("]", "").replace("'","").replace(",","\n").replace("{", "").replace("}", "")
    print(lm)

listAllTasks()