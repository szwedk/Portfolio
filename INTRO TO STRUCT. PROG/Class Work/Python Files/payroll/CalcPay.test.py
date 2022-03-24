#==========================================
#       File:               CalcPay.test
#       Name:           Kamil Szwed
#       Date:             October 29, 2021
#       Purpose:       Sequential file application
#==========================================

#Start Program
#accum
c = 0
sumtaxes = 0.0
sumnet = 0.0

#print header
print("                                 SHU Python Coders")
print("ID   First   Last     Pay    ")
print("======================================")
      
info = open ("pay.txt", 'r')
for emp in info:
    c = c + 1
    emp = emp.split()
    ID = emp[0]
    fn = emp[1]
    ln = emp[2]
    hr = float(emp[3])
    rate = float(emp[4])
    txrate = float(emp[5])
    gross = hr * rate
    txowed = gross * txrate
    sumtaxes = sumtaxes + txowed
    net = gross - txowed
    sumnet = sumnet + net
    print(ID,fn,ln,round(net,2))
#end for emp
info.close()

print("======================================")
print("Numbers of employees paid ", c)
print("Sum of taxes owed ", round(sumtaxes, 2))
print("sum of the net pay is ", round(sumnet, 2))
    

