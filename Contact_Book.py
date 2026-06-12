Contact = []

n = int(input("How many contacts do you want to add? "))

for i in range(n):
    name = input("Enter Name of the Contact: ")
    number = input("Enter Number of the Contact: ")

    Contact.append([name, number])

print("\nContacts:")
for contact in Contact:
    print(contact[0], "=", contact[1])