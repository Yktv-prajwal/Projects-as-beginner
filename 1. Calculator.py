def addnumbers(a,b):
    return  a+b

def subnumbers(a,b):
    return  a-b

def divnumbers(a,b):
    return  a/b

def mulnumbers(a,b):
    return  a*b

a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
print("1.Addition(+)\n"
           "2.Subtraction(-)\n"
           "3.Division(/)\n"
           "4.Multiplication(*)")

operation=input("Enter Which Operation You Want To Perform :")

if operation == "1":
    print("Result =",addnumbers(a,b))
elif operation == "2":
    print("Result =",subnumbers(a,b))
elif operation == "3":
    if b == 0:
        print("Cannot divide by zero.")
    else:
        print("Result =", divnumbers(a, b))
elif operation == "4":
    print("Result =",mulnumbers(a,b))
else:
    print("Invalid Operation")



