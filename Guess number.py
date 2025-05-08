import random

def guess_the_number():
    secret_number = random.randint(1, 10)
    guesses_left = 5

    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 10.")

    while guesses_left > 0:
        try:
            guess = int(input(f"You have {guesses_left} guesses left. Enter your guess: "))

            if 1 <= guess <= 10:
                if guess == secret_number:
                    print(f"Congratulations! You guessed the number {secret_number} in {5 - guesses_left + 1} guesses.")
                    return
                elif guess < secret_number:
                    print("Too low!")
                else:
                    print("Too high!")
            else
                print("Invalid input. Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")

        guesses_left -= 1

    print(f"You ran out of guesses. The number was {secret_number}.")

if __name__ == "__main__":
    guess_the_number()