def main_menu():
    print("\n==== Please Select Option ===")
    print("1. Add a task")

def add_task():
    task_to_add=input("Please write your task: ").strip()
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
    except FileNotFoundError:
        taks=[]
        
    task_number= len(tasks) + 1

    with open("tasks.txt", "a") as file:
        file.write(f"{task_number}. {task_to_add}" + "\n")
    print(f"\n Your task has been added as {task_to_add}")

while True:
    main_menu()
    choice = input("Write your choice (4 to exit)")
    
    if (choice == "4"):
        break
    elif (choice == "1"):
        add_task()
    else:
        print(f"You choice was {choice}")

