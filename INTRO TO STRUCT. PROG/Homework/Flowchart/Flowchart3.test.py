#=======================================
#   File:       FlowChart3.test
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
