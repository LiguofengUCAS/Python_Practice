current_users = ['a', 'b', 'c', 'd', 'e']
new_users = ['a', 'b', 'x', 'y', 'z']

for new_user in new_users:
    if new_user in current_users:
        print("This guy is already in")
    else:
        print("null")
