# Todo list with beer surprise
# List of tasks
tasks = ['buy groceries', 'clean the house', 'pay bills', 'call mom', 'walk the dog']

# Add a new task (with beer surprise)
new_task = input("Enter a new task to add to your list: ").strip()
if new_task:
    # Beer surprise for adding "beer" as a task
    if new_task.lower() == "beer":
        print("Cheers! Enjoy your beer surprise! 🍺")
    # Check for duplicates
    if new_task in tasks:
        print(f"The task '{new_task}' is already in your list. No duplicates allowed.")
    else:
        tasks.append(new_task)
        print(f"Added task: {new_task}")
else:
    print("No task entered. Nothing was added.")

# Mark a task as completed
completed_task = input("Enter a task you have completed: ").strip()
if completed_task:
    if completed_task in tasks:
        tasks.remove(completed_task)
        print(f"Marked '{completed_task}' as completed and removed it from your list.")
    else:
        print(f"Task '{completed_task}' not found in your list.")
else:
    print("No task entered. Nothing was marked as completed.")

# Show current tasks
if tasks:
    print("Your current tasks:")
    for task in tasks:
        print(f"- {task}")
else:
    print("All tasks completed! Enjoy your beer surprise! 🍺"
          "\nCheers! You've earned it!")
# Quit the program
print("Exiting the task manager. Have a great day!")
#