def build_info(name, **others):
    user = {}
    user['fullname'] = name
    for key, value in others.items():
        user[key] = value
    
    return user

user_0 = build_info('lizeng',
                    age = 20,
                    location = 'princeton'
                    )

user_1 = build_info('liguofeng',
                    age = 20,
                    location = 'MIT',
                    girlfriend = 'wbb'
                    )

print(user_0)
print(user_1)
