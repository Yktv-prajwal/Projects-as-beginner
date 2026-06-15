# 🔄 Unit Converter in Python

## 📌 Project Overview
This Python program is a simple Unit Converter that allows users to convert between different units of length, weight, and volume. The program provides a menu-driven interface where users can select a conversion type, enter a value, and instantly receive the converted result.

## 🚀 Features
- Greets the user with a personalized welcome message.
- Converts between common metric units.
- Simple menu-driven interface.
- Accepts decimal values for accurate conversions.
- Displays the converted result with appropriate units.
- Beginner-friendly Python project.

## 📚 Concepts Used
- User Input (`input()`)
- Type Casting (`int()`, `float()`)
- Variables
- String Methods (`upper()`)
- Conditional Statements (`if-elif-else`)
- Arithmetic Operations
- Output Formatting

## 🔍 Working of the Program

### Step 1: User Greeting
The program asks the user to enter their name and converts it to uppercase for display.

### Step 2: Display Conversion Menu
The user is presented with six conversion options:
1. Kilometer to Meter
2. Meter to Kilometer
3. Kilogram to Gram
4. Gram to Kilogram
5. Liter to Milliliter
6. Milliliter to Liter

### Step 3: User Input
The user selects a conversion option and enters the value to be converted.

### Step 4: Perform Conversion
The program uses `if-elif-else` statements to perform the selected conversion using the appropriate mathematical formula.

### Step 5: Display Result
The converted value is displayed along with the corresponding unit.

### Step 6: Exit Message
A personalized thank-you message is displayed after the conversion is completed.

## 💻 Supported Conversions

| Conversion | Formula |
|-----------|----------|
| KM → M | Value × 1000 |
| M → KM | Value ÷ 1000 |
| KG → G | Value × 1000 |
| G → KG | Value ÷ 1000 |
| L → ML | Value × 1000 |
| ML → L | Value ÷ 1000 |

## 💻 Sample Output

```
Enter Your Name : Prajwal

----- Welcome PRAJWAL to The Unit Converter -----

Unit Converter
1. KM to M
2. M to KM
3. KG to G
4. G to KG
5. L to ML
6. ML to L

Enter your choice (1-6): 1

Enter the value: 5

Answer = 5000.0 m

----- Thankyou PRAJWAL for using Unit Converter -----
```

## 🎯 Learning Outcomes
By building this project, I learned:
- Taking user input.
- Working with different data types.
- Using conditional statements.
- Performing mathematical calculations.
- Formatting program output.
- Building a menu-driven Python application.

## 🔮 Future Improvements
- Add temperature conversions.
- Add time conversions.
- Add currency conversions.
- Allow multiple conversions without restarting the program.
- Use functions to make the code more modular.
- Create a graphical user interface (GUI).

This project is part of my Python learning journey and helps me strengthen my understanding of basic programming concepts, conditional logic, and user interaction.
