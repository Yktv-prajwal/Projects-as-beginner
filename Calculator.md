# 🧮 Basic Calculator in Python

## 📌 Project Overview
This is a simple calculator built using Python that performs four basic arithmetic operations: Addition, Subtraction, Division, and Multiplication. The program takes two numbers as input from the user and performs the selected operation using functions.

## 🚀 Features
- Performs Addition, Subtraction, Division, and Multiplication.
- Uses separate functions for each operation.
- Takes user input for numbers and operation selection.
- Prevents division by zero.
- Handles invalid operation choices.

## 📚 Concepts Used
- Python Functions
- User Input
- Conditional Statements (`if-elif-else`)
- Arithmetic Operators
- Basic Error Handling

## 🔍 Working of the Program

### Step 1: Define Functions
Four functions are created to perform the arithmetic operations:
- `addnumbers(a, b)` – Returns the sum of two numbers.
- `subnumbers(a, b)` – Returns the difference of two numbers.
- `divnumbers(a, b)` – Returns the quotient of two numbers.
- `mulnumbers(a, b)` – Returns the product of two numbers.

### Step 2: Take User Input
The program asks the user to enter two numbers that will be used for the calculation.

### Step 3: Display the Menu
A menu is displayed showing the available operations:
1. Addition
2. Subtraction
3. Division
4. Multiplication

### Step 4: Get User Choice
The user selects the desired operation by entering a number from 1 to 4.

### Step 5: Perform the Operation
The program uses `if-elif-else` statements to determine which function to call based on the user's choice.

### Step 6: Handle Division by Zero
Before performing division, the program checks whether the second number is zero. If it is, an error message is displayed to prevent a runtime error.

### Step 7: Handle Invalid Input
If the user enters an invalid operation number, the program displays an appropriate error message.

## 💻 Sample Output

Enter First Number: 10
Enter Second Number: 5

1. Addition(+)
2. Subtraction(-)
3. Division(/)
4. Multiplication(*)

Enter Which Operation You Want To Perform: 1

Result = 15

## 🎯 Learning Outcomes
By creating this project, I learned:
- How to define and use functions.
- How to take user input.
- How to use conditional statements.
- How to perform basic arithmetic operations.
- How to implement basic error handling.
- How to organize code into reusable components.

## 🔮 Future Improvements
- Add more operations such as Modulus and Exponentiation.
- Support decimal numbers using `float`.
- Allow multiple calculations in one execution.
- Add a calculation history feature.
- Build a graphical user interface (GUI).

This project is part of my Python learning journey and helps me strengthen my understanding of fundamental programming concepts.
