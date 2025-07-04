import random
print("Welocme to the guess the number Game !")
print("I'm thinking of a number between 1 and 100.")

secret_number = random.randint(1,100)

attemts = 0

while True:
    guess = input("Guess the number")


    if not guess.isdigit():
        print("Please enter a valid secret_number")
        continue

    guess = int(guess)
    attemts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! you guesses it in {attemts} attemts.")