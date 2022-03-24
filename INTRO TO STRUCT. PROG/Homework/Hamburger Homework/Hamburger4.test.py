#======================================================
#       File:            Hamburger4.test
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


