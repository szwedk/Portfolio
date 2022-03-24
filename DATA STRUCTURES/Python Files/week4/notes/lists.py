#===============================================
#   File:       lists.py
#   Name:       Kamil Szwed
#   Date:       Feb 8, 2022
#   Purpose:    show lists
#===============================================

print('PRINT ALL')
fruit = [ "apple", "banana", "cherry", 34, 'TRUE', 12.8 ]
print( fruit )
print(' ')
print(' ')

#list index
print('PRINT SPECIFIC')
print(fruit[1]) #prints second
print(' ')
print(' ')

#negative indexing
print('PRINT LAST')
print(fruit[-1]) #prints last
print(' ')
print(' ')

print('EMPTY LIST')
Veggies = [] #empty list, nothing prints
print(Veggies)
print(' ')
print(' ')

#printing multiple
print('PRINT MULTIPLE')
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"] 
print( fruits[2:5] ) #stops before 5 / no melon
print(' ')
print(' ')

#changing data
print('CHANGING DATA')
fruit = ["apple", "banana", "cherry"] 
fruit [1] = "Grapes"
print( fruit )
print(' ')
print(' ')

#adding data
print('ADDING DATA')
fr = ["apple", "banana", "cherry"] 
print(len(fr))

fr.append("orange") 
print(fr)
print( len( fr) )
print(' ')
print(' ')

#Insert in the middle
#To add an item at the specified index, use the insert() method:
fruit = ["apple", "banana", "cherry"] 
fruit.insert(1, "orange")
print( fruit )
print(' ')
print(' ')

#for loops
print('FOR LOOP')
fruit = ["apple", "banana", "cherry"] 
for x in fruit:
    print(x)
Nums = [14,40, 32,45] 
for n in Nums:
    n = n+2
    print(n) 
print(Nums)
print(' ')
print(' ')

#List Search
print('LIST SEARCH')
Nums = [14,40, 32,45] 
print(Nums)
x = int(input("Enter an integer ")) 
if x in Nums:
    print("Found it") 
else:
    print(" Not found")
print(' ')
print(' ')

#Remove data
print('REMOVE DATA')
Nums = [14,40, 32,45] 
print(Nums)
if 32 in Nums:
    Nums.remove(32) #put remove in IF statement (like a cage)
print(Nums)
if 13 in Nums:
    Nums.remove(13) #never say remove - program crashed if number isnt there
print(Nums)
print(' ')
print(' ')

#Pop
#The pop() method removes the specified index, (or the last item if index is not specified): 
print('POP')
Nums = [14,40, 32,45,82,45,78] 
print(Nums)
#put in cage
if len(Nums) > 0:
    x = Nums.pop()
    print(x , " was removed") 
print(Nums)
#put in cage so program deosnt crash
if len(Nums) > 14:
    y = Nums.pop(14) 
    print(y , " was removed") 
print(Nums)
print(' ')
print(' ')

#delete
print('DELETE')
Nums = [14,40, 32,45,82,45,78] 
print(Nums)

del Nums[3] 
print(Nums)

del Nums #deletes the list -> cant print a list thats not there
#print(Nums)
print(' ')
print(' ')

#Sort (based on merge sort)
print('SORT')
Nums = [14,40, 32,45,82,45,78] 
print(Nums)

Nums.sort() 
print(Nums)
print(' ')
print(' ')
