import json
from task import Task
from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"

def task_to_dict(task):
    return {
        'title': task.title,
        'description': task.description,
        'due_date': task.due_date.strftime(DATE_FORMAT) if task.due_date else None,
        'priority': task.priority,
        'completed': task.completed,
        'created_at': task.created_at.strftime("%Y-%m-%d %H:%M:%S")
    }

def dict_to_task(data):
    due_date = datetime.strptime(data['due_date'], DATE_FORMAT) if data['due_date'] else None
    task = Task(
        title=data['title'],
        description=data.get('description', ''),
        due_date=due_date,
        priority=data.get('priority', 3)
    )
    task.completed = data.get('completed', False)
    return task

def save_tasks(task_list, filename="tasks.json"):
    with open(filename, 'w') as f:
        json.dump([task_to_dict(task) for task in task_list], f, indent=4)

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return [dict_to_task(item) for item in data]
    except FileNotFoundError:
        return []
