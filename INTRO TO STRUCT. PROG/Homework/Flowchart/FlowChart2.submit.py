#=======================================
#   File:       FlowChart2.submit
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


# End Program

>>> 
= RESTART: /Users/kamilszwed/Documents/SHU/CS-111-B Python Files/Homework/Flowchart/FlowChart2.test.py
Input an ID number ==> 1
Input the rate of pay ==> 25
Input the number of hours worked ==> 44
Input the tax rate ==> 8.75
The ID number is ==>  1
The gross pay is $ 150000.0
The taxes owed are $ 17142.85714285714
The net pay is $ 132857.14285714287
>>> 
= RESTART: /Users/kamilszwed/Documents/SHU/CS-111-B Python Files/Homework/Flowchart/FlowChart2.test.py
Input an ID number ==> 2
Input the rate of pay ==> 25
Input the number of hours worked ==> 39
Input the tax rate ==> 8.75
The ID number is ==>  2
The gross pay is $ 975.0
The taxes owed are $ 111.42857142857143
The net pay is $ 863.5714285714286
>>> 
