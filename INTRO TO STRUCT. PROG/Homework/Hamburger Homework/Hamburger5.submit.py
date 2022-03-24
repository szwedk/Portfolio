#======================================================
#       File:            Hamburger5.submit
#       Programmed by:   K. Szwed
#       Date:            Sept. 15, 2021
#======================================================

#Start Program

answer = 'Y'

print (" Hamburger 5  Pre-test loop....")
print ("===============================")

while answer == 'Y' or answer =='y':

    noBgHugo = input ("Enter amount of Big Hugo burgers desired ==> ")
    noDbCheese = input ("Enter amount of Double Cheese burgers desired ==> ")
    noCheese = input ("Enter amount of Cheese burgers desired ==> ")
    amtGiven = input ("Enter dollar amount given by customer ==>$")

    priceBgHugo = 3.27
    priceDbCheese = 2.50
    priceCheese = 1.55

    costBgHugo = int(noBgHugo) * priceBgHugo
    costDbCheese = int(noDbCheese) * priceDbCheese
    costCheese = int(noCheese) * priceCheese

    total = costBgHugo + costDbCheese + costCheese

    change = int(amtGiven) - total

    print(" The total cost of these burgers is $ ", total)
    print(" The change from ", amtGiven, " is $ ", change)

    answer = input ("Do again? (Y/N) ==> ")

print ("end of job")

#end program

>>> 
= RESTART: /Users/kamilszwed/Documents/SHU/CS-111-B Python Files/Homework/Sept 15, 2021/Hamburger5.test.py
 Hamburger 5  Pre-test loop....
===============================
Enter amount of Big Hugo burgers desired ==> 0
Enter amount of Double Cheese burgers desired ==> 1
Enter amount of Cheese burgers desired ==> 0
Enter dollar amount given by customer ==>$10
 The total cost of these burgers is $  2.5
 The change from  10  is $  7.5
Do again? (Y/N) ==> y
Enter amount of Big Hugo burgers desired ==> 0
Enter amount of Double Cheese burgers desired ==> 5
Enter amount of Cheese burgers desired ==> 0
Enter dollar amount given by customer ==>$20
 The total cost of these burgers is $  12.5
 The change from  20  is $  7.5
Do again? (Y/N) ==> n
end of job
>>> 


