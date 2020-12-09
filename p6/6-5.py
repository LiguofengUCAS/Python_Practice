info = {
    'nile':'egypt',
    'long river':'china',
    'da river':'usa',
    'yellow river':'china'
}

for river, country in info.items():
    print("The " + river + " runs through " + country + ".\n")

for river in sorted(info.keys()):
    print("The name of the river: " + river)

print("\n")

# for country in info.values():
for country in set(info.values()):
    print("The country is: " + country)
