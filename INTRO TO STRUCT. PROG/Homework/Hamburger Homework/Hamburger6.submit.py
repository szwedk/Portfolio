#======================================================
#       File:            Hamburger6.submit
#       Programmed by:   K. Szwed
#       Date:            Sept. 15, 2021
#======================================================

#Start Program

answer = 'Y'

print (" Hamburger 6  Post-test loop....")
print ("===============================")

while True:

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
    if answer == 'N' or answer == 'n':
        break

print ("end of job")

# End Program


= RESTART: /Users/kamilszwed/Documents/SHU/CS-111-B Python Files/Homework/Sept 15, 2021/Hamburger6.test.py
 Hamburger 6  Post-test loop....
===============================
Enter amount of Big Hugo burgers desired ==> 2
Enter amount of Double Cheese burgers desired ==> 1
Enter amount of Cheese burgers desired ==> 1
Enter dollar amount given by customer ==>$30
 The total cost of these burgers is $  10.59
 The change from  30  is $  19.41
Do again? (Y/N) ==> y
Enter amount of Big Hugo burgers desired ==> 2
Enter amount of Double Cheese burgers desired ==> 0
Enter amount of Cheese burgers desired ==> 1
Enter dollar amount given by customer ==>$20
 The total cost of these burgers is $  8.09
 The change from  20  is $  11.91
Do again? (Y/N) ==> n
end of job
>>> 
