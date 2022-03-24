#============================================
#   File:		salescommission.test
#   Date:		Oct. 22, 2021
#   Purpose:	Sales commission
#   Author:		Kamil Szwed
#============================================

#Start Program

c = 0
sum = 0.0
totgal = 0.0

info = open("sales.txt", mode = 'r')

fran = []

for fran in info:
    fran = fran.split()
    name = fran[0]
    loc = fran[1]
    gals = int(fran[2])
    if gals < 500:
        com = gals * 0.03
    else:
        com = gals * 0.04
    #endif
    c = c+1
    sum = sum + com
    totgal = totgal + gals
    print(name," ", loc," ", gals," ",com)
#end for
print("Total customers processed is:", c)
print("Total gallons sold is:", totgal)
print("Total Commission is:", sum)

#end program
            
    
    
