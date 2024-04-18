import json
from datetime import datetime

# Function to load tasks from file/database
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save tasks to file/database
def save_tasks(tasks):
    try:
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file)
    except IOError as e:
        print("Error saving tasks:", e)

# Function to add a new task
def add_task(tasks, task_name, priority, due_date_str):
    # Define accepted priorities
    accepted_priorities = ['low', 'medium', 'high']
    try:
        # Check if the provided priority is valid
        if priority.lower() not in accepted_priorities:
            print("Invalid priority. Please choose from: low, medium, high.")
            return
        # Parsing due date
        due_date = None
        if due_date_str:
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
        tasks.append({"name": task_name, "priority": priority.lower(), "due_date": due_date, "completed": False})
        save_tasks(tasks)  # Save tasks after adding
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
    except Exception as e:
        print("Error adding task:", e)

# Function to remove a task
def remove_task(tasks, task_index):
    try:
        del tasks[task_index]
        save_tasks(tasks)  # Save tasks after removing
    except IndexError:
        print("Invalid task index.")
    except Exception as e:
        print("Error removing task:", e)

# Function to mark a task as completed
def complete_task(tasks, task_index):
    try:
        tasks[task_index]["completed"] = True
        save_tasks(tasks)  # Save tasks after completing
    except IndexError:
        print("Invalid task index.")
    except Exception as e:
        print("Error completing task:", e)

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks.")
        return
    for index, task in enumerate(tasks):
        completed_status = "Yes" if task["completed"] else "No"
        print(f"{index + 1}. {task['name']} - Priority: {task['priority']}, Due Date: {task['due_date']}, Completed: {completed_status}")

# Main function
def main():
    tasks = load_tasks()

    while True:
        # Display menu
        print("\n===== To-Do List Application =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            priority = input("Enter priority (high/medium/low): ")
            due_date_str = input("Enter due date (optional, format: YYYY-MM-DD): ")
            add_task(tasks, task_name, priority, due_date_str)
        elif choice == "2":
            display_tasks(tasks)
            try:
                task_index = int(input("Enter the index of the task to remove: ")) - 1
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            remove_task(tasks, task_index)
        elif choice == "3":
            display_tasks(tasks)
            try:
                task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            complete_task(tasks, task_index)
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)  # Save tasks before exiting
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
