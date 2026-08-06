expenses = []
print("\===== EXPENSE TRACKER =====")
print("1. Add Expense")
print("2. View Expenses")
print("3. Show Total Expense")
print("4. Delete Expense")
print("5. Exit")

choice = input("Enter your choice:")

#Add Expense
if choice == "1":
    category = input("Enter your choice:")
    amount = float(input("Enter Amount:"))
    
    expenses ={
        "category": category,
        "amount": amount
    }
    
    expenses.append(expenses)
    print("Expense Added Successfully")
    
#View Expense
elif choice == "2":
    if len(expenses) == 0:
        print("No Expense Found")
    else:
        print("\n===== YOUR EXPENSES =====")
        for i, expenses in enumerate(expenses, start=1):
            print(f"{i}. {expenses['category']} - rs{expenses['amount']}")
            
#Show Total Expense
elif choice == "3":
    total = 0
    
    for expense in expenses:
        total += expense["amount"]
        
    print(f"\nTotal Expense = rs{total}")
    
#Delete Expense
elif choice == "4":
    if len(expenses) == 0:
        print("No Expenses To Delete!")
        
    else:
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense['category']} - rs{expense['amount']}")
            
        delete = int(input("Enter Expense Number: "))
        
        if 1 <= delete <= len(expenses):
            removed = expenses.pop(delete - 1)
            print(f"{removed['category']} Delete Successfully!")
        else:
            print("Invalid Number!")
            
#exit
elif choice == "5":
    print("Thank You!")
    'break'

else:
    print("Invalid Choice!")
            