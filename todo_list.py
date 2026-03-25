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

def remove_task():
    if not tasks: 
        return print("No tasks to remove.")
    view_tasks()
    try:
            task_number = int(input("Enter the number of the task you want to remove: "))
            removed_task = tasks.pop(task_number - 1)
            print(f"task '{removed_task}' was removed from the list.")
    except ValueError:
            print("Invalid input. Please enter a number.")
            return
    except IndexError:
            print("Invalid task number. Please try again.")
            return
