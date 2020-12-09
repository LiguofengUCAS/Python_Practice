###################################################
#                                                 #
# Name : Li Guofeng                               #
# My_ID: 2018K8009922027                          #
# HW_ID: 14_1                                     #
# This program can be used to find all elements   #
# or subsets of a set given.                      #
#                                                 #
###################################################


def print_element(arrays):
    print("\nElements in the member are: ")
    for element in arrays:
        print(element)


def print_subset(arrays):
    print("\nSubsets of the set are: ")

    N = len(arrays)
    for i in range(2 ** N):
        # 子集个数，每循环一次一个子集
        subset = []
        for j in range(N):
            # 用来判断二进制下标为j的位置数是否为1
            if (i >> j) % 2:
                subset.append(arrays[j])
        print(subset)


print("----Program starts running----")

member_0 = [1,      [1, 2, 3, 4, 5]]
member_1 = [3,      [1, 2, 3, 4, 5]]
subset   = [[2, 4], [1, 2, 3, 4, 5]]

print_element(member_0)
print_element(member_1)

print_subset(subset)
