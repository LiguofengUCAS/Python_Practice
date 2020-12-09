info_1 = {
    'name':'Jack',
    'age' :'18'  ,
    'city':'Beijing',
}

info_2 = {
    'name': 'Rose',
    'age' : '17'  ,
    'city': 'Hangzhou',
}

info_3 = {
    'name': 'Megumi',
    'age' : '16'    ,
    'city': 'Tokyo' ,
}

people = [info_1, info_2, info_3]

for indiv in people:
    for key, value in indiv.items():
        print("\n" + key.title() + ": " + value.title())

print("over")