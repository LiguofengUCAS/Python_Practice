num = input("Please input the number you want to judge: ")
num = int(num)

if num % 10 == 0:
    print("\n" + str(num) + " is equal to 0 (mod 10).")
else:
    print("\n" + str(num) + " is NOT equal to 0 (mod 10).")
