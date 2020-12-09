uconfirm_users = ['alice', 'bob', 'celia']
confirm_users = []

while uconfirm_users:
    user = uconfirm_users.pop()
    confirm_users.append(user)

print("\nThe following users have been confirmed: ")
for confirm_user in confirm_users:
    print(confirm_user.title())

print(uconfirm_users)
print(confirm_users)
