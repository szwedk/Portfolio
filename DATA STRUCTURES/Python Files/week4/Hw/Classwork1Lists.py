#===============================================
#   File:       classwork1lists.py
#   Name:       Kamil Szwed
#   Date:       Feb 8, 2022
#   Purpose:    lists
#===============================================

import random

#1,2
Nums =[]
for i in range(0,10):
    x = int(input('Enter an integer: -->  '))
    Nums.append(x)
print(Nums)
#3
print(F'The sum is {sum(Nums)}')
print(F'The min is {min(Nums)}')
print(F'The max is {max(Nums)}')
print(F'The lenth is {len(Nums)}')
#4
random.shuffle(Nums)
#5
print(f'the numbers shuffled are {Nums}')
#6
Nums.sort() #default sort is min to max
#7
print(f'The numbers sorted are {Nums}')
#8
#create a new list which has the same data with duplicates removed
noDups = []
for i in Nums:
    if i not in noDups:
        noDups.append(i)
print(noDups)


