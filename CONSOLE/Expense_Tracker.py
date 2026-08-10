expenses = []

while True:
    
    print("\===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Show Total Expense")
    print("4. Delete Expense")
    print("5. Exit")
    
    choice = input("Enter your choice:")
    
    if choice == "1":
        category = input("Enter Category:")
        amount = float(input("Enter Amount:"))
        
        expenses.append(expenses) 
        
        print("Expense Added Successfully!")
        
    elif choice == "2":
        
        if len(expenses) == 0:
            print("No Expense Found!")
        
        else:
            for i, expense in enumerate(expenses, start=1):
                print(f"{1}. {expense['category']} - rs{expense['amount']}")
                
    elif choice == "3":
        
        total = 0
        
        for expense in expenses:
            total += expense["amount"]
            
        print(f"Total Expense = r{total}")
        
    elif choice == "4":
        
        if len(expenses) == 0:
            print("No Expense To Delete!")
        
        else:
            
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. {expense['category']} - rs{expense['amount ']}")
                
            delete = int(input("Enter Expense Number: "))
            
            if 1 <= delete <= len(expenses):
                expenses.pop(delete - 1)
                print("Expense Deleted Successfully!")
            else:
                print("Invalid Number!")
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")
                
        
                
         
        
        
        