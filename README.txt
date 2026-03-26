# Todo List Application

A simple command-line To-Do List application built in Python. This project demonstrates core Python concepts including functions, lists, loops, conditionals, and error handling.

## Features

- Add tasks to your list
- View all current tasks
- Remove tasks by number
- Input validation and error handling
- Clean CLI menu interface

## How to Run

Make sure Python is installed on your machine. You can check by running:

```
python --version
```

Then run the application:

```
python todo_list.py
```

## How to Use

When the program starts you will see a menu:

```
Your Todo List Menu:
1. Add a task
2. View tasks
3. Remove a task
4. Exit
```

- Enter `1` to add a new task
- Enter `2` to view all current tasks
- Enter `3` to remove a task by its number
- Enter `4` to exit the program

## Error Handling

The application handles the following edge cases:

- Viewing tasks when the list is empty
- Removing a task when the list is empty
- Entering letters instead of a number when removing a task
- Entering a number that does not match any task

## Project Structure

```
todo_list.py   - Main application file
README.md      - Project documentation
```

## Requirements

- Python 3.9.6
- No external libraries required