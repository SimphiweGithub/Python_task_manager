import datetime
import json
import cmd

class MyCLITaskTracker(cmd.Cmd):
    prompt = 'task-cli> '
    intro = 'Welcome to TaskTracker. Type "help" for available commands.'

    def do_quit(self, line):
        """Exit the CLI."""
        return True

    
    def do_add(self, line):
        """
        Add a new task.
        Usage: add "Task description" [status]
        Example: add "Buy groceries" or add "Buy groceries" todo
        If status is not provided, defaults to 'todo'.
        """
        
        parts = line.split('"')
        if len(parts) < 3:
            print('Usage: add "Task description" [status]')
            return

        description = parts[1].strip()
        
        remaining = parts[2].strip()
        if remaining:
            
            status = remaining.split()[0]
        else:
            status = "todo"

        
        try:
            with open("l.json", "r") as file:
                tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            tasks = []

        
        max_id = 0
        for task in tasks:
            if "id" in task and isinstance(task["id"], int):
                if task["id"] > max_id:
                    max_id = task["id"]
        new_id = max_id + 1
        createdAt = str(datetime.datetime.now())

        new_task = {
            "id": new_id,
            "description": description,
            "status": status,
            "createdAt": createdAt,
            "updatedAt": ""
        }
        tasks.append(new_task)

        with open("l.json", "w") as file:
            json.dump(tasks, file, indent=2)

        print(f"Task added successfully (ID: {new_id})")

    
    def do_update(self, line):
        """
        Update a task's description.
        Usage: update <id> "New description"
        Example: update 1 "Buy groceries and cook dinner"
        """
        
        parts = line.split('"')
        if len(parts) < 3:
            print('Usage: update <id> "New description"')
            return

        id_part = parts[0].strip()
        try:
            task_id = int(id_part.split()[0])
        except (ValueError, IndexError):
            print("Invalid task ID.")
            return

        new_desc = parts[1].strip()

        try:
            with open("l.json", "r") as file:
                tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("No tasks found.")
            return

        updated = False
        for task in tasks:
            if task.get("id") == task_id:
                task["description"] = new_desc
                task["updatedAt"] = str(datetime.datetime.now())
                updated = True
                break

        if not updated:
            print(f"No task found with ID {task_id}")
            return

        with open("l.json", "w") as file:
            json.dump(tasks, file, indent=2)

        print("Task updated successfully.")

    
    def do_delete(self, line):
        """
        Delete a task.
        Usage: delete <id>
        Example: delete 1
        """
        id_str = line.strip()
        if not id_str:
            print("Usage: delete <id>")
            return
        try:
            task_id = int(id_str)
        except ValueError:
            print("Invalid task ID.")
            return

        try:
            with open("l.json", "r") as file:
                tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("No tasks found.")
            return

        new_tasks = []
        deleted = False
        for task in tasks:
            if task.get("id") == task_id:
                deleted = True
            else:
                new_tasks.append(task)

        if not deleted:
            print(f"No task found with ID {task_id}")
            return

        with open("l.json", "w") as file:
            json.dump(new_tasks, file, indent=2)
        print(f"Task {task_id} deleted successfully.")

    
    def do_mark_in_progress(self, line):
        """
        Mark a task as in-progress.
        Usage: mark-in-progress <id>
        Example: mark-in-progress 1
        """
        id_str = line.strip()
        if not id_str:
            print("Usage: mark-in-progress <id>")
            return
        try:
            task_id = int(id_str)
        except ValueError:
            print("Invalid task ID.")
            return

        try:
            with open("l.json", "r") as file:
                tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("No tasks found.")
            return

        updated = False
        for task in tasks:
            if task.get("id") == task_id:
                task["status"] = "in-progress"
                task["updatedAt"] = str(datetime.datetime.now())
                updated = True
                break

        if not updated:
            print(f"No task found with ID {task_id}")
            return

        with open("l.json", "w") as file:
            json.dump(tasks, file, indent=2)
        print(f"Task {task_id} marked as in-progress.")

    def do_mark_done(self, line):
        """
        Mark a task as done.
        Usage: mark-done <id>
        Example: mark-done 1
        """
        id_str = line.strip()
        if not id_str:
            print("Usage: mark-done <id>")
            return
        try:
            task_id = int(id_str)
        except ValueError:
            print("Invalid task ID.")
            return

        try:
            with open("l.json", "r") as file:
                tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("No tasks found.")
            return

        updated = False
        for task in tasks:
            if task.get("id") == task_id:
                task["status"] = "done"
                task["updatedAt"] = str(datetime.datetime.now())
                updated = True
                break

        if not updated:
            print(f"No task found with ID {task_id}")
            return

        with open("l.json", "w") as file:
            json.dump(tasks, file, indent=2)
        print(f"Task {task_id} marked as done.")

    
    def do_list(self, line):
        """
        List tasks.
        Usage:
          list              -> lists all tasks
          list <status>     -> lists tasks filtered by status (e.g., list done)
        """
        try:
            with open("l.json", "r") as file:
                tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("No tasks found.")
            return

        if not tasks:
            print("No tasks available.")
            return

        filter_status = line.strip().lower()
        found = False
        for task in tasks:
            if filter_status:
                if task.get("status", "").lower() == filter_status:
                    print("ID: {0}, Description: {1}, Status: {2}, CreatedAt: {3}, UpdatedAt: {4}".format(
                        task.get('id'),
                        task.get('description'),
                        task.get('status'),
                        task.get('createdAt'),
                        task.get('updatedAt')
                    ))
                    found = True
            else:
                print("ID: {0}, Description: {1}, Status: {2}, CreatedAt: {3}, UpdatedAt: {4}".format(
                    task.get('id'),
                    task.get('description'),
                    task.get('status'),
                    task.get('createdAt'),
                    task.get('updatedAt')
                ))
                found = True
        if filter_status and not found:
            print("No tasks with status '{0}' found.".format(filter_status))


if __name__ == '__main__':
    MyCLITaskTracker().cmdloop()

    #these functions are used to list all tasks, done tasks, not done tasks, and in progress tasks
    #I think they could b more efficient ngl

    
    