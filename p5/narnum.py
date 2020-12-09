###########################################################
#                                                         #
# Author_name : Li Guofeng                                #
# This  Python program is used to compute                 #
# Narcissistic numbers from 1 to 999.                     #
# I hope you can enjoy the Python world!                  #
#                                                         #
###########################################################


for num in range(1,1000):
    hundred = int(num/100)
    ten = int((num - hundred*100)/10)
    one = int(num - hundred*100 - ten*10)

    if(hundred**3 + ten**3 + one**3 == num):
        print(num)
print("over")
