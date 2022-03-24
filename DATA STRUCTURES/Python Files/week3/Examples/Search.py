

import array
def Search( s ):
    for n in Nums: 
        if n==s:
            print(" Found it ")
        return
    print(" Not found") 
    return
Nums = array.array( 'i' , [ 37, 45, 66, 12, 82, 4, 31, 12, 59, 19 ] ) 
x = int ( input( "Enter number to look for: "))
Search(x)

if x in Nums:
    print('found IT')
