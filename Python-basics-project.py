#Simple To-Do List Application
# This application allows users to manage a to-do list by adding, viewing, and removing tasks. The tasks are stored in a list and can be saved to a file for persistence. 
# The application provides a simple command-line interface for user interaction.
import json
# This is a simple to-do list application that allows users to add, view, and remove tasks. The tasks are stored in a list called 'tasks'.  
tasks = []

# The 'add_task' function takes a task as an argument and adds it to the 'tasks' list.
def add_task(task):
    if task.strip():
        tasks.append(task)
        print("Task added.")
    else:
        print("Task cannot be empty.")     

# The 'show_tasks' function prints all the tasks in the 'tasks' list, including both active and completed tasks.
def show_tasks():  
    print("Tasks:") 
    for i, task in enumerate(tasks):
        print(i+1,task)

# The 'show_aktive_tasks' function prints all the active tasks in the 'tasks' list.
def show_aktive_tasks():   
    print("Active Tasks:")
    for i, task in enumerate(tasks):
            if "(Done)" not in task:    
              print(i+1,task)        
# The 'show_done_tasks' function prints all the completed tasks in the 'tasks' list, which are identified by the presence of "(Done)" in the task description.
def show_done_tasks():
    print("Done Tasks:")
    for i, task in enumerate(tasks):
            if "(Done)" in task:    
              print(i+1,task)   
# The 'remove_task' function takes a task as an argument and removes it from the 'tasks' list if it exists.    
def remove_task(index):
    try:       
        tasks.pop(int(index)-1)
        print("Task removed.")
    except (IndexError, ValueError):
        print("Invalid task number , please enter a valid number.")
    
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

# The 'edit_tasks' function allows the user to edit an existing task. It first shows the current tasks, 
# then prompts the user to enter the task number they want to edit and the new task description. It updates the task in the list if the input is valid.
def edit_tasks():
    show_aktive_tasks()
    task_number = input("Enter the task number to edit: ")   
    try:
        print("Current task:", tasks[int(task_number)-1])
        new_task = input("Edit the task: " )
        if new_task.strip():
            tasks[int(task_number)-1] = new_task
            print("Task updated.")
        else:
            print("Task cannot be empty.")
    except (IndexError, ValueError):
        print("Invalid task number , please enter a valid number.")

# The 'mark_Task_done' function allows the user to mark a task as done. It shows the current tasks, 
# prompts the user to enter the task number they want to mark as done, and appends "(Done)" to the task description if the input is valid.
def mark_Task_done():
    show_aktive_tasks()
    try:
       Done_task_number = input("Enter the task number to mark as done: ")   
       if Done_task_number.strip():
          tasks[int(Done_task_number)-1] = tasks[int(Done_task_number)-1] + " (Done)"
          print("Task marked as done.")
       else: 
          print("Task number cannot be empty.")
    except (IndexError, ValueError):
        print("Invalid task number , please enter a valid number.")

# The 'main' function is the entry point of the application. It displays a menu to the user and performs actions based on the user's choice.
def main():    
    global tasks        
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Show Active Tasks")
        print("4. Show Done Tasks")
        print("5. Edit Task")
        print("6. Mark Task as Done")
        print("7. Remove Task")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task to add: ")
            add_task(task)
            save_tasks()
          
        elif choice == '2':
            show_tasks()
       
        elif choice == '3':
            show_aktive_tasks()
            save_tasks()

        elif choice == '4':
            show_done_tasks()
            save_tasks()

        elif choice == '5':
            edit_tasks()
            save_tasks()

        elif choice == '6':
            mark_Task_done()
            save_tasks()

        elif choice == '7':
            show_aktive_tasks()
            task = input("Enter the task number to remove: ")
            remove_task(task)
            save_tasks()
          
        elif choice == '8':
            print("Goodbye! Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a valid number.")
 # The 'main' function is the entry point of the application. It displays a menu to the user and performs actions based on the user's choice. 
 # The user can add tasks, view tasks, remove tasks, or exit the application. The loop continues until the user chooses to exit.           
if __name__ == "__main__":
    main()  