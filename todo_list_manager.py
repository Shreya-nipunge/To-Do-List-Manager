def load_tasks(filename):
    tasks = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                task, done = line.strip().split(',')
                tasks.append({"task": task, "done": done == "True"})
    except FileNotFoundError:
        print("No previous task file found. Starting fresh.")
    return tasks

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for item in tasks:
            file.write(f"{item['task']},{item['done']}\n")
    print("Tasks saved to file.")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nTo-Do List:")
    for idx, item in enumerate(tasks, start=1):
        status = "Done" if item['done'] else "Not done"
        print(f"{idx}. {item['task']} [{status}]")

def mark_task_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]['done'] = True
            print(f"Task '{tasks[num-1]['task']}' marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"Removed task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Save & Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            save_tasks(filename, tasks)
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
