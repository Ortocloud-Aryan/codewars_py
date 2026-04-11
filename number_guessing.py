import random
number = random.randint(10,12) 
lives = 5
while lives > 0:
    guess = int(input("Enter the number you want to guess! : "))
    
    if guess == number:
        print("You won!")
        break
    else:
        lives -= 1 
        print(f"Wrong guess, {lives} lives remaining")

if lives == 0:
    print("You lost, Try Again!")
