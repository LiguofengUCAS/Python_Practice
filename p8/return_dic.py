def build_person(first_name, last_name):
    person = {'first': first_name.title(), 'last': last_name.title()}
    return person

musician = build_person('jim', 'gorden')
print(musician)
