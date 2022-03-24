#================================================================
#   File:               PurchasesCode.Test.py
#   Name:           Kamil Szwed
#   Date:             December 1, 2021
#   Purpose:        Write a program that reads from a sequential file,
#                           using fuctions to read data, calculate answers and outputs answers
#================================================================

#Functions

def headers():
    print("")
    print("         Purchases")
    print("   ID    Product   Cost")
    print("==============================")
#end ftn headers

def getData():
    items= []
    p_data = open('purchases.txt', 'r')
    for thing in p_data:
        #print(thing)
        thing = thing.split()
        #print(thing[0], thing[1], thing[2], thing[3])
        items.append(thing)
    #end For things
    p_data.close()
    return items
#end Ftn getDat

def priceCalc(items):
    calculated = []
    for object in items:
        amt = int(object[2])
        price = float(object[3])
        cost = amt * price
        lst = [object[0],object[1], cost]
        calculated.append(lst)
    #end For Object
    return calculated
#end ftn priceCalc

def output(x): # x is calculated from output(calculated)
    for item in x:
        print(item[0],"  ", item[1],"      ", round(item[2],2))
    #end for item
#end ftn output


#Main Program
#assignment statement
items = getData()
#Returned from func = What's sent to func
calculated = priceCalc(items) #can be any name that comes back from list
headers()
output(calculated) #nothing getting sent to fuctions
#end Main

