##############################################
# Title: Participation Activity - Sequence Data Types
# Author: Seunghyun Cho
# Version: 3.10.6
# Date: Jan 27th, 2023
#
# Description: This program makes three lists(integers from 1 to 10, 10 random numbers between 5~20, combined two lists) and one tuple(combined two lists).
##############################################

import random

list_1 = [*range(1, 11)]
print("list 1: ", list_1)

list_2 = list()

for i in range(10):
    n = random.randint(5, 21)
    list_2.append(n)

print("list 2: ", list_2)

combined_list = list_1
combined_list = combined_list + list_2
print("combined list: ", combined_list)

combined_tuple = tuple(combined_list)
print("combined tuple: ", combined_tuple)
