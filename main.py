# Zapan
lazy import json
lazy import datetime

# importing database
with open("tasks.json", "r") as file:
    tasks = json.load(file)


def view_tasks():
    """
    with this method you can see all of your tasks
    """
    if not tasks:
        print("-------------------------------------")
        print("No tasks available.")
        print("-------------------------------------")
    else:
        print("-------------------------------------")
        print("\nTasks:")
        for task_id, task in tasks.items():
            print(f"ID: {task_id}")
            print(f"Name: {task['name']}")
            print(f"Description: {task['description']}")
            print(f"Status: {task['status']}")
            print(f"Created on: {task['create_date']}")
            print(f"Last updated on: {task['update_date']}\n")
            print("-------------------------------------")


def add_task():
    
    """
    with this method user can add new task 
    """
    
    # getting the information
    id = []
    for key in tasks.keys():
        id.append(key)
    task_id = int(id[-1]) + 1
    print("-------------------------------------")
    name = input("Enter your task name: ")
    description = input("Enter your task description: ")
    status = input("Enter your task status (incomplete/completed/inprogress): ")
    print("-------------------------------------")
    date = datetime.datetime.now().__str__().split(" ")
    time = datetime.datetime.now().__str__().split(" ")[1].split(".")
    create_date = date[0] + " " + time[0]

    # add new task to dict
    tasks[str(task_id)] = {
        "name": name,
        "description": description,
        "status": status,
        "create_date": create_date,
        "update_date": create_date
    }

    # updating json file
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
    
    print("-------------------------------------")
    print("Task added successfully!")
    print("-------------------------------------")


def update_task():
    """
    with this method user can update task
    """
    print("-------------------------------------")
    task_tracker = input("Enter the task ID: ")
    print("-------------------------------------")
    for task_id, task in tasks.items():
        if task_id == task_tracker:
            
            while True:
                print("-------------------------------------")
                print(f"\nthe selected task is: \nID: {task_id}\nName: {task['name']}\nDescription: {task['description']}\nStatus: {task['status']}\nCreated on: {task['create_date']}\nLast updated on: {task['update_date']}\n")
                
                print("What would you like to update?")
                print("1. Name")
                print("2. Description")
                print("3. Status")
                print("4. exit")
                print("-------------------------------------")
                
                # updating name
                update_choice = input("Enter your choice: ")
                if update_choice == "1":
                    print("-------------------------------------")
                    new_name = input("Enter your new name: ")
                    date = datetime.datetime.now().__str__().split(" ")
                    time = datetime.datetime.now().__str__().split(" ")[1].split(".")

                    tasks[task_id]['update_date'] = date[0] + " " + time[0]
                    tasks[task_id]['name'] = new_name
                    
                    with open("tasks.json", "w") as file:
                        json.dump(tasks, file, indent=4)
                    
                    print("-------------------------------------")
                    print("the name has changed")
                    print("-------------------------------------")
                # updating description
                elif update_choice == "2":
                    print("-------------------------------------")
                    new_description = input("Enter your new description: ")
                    date = datetime.datetime.now().__str__().split(" ")
                    time = datetime.datetime.now().__str__().split(" ")[1].split(".")
                    
                    tasks[task_id]['update_date'] = date[0] + " " + time[0]
                    tasks[task_id]['description'] = new_description
                    
                    with open("tasks.json", "w") as file:
                        json.dump(tasks, file, indent=4)
                    
                    print("-------------------------------------")
                    print("the description has changed")
                    print("-------------------------------------")
                # updating status
                elif update_choice == "3":
                    print("-------------------------------------")
                    new_update = input("Enter your new status(inprogress/completed): ")
                    date = datetime.datetime.now().__str__().split(" ")
                    time = datetime.datetime.now().__str__().split(" ")[1].split(".")
                    
                    tasks[task_id]['update_date'] = date[0] + " " + time[0]
                    tasks[task_id]['status'] = new_update
                    
                    with open("tasks.json", "w") as file:
                        json.dump(tasks, file, indent=4)
                    
                    print("-------------------------------------")
                    print("the status has changed")    
                    print("-------------------------------------")
                    
                elif update_choice == "4":
                    print("-------------------------------------")
                    print("finish updating back to main menu.")
                    print("-------------------------------------")
                    break
                else:
                    print("-------------------------------------")
                    print("Invalid input")
                    print("-------------------------------------")


def remove_task():
    """
    with this method user can remove task
    """
    print("-------------------------------------")
    task_id = input("Enter the task ID to remove: ").strip()
    
    if task_id in tasks:
        del tasks[task_id]

        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
        print("-------------------------------------")
        print("Task removed.")
        print("-------------------------------------")
    else:
        print("-------------------------------------")
        print("Task doesn't exist!")
        print("-------------------------------------")



def main():
    print("-------------task manager------------")
    print("welcome to task manager")
    print("-------------------------------------")
    
    while True:
        print("\nMenu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Remove task")
        print("5. Exit")
        print("-------------------------------------")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("-------------------------------------")
            print("Thank you for using Task Manager!")
            print("-------------------------------------")
            break
        else:
            print("-------------------------------------")
            print("Invalid choice. Please try again.")
            print("-------------------------------------")

if __name__ == "__main__":
    main()