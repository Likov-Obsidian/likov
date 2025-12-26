class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, description, priority):
        new_task = Task(description, priority)
        self.tasks.append(new_task)
    
    def show_tasks(self):
        for task in self.tasks:
            print(f"{task.description} - {task.priority}")
manager = TaskManager()
manager.add_task("Купить хлеб", 1)
manager.add_task("Сделать домашку", 10)
manager.show_tasks()