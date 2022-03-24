#=============================================
#   File:       Payroll
#   Name:       K. Szwed
#   Date:       Oct. 13
#   Purpose:    to do payroll with counter and accumulators
#=============================================

#start Program

#initialize counter to zero
c = 0
#initialize accumulator to zero
totNet = 0.0
totTax = 0.0

id = int(input("Enter an ID ==> "))
while not(id == -999):
    fn = input("Enter first name: ")
    ln = input("Enter last name: ")
    hr = int(input("Enter number of hours wokerd ==> "))
    rate = float(input("Enter rate of pay $"))
    txrate = float(input("Enter tax rate in decimal format ==> "))
    # calc gross, taxes owed
    if hr <= 40:
        gross = hr * rate
    else:
        oth = hr - 40
        otp = oth * 1.5 * rate
        regp = rate * 40
        gross = regp + otp
    #endIf
    taxesOwed = gross * txrate
    net = gross - taxesOwed
    print(id,", ",fn," ",ln,", ","Your pay is $",net)
    print("Your taxes are $",taxesOwed)
    c = c + 1
    totNet = totNet + net
    totTax = totTax + taxesOwed
    id = int(input("Enter an ID:"))

#endWhile
print("\n. . . Total taxes collected is $", totTax)
print(". . . Total Net pay is $", totNet)
print(". . . Total employees paid is ")
print(". . . End of Job")

      
