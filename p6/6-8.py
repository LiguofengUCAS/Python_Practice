julia = {
    'type': 'cat',
    'owner': 'jack'
}

megumi = {
    'type': 'dog',
    'owner': 'Rose'
}

tosaka = {
    'type': 'snake',
    'owner': 'emiya'
}

pets = [julia, megumi, tosaka]

for pet in pets:
    for key, value in pet.items():
        print("\n" + key + ": " + value)

print("\nover")
