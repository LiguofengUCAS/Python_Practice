def get_name(first_name, last_name, middle_name = ''):
    full_name = first_name +" " + middle_name + " " + last_name
    return full_name.title()

musician = get_name('jim', 'gorden')
print(musician)
