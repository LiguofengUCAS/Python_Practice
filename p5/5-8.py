users = ['admin', 'bullshit', 'asshole', 'pussy', 'dick']

for user in users:
    if(user == 'admin'):
        print("Hello admi, would you like to pick up a girl?")
    else:
        print("Hello " + user + ", thanks for logging in!")

if(users):
    del users
    users = []
    print("refreshing is over")
else:
    print("We need to find some users")
print(users)
