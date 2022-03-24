#===============================
#   File:           Flowchart11.test
#   Name:       Kamil Szwed
#   Date:         October 23 2021
#===============================

#start program

c = 0

n = int(input("Input a value for N ==>"))

if not(n==-1):
    max = n
    c = c + 1
    n = int(input("Input a value for N ==>"))
    while (n !=-1):
        if n > max:
            max = n
        else:
            c = c + 1
        #end if
        n = int(input("Input a value for N ==>"))
    else:
        print("The Max is:", max)
        print("The counter is at:", c)
    #end while
else:
    print("null list, no max, c = 0")
#end if
print("End of Job")


#end program
