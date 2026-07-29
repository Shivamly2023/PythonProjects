import random
 
choices = ["rock",  "paper", "scissor"]

computer = random.choice(choices)

user = input("Enter rock, paper, or scissors: ").lower()

print("Computer chose:", computer)

if user == computer:
    print("it's a tie!")
elif(user == "rock" and computer == "scissors") or \
    (user == "paper" and computer == "rock") or \
    (user == "scissors" and computer == "paper"):
   print("You Win!")
elif user in choices:
    print("Computer Wins!")
else:
    print("Invalid Choices!")
