contact = {}

while True:
    print("\===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contact")
    print("3.Search Contacts")
    print("4.Update Contacts")
    print("5.Delete Contacts")
    print("6.Exit")
    
    choice = input("Enter your choice:")
    
    #Add Contact
    if choice == "1":
        name = input("Enter Name:")
        phone = input("Enter Phone Number:")
        
        contact[name] = phone
        print("Contact Added Successfully!")
        
    #View Contact
    elif choice == "2":
        if len(contact) == 0:
            print("no contact available!")
        else:
            print("\n===== CONTACTS LIST =====")
            for name, phone in contact.items():
                print(f"{name} : {phone}")
    
    #search contact
    elif choice == "3":
        name = input("Enter Name To Search: ")
        
        if name in contact:
            print(f"Phone Number: {contact[name]}")
        else:
            print("Contact Not Found!")
            
    #update Contact
    elif choice == "4":
        name = input("Enter Name To Update:")
        
        if name in contact:
            new_phone = input("Enter New Phone Number:")
            contact[name] = new_phone
            print("contact update successfully!")
        else:
            print("Contact Not Found!")
            
    #Delete Contact
    elif choice == "5":
        name = input("Enter Name to Delete:")
        
        if name in contact:
            del contact[name]
            print("contact deleted successfully1") 
        else:
            print("contact not found!")
    #exit
    
    elif choice == "6":
        print("Thank You! Goodbye")
        break
    
    #Invalid choice
    else:
        print("Invalid Choice! Please Try Again.")       