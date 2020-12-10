class Restaurant():

    def __init__(self, restaurant_name, restaurant_type):
        self.name = restaurant_name
        self.type = restaurant_type
        self.num = 0

    def describe_res(self):
        print("The name of the restaurant is " + self.name + ".")
        print("The type of the restaurant is " + self.type + ".")

    def open_res(self):
        print("The restauraut is open now.")

    def updata_num(self, boost):
        self.num += boost
        print(str(self.num) + " customers have been served in " + self.name + ".")


res_0 = Restaurant('东来顺', '火锅')
res_1 = Restaurant('呷哺呷哺', '小火锅')
res_2 = Restaurant('村上一屋', '寿司')

res_0.describe_res()
res_0.open_res()

res_1.describe_res()
res_1.open_res()

res_2.describe_res()
res_2.open_res()

res_0.updata_num(5)
res_0.updata_num(6)
