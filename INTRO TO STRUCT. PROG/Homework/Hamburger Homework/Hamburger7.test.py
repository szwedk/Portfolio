#======================================================
#   Author:         K. Szwed
#   Date:           Sept. 27, 2021
#   File Name:      Hamburger7.Test
#   Purpose:        Calculating cost of burgers, drinks, fries
#======================================================

# Start Program

print(" Hamburger 7 ...")
print("==================")

costHamburger = 1.75;
costCheese = 0.55;
costDrink = 0.99;
costFrenchFries = 1.55;

noHamburgers = input("Enter amount of Hamburgers desired ===>")
cheese = input("Do you want cheese on it? (Y/N) ===> ")

if cheese == 'Y' or cheese == 'y':
    noCheeses = input("How many with cheese?, 0 for none ===>")
else:
    noCheeses = 0

noDrink = input ("Enter amount of drinks desired, 0 for none ===>$   ===>")
noFrenchFries = input("Enter amount of french fries desired, 0 for none ===>$")

hambCost = float(noHamburgers) * costHamburger
print(" ... cost of burgers is $", hambCost)

cheeseCost = float(noCheeses) * costCheese
print(" ... cost of cheese is $", cheeseCost)

drinkCost = float(noDrink) * costDrink
print(" ... cost of drink is $", drinkCost)

ffCost = float(noFrenchFries) * costFrenchFries
print(" ... cost of French Fries is $", ffCost)

totalCost = cheeseCost + hambCost + drinkCost + ffCost
print(" ... total cost is $", totalCost)

amtGiven = input ("Amount Given: $ ")

change = float(amtGiven) - totalCost

print("Your Change from ", amtGiven, " dollars is, $ ", change)
print ("end of job")

# End main Program

