from random import randint


class Die():

    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        print("Die_" + str(self.sides) + "'s rolling result: " + str(randint(1, self.sides)))


die_6 = Die(6)
die_10 = Die(10)
die_20 = Die(20)

i = 1
while i <= 10:
    die_6.roll_die()
    i += 1

i = 1
while i <= 10:
    die_10.roll_die()
    i += 1

i = 1
while i <= 10:
    die_20.roll_die()
    i += 1
