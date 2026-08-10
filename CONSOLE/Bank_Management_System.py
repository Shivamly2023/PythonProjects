balance = 0

def deposit():
    global balance
    
    amount = float(input("Enter Amount to deposit:"))
    
    if amount > 0:
        balance += amount
        print("rs{amount} deposited successfully!")
        
    else:
        print("Invalid amount!")
        
def withdraw():
    global balance
    
    amount = float(input("Enter amount to withdraw:"))
    
    if amount <= 0:
        print("Invalid amount!")
        
    elif amount > balance:
        print("Insufficient Balance!")
        
    else:
        balance -= amount
        print(f"rs{amount} withdrawn successfully!")
        
def check_balance():
    print(f"Your Current Balance is rs{balance}")
    
while True:
    
    print("\n===== BANK MANAGENT SYSTEM =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")
    
    choice = input("Enter your choice:")
    
    if choice == "1":
        deposit()
        
    elif choice == "2":
        withdraw()
        
    elif choice == "4":
        print("Thank You for using our Bank!")
        break
    else:
        print("Invalid Choice!")