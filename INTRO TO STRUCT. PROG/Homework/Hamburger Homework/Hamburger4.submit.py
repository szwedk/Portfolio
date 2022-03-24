#======================================================
#       File:            Hamburger4.submit
#       Programmed by:   K. Szwed
#       Date:            Sept. 15, 2021
#======================================================

#Start Program


priceBgHugo = 3.27
priceDbCheese = 2.50
priceCheese = 1.55

noBgHugo = input ("Enter amount of Big Hugo burgers desired ==> ")
noDbCheese = input ("Enter amount of Double Cheese burgers desired ==> ")
noCheese = input ("Enter amount of Cheese burgers desired ==> ")
amtGiven = input ("Enter dollar amount given by customer ==>$")

costBgHugo = int(noBgHugo) * priceBgHugo
costDbCheese = int(noDbCheese) * priceDbCheese
costCheese = int(noCheese) * priceCheese

total = costBgHugo + costDbCheese + costCheese

change = int(amtGiven) - total

print(" The total cost of these burgers is $ ", total)
print(" The change from ", amtGiven, " is $ ", change)
print(" Thank you for shopping with us, hope you enjoyed")



>>> 
= RESTART: /Users/kamilszwed/Documents/SHU/CS-111-B Python Files/Homework/Sept 15, 2021/Hamburger4.test.py
Enter amount of Big Hugo burgers desired ==> 1
Enter amount of Double Cheese burgers desired ==> 0
Enter amount of Cheese burgers desired ==> 1
Enter dollar amount given by customer ==>$10
 The total cost of these burgers is $  4.82
 The change from  10  is $  5.18
 Thank you for shopping with us, hope you enjoyed
>>> 
