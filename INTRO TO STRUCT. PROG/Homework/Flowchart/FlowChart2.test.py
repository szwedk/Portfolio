#=======================================
#   File:       FlowChart2.test
#   Name:       K. Szwed
#   Date:       October, 3 2021
#=======================================

# Start Program

ID = input("Input an ID number ==> ")
rate = input("Input the rate of pay ==> ")
HR = int(input("Input the number of hours worked ==> "))
TXrate = input("Input the tax rate ==> ")

if HR > 40 :
    oth = float(HR) - 40
    otp = 1.5 * float(rate) * float(oth)
    RegPay = 40 * float(rate)
    gross = float(RegPay) * float(otp)
else:
    gross = float(HR) * float(rate)

TXowed = float(gross) / float(TXrate)
net = float(gross) - float(TXowed)

#endif

print("The ID number is ==> ",ID)
print("The gross pay is $",gross)
print("The taxes owed are $",TXowed)
print("The net pay is $",net)



