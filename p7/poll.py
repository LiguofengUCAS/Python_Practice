rps = {}

polling_active = True

while polling_active:
    name = input("\nWhat the fuck is your name? ")
    rp = input("Which mountain would you like to climb someday? ")

    rps[name] = rp

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, rp in rps.items():
    print(name + " would like to climb " + rp + ".")
