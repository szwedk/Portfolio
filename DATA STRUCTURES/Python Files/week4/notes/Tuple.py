


print('print tuple')
thistuple = ("apple", "banana", "cherry") 
print(thistuple)
#thistuple[1] ="grape" #does not allow change
print(' ')
print(' ')

print('print first and last')
thistuple = ("apple", "banana", "cherry") 
print(thistuple)
print(thistuple[1]) # second one 
print(thistuple[-1]) # last one
print(' ')
print(' ')

print('tuple to list') 
x = ("apple", "banana", "cherry") #regular parenthesis = tuple
y = list(x) # convert to a list
y[1] = "kiwi" # change the list
x = tuple(y)  # Convert back to a tuple
print(x)
print(' ')
print(' ')

print('other tuple functions') 
x = ("apple", "banana", "cherry")

y = x.count("cherry")
print(" There are ",y," cherries") 
z = x.index("cherry") 
print("Cherries at location ",z)
del x
print(' ')
print(' ')
