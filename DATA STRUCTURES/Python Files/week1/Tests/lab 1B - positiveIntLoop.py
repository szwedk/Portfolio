#====================================
#   File:                 positiveIntLoop
#   Name:                 Kamil Szwed
#   Date:                 Jan 20, 22
#   Purpose:              Write a program to ask the user for a positive integer,
#                               and then print out all number from 0 to that number.
#====================================

#mainProgram

integers = []
ans = 0
while ans >= 0:
    ans = int(input("Enter a postive integer, Enter done when done ==> "))
    integers.append(ans)
else:
    for item in integers:
        if item < 0:
            integers.remove(item)
    integers.sort()
    print(integers)
#endMain
    
