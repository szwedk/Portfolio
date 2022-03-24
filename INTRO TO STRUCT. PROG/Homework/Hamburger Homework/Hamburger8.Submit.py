#======================================================================
#   File:       Hamburger8.Submit
#   Author:     K. Szwed
#   Date:       Sept. 2, 2021
#   Purpose:    Nested if statements - note 3 if statements & 3 end statements
#======================================================================

# Start Program

print(" ...Hamburger 8... ")
print("====================")

qty = input("Enter the number of hamburgers desired ==> ")
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

# Execution
= RESTART: /Users/kamilszwed/Documents/SHU/CS-111-B Python Files/Homework/Hamburger Homework/Hamburger8.test.py
 ...Hamburger 8... 
====================
Enter the number of hamburgers desired ==> 10
 Type? Enter C for cheese, P for plain, or D for double ==> p
total cost is ==> $  20.5
Enter amount intended ==> $ 50
your change is ==> $  29.5
End of Job :)
>>> 
= RESTART: /Users/kamilszwed/Documents/SHU/CS-111-B Python Files/Homework/Hamburger Homework/Hamburger8.test.py
 ...Hamburger 8... 
====================
Enter the number of hamburgers desired ==> 1
 Type? Enter C for cheese, P for plain, or D for double ==> c
total cost is ==> $  2.79
Enter amount intended ==> $ 10
your change is ==> $  7.21
End of Job :)
>>> 

