

print('This is a set')
fruit = { "apple", "banana", "cherry" } #uses brackets
print( fruit )
print(' ')
print(' ')

print('printing a whole set')
fruit = {"apple", "banana", "cherry"}
for x in fruit : 
    print(x) #dont control who goes first or second
print(' ')
print(' ')

print('adding to set')
fruit = {"apple", "banana", "cherry"} #no order
fruit.add("orange")
print(fruit)
fruit.update(["kiwi", "mango", "grapes"]) #no order, no end or beginning cant append
print(fruit)
print(' ')
print(' ')

print('removing from set')
Numbers = {7,13,34,56,22} 
print(Numbers) 
Numbers.remove(34) 
print(Numbers) 
Numbers.discard(56) 
print(Numbers)


