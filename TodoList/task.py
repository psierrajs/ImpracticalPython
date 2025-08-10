from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"

class Task:
    def __init__(self, title, description='', due_date=None, priority=3):
        self.title = title
        self.description = description

        if due_date:
            if isinstance(due_date, str):
                self.due_date = datetime.strptime(due_date, DATE_FORMAT)
            else:
                self.due_date = due_date
        else:
            self.due_date = None

        self.priority = priority
        self.completed = False
        self.created_at = datetime.now()

    def mark_complete(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else "✗"
        due = self.due_date.strftime(DATE_FORMAT) if self.due_date else "No due date"
        return f"[{status}] {self.title} (Priority: {self.priority}) - Due: {due}\n    Description: {self.description}"
