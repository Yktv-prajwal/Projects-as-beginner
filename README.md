# Projects-as-beginner
Since I am learning Python from scratch, I am building very basic projects.

# 1.Simple Python Calculator

A beginner-friendly, interactive command-line calculator written in Python. This project was built to practice foundational Python programming concepts including functions, control flow, and user input handling.

## Features
* **Basic Arithmetic:** Performs addition, subtraction, multiplication, and division.
* **Interactive Menu:** Prompts the user to select an operation and input their numbers.
* **Error Handling:** Includes a safety check to prevent program crashes from division by zero.

## Technologies Used
* **Language:** Python 3
* **Core Concepts:** `def` functions, `if/elif/else` conditional logic, type casting (`int()`), and standard I/O (`input()`, `print()`).


# 2.Number Guessing Game in Python

## Description
This is a simple Python number guessing game for beginners. The program generates a random number between 1 and 10 using the `random` module. The user is asked to guess the number by entering a value between 1 and 10. The program then compares the user's guess with the computer-generated number. If both numbers are the same, the user wins; otherwise, the user loses. This project demonstrates the use of random number generation, user input, type conversion, variables, and conditional statements (`if-else`) in Python.

## Features
• Generates a random number between 1 and 10.
• Accepts user input.
• Compares the user's guess with the computer's number.
• Displays whether the user has won or lost.
• Beginner-friendly project for learning Python basics.

## Concepts Used
• Python `random` module
• `randint()` function
• User input with `input()`
• Type casting using `int()`
• Variables
• Conditional statements (`if-else`)
• Output using `print()`

# 3.Number Guessing Game with 3 Attempts

## Description
This Python program is a simple number guessing game where the computer randomly selects a number between 1 and 10. The player gets three chances to guess the correct number. After each incorrect guess, the program provides a hint by telling the player whether the correct number is higher or lower than their guess. If the player guesses the number within three attempts, they win; otherwise, they lose, and the correct number is revealed at the end.

## Features
• Generates a random number between 1 and 10.
• Gives the player 3 chances to guess the number.
• Provides "Higher" or "Lower" hints after each wrong guess.
• Ends the game immediately when the correct number is guessed.
• Displays the correct number if the player loses.
• Beginner-friendly project for learning Python fundamentals.

## Concepts Used
• Python `random` module
• Random number generation using `randint()`
• `for` loop
• `if`, `elif`, and `else` conditional statements
• User input with `input()`
• Type casting using `int()`
• `break` statement
• `for-else` loop
• Variables and program flow control

## Working
1. The computer generates a random number between 1 and 10.
2. The player has three attempts to guess the number.
3. After each incorrect guess, a hint is provided:
   - "Higher" if the guessed number is too low.
   - "Lower" if the guessed number is too high.
4. If the player guesses correctly, the game displays a winning message and ends.
5. If all three attempts are used without guessing correctly, the game displays a losing message along with the correct number.

#4. Stone, Paper, Scissor Game in Python

## Description
This Python program is a simple Stone, Paper, Scissor game where the player competes against the computer. The player selects either Stone, Paper, or Scissor by entering a number between 1 and 3, while the computer randomly chooses one of the three options. The program compares both choices according to the game rules and declares the winner. If both choices are the same, the game ends in a tie.

## Features
• User selects Stone, Paper, or Scissor using numbers.
• Computer randomly generates its choice.
• Displays both the user's and computer's choices.
• Determines the winner based on the game rules.
• Handles invalid user input.
• Beginner-friendly project for learning Python basics.

## Concepts Used
• Python `random` module
• `random.choice()` function
• User input with `input()`
• Type casting using `int()`
• Lists
• Variables
• `if`, `elif`, and `else` conditional statements
• Logical operators (`and`, `or`)
• Program termination using `exit()`

## Working
1. The program displays three choices: Stone, Paper, and Scissor.
2. The user enters a number between 1 and 3 to select a choice.
3. The computer randomly selects one of the three options.
4. The program displays both the user's and computer's choices.
5. The winner is determined using the following rules:
   - Stone beats Scissor.
   - Paper beats Stone.
   - Scissor beats Paper.
   - If both choices are the same, the game is a tie.
6. The program announces whether the user wins, the computer wins, or the game ends in a tie.
