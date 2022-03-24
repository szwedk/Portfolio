#Dictionary (Called a struct on other languages)
#A dictionary is a collection which is 
#   unordered, 
#   changeable  
#   indexed. 
#In Python dictionaries are written with curly brackets, 
# and they have keys and values.
#So rather than an index 0,1,2,... 
#   we give each item a distinct key name

print('This is a Dictionary')
thisdict = {
"brand": "Ford", 
"model": "Mustang", 
"year": 1964
} 
print(thisdict)
print(' ')
print(' ')
print(' ')
print(' ')


print('Dictionary Indexing') #uses brackets and indexing
thisdict = {
"brand": "Ford", 
"model": "Mustang", 
"year": 1964
}
print(thisdict) 
thisdict["year"] = 2018 
x = thisdict["model"] 
print(x)
#y = thisdict[1] #-> Crash, No numeric index, only names
#print(y)
print(' ')
print(' ')
print(' ')
print(' ')


print('Dictionary: Adding an item')
thisdict = {
"brand": "Ford", "model": "Mustang", "year": 1964
}
thisdict["color"] = "red" #smart enough to figure out an append
print(thisdict)
print(' ')
print(' ')
print(' ')
print(' ')


print('Dictionary: Remove an item')
thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964
} 
thisdict.pop("model") 
print(thisdict)
print(' ')
print(' ')
print(' ')
print(' ')


print('Dictionary Loop')
thisdict = {
"brand": "Ford", "model": "Mustang", "year": 1964
}
print('\n Ugly print') 
print(thisdict)

print("\n key names only ")
for x in thisdict: 
    print(x)
print("\n Print Values ")
for x in thisdict:
    print(thisdict[x])
print(' ')
print(' ')
print(' ')
print(' ')


print('Nested Dictionaries')
child1 = { "name" : "Emil", "year" : 2004
}
child2 = {
"name" : "Tobias",
"year" : 2007 }
child3 = {
"name" : "Linus", "year" : 2011
}
myfamily = { "child1" : child1, "child2" : child2, "child3" : child3
}
print("\n Whole family:")
print(myfamily)
print("\n Just the second child data") 
print(myfamily["child2"])
print("\n Just the name of second child data") 
print(myfamily["child2"]["name"])
print(' ')
print(' ')
print(' ')
print(' ')







