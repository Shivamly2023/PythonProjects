pin = "1234"
balance = 4000
transactions = []

def check_pin():
    entered_pin = input("Enter your pin:")
    
    if entered_pin == pin:
        return True
    else:
        return False
    
if check_pin():
    print("login successfully!")
        
    while True:
        print("\n===== ATM MACHINE =====")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Transaction History")
        print("5. Change PIN")
        print("6. Exit")
            
        choice = input("Enter your choice: ")
            
        if choice == "1":
            print(f"Your Balance: rs{balance}")
                
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))  
                
            if amount <= 0:
                print("Invalid Amount!")
                    
            elif amount > balance:
                print("insufficient Balance!")
                    
            else:
                balance -= amount
                transactions.append(f"Withdraw: rs{amount}")
                print(f"{amount} withdrawn successfully!")
                print(f"Remaining Balance: rs {balance}")
                    
        elif choice == "3":
            amount = float(input("Enter amount to deposit:"))
                
            if amount <= 0:
                print("Invalid amount!")
                    
            else:
                balance += amount
                transactions.append(f"Deposited Successfully!")
                print(f"{amount} deposited successfully!")
                print(f"New Balance: rs{balance}")
                
        elif choice == "4":
            print("\n===== TRANACTION HISTORY =====")
                
            if len(transactions) == 0:
                print("No transactions yet.")
                    
            else:
                for transaction in transactions:
                    print(transaction)
                    
        elif choice =="5":
            new_pin = input("Enter new PIN:")
        
            if len(new_pin) == 4:
                pin = new_pin
                print("PIN Changed successfully!")
            
            else:
                print("PIN must be 4 digits!")
            
        elif choice == "6":
            print("Thank you for using ATM!")
            break
    
        else:
            print("Invalid Choice!")
            
else:
    print("Incorrect PIN!")
            


    
    