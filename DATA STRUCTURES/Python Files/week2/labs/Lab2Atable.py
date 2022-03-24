#====================
#   File:       Lab2Atable
#   Name:       Kamil Szwed
#   Date:       Jan 25, 2022
#   Purpose:    Complete the program that uses the function above to
#               display a table of temperatures in Fahrenheit and Celsius, 
#               starting from 50 to 100, with a step of 5. 
#=====================


#Ftn
def TempConvert(feh):
    celsTemp = (5.0/9.0)*(feh - 32.00)
    return celsTemp
#endFtnTempConvert

#mainProgram
print('------------------------------')
print('Fahrenheit       Celsius')
print('------------------------------')
for F in range(50,101,5):
    print(F,"\t\t", round(TempConvert(F),2))
print('------------------------------')
