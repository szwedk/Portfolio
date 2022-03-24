#================================================================
#   File:               PracticeForFinal.Test.py
#   Name:           Kamil Szwed
#   Date:             December 9, 2021
#   Purpose:        Write a program that reads from a sequential file,
#                           using fuctions to read data, calculate answers and outputs answers
#================================================================

#functions
def getData():
    items = []
    purchaseData = open('purchases.txt', 'r')
    for item in purchaseData:
        item = item.split()
        items.append(item)
    #end for item
    purchaseData.close()
    return items
#end Ftn getData

def priceCalc(items):
    calculatedCost = []
    totCost = 0.0
    c = 0
    for item in items:
        c = c + 1
        prodID = item[0]
        prodDesc = item[1]
        qty = int(item[2])
        price = float(item[3])
        cost = qty * price
        totCost = totCost + cost
        calculated = [prodID, prodDesc, cost]
        calculatedCost.append(calculated)
    #end for item
    return calculatedCost, totCost, c
#end fftn priceCalc

def headers():
    print("\n          Inventory Costs")
    print("\n    ID      PRODUCT      COST")
    print("=================================")
#end ftn headers

def output(calculatedCost, totCost, c):
    for x in calculatedCost:
        print(x[0],x[1],round(x[2],2))
    #end for x
    print("====================================")
    print("number of items puchased is",c)
    print("total cost of all items is", totCost)
#end ftn output
            



#mainProgram
items = getData()
calculatedCost, totCost, c = priceCalc(items)
headers()
output(calculatedCost, totCost, c)
#end main
