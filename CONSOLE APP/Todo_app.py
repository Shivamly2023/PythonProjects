tasks = ["gym", "lunch", "study"]

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Enter your choice:")

    if choice == "1":
        task = input("Enter task:")
        tasks.append(task)
        print("Task Added successfully")
    
    elif choice == "2":
        if len(tasks) == 0:
            print("No Tasks Available") 
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
            
    elif choice == "3":
        if len(tasks)==0:
            print("No Task To Delete")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
                
            try:
                delete = int(input("enter task number to delete:"))
                
                if 1 <= delete <= len(tasks):
                    removed = tasks.pop(delete - 1)
                    print(f"'{removed}' Delete Successfully")
                else:
                    print("invalid Task Number!")
                    
            except ValueError:
                print("Please enter a valid number")
    
    elif choice == "4":
        print("Thank You Goodbye")
        break    
            
    else:
        print("invalid coices! Please try again.")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
     
              