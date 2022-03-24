#======================================================
#   Author:         K. Szwed
#   Date:           Sept. 27, 2021
#   File Name:      Hamburger7.Submit
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


# Execution Run

>>> 
= RESTART: /Users/kamilszwed/Documents/SHU/CS-111-B Python Files/Homework/Hamburger Homework/Hamburger7.test.py
 Hamburger 7 ...
==================
Enter amount of Hamburgers desired ===>3
Do you want cheese on it? (Y/N) ===> y
How many with cheese?, 0 for none ===>2
Enter amount of drinks desired, 0 for none ===>$   ===>3
Enter amount of french fries desired, 0 for none ===>$2
 ... cost of burgers is $ 5.25
 ... cost of cheese is $ 1.1
 ... cost of drink is $ 2.9699999999999998
 ... cost of French Fries is $ 3.1
 ... total cost is $ 12.42
Amount Given: $ 20
Your Change from  20  dollars is, $  7.58
end of job
>>> 
