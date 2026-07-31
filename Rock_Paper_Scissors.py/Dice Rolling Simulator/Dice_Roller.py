import random

while True:
    input("Press Enter to roll the dice...")
    
    dice = random.randint(1,6)
    
    print("You rolled:", dice)
    
    again = input("Roll again? (yes/no): ").lower()
    
    if again != "yes":
        print("Thanks for playing!")
        break