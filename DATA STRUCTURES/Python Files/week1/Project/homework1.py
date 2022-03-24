#====================
#   File:       Project1.py
#   Name:       Kamil Szwed
#   Date:       Jan 25, 2022
#   Purpose:    The Yorktown theatre has 300 hall seats and 100 mezzanine seats. A hall seat costs $10 for an adult
#               and $7 for a child. A mezzanine seat costs $8 for an adult and $5 for a child. Write a program to
#               REPEATEDLY prompt the user to enter the required seating (1 for hall, 2 for mezzanine), the number
#               of adults and children in the party, and the print out a receipt and the number of remaining seats in
#               Hall and Mezzanine. An order will be refused if there are not enough seats in the required area. The
#               program loops until there are no more seats in either hall or mezzanine.
#=====================


#mainProgram
print('Yorktown theatre has 300 hall seats and 100 mezzanine seats.')
yorktown = 300
mezzanine = 100
while (mezzanine >= 0 or yorktown >= 0):
    theat = int(input('Enter 1 for Hall seat, 2 for Mezzanine seat'))
    if theat == 1 or theat == 2:
        adl = int(input('Enter amt of adults ==> '))
        kid = int(input('Enter amt of children ==> '))
        cost = 0
        Ma, Mk, Ha, Hk = 8, 5, 10 ,7
        if theat == 1 and  yorktown - (adl + kid) >= 0:
            yorktown = yorktown - (adl + kid)
            cost = (adl * Ha)+(kid * Hk)
            adlCost = (adl * Ha)
            kidCost = (kid * Hk)
            print(f'Great, You got {adl} adult tickets for $ {adlCost} and {kid} child tickets for ${kidCost} so your total is ${cost} ')
            print(f'Remaining seats: Hall {yorktown} Mezzanine {mezzanine} ')
        elif theat == 2 and mezzanine - (adl + kid) >= 0:
            mezzanine = mezzanine - (adl + kid)
            cost = (adl * Ma)+(kid * Mk)
            adlCost = (adl * Ma)
            kidCost = (kid * Mk)
            print(f'Great, You got {adl} adult tickets for $ {adlCost} and {kid} child tickets for ${kidCost} so your total is ${cost} ')
            print(f'Remaining seats: Hall {yorktown} Mezzanine {mezzanine} ')
        else:
            print('not enough seats')

    else:
        print('please enter 1 or 2 !')

#endMain
