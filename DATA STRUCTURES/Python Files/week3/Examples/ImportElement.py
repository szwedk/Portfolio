#====================
#   File:       
#   Name:       Kamil Szwed
#   Date:       Jan 25, 2022
#   Purpose:    
#=====================

print(' test 1 - append')
import array
sizes = array.array('i',[10,12,14,16,18]) 
print(sizes)
print( len(sizes) )

sizes.append(20) 
print(sizes) 
print( len(sizes) )
print('')

#another
print(' test 2 - instert')
import array
sizes = array.array('i',[10,12,14,16,18]) 
print(sizes)
sizes.insert(2,20) #EXPESNIVE only use when needed (insert)
print(sizes)
print( len(sizes) )

sizes.insert(0,22) 
print(sizes) 
print( len(sizes) )
print('')
print('')

#another
print('test 3 - extend')
import array
first = array.array('i',[10,12,14,16,18]) 
second = array.array('i',[20,22,24]) 
first.extend(second) #better use
print(first)
print( len(first) )
print('')
print('')

#another
print('test 4 - remove')
import array
first = array.array('i',[10,12,14,16,18]) 
first.remove(14)
print(first)
print( len(first) )
print('')
print('')

#another
print('test 5 - remove/ not found')
import array
first = array.array('i',[10,12,14,16,18])
# search before you remove 
c = first.count(23)
if c>0:
    first.remove(23)
else: 
    print("23 not found")
print('')
print('')

#another
print('test 6 - pop last')
import array
first = array.array('i',[10,12,14,16,18])
x = first.pop() 
# Remove last item and put it in x 
print(first)
print(x , " was popped!")
print('')
print('')

#another
print('test 7 - pop specific')
import array
first = array.array('i',[10,12,14,16,18])
x = first.pop(2) 
# Remove item with index 2 
print(first)
print(x , " was popped!")
print('')
print('')