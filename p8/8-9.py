magicians = ['a', 'b', 'c', 'd']

def make_great(names):
    new_names = []
    while names:
        new_names.append(names.pop())
    new_names.sort()
    return new_names

def show_magicians(names):
    for name in names:
        print(name)

magicians = make_great(magicians[:])
show_magicians(magicians)
