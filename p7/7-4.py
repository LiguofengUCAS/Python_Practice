message = "\nPlease tell us the toppings you want to add in your pizza: "

while True:
    top = input(message)

    if top == 'quit':
        print("\nWe will get what you want!")
        break
    else:
        print("\nWe will add " + top.upper() + " to your pizza. Do you need anything else? ")
print("over")
