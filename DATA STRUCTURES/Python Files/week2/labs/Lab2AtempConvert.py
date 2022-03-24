#====================
#   File:       Lab2AtempConvert
#   Name:       Kamil Szwed
#   Date:       Jan 25, 2022
#   Purpose:    write a function “TempConvert” that takes as a parameter 
#               a temperature measure in Fahrenheit, and returns the equivalent 
#               temperature in Celsius. Use the formula:
#               celsTemp = (5.0/9.0)* (fahrenTemp – 32.00)
#=====================

#Ftn

def TempConvert(feh):
    celsTemp = (5.0/9.0)*(feh - 32.00)
    return celsTemp
#endFtnTempConvert

#mainProgram
f = float(input("what is the temp in Fahrenheit? ==> "))
C = TempConvert(f)
print('The temp in celsius is ', round(C,2),'degrees')



