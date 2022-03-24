#===============================================
#   File:       classwork2Dictionary.py
#   Name:       Kamil Szwed
#   Date:       Feb 8, 2022
#   Purpose:    Dictionary
#===============================================

prices = {
    'Banana':1.5 , 
    'Apple':2.3, 
    'Orange':4.5, 
    'Cherry':6
    }
#dictionary of floats
stock = {
    'Banana':35 , 
    'Apple':42, 
    'Orange':40, 
    'Cherry':12 
    }


print(' Fruit \t Price \t Stock \t Value')
print('=========================================')
sum = 0
for x in prices and stock:
    print(x, '\t $',prices[x] ,'\t', stock[x],'\t $',(prices[x]*stock[x]))
    sum = sum + (prices[x]*stock[x])
print('==========================================')
print(f'The value of the whole shop is ${sum}')