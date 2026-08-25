import random

print("Welcome to Guess The Number")
print("I am thinking of a number betwen 1 and 100")
print("Try to guess it in as few attempts as possible")

number = random.randint(1,100)
attempts = 0
while True:
    guess = int(input("Enter your Guess: "))
    attempts += 1

    if guess < 1 or guess > 100:
        print("Invalid input. Please enter a number: ")

    if guess < number:
        print("Too Low. Try Again.")
    elif guess > number:
        print("Too High. Try Again.")
    else:
        print(f"Congratulations! You guessed the number. You guessed the in {attempts} attempts")   
        break      
