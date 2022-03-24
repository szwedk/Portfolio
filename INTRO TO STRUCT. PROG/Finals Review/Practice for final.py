#================================================================
#   File:               PracticeForFinal.Test.py
#   Name:           Kamil Szwed
#   Date:             December 9, 2021
#   Purpose:        Write a program that reads from a sequential file,
#                           using fuctions to read data, calculate answers and outputs answers
#================================================================

#Functions
def getData():
    items = []
    purchaseData = open('purchases.txt', 'r')
    for theThing in purchaseData:
        theThing = theThing.split()
        items.append(theThing)
    #end for theThing
    purchaseData.close()
    return items
#end ftn Def

def priceCalc(items):
    calculatedCost = []
    for object in items:
        amt = int(object[2])
        price = float(object[3])
        cost = amt * price
        theList = [object[0],object[1], cost]
        calculatedCost.append(theList)
    #end For object
    return calculatedCost
#end Ftn priceCalc

def headers():
    print("")
    print("         Purchases")
    print("   ID    Product   Cost")
    print("==============================")
# end Ftn headers

def output(x):
    for anyItem in x:
        print(anyItem[0],' ',anyItem[1],' ',round(anyItem[2],2))
    #end for anyItem
#end Ftn output


#Main Code

items = getData()
calculatedCost = priceCalc(items)
headers()
output(calculatedCost)

#end Main






