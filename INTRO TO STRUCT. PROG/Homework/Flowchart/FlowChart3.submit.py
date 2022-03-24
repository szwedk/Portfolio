#=======================================
#   File:       FlowChart3.submit
#   Name:       K. Szwed
#   Date:       October, 3 2021
#=======================================

# Start Program

B1 = 5000
B2 = 6000
B3 = 5500

W1 = 820
W2 = 910
W3 = 850

E1 = B1/W1
E2 = B2/W2
E3 = B3/W3

if E1>E2>E3:
    print("Buy model A")
else:
    if E2>E3:
        print("Buy model B")
    else:
        print("Buy model C")
    #endif
#endif

print(" The EER value of model a is ", E1)
print(" The EER value of model b is ", E2)
print(" The EER value of model c is ", E3)

# End Program

>>> 
= RESTART: /Users/kamilszwed/Documents/SHU/CS-111-B Python Files/Homework/Flowchart/Flowchart3.test.py
Buy model B
>>> 
= RESTART: /Users/kamilszwed/Documents/SHU/CS-111-B Python Files/Homework/Flowchart/Flowchart3.test.py
Buy model B
 The EER value of model a is  6.097560975609756
 The EER value of model b is  6.593406593406593
 The EER value of model c is  6.470588235294118
>>> 
