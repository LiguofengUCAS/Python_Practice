names = ['lizeng', 'zhuxihong', 'liguofeng']

message_0 = "Dear " + names[0] + ", welcome to our party!"
message_1 = "Dear " + names[1] + ", welcome to our party!"
message_2 = "Dear " + names[2] + ", welcome to our party!"

print(message_0)
print(message_1)
print(message_2)

invalid_name = names.pop()
print("invalid name is: " + invalid_name)
print(message_0)
print(message_1)

print("\nI got one bigger table!")

names.insert(1, 'huboxiang')
names.append('wangweitong')
message_3 = "Dear " + names[3] + ", welcome to our party!"

print(message_0)
print(message_1)
print(message_2)
print(message_3)

print("FUCK! The table is not avalible so we must remove someone.")

pop_1 = names.pop()
print("Sorry to tell you Mr." + pop_1 + " that you must leave")

pop_2 = names.pop()
print("Sorry to tell you Mr." + pop_2 + " that you must leave")

message_0 = "Dear " + names[0] + ", welcome to our party!"
message_1 = "Dear " + names[1] + ", welcome to our party!"

print(message_0)
print(message_1)

del names[0]
del names[0]
print(names)
