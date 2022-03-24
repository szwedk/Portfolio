#======================================================================
#   File:       Hamburger8.test
#   Author:     K. Szwed
#   Date:       Sept. 2, 2021
#   Purpose:    Nested if statements - note 3 if statements & 3 end statements
#======================================================================

# Start Program

print(" ...Hamburger 8... ")
print("====================")

qty = int(input("Enter the number of hamburgers desired ==> "))
hamburgerType = input(" Type? Enter C for cheese, P for plain, or D for double ==> ")

if hamburgerType == 'C' or hamburgerType == 'c':
    cost = 2.79
else:
    if hamburgerType == 'P' or hamburgerType == 'p':
        cost = 2.05
    else:
        if hamburgertype == 'D' or hamburgerType =="d":
                cost = 0.0

        else:
            print ("Wrong type! Run again!")
            cost = 0.0

total = cost * float(qty)
print("total cost is ==> $ ", total)

amtGiven = input ("Enter amount intended ==> $ ")

change = float(amtGiven) - total
print ("your change is ==> $ ", change)
print ("End of Job :)")

# End Program
