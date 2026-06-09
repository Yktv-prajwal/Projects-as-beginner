import random

print("----- Welcome to the Game -----")

print("1. Stone")
print("2. Paper")
print("3. Scissor")

a = int(input("Enter Your Choice (1-3): "))

choices = ["Stone", "Paper", "Scissor"]
b = random.choice(choices)

if a == 1:
    user = "Stone"
elif a == 2:
    user = "Paper"
elif a == 3:
    user = "Scissor"
else:
    print("Invalid Choice")
    exit()

print("Your Choice:", user)
print("Computer Choice:", b)

if user == b:
    print("Tie")
elif (user == "Stone" and b == "Scissor") or \
     (user == "Paper" and b == "Stone") or \
     (user == "Scissor" and b == "Paper"):
    print("🎉 You Win!")
else:
    print("😢 Computer Wins!")

print("----- Game END -------")