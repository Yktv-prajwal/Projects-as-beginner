wel =input("Enter Your Name : ")
print(f"Hey {wel} !!!")

table = int(input("Enter Which Number of Table You Want : "))
print(f"Your Table of {table} is :")
for i in range(1,11):
    final=table * i
    print(f"{table} X {i} = {final}")   
