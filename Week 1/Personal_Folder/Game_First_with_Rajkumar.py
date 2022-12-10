'''  ### Guessing game
1. Take input from user (int)
2. Compare the number:
    Lower -> "The number is Lower"
    Greater -> "The number is Greater" 
'''
import random
random_number = random.randint(1,10)
for _ in range(5):
    guess = int (input("Enter your guess number between 1 to 20"))
    if guess==random_number:
        print("your guess is right")
        break
    elif guess>random_number:
        print("your guess is greater than random number")
    
    elif guess<random_number:
        print("your guess is lower than random number")

        