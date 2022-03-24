#==============================================
#   file:       DoubleTripleLOOP.test
#   Name:       K. Szwed
#   Date:       October 6, 2021
#==============================================

#Start Program

x = int(input("Input an integer ==> "))

while not(x == -999):
    ans = input("D for double / T for Triple ==> ")
    if ans == 'D' or ans == 'd':
        prod = x * 2
    else:
        if ans == 'T' or ans == 't':
            prod = x * 3
        else:
            prod = 0
    #endif
#endif
    print(" X = ",x)
    print("(D/T): ", ans)
    print("Your answer is", prod)

    x = int(input("Input an integer ==> "))
#endwhile
    
#end Program
