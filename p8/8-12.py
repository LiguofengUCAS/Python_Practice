def make_sandwich(*toppings):
    print("\nYour sandwich includes: ")
    for topping in toppings:
        print(topping)

make_sandwich('a','b','c')
make_sandwich('shit')
make_sandwich()
