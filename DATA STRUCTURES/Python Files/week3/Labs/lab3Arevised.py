#===============================================
#   File:       
#   Name:       Kamil Szwed
#   Date:       Jan 26, 2022
#   Purpose:    
# • Write a program to ask the user to enter 10 integers and append them one by one to an empty array
# • Print it out
# • Get the sum and average of the numbers in the array 
# • Print out the sum and the average
# • Print out the numbers that are bigger than the average 
# • Get the maximum of the numbers in the array
# • Print out the maximum
# • Get the minimum of the numbers in the array
# • Print out the minimum
#================================================


import array
ints = array.array('i',[])

for x in ints:
    n = int(input('Enter an integer:'))
    ints.append(n)
print(ints)

sum = 0
for mem in ints:
    sum = sum+mem
avg = sum/10
print(f'The sum is {sum}')
print(f'The average is {avg}')
print(f'The Maximum is {max(ints)}')
print(f'The Minimum is {min(ints)}')
