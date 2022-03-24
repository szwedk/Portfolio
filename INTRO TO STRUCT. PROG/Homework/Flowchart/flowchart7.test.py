#=======================================
#   File:       flowchart7.test
#   Date:       October 22, 2021
#   Name:       Kamil Szwed
#=======================================

#Start Program

ans = input("would you like to start the program? (Y/N)")

while (ans=='y') or (ans=='Y'):
    id = int(input("Input workers ID number: "))
    rate = int(input("Input workers rate of pay: "))
    hr = int(input("Input workers hours worked: "))
    txRate = int(input("Input tax rate: "))
    if hr > 40:
        oth = hr - 40
        otp = 1.5 * rate * oth
        regPay = 40 * rate
        gross = regPay * otp
    else:
        gross = hr * rate
    #endif
    txOwed = gross * txRate
    net = gross - txOwed
    print("Workers ID number is", id)
    print("Workers gross pay is", gross)
    print("Workers taxes owed are", txOwed)
    print("Workers net pay is", net)
    ans = input("Do again? (Y/N)")
#endwhile
print("end of job")

#end prgram

