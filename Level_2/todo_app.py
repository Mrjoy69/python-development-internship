import json
import os

tasks = []


def view_tasks():
    print("\n===== MY TO-DO LIST =====")

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(f"ID: {task['id']}. Title: {task['title']} - status: {status}")


def add_task():
    title = input("Enter the task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    if tasks:
        new_id = max(task["id"] for task in tasks) + 1

    else:
        new_id = 1

    new_task = {
        "id": new_id,
        "title": title,
        "completed": False
    }

    tasks.append(new_task)

    save_tasks()

    print(f"Task added successfully!")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_id = int(input("Enter the ID of the task to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)

            save_tasks()
            
            print("Task deleted successfully!")
            return

    print("Task not found.")

def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_id = int(input("Enter the ID of the task to mark as completed: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print("Task already completed")
            else:
                task["completed"]=True

                save_tasks()
                
                print("Task marked completed!")
            return

    print("Task not found.")

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

    print("Task saved successfully!")


def load_tasks():
    if os.path.exists("tasks.json"):
        return []

    try:
        with open("tasks.json", "r") as file:
            loaded_tasks = json.load(file)

        if not isinstance(loaded_tasks, list):
            print("Error: Tasks file must contain a list of tasks.")
            return []

        return loaded_tasks

    except json.JSONDecodeError:
        print("Error: the task file contains invalid JSON.")
        return[]

    except OSError as error:
        print(f"Error: Unable to read the tasks file. {error}")
        return []


def main():
    while True:
        print("\n================================")
        print("       MY TO-DO LIST APP")
        print("================================")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            view_tasks()

        elif choice == "2":
            add_task()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            complete_task()

        elif choice == "5":
            print("Exiting the app. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

tasks = load_tasks()

if __name__ == "__main__":
    main()
