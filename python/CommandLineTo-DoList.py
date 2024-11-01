import json
import os

class ToDoApp:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []
    
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
    
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    
    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)
    
    def view_tasks(self):
        for idx, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else "✗"
            print(f"{idx + 1}. [{status}] {task['task']}")

# Example usage
todo = ToDoApp()
todo.add_task("Learn Python")
todo.add_task("Build a to-do list app")
todo.complete_task(0)
todo.view_tasks()
