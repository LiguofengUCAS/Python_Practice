class User():

    def __init__(self, firstname, lastname, age):
        self.fn = firstname
        self.ln = lastname
        self.age = age

    def describe_user(self):
        print("The full name of the user: " + self.fn.title() + " " + self.ln.title())
        print("The age of the user: " + str(self.age))

    def greet_user(self):
        print("Dear " + self.fn.title() + ", welcome to our website!")


user_0 = User('guofeng', 'li', 20)
user_1 = User('zeng', 'li', 20)
user_2 = User('xihong', 'zhu', 20)

user_0.describe_user()
user_0.greet_user()

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()
