from task import Task
from todo_list import ToDoList

def main():
    todo = ToDoList()
    todo.load_from_file()

    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task complete")
        print("4. Remove task")
        print("5. Save and Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Task title: ")
            desc = input("Description (optional): ")
            due_date = input("Due date (YYYY-MM-DD, optional): ")
            priority_input = input("Priority (1-5, default 3): ")
            priority = int(priority_input) if priority_input.isdigit() else 3

            task = Task(title, desc, due_date if due_date else None, priority)
            todo.add_task(task)
            print("Task added.")

        elif choice == '2':
            todo.list_tasks()

        elif choice == '3':
            title = input("Task title to mark complete: ")
            task = todo.find_task(title)
            if task:
                task.mark_complete()
                print(f"Task '{title}' marked complete.")
            else:
                print("Task not found.")

        elif choice == '4':
            title = input("Task title to remove: ")
            if todo.remove_task(title):
                print(f"Task '{title}' removed.")
            else:
                print("Task not found.")

        elif choice == '5':
            todo.save_to_file()
            print("Tasks saved. Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
