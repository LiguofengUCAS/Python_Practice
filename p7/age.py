message = "\nPlease tell me your age : "

age = input(message)
while age != 'quit':
    age = int(age)
    if age < 3:
        print("\nFree")
    elif age <= 12:
        print("\n$12")
    else:
        print("\n$15")
    age = input(message)

print("over")
