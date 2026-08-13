books = {}

while True :
    
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("\1. Add Book")
    print("\2. View Book")
    print("\3. Search Book")
    print("\4. Issue Book")
    print("\5. Return Book")
    print("\6. Delete Book")
    print("\7. Exit")
    
    choice = input("Enter Your Choice")
    
    #Add Book 
    if choice == "1":
        title = input("Enter Book Title: ")
        author = input("Enter Author Name:")
        
        books[title] = {
            "author": author,
            "status": "Available"
        }
        
        print("Book Added Successfully!")
        
    #View Books
    elif choice == "2":
        
        if len(books) == 0:
            print("No Books Found")
        else: 
            print("\===== ALL BOOKS =====")
            
            for title, details in books.items():
                
                print("Title:", title)
                print("Author:", details["author"])
                print("Status", details["status"])
                print("_ "* 30)
                        
    #Search Book
    elif choice == "3":
        
        title = input("Enter Book Title: ")
        
        if title in books:
            
            print("Book Found!")
            print("Author:", books[title]["author"])
            print("Status:", books[title]["status"])
            
        else:
            print("Book Not Found!")
     
    #Issue Book
    elif choice == "4":
         
         title = input("Enter Book Title: ")
         
         if title in books:
             
             if books[title]["status"] == "Available":
                 
                 books[title]["status"] = "Issued"
                 
                 print("Book Issued Successfully!")
                 
         else:
             print("Book is already issued!")
             
    #Return Book
    elif choice == "5":
        
        title = input("Enter Book Title:")
        
        if title in books:
            
            if books[title]["status"] == "Issued":
                
                books[title]["status"] = "Available"
                
                print("Book Returned Successfullly!")
             
            else:
                print("Book Not Found!")
                
    #Delete Book
    elif choice == "6":
        
        title = input("Enter Book Title:")
        
        if title in books:
            del books[title]
            
            print("Book Deleted Successfully!")
            
        else:
            print("Book Not Found1")
            
    #Exit
    elif choice == "7":
        
        print("Thank You for using Library Management System!")
        
        break
    else:
        print("Invalid Choice!")             
             
             
                