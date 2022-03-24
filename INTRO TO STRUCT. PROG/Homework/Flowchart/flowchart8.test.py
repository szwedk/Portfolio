#=======================================
#   File:       flowchart8.test
#   Date:       October 22, 2021
#   Name:       Kamil Szwed
#=======================================

#Start Program

base = 185
c = 0
sum = 0

id = int(input("Input salesperson ID number: "))

while not(id==-999):
    c = 1
    sum = sum + c
    ws = int(input("Input salesperson WS ==> "))
    if ws <= 1000:
        wp = base
    else:
        if ws > 5000:
            wp = base + 0.053 * 5000 + 0.078 *(ws - 5000)
        else:
            wp = base + 0.053 * ws
        #endif
    #endif
    print("Salesperson ID:",id)
    print("Their weekly sales are", ws)
    print("Their weekly pay is", wp)

    id = int(input("Input salesperson ID number: "))
#endwhile

print("Number of salespeople processed is", sum)
print("end of job")


         
