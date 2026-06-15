a=input("Enter Your Name : ").upper()

print(f"\n----- Welcome {a} to The Unit Converter -----\n")

print("Unit Converter")
print("1. KM to M")
print("2. M to KM")
print("3. KG to G")
print("4. G to KG")
print("5. L to ML")
print("6. ML to L")

choice = int(input("\nEnter your choice (1-6): "))
value = float(input("\nEnter the value: "))

if choice == 1:
    print("Answer =", value * 1000, "m")

elif choice == 2:
    print("Answer =", value / 1000, "km")

elif choice == 3:
    print("Answer =", value * 1000, "g")

elif choice == 4:
    print("Answer =", value / 1000, "kg")

elif choice == 5:
    print("Answer =", value * 1000, "mL")

elif choice == 6:
    print("Answer =", value / 1000, "L")

else:
    print("Invalid Choice!")

print(f"\n----- Thankyou {a} for using Unit Converter -----")