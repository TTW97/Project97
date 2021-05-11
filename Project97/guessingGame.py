import random
chances = 0
number = random.randint(1,10)
while chances < 5:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("YOU WON")
        break
    elif guess > number:
        print("Guess Lower")
    else: 
        print("Guess Higher")
    chances = chances + 1
if not chances < 5:
    print("You Lose")

    
