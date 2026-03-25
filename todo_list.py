tasks = []

def display_menu(): 
    print("Your Todo List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

def add_task():
    task = input("Enter the tasks you would like to add: ")
    tasks.append(task)
    print(f"task '{task}' added to the list.")

def view_tasks():
    if not tasks:
        print("No current tasks")
    else: 
        print("Current tasks: ")
        for i, task in enumerate(tasks, 1): 
            print(f"{i} - {task}")