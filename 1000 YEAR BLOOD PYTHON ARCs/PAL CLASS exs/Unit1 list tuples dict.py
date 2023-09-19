
####################################################################################################
######     Lists[]
"""
Excercise 1.1.1: Access List elements/Append to list
Write a Python program that creates a list named my_list with elements [1,2,3,4,5]. 
Print the third element of the list
"""




my_list = []

for i in range(1,6): 
    my_list.append(i)

print(my_list)
print(my_list[2])

print()
print()
"""
Excercise 1.1.2: remove element/sort list/ find min and max
Write a Python program that creates a list named my_list with random 69 elements . 
Print the min and max
"""
import random

my_list1 = []

for i1 in range(random.randint(18, 30)):
    my_list1.append(random.randint(0, 69))

my_list1.reverse()
my_list1.sort()

print(my_list1)
min = min(my_list1)
max = max(my_list1)

print("the Min is ",min," and the Max is ",max)