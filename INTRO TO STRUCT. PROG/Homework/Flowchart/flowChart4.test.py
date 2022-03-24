#=======================================
#   File:       FlowChart4.test
#   Name:       K. Szwed
#   Date:       October, 3 2021
#=======================================

# Start Program

ID= input("Input an ID number ==> ")
T1= int(input("Input the first test grade ==> "))
T2= int(input("Input the second test grade ==> "))
T3= int(input("Input the third test grade ==> "))
FE= int(input("Input the final exam grade ==> "))

ts= T1 + T2 + T3
fs= (float(FE) * .4) + (float(ts) * .2)

print(" The students ID number is ", ID)
print(" The final score is ",fs)

# End Program
