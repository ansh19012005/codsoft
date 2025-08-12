# todo.py

tasks = []

def show_menu():
    print("\n==== TO-DO LIST MENU ====")
    print("1. Add Task(s)")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    input_tasks = input("Enter task(s) (separate multiple with commas): ")
    task_list = [task.strip() for task in input_tasks.split(',') if task.strip()]
    for task in task_list:
        tasks.append({"task": task, "done": False})
    print(f" {len(task_list)} task(s) added!")

def view_tasks():
    if not tasks:
        print("No tasks in your list.")
        return
    print("\n Your Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else " Not Done"
        print(f"{index}. {task['task']} - {status}")

def mark_done():
    view_tasks()
    try:
        task_no = int(input("Enter task number to mark as done: "))
        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]["done"] = True
            print("Task marked as done!")
        else:
            print(" Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            deleted = tasks.pop(task_no - 1)
            print(f"Deleted: {deleted['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting To-Do List. Goodbye! 👋")
        break
    else:
        print(" Invalid option. Please choose between 1-5.")
