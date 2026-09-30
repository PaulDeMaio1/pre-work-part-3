
print("=" * 30)
print("     My To-Do List")
print("=" * 30)

def show_tasks(title=None):
    if title:
        print(f"\n{title}")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print(f"\nTotal tasks: {len(tasks)}")
    #Above is in order to define "show_tasks" as to ensure when the user adds or subtracts a task from the list, python will be able to print the new list after user inputs their new data
tasks = ["Buy groceries", "Finish homework", "Call the dentist"]
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")

print(f"\nTotal tasks: {len(tasks)}")
# Below 3 lines are for giving the user a choice as what they would like to do, and line 15 is to tell python to wait for user input before moving forward.
print("\nWhat would you like to do?")
print("1. Add a task")
print("2. Remove a task")
choice = input("\nChoice: ").strip()
if choice == "1":
    new_task = input("Enter new task: ").strip()
    tasks.append(new_task)
    show_tasks("Updated list:")
elif choice == "2":
    try:
        num = int(input("Enter task number to remove: "))
        #Below is to make sure that we subtract the int by 1 to ensure we choose the correct int and not crash python.
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            ("Updated list:")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
else:
    print("Please enter 1 or 2.")
    # Above are examples of possible input errors that could crash the function, such as a user entering letters instead of numbers, and if the user enters any other number besides 1 or 2