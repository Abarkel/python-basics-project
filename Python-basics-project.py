#Simple To-Do List Application

# This is a simple to-do list application that allows users to add, view, and remove tasks. The tasks are stored in a list called 'tasks'.  
tasks = []
# The 'add_task' function takes a task as an argument and adds it to the 'tasks' list.
def add_task(task):
    tasks.append(task)
# The 'show_tasks' function prints all the tasks in the 'tasks' list.
def show_tasks():   
    for i, task in enumerate(tasks):
        print(i,task)     
# The 'remove_task' function takes a task as an argument and removes it from the 'tasks' list if it exists.    
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
# The 'main' function is the entry point of the application. It displays a menu to the user and performs actions based on the user's choice.
def main():
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
            print("Task added.")
        elif choice == '2':
            print("Tasks:")
            show_tasks()
        elif choice == '3':
            task = input("Enter the task to remove: ")
            remove_task(task)
            print("Task removed.")
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
 # The 'main' function is the entry point of the application. It displays a menu to the user and performs actions based on the user's choice. 
 # The user can add tasks, view tasks, remove tasks, or exit the application. The loop continues until the user chooses to exit.           
if __name__ == "__main__":
    main()  