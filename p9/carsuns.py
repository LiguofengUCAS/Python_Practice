class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_info(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def updata_odometer(self, miles):
        if miles < self.odometer_reading:
            print("You cannot roll back the odometer!")
        else:
            self.odometer_reading = miles

    def increase_odometer(self, miles):
        self.odometer_reading += miles

    def take_place_test(self):
        print("Now is Car!!!")


class Elecar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # self.battery = 70
        self.battery = Battery()

    def take_place_test(self):
        print("Now is Elecar!!!")


class Battery():
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWH battery.")


my_tesla = Elecar('tesla', 'model s', 2016)

print(my_tesla.get_info())
# my_tesla.describe_battery()
my_tesla.battery.describe_battery()
my_tesla.take_place_test()
