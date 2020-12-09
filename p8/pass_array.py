def greet(names):
    new_name = []
    while names:
        name = names.pop()
        if name == 'a':
            new_name.append(name + 'change')
        else:
            new_name.append(name)

    return new_name

users = ['a', 'b', 'c']
new_name = greet(users[:])
print(users)
print(new_name)
