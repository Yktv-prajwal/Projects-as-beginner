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

# 4.Stone, Paper, Scissor Game in Python

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

# 5.Even and Odd Number Checker in Python

## Description
This Python program checks whether a user-entered number is even or odd. The program takes an integer as input and uses conditional statements to determine its type based on the remainder when divided by 2. It then displays whether the number is even or odd, making it a simple beginner-friendly project for understanding arithmetic and decision-making in Python.

## Features
• Accepts an integer from the user.
• Checks whether the number is even or odd.
• Displays the appropriate result.
• Beginner-friendly and easy to understand.
• Demonstrates the use of conditional statements and arithmetic operators.

## Concepts Used
• User input with `input()`
• Type casting using `int()`
• Variables
• Modulus operator (`%`)
• `if`, `elif`, and `else` statements
• Output using `print()`

## Working
1. The user enters a number.
2. The program checks if the number is divisible by 2.
3. If the remainder is 0, the number is even.
4. Otherwise, the number is odd.
5. The result is displayed to the user.

## Note
The current code has a small logical error:
```python
elif a % 3 == 1:
```
This condition does not correctly identify odd numbers.

A better version is:
```python
if a % 2 == 0:
    print(a, "is EVEN Number")
else:
    print(a, "is ODD Number")
```
This correctly classifies every integer as either even or odd.

# 6.Student Grade Calculator in Python

## Description
This Python program calculates a student's grade based on the marks entered by the user. The program uses conditional statements (`if-elif-else`) to compare the entered marks with predefined grading criteria and displays the corresponding grade. If the marks are below the passing criteria, the program indicates that the student has failed.

## Features
• Accepts marks as user input.
• Assigns grades based on predefined ranges.
• Displays the student's grade along with the obtained marks.
• Identifies failing marks.
• Beginner-friendly project for learning Python decision-making.

## Concepts Used
• User input with `input()`
• Type casting using `int()`
• Variables
• `if`, `elif`, and `else` statements
• Comparison operators (`>=`, `<=`)
• Logical operators (`and`)
• Output using `print()`

## Working
1. The user enters their marks.
2. The program compares the marks with the grading criteria.
3. Based on the marks, an appropriate grade is assigned:
   - 90–100 : A+
   - 80–89  : A
   - 70–79  : B+
   - 60–69  : B
   - 50–59  : C+
   - 40–49  : C
   - Below 40 : Fail
4. The corresponding grade and marks are displayed.

## Note
The first condition in the code:
```python
if a >= 90 and a == 100:
```
only accepts exactly 100 for an A+ grade.

A better condition is:
```python
if a >= 90 and a <= 100:
```
or simply:
```python
if 90 <= a <= 100:
```
This correctly awards an A+ grade for marks between 90 and 100.

# 7.Contact Book in Python

## Description
This Python program is a simple Contact Book that allows users to store and display contact information. The user specifies how many contacts they want to add, then enters the name and phone number for each contact. The program stores the details in a list and finally displays all saved contacts.

## Features
• Allows users to add multiple contacts.
• Stores contact names and phone numbers.
• Displays all saved contacts in a readable format.
• Beginner-friendly project for learning Python data structures.
• Demonstrates the use of loops, lists, and user input.

## Concepts Used
• User input using `input()`
• Type casting with `int()`
• Lists and nested lists
• `for` loops
• Variables
• List methods (`append()`)
• Output using `print()`

## Working
1. The user enters the number of contacts to save.
2. The program asks for the contact's name and phone number.
3. Each contact is stored as a list containing the name and number.
4. The process repeats until all contacts are added.
5. The program displays all stored contacts.

## Note
The current code contains a small error:
```python
number = input("Enter Number of the Contact: ").len(10)
```
The `len()` method cannot be used this way.

A correct approach is:
```python
number = input("Enter Number of the Contact: ")

if len(number) == 10:
    Contact.append([name, number])
else:
    print("Invalid Contact Number")
```
This checks whether the entered phone number contains exactly 10 digits before storing it.
