
# 🎮 Guess the Number

A simple Python terminal game where the user tries to guess a randomly chosen number between 1 and 10.

## 📋 How It Works

- The computer randomly selects a number between 1 and 10.
- The player has **5 attempts** to guess the number.
- After each guess, the program provides feedback:
  - "Too high!"
  - "Too low!"
  - "Correct!" if the guess is right.

## 🚀 How to Run

### Prerequisites
- Python 3.x installed on your system.

### Running the game

Open a terminal and run:

```bash
python Guess number.py
```


## 🧠 Example Output

```
Welcome to Guess the Number!
I'm thinking of a number between 1 and 10.
You have 5 guesses left. Enter your guess: 4
Too low!
You have 4 guesses left. Enter your guess: 7
Too high!
You have 3 guesses left. Enter your guess: 6
Congratulations! You guessed the number 6 in 3 guesses.
```

## 📦 Features

- Input validation (non-number and out-of-range handling)
- Random number generation
- Limited attempts for added challenge