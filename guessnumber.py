import random

number = random.randint(1, 100)

while True:
    guess = input("Guess the number or Quit(Q): ")
    if guess == "Q":
        break
    guess = int(guess)
    
    if guess == number:
        print("Nice one! You've guessed the number right")
        break
    elif guess < number:
        print("Your guess was too low. Try a bigger number.")
    else:
        print("Your guess was too high. Try a smaller number.")

print("----- GAME OVER -----")
