#Simple To-Do List Application
# This application allows users to manage a to-do list by adding, viewing, and removing tasks. The tasks are stored in a list and can be saved to a file for persistence. 
# The application provides a simple command-line interface for user interaction.
import json
# This is a simple to-do list application that allows users to add, view, and remove tasks. The tasks are stored in a list called 'tasks'.  
tasks = []

# The 'add_task' function takes a task as an argument and adds it to the 'tasks' list.
def add_task(task):
    if task.strip():
        tasks.append(task.strip())
        print("Task added.")
    else:
        print("Task cannot be empty.")     

# The 'show_tasks' function prints all the tasks in the 'tasks' list.
def show_tasks():   
    for i, task in enumerate(tasks):
        print(i+1,task)

# The 'remove_task' function takes a task as an argument and removes it from the 'tasks' list if it exists.    
def remove_task(index):
    try:
        tasks.pop(int(index)-1)
        print("Task removed.")
    except (IndexError, ValueError):
        print("Invalid task number.")
    
# The 'save_tasks' function saves the current list of tasks to a file called 'tasks.json' using the JSON format. 
def save_tasks():
  with open('tasks.json', 'w') as f:
     json.dump(tasks, f)

# The 'load_tasks' function loads the tasks from the 'tasks.json' file and returns them as a list. If the file does not exist, it returns an empty list.
def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return json.load(f)
    except(FileNotFoundError,json.JSONDecodeError):
        return []
            
# The 'main' function is the entry point of the application. It displays a menu to the user and performs actions based on the user's choice.
def main():    
    global tasks        
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task to add: ")
            add_task(task)
            save_tasks()
          
        elif choice == '2':
            print("Tasks:")
            show_tasks()
       
        elif choice == '3':
            show_tasks()
            task = input("Enter the task number to remove: ")
            remove_task(task)
            save_tasks()
          
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
 # The 'main' function is the entry point of the application. It displays a menu to the user and performs actions based on the user's choice. 
 # The user can add tasks, view tasks, remove tasks, or exit the application. The loop continues until the user chooses to exit.           
if __name__ == "__main__":
    main()  