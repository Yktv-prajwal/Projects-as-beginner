import random

a = random.randint(1, 10)
b = int(input("Enter Your Number (1-10): "))

print("Computer Number =", a)
        
if a == b:
    print("You Won!!")
else:
    print("You Lose!!")