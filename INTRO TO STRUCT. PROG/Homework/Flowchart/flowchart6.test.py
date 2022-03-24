#=======================================
#   File:       flowchart6.test
#   Date:       October 22, 2021
#   Name:       Kamil Szwed
#=======================================

#Start Program


while True:
    a = int(input("Input integer 'a' "))
    b = int(input("Input another integer 'b' "))
    if not(a==b):
        if a > b:
            print("A is Larger")
        else:
            print("A is not Larger")
        #Endif
    else:
        print("The numbers are equal")
    #Endif
    ans = input("do again? (Y/N)")
    print("value of ans is ", ans)
    if (ans != 'Y'):
        print("you said y")
        break
    #Endif
#Endwhile

print("end of job")
#End Program

