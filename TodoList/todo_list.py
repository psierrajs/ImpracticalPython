from task import Task

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)
        else:
            raise TypeError("Only Task instances can be added")

    def remove_task(self, title):
        for i, task in enumerate(self.tasks):
            if task.title == title:
                del self.tasks[i]
                return True
        return False

    def find_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("To-Do List:")
        for task in self.tasks:
            print(task)

    # Import storage functions here to avoid circular imports
    def save_to_file(self, filename="tasks.json"):
        from storage import save_tasks
        save_tasks(self.tasks, filename)

    def load_from_file(self, filename="tasks.json"):
        from storage import load_tasks
        self.tasks = load_tasks(filename)
