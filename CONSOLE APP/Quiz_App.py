questions = [
    {
        "question": "Python ki type ki language hai?",
        "options": [
            "A. Programming Language",
            "B. Operating System",
            "C. Browser",
            "D. Database"
        ],
        "answer": "A"
    },
    
    {
        "question": "Python file ka extenion kya hota hai?",
        "options": [
            "A. .java",
            "B. .py",
            "c. . html",
            "D. .css"
        
        ],
        "answer": "B"
    
    },
    {
        "question": "Python me output ke liye kya use hota hai?",
        "options": [
            "A. {}",
            "B. ()",
            "C. []",
            "D. <>"
        ],
        "answer": "C"
    },
    
    {
        "question": "Python kisne banayi?",
        "options": [
            "A. Elon Musk",
            "B. Bill Gates",
            "C. Guido Van Russum",
            "D. Mark Zuckerberg"
        ],
        "answer": "c" 
    }
]

score = 0
for question in questions:
    
    print("\n" + question["question"])
    
    for option in question["options"]:
        print(option)
    
    user_answer = input("Enter your answer: ").upper()
    
    if user_answer == question["answer"]:
        print("correct!")
        score += 1
        
    else:
        print("wrong!")
        
        
print("\n===== QUIZ RESULT =====")

print("Total Question:", len(questions))
print("Correct Answer:", score)
print("Wrong Answer:", len(questions) - score)

percentage = (score / len(questions)) * 100

print("Score:", percentage, "%")