#=======================================
#   File:       FlowChart4.submit
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


= RESTART: /Users/kamilszwed/Documents/SHU/CS-111-B Python Files/Homework/Flowchart/flowChart4.test.py
Input an ID number ==> 12345
Input the first test grade ==> 95
Input the second test grade ==> 99
Input the third test grade ==> 94
Input the final exam grade ==> 98
 The students ID number is  12345
 The final score is  96.80000000000001
>>> 
