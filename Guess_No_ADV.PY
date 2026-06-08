import random

a = random.randint(1, 10)

for i in range(3): 
    b = int(input("Enter Your Number (1-10): "))      
    if b>a:
        print("Lower")
    elif b<a:
        print("Higher")
    else:
        print("You Won!!!")
print("Computer Number =", a)