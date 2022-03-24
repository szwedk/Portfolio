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
#ftns

#main
import array
tenInts = array.array('i',[])

for x in range(0,10): #gives number starting at zero and ends BEFORE 10... so 9
    n = int(input('Enter an integer: '))
    tenInts.append(n)
print(tenInts)

sum = 0
for mem in tenInts:
    sum = sum+mem
print('The Sum is', sum)
average = sum /10
print('The Average is', average)

for mem in tenInts:
    if mem > average:
        print(mem, end=' ')
print(" ")

maxs = tenInts[0]
for mem in tenInts:
    if mem > maxs:
        maxs = mem
print('Maximum is ', maxs)

mins = tenInts[0]
for mem in tenInts:
    if mem < mins:
        mins = mem
print('Minimum is ', mins)

print(min(tenInts))
print(max(tenInts))

