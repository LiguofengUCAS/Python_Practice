from car import Car
# import car


# my_new_car = car.Car('audi', 'a4', 2016)
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_info())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
