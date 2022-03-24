#===============================================
#   File:       
#   Name:       Kamil Szwed
#   Date:       Jan 26, 2022
#   Purpose:    Write a program that
#   a. Generates 50,000 random numbers and puts them in
#       an array.
#   b. Sorts the numbers using any sorting technique
#       (Selection sort is fine, but you can try another one).
#       This should take a few minutes to run.
#   c. Ask the user for a number between 0 and 20,000,000
#       and search for it in your sorted array using a simple
#       linear search. Is this a good idea?
#   d. Ask the user for a number between 0 and 20,000,000
#       and search for it in your sorted array using a binary search.
#================================================

import array
import random

#ftns

# Uses a slow Linear search to find the number
#def linearSearch(arr, x):
#    for i in range(len(arr)):
#        if arr[i] == x:
#            return i
#    return -1

# Iterative Binary Search Function
def binarySearch(arr, x):
    l = 0 # l stands for low
    h = len(arr) - 1 # h stands for high
    m = 0 # m stands for middle
    while l <= h:
        m = (h + l) // 2
        # If x is greater, ignore left half
        if arr[m] < x:
            l = m + 1
        # If x is smaller, ignore right half
        elif arr[m] > x:
            h = m - 1
        # X is at the middle of the array
        else:
            return m
    # Number not in array if -1 is returned
    return -1

# Sorts the array into numerical order
def sort(list):
    for i in range(1,len(list)):
        value = list[i]
        i = i-1
        while i>=0:
            if value < list[i]:
                list[i+1] = list[i]
                list[i] = value
                i -= 1
            else:
                break
    return list


def randomNum():
    rdmInt = array.array('L',[])
    for x in range(0,21):
        rdm = random.randint(0,20)
        rdmInt.append(rdm)
#    print(rdmInt, end=' ')
    return rdmInt

def foundOrNot(Bin): #to use linear search add (lin, )
    if (Bin==-1): #to use linear search ass ((lin ==-1) or )
        print('Not Found')
    else:
        print('Number Found!')
        print(f'The position of your number within the array is {Bin}')
        #print(f'The number you found is {lin}')
#endFtns

#main
arr = randomNum()
sortedList = sort(arr)
print(sortedList)
x = int(input('Enter a number to find: '))
#type1 = linearSearch(arr,x)
type2 = binarySearch(arr,x)
FnF = foundOrNot(type2) #to use linearSearch add ( )
#endMain


