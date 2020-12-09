def make_shirt(size, message):
    print("\nThe size of the shirt is " + size + ". ")
    print("\nThe message on the shirt is " + '"' + message + '". ')

# shirt_size = input("Please input your size:     ")
# shirt_message = input("Please input your message:       ")

# make_shirt(shirt_size, shirt_message)
# make_shirt(size = 'L', message = 'make it possible')

def spec_shirt(size = 'XL', message = 'PYTHON'):
    print("\nThe size of the shirt is " + size + ". ")
    print("\nThe message on the shirt is " + '"' + message + '". ')

spec_shirt()
spec_shirt(size = 'L')
spec_shirt(message = 'C++')
spec_shirt(size = 'L', message = 'make it possible')
