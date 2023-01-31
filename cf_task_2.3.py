# Number guessing game
number = 18
guess_count = 0
while guess_count != 3:
    guess = input("Guess a whole number between 1 and 20!")
    if guess.isdigit() and int(guess) > 1 and int(guess) > 20:
        print("Your guess needs to be a whole number between 1 and 20. Please try again!")
    elif int(guess) == number:
        print("You have guessed the correct number!")
        break
    elif int(guess) != number:
        guess_count += 1
        print(f"You have used {guess_count} out of 3 guesses. Please try again!")

print(" You have used all 3 of your guesses!")


