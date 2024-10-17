import json

class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False
    
    def mark_completed(self):
        self.completed = True

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks):
        status = "✓" if task.completed else "✗"
        print(f"{i + 1}. [{status}] {task.title} - {task.description} ({task.category})")

def main():
    tasks = load_tasks()
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter task category: ")
            tasks.append(Task(title, description, category))
            print("Task added successfully.")
        
        elif choice == '2':
            print("\nYour Tasks:")
            display_tasks(tasks)
        
        elif choice == '3':
            display_tasks(tasks)
            task_number = int(input("Enter task number to mark as completed: ")) - 1
            if 0 <= task_number < len(tasks):
                tasks[task_number].mark_completed()
                print("Task marked as completed.")
            else:
                print("Invalid task number.")
        
        elif choice == '4':
            display_tasks(tasks)
            task_number = int(input("Enter task number to delete: ")) - 1
            if 0 <= task_number < len(tasks):
                tasks.pop(task_number)
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
        
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting the application.")
            break

if __name__ == "__main__":
    main()
