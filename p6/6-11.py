cities = {
    'beijing':{
        'country': 'china',
        'popularity' : 10000000,
        'fact' : 'nb'
    },

    'tokyo':{
        'country': 'japan',
        'popularity': 1000000,
        'fact' : 'hot'
    },

    'london':{
        'country': 'england',
        'popularity': 100000,
        'fact': 'ypm'
    }
}

for city, info in cities.items():
    print("\n" + city.title() + ": ")
    for item, context in info.items():
        print("\n" + item.title() + ": " + str(context).title())

print("\nover")
