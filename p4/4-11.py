names = ['a', 'b', 'c', 'd']
friend_names = names[:]

names.append('e')
friend_names.append('f')

print("My favorite pizza are:")
for name in names:
    print(name)

print("My friend's favorite pizza are:")
for friend_name in friend_names:
    print(friend_name)
