

import array
def BinarySearch( s ):
    l =0
    r = len(Nums)-1
    while (l <= r):
        m = ( l+r )// 2
        if (Nums[m] == s):
            return m
        elif (Nums[m] < s):
            l= m+ 1 
        else :
            r = m- 1
# if we reach here, then element was not present 
    return -1

Nums = array.array( 'i' , [2, 5, 8, 12, 16, 23, 38, 56, 72, 91 ]) 
x = int(input("Enter number to look for: "))
loc = BinarySearch(x)
if loc == -1:
    print(x, " not found in the array ")
else:
    print(x , " found at location ", loc )